#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tag 代码生成器
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import MODULE_NAME


class TagCodeGenerator:
    """Tag 代码生成器"""
    
    @staticmethod
    def generate_header(tags_by_category: dict, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated GameplayTags")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append('#include "NativeGameplayTags.h"')
        lines.append("")
        lines.append(f"namespace {MODULE_NAME}GameplayTags")
        lines.append("{")
        
        for category, tags in tags_by_category.items():
            lines.append(f"    // ========== {category} ==========")
            for tag in tags:
                var_name = tag.tag.replace('.', '_')
                lines.append(f"    {MODULE_NAME}_API UE_DECLARE_GAMEPLAY_TAG_EXTERN({var_name});")
            lines.append("")
        
        lines.append("}")
        lines.append("")
        return "\n".join(lines)
    
    @staticmethod
    def generate_source(tags_by_category: dict, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated GameplayTags")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append('#include "DJ01/System/Public/DJ01GameplayTags.h"')
        lines.append("")
        lines.append(f"namespace {MODULE_NAME}GameplayTags")
        lines.append("{")
        
        for category, tags in tags_by_category.items():
            lines.append(f"    // ========== {category} ==========")
            for tag in tags:
                var_name = tag.tag.replace('.', '_')
                desc = tag.description or tag.tag
                lines.append(f'    UE_DEFINE_GAMEPLAY_TAG_COMMENT({var_name}, "{tag.tag}", "{desc}");')
            lines.append("")
        
        lines.append("}")
        lines.append("")
        return "\n".join(lines)