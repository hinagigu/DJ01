#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C++ 类扫描器
扫描项目中的 UCLASS 并支持自动添加 BindingSet
"""

import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Set, Tuple
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import PROJECT_ROOT


@dataclass
class UClassInfo:
    """扫描到的 UCLASS 信息"""
    class_name: str                          # 类名 (如 UMyAnimInstance)
    base_class: str                          # 基类 (如 UAnimInstance)
    file_path: Path                          # 文件路径
    line_number: int                         # class 声明行号
    binding_sets: List[str] = field(default_factory=list)  # 已添加的 BindingSet
    
    @property
    def display_name(self) -> str:
        """显示名称"""
        return f"{self.class_name} ({self.base_class})"
    
    @property
    def relative_path(self) -> str:
        """相对于项目根目录的路径"""
        try:
            return str(self.file_path.relative_to(PROJECT_ROOT))
        except:
            return str(self.file_path)
    
    @property
    def is_anim_instance(self) -> bool:
        return 'AnimInstance' in self.base_class
    
    @property
    def is_widget(self) -> bool:
        return 'Widget' in self.base_class or 'UserWidget' in self.base_class
    
    @property
    def is_actor(self) -> bool:
        return 'Actor' in self.base_class or 'Character' in self.base_class or 'Pawn' in self.base_class


class ClassScanner:
    """C++ 类扫描器"""
    
    # 匹配 UCLASS 声明的正则（支持多行和复杂宏参数）
    UCLASS_PATTERN = re.compile(
        r'UCLASS\s*\([^)]*\)\s*'
        r'class\s+(?:\w+_API\s+)?'
        r'(\w+)\s*'
        r'(?:final\s*)?'
        r':\s*public\s+'
        r'(\w+)',
        re.MULTILINE | re.DOTALL
    )
    
    # 备用正则：单独匹配 class 行
    CLASS_PATTERN = re.compile(
        r'^class\s+(?:\w+_API\s+)?'
        r'(\w+)\s*'
        r'(?:final\s*)?'
        r':\s*public\s+'
        r'(\w+)',
        re.MULTILINE
    )
    
    # 匹配已添加的 BindingSet
    BINDING_SET_PATTERN = re.compile(
        r'DJ01_DECLARE_BINDING_SET\s*\(\s*(\w+)\s*\)'
    )
    
    # 感兴趣的基类
    INTERESTING_BASE_CLASSES = {
        'UAnimInstance', 'UUserWidget', 'UWidget', 'UCommonUserWidget',
        'AActor', 'ACharacter', 'APawn', 'APlayerController',
        'UActorComponent', 'USceneComponent',
    }
    
    def __init__(self, search_paths: List[Path] = None):
        if search_paths is None:
            search_paths = [PROJECT_ROOT / "Source"]
        self.search_paths = search_paths
        self.classes: List[UClassInfo] = []
    
    def scan(self, filter_base_classes: Set[str] = None) -> List[UClassInfo]:
        self.classes = []
        
        for search_path in self.search_paths:
            if not search_path.exists():
                continue
            for header_file in search_path.rglob("*.h"):
                self._scan_file(header_file, filter_base_classes)
        
        self.classes.sort(key=lambda c: c.class_name)
        return self.classes
    
    def _scan_file(self, file_path: Path, filter_base_classes: Set[str] = None):
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return
        
        if 'UCLASS' not in content:
            return
        
        matches = list(self.UCLASS_PATTERN.finditer(content))
        if not matches:
            matches = list(self.CLASS_PATTERN.finditer(content))
        
        for match in matches:
            class_name = match.group(1)
            base_class = match.group(2)
            
            if filter_base_classes:
                if not any(base in base_class for base in filter_base_classes):
                    continue
            else:
                if not any(base in base_class for base in self.INTERESTING_BASE_CLASSES):
                    continue
            
            line_number = content[:match.start()].count('\n') + 1
            binding_sets = self.BINDING_SET_PATTERN.findall(content)
            
            self.classes.append(UClassInfo(
                class_name=class_name,
                base_class=base_class,
                file_path=file_path,
                line_number=line_number,
                binding_sets=list(binding_sets)
            ))
    
    def refresh_class(self, class_info: UClassInfo) -> UClassInfo:
        try:
            content = class_info.file_path.read_text(encoding='utf-8', errors='ignore')
            class_info.binding_sets = self.BINDING_SET_PATTERN.findall(content)
        except Exception:
            pass
        return class_info


class BindingSetInjector:
    """BindingSet 代码注入器"""
    
    # 正确的 include 路径
    BINDINGSETS_INCLUDE = '#include "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"'
    
    # 旧的错误 include 路径（用于检测和修复）
    OLD_BINDINGSETS_INCLUDES = [
        '#include "DJ01/GAS/Generated/BindingSets/BindingSets.h"',
        'DJ01/GAS/Generated/BindingSets/BindingSets.h',
    ]
    
    GENERATED_BODY_PATTERN = re.compile(r'GENERATED_BODY\s*\(\s*\)', re.MULTILINE)
    GENERATED_INCLUDE_PATTERN = re.compile(r'^(#include\s+["\'][^"\']+\.generated\.h["\'])', re.MULTILINE)
    
    # 匹配第一个 #include
    FIRST_INCLUDE_PATTERN = re.compile(r'^#include\s+', re.MULTILINE)
    
    # 匹配 InitializeWithAbilitySystem 函数（用于注入初始化调用）
    INIT_WITH_ASC_PATTERN = re.compile(
        r'void\s+(\w+)::InitializeWithAbilitySystem\s*\(\s*UAbilitySystemComponent\s*\*\s*(\w+)\s*\)\s*\{',
        re.MULTILINE
    )
    
    @staticmethod
    def _fix_old_include(content: str) -> str:
        """修复旧的错误 include 路径"""
        for old_include in BindingSetInjector.OLD_BINDINGSETS_INCLUDES:
            if old_include in content:
                content = content.replace(old_include, BindingSetInjector.BINDINGSETS_INCLUDE.replace('#include ', '').strip('"'))
        return content
    
    @staticmethod
    def _add_include_if_needed(content: str) -> str:
        """如果需要，添加 BindingSets.h 的 include（在第一个 #include 之前）"""
        # 首先修复旧的 include 路径
        content = BindingSetInjector._fix_old_include(content)
        
        # 检查正确的路径是否已存在
        if 'AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h' in content:
            return content
        
        # 找到第一个 #include，在其前面插入
        match = BindingSetInjector.FIRST_INCLUDE_PATTERN.search(content)
        if match:
            insert_pos = match.start()
            return content[:insert_pos] + BindingSetInjector.BINDINGSETS_INCLUDE + '\n' + content[insert_pos:]
        
        # 如果没找到 #include，尝试在 #pragma once 后面添加
        pragma_match = re.search(r'#pragma\s+once', content)
        if pragma_match:
            insert_pos = pragma_match.end()
            return content[:insert_pos] + '\n\n' + BindingSetInjector.BINDINGSETS_INCLUDE + content[insert_pos:]
        
        return BindingSetInjector.BINDINGSETS_INCLUDE + '\n\n' + content
    
    @staticmethod
    def _remove_include_if_unused(content: str) -> str:
        """如果没有任何 BindingSet 声明，移除 include"""
        if 'DJ01_DECLARE_BINDING_SET' in content:
            return content
        pattern = re.compile(r'#include\s+["\'].*?BindingSets/BindingSets\.h["\']\s*\n?', re.MULTILINE)
        return pattern.sub('', content)
    
    @staticmethod
    def _find_cpp_file(header_path: Path) -> Optional[Path]:
        """根据头文件路径查找对应的 .cpp 文件"""
        # 尝试常见的 cpp 文件位置
        cpp_candidates = [
            header_path.with_suffix('.cpp'),  # 同目录
            header_path.parent.parent / 'Private' / header_path.with_suffix('.cpp').name,  # Private 目录
            header_path.parent.parent.parent / 'Private' / header_path.parent.name / header_path.with_suffix('.cpp').name,
        ]
        
        for cpp_path in cpp_candidates:
            if cpp_path.exists():
                return cpp_path
        
        # 递归查找同名 .cpp 文件
        cpp_name = header_path.with_suffix('.cpp').name
        for cpp_file in header_path.parent.parent.parent.rglob(cpp_name):
            return cpp_file
        
        return None
    
    @staticmethod
    def _add_init_call_to_cpp(cpp_path: Path, class_name: str, binding_set_name: str) -> tuple:
        """在 .cpp 文件的 InitializeWithAbilitySystem 函数中添加初始化调用"""
        if not cpp_path or not cpp_path.exists():
            return False, "未找到对应的 .cpp 文件"
        
        try:
            content = cpp_path.read_text(encoding='utf-8')
        except Exception as e:
            return False, f"读取 .cpp 文件失败: {e}"
        
        init_call = f"InitBindingSet_{binding_set_name}"
        
        # 检查是否已经有此调用
        if init_call in content:
            return True, "初始化调用已存在"
        
        # 查找 InitializeWithAbilitySystem 函数
        match = BindingSetInjector.INIT_WITH_ASC_PATTERN.search(content)
        if not match:
            # 如果没找到标准函数，尝试查找 NativeInitializeAnimation
            native_init_pattern = re.compile(
                r'void\s+' + re.escape(class_name) + r'::NativeInitializeAnimation\s*\(\s*\)\s*\{[^}]*?'
                r'(InitializeWithAbilitySystem\s*\(\s*(\w+)\s*\))',
                re.MULTILINE | re.DOTALL
            )
            native_match = native_init_pattern.search(content)
            if native_match:
                # 在现有的 InitializeWithAbilitySystem 调用后添加
                insert_pos = native_match.end(1)
                asc_var = native_match.group(2)
                new_call = f"\n\t\t{init_call}({asc_var});"
                new_content = content[:insert_pos] + new_call + content[insert_pos:]
            else:
                return False, f"未找到 InitializeWithAbilitySystem 函数在 {cpp_path.name}"
        else:
            # 找到了 InitializeWithAbilitySystem 函数
            asc_param = match.group(2)  # ASC 参数名
            func_start = match.end()
            
            # 查找函数体内的 check(ASC) 语句，在其后插入
            check_pattern = re.compile(rf'check\s*\(\s*{asc_param}\s*\)\s*;', re.MULTILINE)
            check_match = check_pattern.search(content, func_start)
            
            if check_match:
                # 在 check(ASC) 后插入
                insert_pos = check_match.end()
                new_call = f"\n\n\t// 初始化 BindingSet - 自动注册 GAS 监听并同步初始值\n\t{init_call}({asc_param});"
            else:
                # 没有 check，在函数开头插入
                insert_pos = func_start
                new_call = f"\n\tcheck({asc_param});\n\n\t// 初始化 BindingSet - 自动注册 GAS 监听并同步初始值\n\t{init_call}({asc_param});\n"
            
            new_content = content[:insert_pos] + new_call + content[insert_pos:]
        
        try:
            cpp_path.write_text(new_content, encoding='utf-8')
            return True, f"已在 {cpp_path.name} 中添加 {init_call} 调用"
        except Exception as e:
            return False, f"写入 .cpp 文件失败: {e}"
    
    @staticmethod
    def add_binding_set(class_info: UClassInfo, binding_set_name: str) -> tuple:
        """向类中添加 BindingSet 声明（包括必要的 #include 和 .cpp 初始化调用）"""
        if binding_set_name in class_info.binding_sets:
            return False, f"BindingSet '{binding_set_name}' 已存在于 {class_info.class_name}"
        
        try:
            content = class_info.file_path.read_text(encoding='utf-8')
        except Exception as e:
            return False, f"读取文件失败: {e}"
        
        # 添加 #include（同时修复旧路径）
        content = BindingSetInjector._add_include_if_needed(content)
        
        # 在 GENERATED_BODY() 后面添加宏声明
        match = BindingSetInjector.GENERATED_BODY_PATTERN.search(content)
        if not match:
            return False, f"未找到 GENERATED_BODY() 在 {class_info.class_name}"
        
        insert_pos = match.end()
        indent = "\t"
        new_code = f"\n\n{indent}// BindingSet: {binding_set_name}\n{indent}DJ01_DECLARE_BINDING_SET({binding_set_name})\n"
        new_content = content[:insert_pos] + new_code + content[insert_pos:]
        
        try:
            class_info.file_path.write_text(new_content, encoding='utf-8')
            class_info.binding_sets.append(binding_set_name)
        except Exception as e:
            return False, f"写入文件失败: {e}"
        
        # 尝试在 .cpp 文件中添加初始化调用
        cpp_path = BindingSetInjector._find_cpp_file(class_info.file_path)
        cpp_result = ""
        if cpp_path:
            success, cpp_msg = BindingSetInjector._add_init_call_to_cpp(
                cpp_path, class_info.class_name, binding_set_name
            )
            if success:
                cpp_result = f"\n{cpp_msg}"
            else:
                cpp_result = f"\n⚠️ {cpp_msg}（请手动添加初始化调用）"
        else:
            cpp_result = "\n⚠️ 未找到 .cpp 文件，请手动添加 InitBindingSet_" + binding_set_name + "(ASC) 调用"
        
        return True, f"已添加 BindingSet '{binding_set_name}' 到 {class_info.class_name}（含 #include）{cpp_result}"
    
    @staticmethod
    def _remove_init_call_from_cpp(cpp_path: Path, binding_set_name: str) -> tuple:
        """从 .cpp 文件中移除初始化调用"""
        if not cpp_path or not cpp_path.exists():
            return True, ""  # 没有 cpp 文件就不需要移除
        
        try:
            content = cpp_path.read_text(encoding='utf-8')
        except Exception as e:
            return False, f"读取 .cpp 文件失败: {e}"
        
        init_call = f"InitBindingSet_{binding_set_name}"
        
        if init_call not in content:
            return True, ""  # 没有此调用，无需移除
        
        # 移除初始化调用（包括注释行）- 使用更精确的正则
        # 先尝试移除带注释的完整块
        pattern1 = re.compile(
            rf'(\t*)// 初始化 BindingSet[^\n]*\n\1{init_call}\s*\([^)]*\)\s*;\s*\n',
            re.MULTILINE
        )
        new_content, count = pattern1.subn('', content)
        
        if count == 0:
            # 只移除调用行本身（保留换行）
            pattern2 = re.compile(
                rf'^(\s*){init_call}\s*\([^)]*\)\s*;\s*\n',
                re.MULTILINE
            )
            new_content, count = pattern2.subn('', content)
        
        if count == 0:
            return True, ""  # 没找到匹配的模式
        
        try:
            cpp_path.write_text(new_content, encoding='utf-8')
            return True, f"已从 {cpp_path.name} 移除 {init_call} 调用"
        except Exception as e:
            return False, f"写入 .cpp 文件失败: {e}"
    
    @staticmethod
    def remove_binding_set(class_info: UClassInfo, binding_set_name: str) -> tuple:
        """从类中移除 BindingSet 声明（包括 .cpp 中的初始化调用）"""
        if binding_set_name not in class_info.binding_sets:
            return False, f"BindingSet '{binding_set_name}' 不存在于 {class_info.class_name}"
        
        try:
            content = class_info.file_path.read_text(encoding='utf-8')
        except Exception as e:
            return False, f"读取文件失败: {e}"
        
        # 匹配要移除的代码（更精确的正则，保留格式）
        # 先尝试匹配完整的带注释块
        pattern = re.compile(
            rf'\n\t// BindingSet: {re.escape(binding_set_name)}\n'
            rf'\tDJ01_DECLARE_BINDING_SET\({re.escape(binding_set_name)}\)\n',
            re.MULTILINE
        )
        new_content, count = pattern.subn('\n', content)
        
        if count == 0:
            # 尝试更宽松的模式
            pattern2 = re.compile(
                rf'(\n\s*)// BindingSet: {re.escape(binding_set_name)}\s*\n'
                rf'\s*DJ01_DECLARE_BINDING_SET\s*\(\s*{re.escape(binding_set_name)}\s*\)\s*\n',
                re.MULTILINE
            )
            new_content, count = pattern2.subn(r'\1', content)
        
        if count == 0:
            # 只匹配宏声明行
            pattern3 = re.compile(
                rf'^\s*DJ01_DECLARE_BINDING_SET\s*\(\s*{re.escape(binding_set_name)}\s*\)\s*\n',
                re.MULTILINE
            )
            new_content, count = pattern3.subn('', content)
        
        if count == 0:
            return False, f"未能找到并移除 BindingSet '{binding_set_name}'"
        
        # 清理未使用的 include
        new_content = BindingSetInjector._remove_include_if_unused(new_content)
        
        try:
            class_info.file_path.write_text(new_content, encoding='utf-8')
            class_info.binding_sets.remove(binding_set_name)
        except Exception as e:
            return False, f"写入文件失败: {e}"
        
        # 尝试从 .cpp 文件中移除初始化调用
        cpp_path = BindingSetInjector._find_cpp_file(class_info.file_path)
        cpp_result = ""
        if cpp_path:
            success, cpp_msg = BindingSetInjector._remove_init_call_from_cpp(cpp_path, binding_set_name)
            if cpp_msg:
                cpp_result = f"\n{cpp_msg}"
        
        return True, f"已从 {class_info.class_name} 移除 BindingSet '{binding_set_name}'{cpp_result}"