# AbilityMaker - AngelScript 技能生成器

从 JSON 配置文件生成 AngelScript 技能代码，支持热更新无需重新编译。

## 功能特点

- **数据驱动**: 通过 JSON 配置定义技能行为
- **热更新**: 生成的 AngelScript 代码可以热重载
- **条件系统**: 支持属性捕获和条件代码，实现复杂逻辑
- **多阶段触发**: 支持 OnActivate、OnCommit、OnAnimEvent、OnEnd 四个阶段

## 快速开始

```bash
# 进入工具目录
cd D:\UnrealProjects\DJ01\Tools\AbilityMaker

# 生成示例配置
python main.py --sample

# 从配置生成 AngelScript
python main.py --generate
```

## 配置文件结构

配置文件位于: `Source/DJ01/AbilitySystem/Abilities/Config/AbilityDefinitions.json`

```json
{
  "Abilities": [
    {
      "Name": "Fireball",
      "DisplayName": "火球术",
      "Description": "释放一颗燃烧的火球...",
      "Effects": [
        {
          "Name": "MainDamage",
          "Phase": "OnAnimEvent",
          "EventTag": "Event.Montage.Ability.Fire",
          "Type": "Damage",
          "Condition": {
            "Captures": [
              { "source": "Target", "set": "CoreStats", "attr": "Health", "layer": "Current" }
            ],
            "TagConditions": [
              { "source": "Target", "tag": "Status.Immunity.Damage" }
            ],
            "Code": "if (bTarget_Status_Immunity_Damage) { return; }"
          },
          "DamageConfig": {
            "BaseDamage": 80.0,
            "DamageType": "Magical",
            "ScalingRatios": [
              { "attr": "AbilityPower", "ratio": 0.75 }
            ]
          }
        }
      ]
    }
  ]
}
```

## 效果类型

| 类型 | 说明 | 配置 |
|------|------|------|
| `Damage` | 造成伤害 | `DamageConfig` |
| `Heal` | 恢复生命 | `HealConfig` |
| `ApplyEffect` | 应用 GE | `ApplyEffectConfig` |
| `SpawnActor` | 生成 Actor | `SpawnConfig` |

## 触发阶段

| 阶段 | 时机 |
|------|------|
| `OnActivate` | 技能激活时 |
| `OnCommit` | CommitAbility 后 |
| `OnAnimEvent` | 动画事件触发时 |
| `OnEnd` | 技能结束时 |

## 条件系统

### 属性捕获

```json
{
  "Captures": [
    { "source": "Target", "set": "CoreStats", "attr": "Health", "layer": "Current" }
  ]
}
```

生成变量: `Health_TargetValue`

### Tag 检查

```json
{
  "TagConditions": [
    { "source": "Target", "tag": "Status.Immunity.Damage" }
  ]
}
```

生成变量: `bTarget_Status_Immunity_Damage`

### 条件代码

```json
{
  "Code": "if (bTarget_Status_Immunity_Damage) { return; }\nDamageMultiplier = 2.0f;"
}
```

- 写 `return;` 跳过当前效果
- 可设置 `DamageMultiplier` / `HealMultiplier` 影响最终数值

## 生成输出

生成的文件位于: `Script/GeneratedAbilities/`

```
GA_Fireball.as
GA_HealingWave.as
...
```

## 与 GAS 集成

生成的技能通过 SetByCaller 将计算好的原始伤害/治疗量传递给 Execution:

- `SetByCaller.Damage.Raw` - 原始伤害
- `SetByCaller.Damage.Type` - 伤害类型 (0=物理, 1=魔法, 2=真实)
- `SetByCaller.Heal.Raw` - 原始治疗量

Execution 负责应用护甲减伤、治疗增益等最终计算。