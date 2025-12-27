#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnimInstance 变量代码生成器
为 DJ01AnimInstance 生成与 GameplayTag 映射的变量声明和自动初始化代码
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import MODULE_NAME


class AnimInstanceVarGenerator:
    """AnimInstance 变量代码生成器"""
    
    @staticmethod
    def _normalize_var_name(var_name: str) -> str:
        """确保变量名符合 UE 规范（布尔变量以 b 开头）"""
        if not var_name.startswith('b'):
            return 'b' + var_name
        return var_name
    
    @staticmethod
    def generate_header(anim_tags: list, timestamp: str) -> str:
        """
        生成包含两个宏的头文件：
        1. DJ01_ANIM_INSTANCE_GENERATED_VARS - 变量声明，用于头文件
        2. DJ01_ANIM_INSTANCE_INIT_TAG_MAPPINGS - 映射初始化，用于构造函数
        """
        lines = []
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated AnimInstance Variables & Tag Mappings")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("//")
        lines.append("// 使用方式：")
        lines.append("// 1. 在 DJ01AnimInstance.h 顶部 #include 此文件")
        lines.append("// 2. 在类的 protected 区域使用 DJ01_ANIM_INSTANCE_GENERATED_VARS")
        lines.append("// 3. 在构造函数中使用 DJ01_ANIM_INSTANCE_INIT_TAG_MAPPINGS()")
        lines.append("//    映射会自动完成，无需在蓝图中配置！")
        lines.append("//")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append(f'#include "{MODULE_NAME}/System/Public/{MODULE_NAME}GameplayTags.h"')
        lines.append("")
        
        # 按 category 分组
        by_category = {}
        for tag in anim_tags:
            cat = tag.category
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(tag)
        
        # ========== 宏1: 变量声明 ==========
        lines.append("// ========== 变量声明宏 (用于头文件 protected 区域) ==========")
        lines.append("#define DJ01_ANIM_INSTANCE_GENERATED_VARS \\")
        
        var_lines = []
        for category, tags in by_category.items():
            for tag in tags:
                var_name = AnimInstanceVarGenerator._normalize_var_name(tag.anim_var)
                desc = tag.description or tag.tag
                var_lines.append(f'    /** {desc} (映射自 {tag.tag}) */ \\')
                var_lines.append(f'    UPROPERTY(BlueprintReadOnly, Category = "Character State Data|{category}") \\')
                var_lines.append(f'    bool {var_name} = false; \\')
        
        # 移除最后一个反斜杠并添加空行结尾
        if var_lines:
            var_lines[-1] = var_lines[-1].rstrip(' \\')
        
        lines.extend(var_lines)
        lines.append("")
        lines.append("")
        
        # ========== 宏2: 映射初始化 ==========
        lines.append("// ========== 映射初始化宏 (用于构造函数) ==========")
        lines.append("// 使用 FDJ01GameplayTagPropertyMap::AddMapping 自动配置映射")
        lines.append("#define DJ01_ANIM_INSTANCE_INIT_TAG_MAPPINGS() \\")
        
        mapping_lines = []
        for category, tags in by_category.items():
            for tag in tags:
                var_name = AnimInstanceVarGenerator._normalize_var_name(tag.anim_var)
                tag_var = tag.tag.replace('.', '_')  # 对应 DJ01GameplayTags 中的变量名
                mapping_lines.append(
                    f'    GameplayTagPropertyMap.AddMapping({MODULE_NAME}GameplayTags::{tag_var}, '
                    f'GET_MEMBER_NAME_CHECKED(ThisClass, {var_name})); \\'
                )
        
        # 移除最后一个反斜杠
        if mapping_lines:
            mapping_lines[-1] = mapping_lines[-1].rstrip(' \\')
        
        lines.extend(mapping_lines)
        lines.append("")
        lines.append("")
        lines.append("// ========== 宏结束 ==========")
        lines.append("")
        
        return "\n".join(lines)