#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迁移脚本：将旧版 CSV（含 BehaviorConfig）转换为新版 CSV + JSON 混合存储

使用方法：
    python migrate_to_hybrid.py

功能：
    1. 读取旧 CSV（含 BehaviorConfig 列）
    2. 提取行为配置到 JSON 文件
    3. 写入新 CSV（无 BehaviorConfig 列）
    4. 备份原始文件
"""

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path

# 导入配置
import sys
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    ATTRIBUTES_CONFIG, ATTRIBUTES_BEHAVIORS,
    ATTRIBUTES_CSV_FIELDS, ATTRIBUTES_CSV_FIELDS_LEGACY
)
from attribute.data import AttributeData


def migrate():
    """执行迁移"""
    print("=" * 60)
    print("属性配置迁移工具：CSV → CSV + JSON")
    print("=" * 60)
    
    # 检查源文件
    if not ATTRIBUTES_CONFIG.exists():
        print(f"❌ 源文件不存在: {ATTRIBUTES_CONFIG}")
        return False
    
    # 读取旧 CSV
    print(f"\n📖 读取旧 CSV: {ATTRIBUTES_CONFIG}")
    attributes = []
    has_behavior_config = False
    
    with open(ATTRIBUTES_CONFIG, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        
        # 检查是否包含 BehaviorConfig 列
        if 'BehaviorConfig' in fieldnames:
            has_behavior_config = True
            print("   ✓ 检测到 BehaviorConfig 列（旧格式）")
        else:
            print("   ⚠ 未检测到 BehaviorConfig 列（可能已是新格式）")
        
        for row in reader:
            attr = AttributeData.from_dict(row)
            attributes.append(attr)
    
    print(f"   ✓ 读取 {len(attributes)} 个属性")
    
    if not has_behavior_config:
        print("\n⚠ CSV 已是新格式，无需迁移")
        
        # 检查 JSON 是否存在
        if ATTRIBUTES_BEHAVIORS.exists():
            print(f"   ✓ 行为配置 JSON 已存在: {ATTRIBUTES_BEHAVIORS}")
        else:
            print(f"   ⚠ 行为配置 JSON 不存在，将创建空文件")
            _save_behaviors_json({})
        
        return True
    
    # 备份原始文件
    backup_path = ATTRIBUTES_CONFIG.with_suffix(
        f'.csv.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    )
    print(f"\n📦 备份原始文件: {backup_path}")
    shutil.copy2(ATTRIBUTES_CONFIG, backup_path)
    
    # 提取行为配置
    behaviors = {}
    for attr in attributes:
        if attr.has_non_default_behavior():
            key = attr.get_behavior_key()
            behaviors[key] = attr.to_behavior_dict()
    
    print(f"\n📝 提取行为配置:")
    print(f"   ✓ {len(behaviors)} 个属性有非默认行为配置")
    for key in behaviors:
        print(f"      - {key}")
    
    # 写入新 CSV（不含 BehaviorConfig）
    print(f"\n💾 写入新 CSV: {ATTRIBUTES_CONFIG}")
    with open(ATTRIBUTES_CONFIG, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=ATTRIBUTES_CSV_FIELDS)
        writer.writeheader()
        for attr in attributes:
            writer.writerow(attr.to_csv_dict())
    print(f"   ✓ 写入 {len(attributes)} 行")
    
    # 写入 JSON
    _save_behaviors_json(behaviors)
    
    print("\n" + "=" * 60)
    print("✅ 迁移完成！")
    print("=" * 60)
    print(f"\n新文件:")
    print(f"   - CSV: {ATTRIBUTES_CONFIG}")
    print(f"   - JSON: {ATTRIBUTES_BEHAVIORS}")
    print(f"\n备份文件:")
    print(f"   - {backup_path}")
    
    return True


def _save_behaviors_json(behaviors):
    """保存行为配置 JSON"""
    print(f"\n💾 写入行为配置 JSON: {ATTRIBUTES_BEHAVIORS}")
    
    behavior_data = {
        "Version": "1.0",
        "Behaviors": behaviors
    }
    
    ATTRIBUTES_BEHAVIORS.parent.mkdir(parents=True, exist_ok=True)
    with open(ATTRIBUTES_BEHAVIORS, 'w', encoding='utf-8') as f:
        json.dump(behavior_data, f, ensure_ascii=False, indent=2)
    
    print(f"   ✓ 写入 {len(behaviors)} 个行为配置")


def verify():
    """验证迁移结果"""
    print("\n" + "=" * 60)
    print("验证迁移结果")
    print("=" * 60)
    
    # 读取新 CSV
    if not ATTRIBUTES_CONFIG.exists():
        print(f"❌ CSV 不存在: {ATTRIBUTES_CONFIG}")
        return False
    
    print(f"\n📖 读取新 CSV: {ATTRIBUTES_CONFIG}")
    attributes = []
    with open(ATTRIBUTES_CONFIG, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if 'BehaviorConfig' in reader.fieldnames:
            print("   ❌ 仍包含 BehaviorConfig 列")
            return False
        print("   ✓ 不包含 BehaviorConfig 列")
        
        for row in reader:
            attr = AttributeData.from_dict(row)
            attributes.append(attr)
    print(f"   ✓ 读取 {len(attributes)} 个属性")
    
    # 读取 JSON
    if not ATTRIBUTES_BEHAVIORS.exists():
        print(f"❌ JSON 不存在: {ATTRIBUTES_BEHAVIORS}")
        return False
    
    print(f"\n📖 读取行为配置 JSON: {ATTRIBUTES_BEHAVIORS}")
    with open(ATTRIBUTES_BEHAVIORS, 'r', encoding='utf-8') as f:
        behavior_data = json.load(f)
    
    behaviors = behavior_data.get('Behaviors', {})
    print(f"   ✓ 版本: {behavior_data.get('Version', 'N/A')}")
    print(f"   ✓ {len(behaviors)} 个行为配置")
    
    # 应用行为配置
    for attr in attributes:
        key = attr.get_behavior_key()
        if key in behaviors:
            attr.apply_behavior_dict(behaviors[key])
    
    # 显示结果
    print("\n📋 属性列表:")
    for attr in attributes:
        has_behavior = "✓" if attr.has_non_default_behavior() else " "
        print(f"   [{has_behavior}] {attr.set_name}.{attr.name} ({attr.type})")
    
    print("\n✅ 验证通过！")
    return True


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='属性配置迁移工具')
    parser.add_argument('--verify', action='store_true', help='仅验证，不执行迁移')
    args = parser.parse_args()
    
    if args.verify:
        verify()
    else:
        if migrate():
            verify()