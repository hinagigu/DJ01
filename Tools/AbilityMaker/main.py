#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AbilityMaker - AngelScript 技能生成器
用于从 JSON 配置生成技能 AngelScript 代码
"""

import sys
import argparse
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    CONFIG_DIR, ABILITY_DEFINITIONS_FILE, SCRIPT_OUTPUT_DIR
)
from ability.data import load_ability_definitions, save_ability_definitions, AbilityDefinition
from ability.generator import AbilityScriptGenerator


def ensure_directories():
    """确保必要的目录存在"""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    SCRIPT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_all():
    """生成所有技能的 AngelScript 代码"""
    print(f"[AbilityMaker] 加载配置: {ABILITY_DEFINITIONS_FILE}")
    
    if not ABILITY_DEFINITIONS_FILE.exists():
        print(f"[AbilityMaker] 配置文件不存在，创建示例配置...")
        create_sample_config()
        return
    
    abilities = load_ability_definitions(ABILITY_DEFINITIONS_FILE)
    
    if not abilities:
        print("[AbilityMaker] 没有找到技能定义")
        return
    
    print(f"[AbilityMaker] 找到 {len(abilities)} 个技能定义")
    
    for ability in abilities:
        output_file = SCRIPT_OUTPUT_DIR / f"GA_{ability.name}.as"
        
        print(f"[AbilityMaker] 生成: {ability.name} -> {output_file}")
        
        code = AbilityScriptGenerator.generate(ability)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(code)
    
    print(f"[AbilityMaker] 完成! 生成了 {len(abilities)} 个技能文件到 {SCRIPT_OUTPUT_DIR}")


def create_sample_config():
    """创建示例配置文件"""
    from ability.data import (
        AbilityDefinition, EffectDefinition, ConditionDefinition,
        DamageConfig, HealConfig, ScalingRatio, AttributeCapture, TagCondition
    )
    
    sample_abilities = [
        AbilityDefinition(
            name="Fireball",
            display_name="火球术",
            description="释放一颗燃烧的火球，对目标造成魔法伤害。目标血量低于30%时伤害翻倍。",
            effects=[
                EffectDefinition(
                    name="MainDamage",
                    phase="OnAnimEvent",
                    event_tag="Event.Montage.Ability.Fire",
                    effect_type="Damage",
                    condition=ConditionDefinition(
                        captures=[
                            AttributeCapture(source="Target", set="CoreStats", attr="Health", layer="Current"),
                            AttributeCapture(source="Target", set="CoreStats", attr="MaxHealth", layer="Total"),
                        ],
                        tag_conditions=[
                            TagCondition(source="Target", tag="Status.Immunity.Damage")
                        ],
                        code="""// 如果目标免疫伤害，跳过此效果
if (bTarget_Status_Immunity_Damage) { return; }

// 斩杀效果：目标血量低于30%时伤害翻倍
float HealthPercent = Health_TargetValue / FMath::Max(MaxHealth_TargetValue, 1.f);
if (HealthPercent < 0.3f) { DamageMultiplier = 2.0f; }"""
                    ),
                    damage_config=DamageConfig(
                        base_damage=80.0,
                        damage_type="Magical",
                        scaling_ratios=[
                            ScalingRatio(attr="AbilityPower", ratio=0.75)
                        ]
                    )
                )
            ]
        ),
        AbilityDefinition(
            name="HealingWave",
            display_name="治疗波",
            description="对友方目标释放治疗波，恢复生命值。",
            effects=[
                EffectDefinition(
                    name="MainHeal",
                    phase="OnCommit",
                    event_tag="",
                    effect_type="Heal",
                    condition=ConditionDefinition(
                        captures=[],
                        tag_conditions=[
                            TagCondition(source="Target", tag="Status.Immunity.Heal")
                        ],
                        code="if (bTarget_Status_Immunity_Heal) { return; }"
                    ),
                    heal_config=HealConfig(
                        base_heal=100.0,
                        scaling_ratios=[
                            ScalingRatio(attr="AbilityPower", ratio=0.5)
                        ]
                    )
                )
            ]
        ),
    ]
    
    save_ability_definitions(ABILITY_DEFINITIONS_FILE, sample_abilities)
    print(f"[AbilityMaker] 示例配置已创建: {ABILITY_DEFINITIONS_FILE}")


def main():
    parser = argparse.ArgumentParser(
        description="AbilityMaker - AngelScript 技能生成器"
    )
    parser.add_argument(
        "--generate", "-g",
        action="store_true",
        help="从 JSON 配置生成 AngelScript 代码"
    )
    parser.add_argument(
        "--sample", "-s",
        action="store_true",
        help="创建示例配置文件"
    )
    parser.add_argument(
        "--config", "-c",
        type=str,
        help="指定配置文件路径"
    )
    
    args = parser.parse_args()
    
    ensure_directories()
    
    if args.sample:
        create_sample_config()
    elif args.generate or not any(vars(args).values()):
        generate_all()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()