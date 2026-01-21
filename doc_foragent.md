# DJ01 Project Context

## Stack
- UE5 + C++ + AngelScript
- GAS (Gameplay Ability System)
- Lyra Architecture

## Source Structure
```
Source/DJ01/
├── AbilitySystem/        # GAS核心
│   ├── Abilities/        # 技能类 + Config/AbilityDefinitions.json
│   ├── Attributes/       # 属性集 + Config/AttributeDefinitions.csv
│   │   └── BindingSets/  # 动画绑定 + Config/BindingSetDefinitions.json
│   └── Executions/       # 伤害计算 + Config/ExecutionDefinitions.json
├── Animation/            # DJ01AnimInstance, AnimLayers
├── Camera/               # 相机模式栈
├── Character/            # DJ01Character, PawnExtension, HeroComponent
├── Combo/                # ComboGraph技能
├── Experience/           # 游戏模式定义
├── Input/                # 输入配置
├── Player/               # PlayerController, PlayerState
├── System/               # GameMode, Tags + Config/GameplayTagDefinitions.csv
├── Team/                 # 队伍系统
└── UI/                   # Widget + Generated/
```

## Tools (Python)
| Tool | Path | Config | Function |
|------|------|--------|----------|
| AttributeGenerator | `Tools/AttributeGenerator/` | `**/Config/*.csv|json` | 生成Attributes/Tags/BindingSets/MMC/Executions |
| AbilityMaker | `Tools/AbilityMaker/` | `AbilityDefinitions.json` | 生成技能C++类 |
| DataAssetManager | `Tools/DataAssetManager/` | `configs/*.json` | 管理PawnData/Experience/InputConfig |
| UIGenerator | `Tools/UIGenerator/` | `schemas/*.json` | 生成Widget C++ |
| AngelscriptAPIQuery | `Tools/AngelscriptAPIQuery/` | `angelscript_api_database.json/` | 查询AS API |

## Key Classes
| Class | Role |
|-------|------|
| `ADJ01Character` | 角色基类 |
| `ADJ01CharacterWithAbilities` | 带ASC的角色 |
| `UDJ01AbilitySystemComponent` | ASC扩展 |
| `UDJ01GameplayAbility` | 技能基类 |
| `UDJ01PawnExtensionComponent` | Pawn生命周期 |
| `UDJ01HeroComponent` | 玩家输入 |
| `UDJ01AnimInstance` | 动画实例 |
| `UDJ01ExperienceDefinition` | 游戏模式配置 |
| `UDJ01PawnData` | Pawn配置 |
| `UDJ01InputConfig` | 输入配置 |
| `UDJ01AbilitySet` | 技能集配置 |

## Scripts
```
Script/
├── GameAbilityAS/    # 正式AS技能
└── Test/             # 测试脚本
```

## Plugins
- `ComboGraph` - 连招图编辑器
- `CommonGame/CommonUser` - Lyra通用框架
- `ModularGameplayActors` - 模块化Actor
- `GameFeatures/RPGCombat|RPGCore` - 游戏特性

## Config Locations
| Type | Path |
|------|------|
| Attributes | `Source/DJ01/AbilitySystem/Attributes/Config/AttributeDefinitions.csv` |
| BindingSets | `Source/DJ01/AbilitySystem/Attributes/BindingSets/Config/BindingSetDefinitions.json` |
| Tags | `Source/DJ01/System/Config/GameplayTagDefinitions.csv` |
| Abilities | `Source/DJ01/AbilitySystem/Abilities/Config/AbilityDefinitions.json` |
| Executions | `Source/DJ01/AbilitySystem/Executions/Config/ExecutionDefinitions.json` |

## Generated Code Locations
| Type | Path |
|------|------|
| Attributes | `Source/DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h` |
| BindingSets | `Source/DJ01/AbilitySystem/Attributes/BindingSets/Generated/` |
| Executions | `Source/DJ01/AbilitySystem/Executions/Generated/` |
| UI | `Source/DJ01/UI/Generated/` |

## Docs
| Topic | Path |
|-------|------|
| 架构总览 | `docs/Now/Architecture_Guide.md` |
| 动画系统 | `docs/Now/AnimationSystem_Design.md` |
| 连招教程 | `docs/ComBoFirst/` |
| ComboGraph | `docs/ComboGraph/` |
| AngelScript | `docs/AngelscriptGuide/` |
| GAS | `Source/DJ01/AbilitySystem/AbilitySystem_Architecture.md` |
| 工具 | `Tools/Docs/` |

## Naming
- Actor: `ADJ01*`
- Component: `UDJ01*Component`
- Ability: `UGA_*`
- Effect: `UGE_*`
- AttributeSet: `UDJ01*Set`
- DataAsset: `UDJ01*Data`
- AnimBP: `ABP_*`
- AnimLayer: `ABP_AnimLayer_*`

## Init Order
GameMode → Experience → GFA → Character → PawnExt → ASC → HeroComponent → Ready

## ASC Access
```cpp
// From Actor
UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(Actor);
// From PlayerState (preferred)
PlayerState->GetDJ01AbilitySystemComponent();
```

## Animation
- `RootMotionMode = RootMotionFromMontagesOnly`
- Locomotion: CharacterMovement驱动
- Combat: RootMotion驱动(Montage)
- AnimLayers: 运行时通过`LinkAnimClassLayers()`切换