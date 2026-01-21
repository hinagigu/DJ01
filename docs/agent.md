# DJ01 项目 Agent 指南

> **目的**: 为 AI 助手/大模型提供项目快速了解指南  
> **更新日期**: 2025

---

## 🎯 项目概述

**DJ01** 是一个基于 **Unreal Engine 5** 的 RPG 动作游戏项目。

| 项目信息 | 详情 |
|----------|------|
| **引擎版本** | Unreal Engine 5.x |
| **架构基础** | Epic Games Lyra Starter Game |
| **脚本语言** | C++ + AngelScript |
| **核心系统** | Gameplay Ability System (GAS) |
| **开发工具** | 多个 Python 自动化工具 |

---

## 📁 项目结构

```
DJ01/
├── Source/                    # C++ 源代码
│   ├── DJ01/                  # 主游戏模块
│   │   ├── AbilitySystem/     # GAS 技能系统 (核心)
│   │   ├── Animation/         # 动画系统
│   │   ├── Camera/            # 相机系统
│   │   ├── Character/         # 角色系统
│   │   ├── Combo/             # 连招系统
│   │   ├── Experience/        # 游戏体验/模式系统
│   │   ├── Input/             # 输入系统
│   │   ├── Player/            # 玩家控制器/状态
│   │   ├── System/            # 基础系统类
│   │   ├── Team/              # 队伍系统
│   │   └── UI/                # UI 系统
│   ├── DJ01Editor/            # 编辑器模块
│   └── GameFeatureActions/    # 可复用的 GFA
│
├── Script/                    # AngelScript 脚本
│   ├── GameAbilityAS/         # 技能脚本
│   └── Test/                  # 测试脚本
│
├── Plugins/                   # 插件
│   ├── ComboGraph/            # 连招图插件
│   ├── CommonGame/            # 通用游戏框架
│   ├── CommonUser/            # 通用用户系统
│   ├── ModularGameplayActors/ # 模块化 Actor
│   ├── GameplayMessageRouter/ # 消息路由
│   ├── UIExtension/           # UI 扩展
│   ├── LoadingScreen/         # 加载屏幕
│   └── GameFeatures/          # 游戏特性插件
│       ├── RPGCombat/         # RPG 战斗特性
│       └── RPGCore/           # RPG 核心特性
│
├── Tools/                     # Python 开发工具
│   ├── AttributeGenerator/    # GAS 属性生成器
│   ├── AbilityMaker/          # 技能生成器
│   ├── DataAssetManager/      # 数据资产管理器
│   ├── UIGenerator/           # UI 生成器
│   ├── AngelscriptAPIQuery/   # AS API 查询工具
│   └── Docs/                  # 工具文档
│
├── Content/                   # UE 内容资产
│   ├── Characters/            # 角色资产
│   ├── Gameplay/              # 游戏玩法资产
│   ├── Input/                 # 输入配置
│   ├── System/                # 系统配置
│   └── UI/                    # UI 资产
│
└── docs/                      # 项目文档
    ├── AngelscriptGuide/      # AngelScript 指南
    ├── ComBoFirst/            # 连招系统教程
    ├── ComboGraph/            # ComboGraph 插件文档
    ├── DJ01_ABILITY_SYSTEM/   # GAS 系统文档
    └── Now/                   # 当前架构文档
```

---

## 🔧 核心工具集

### 1. AttributeGenerator (属性生成器)
**路径**: `Tools/AttributeGenerator/`

自动生成 GAS 相关代码：
- **Attributes**: 属性集 (AttributeSet) 代码生成
- **BindingSets**: 动画蓝图绑定宏生成
- **Tags**: GameplayTag 定义生成
- **MMC**: ModifierMagnitudeCalculation 生成
- **Executions**: GameplayEffectExecutionCalculation 生成

**配置文件**:
- `Source/DJ01/AbilitySystem/Attributes/Config/AttributeDefinitions.csv`
- `Source/DJ01/AbilitySystem/Attributes/BindingSets/Config/BindingSetDefinitions.json`
- `Source/DJ01/System/Config/GameplayTagDefinitions.csv`

**运行**: `python Tools/AttributeGenerator/main.py`

---

### 2. AbilityMaker (技能生成器)
**路径**: `Tools/AbilityMaker/`

生成 GAS 技能类代码：
- 从 JSON 配置生成 C++ 技能类
- 支持自定义技能模板

**配置文件**: `Source/DJ01/AbilitySystem/Abilities/Config/AbilityDefinitions.json`

**运行**: `python Tools/AbilityMaker/main.py`

---

### 3. DataAssetManager (数据资产管理器)
**路径**: `Tools/DataAssetManager/`

管理 UE 数据资产：
- **PawnData**: 角色配置
- **Experience**: 游戏体验配置
- **InputConfig**: 输入配置
- **AbilitySet**: 技能集配置
- **ActionSet**: 动作集配置

**核心特性**:
- 与 UE Editor 通过 Python 脚本通信
- Schema 驱动的配置验证
- 可视化编辑界面

**配置目录**: `Tools/DataAssetManager/configs/`

**运行**: `python Tools/DataAssetManager/main.py` 或 `Tools/DataAssetManager/run.bat`

---

### 4. UIGenerator (UI 生成器)
**路径**: `Tools/UIGenerator/`

生成 UMG Widget 代码：
- 从 JSON Schema 生成 C++ Widget 类
- 支持 MVVM 模式
- 自动生成蓝图基类

**运行**: `python Tools/UIGenerator/main.py` 或 `Tools/UIGenerator/RunUIGenerator.bat`

---

### 5. AngelscriptAPIQuery (API 查询)
**路径**: `Tools/AngelscriptAPIQuery/`

查询 AngelScript API：
- 完整的 API 数据库 (JSON 格式)
- 支持按类型查询
- 生成 Markdown 文档

**数据库**: `Tools/AngelscriptAPIQuery/angelscript_api_database.json/`

---

## 🏗️ 核心架构

### 系统关系图

```
┌─────────────────────────────────────────────────────────────────┐
│                        游戏启动流程                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  GameMode → GameState → ExperienceManager                       │
│                              │                                  │
│                              ▼                                  │
│                    ExperienceDefinition                         │
│                     ┌─────────────────┐                         │
│                     │ • GameFeatures  │                         │
│                     │ • PawnData      │                         │
│                     │ • Actions       │                         │
│                     │ • ActionSets    │                         │
│                     └────────┬────────┘                         │
│                              │                                  │
│              ┌───────────────┼───────────────┐                  │
│              ▼               ▼               ▼                  │
│         PawnData      GameFeatures    ActionSets               │
│              │               │               │                  │
│              ▼               ▼               ▼                  │
│         Character    GFA_AddAbilities  GFA_AddWidgets          │
│              │                                                  │
│    ┌─────────┼─────────┐                                        │
│    ▼         ▼         ▼                                        │
│  PawnExt  Camera    Hero                                        │
│  Component Component Component                                   │
│    │                   │                                        │
│    ▼                   ▼                                        │
│   ASC              InputConfig                                  │
│    │                                                            │
│    ▼                                                            │
│  Abilities + Attributes                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 核心类速查

| 类名 | 职责 | 路径 |
|------|------|------|
| `ADJ01Character` | 角色基类 | `Source/DJ01/Character/` |
| `ADJ01CharacterWithAbilities` | 带 GAS 的角色 | `Source/DJ01/Character/` |
| `UDJ01AbilitySystemComponent` | ASC 扩展 | `Source/DJ01/AbilitySystem/` |
| `UDJ01GameplayAbility` | 技能基类 | `Source/DJ01/AbilitySystem/Abilities/` |
| `UDJ01PawnExtensionComponent` | Pawn 生命周期管理 | `Source/DJ01/Character/` |
| `UDJ01HeroComponent` | 玩家输入处理 | `Source/DJ01/Character/` |
| `UDJ01CameraComponent` | 相机控制 | `Source/DJ01/Camera/` |
| `UDJ01ExperienceDefinition` | 游戏体验配置 | `Source/DJ01/Experience/` |
| `UDJ01PawnData` | Pawn 配置数据 | `Source/DJ01/Character/` |
| `UDJ01InputConfig` | 输入配置 | `Source/DJ01/Input/` |
| `UDJ01AbilitySet` | 技能集配置 | `Source/DJ01/AbilitySystem/` |
| `UDJ01AnimInstance` | 动画实例 | `Source/DJ01/Animation/` |

---

## 🎮 GAS (Gameplay Ability System)

### 属性系统

**生成的属性集**:
- 配置: `Source/DJ01/AbilitySystem/Attributes/Config/AttributeDefinitions.csv`
- 生成: `Source/DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h`

**BindingSet (动画绑定)**:
- 配置: `Source/DJ01/AbilitySystem/Attributes/BindingSets/Config/BindingSetDefinitions.json`
- 生成: `Source/DJ01/AbilitySystem/Attributes/BindingSets/Generated/`

### 技能系统

**技能激活策略**:
| 策略 | 说明 |
|------|------|
| `OnInputTriggered` | 按键触发 |
| `WhileInputActive` | 按住持续 |
| `OnSpawn` | 生成时自动激活 |

**激活组**:
| 组 | 行为 |
|------|------|
| `Independent` | 独立运行 |
| `Exclusive_Replaceable` | 可被替换 |
| `Exclusive_Blocking` | 阻止其他 |

### Tag 系统

**Tag 配置**: `Source/DJ01/System/Config/GameplayTagDefinitions.csv`

**常用 Tag 前缀**:
- `InputTag.*` - 输入标签
- `Ability.*` - 技能标签
- `State.*` - 状态标签
- `Event.*` - 事件标签
- `Cooldown.*` - 冷却标签

---

## 🎬 动画系统

### 架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    ABP_DJ01Character_Base                        │
│                    (主动画蓝图)                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Locomotion State Machine                   │   │
│   │   ┌───────┐     ┌───────┐     ┌───────┐                │   │
│   │   │ Idle  │ ──► │ Walk  │ ──► │  Run  │                │   │
│   │   └───┬───┘     └───────┘     └───────┘                │   │
│   │       │                                                 │   │
│   │       ▼                                                 │   │
│   │   Linked Anim Layer 节点                                │   │
│   │   (调用动画层接口)                                       │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   Linked Layers: [可运行时切换]                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
   ABP_AnimLayer_Katana  ABP_AnimLayer_Sword  ABP_AnimLayer_Unarmed
```

### 关键文件

| 文件 | 说明 |
|------|------|
| `DJ01AnimInstance.h/cpp` | 动画实例基类 |
| `ALI_DJ01AnimLayers.h` | 动画层接口 |
| `BindingSet_*.h` | GAS 属性到动画变量的绑定宏 |

### Root Motion 配置

```cpp
// DJ01AnimInstance.cpp
RootMotionMode = ERootMotionMode::RootMotionFromMontagesOnly;
```

- **移动**: CharacterMovement 驱动
- **攻击**: Root Motion 驱动 (从蒙太奇)

---

## 📜 AngelScript

### 目录结构

```
Script/
├── GameAbilityAS/      # 正式技能脚本
│   └── GA_*.as         # 技能实现
├── Test/               # 测试脚本
├── Binds.Cache         # 绑定缓存
└── Binds.Cache.Headers # 绑定头文件缓存
```

### 技能脚本模板

```angelscript
// Script/GameAbilityAS/GA_Example.as

class UGA_Example : UDJ01GameplayAbility
{
    default ActivationPolicy = EDJ01AbilityActivationPolicy::OnInputTriggered;
    
    UFUNCTION(BlueprintOverride)
    void ActivateAbility()
    {
        // 技能逻辑
        EndAbility();
    }
}
```

### API 查询

使用 `Tools/AngelscriptAPIQuery/` 查询可用 API：
```bash
python Tools/AngelscriptAPIQuery/api_query.py UDJ01GameplayAbility
```

---

## 📊 连招系统 (ComboGraph)

### 插件位置
`Plugins/ComboGraph/`

### 核心概念

```
┌─────────────────────────────────────────────────────────────────┐
│                        ComboGraph                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Entry ──► Node_Attack1 ──► Node_Attack2 ──► Node_Attack3     │
│                  │               │               │              │
│                  ▼               ▼               ▼              │
│              Montage1        Montage2        Montage3           │
│                                                                 │
│   每个节点可配置:                                                │
│   • 播放的蒙太奇                                                 │
│   • 输入窗口时机                                                 │
│   • 分支条件                                                     │
│   • GAS 效果                                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 相关技能类
`Source/DJ01/Combo/Public/DJ01ComboGraphAbility.h`

---

## 📚 重要文档

| 文档 | 路径 | 说明 |
|------|------|------|
| 架构指南 | `docs/Now/Architecture_Guide.md` | 完整架构说明 |
| 动画系统 | `docs/Now/AnimationSystem_Design.md` | 动画架构 |
| 连招教程 | `docs/ComBoFirst/00_Overview.md` | 连招系统教程 |
| ComboGraph | `docs/ComboGraph/README.md` | 插件文档 |
| AngelScript | `docs/AngelscriptGuide/README.md` | AS 使用指南 |
| GAS 系统 | `docs/DJ01_ABILITY_SYSTEM/` | 技能系统文档 |
| 工具文档 | `Tools/Docs/README.md` | 开发工具文档 |

---

## ⚡ 常用操作

### 添加新属性

1. 编辑 `Source/DJ01/AbilitySystem/Attributes/Config/AttributeDefinitions.csv`
2. 运行 `python Tools/AttributeGenerator/main.py`
3. 重新编译 C++

### 添加新技能 (AngelScript)

1. 在 `Script/GameAbilityAS/` 创建 `GA_NewAbility.as`
2. 继承 `UDJ01GameplayAbility`
3. 在 AbilitySet 中配置

### 添加新技能 (C++)

1. 编辑 `Source/DJ01/AbilitySystem/Abilities/Config/AbilityDefinitions.json`
2. 运行 `python Tools/AbilityMaker/main.py`
3. 重新编译 C++

### 修改动画绑定

1. 编辑 `Source/DJ01/AbilitySystem/Attributes/BindingSets/Config/BindingSetDefinitions.json`
2. 运行 `python Tools/AttributeGenerator/main.py`
3. 在 AnimInstance 中调用生成的宏

### 创建数据资产

1. 运行 `python Tools/DataAssetManager/main.py`
2. 使用 GUI 编辑配置
3. 点击生成

---

## 🔍 调试技巧

### GAS 调试
```
控制台命令: ShowDebug AbilitySystem
```

### 日志通道
```cpp
// DJ01LogChannels.h
DECLARE_LOG_CATEGORY_EXTERN(LogDJ01, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogDJ01Ability, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogDJ01Experience, Log, All);
```

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| ASC 为空 | 初始化时序 | 使用延迟初始化模式 |
| 技能无法激活 | Tag 阻塞 | 检查 Block/Cancel Tags |
| 属性未同步 | 网络复制 | 确保 DOREPLIFETIME |
| 动画不播放 | 骨骼不匹配 | 检查动画层骨骼 |

---

## 🏷️ 命名约定

| 类型 | 前缀 | 示例 |
|------|------|------|
| Actor | A | `ADJ01Character` |
| Component | U | `UDJ01CameraComponent` |
| Interface | I | `IDJ01TeamAgentInterface` |
| Ability | UGA_ | `UGA_Attack` |
| Effect | UGE_ | `UGE_Damage` |
| AttributeSet | U...Set | `UDJ01HealthSet` |
| DataAsset | U...Data | `UDJ01PawnData` |
| AnimInstance | U...AnimInstance | `UDJ01AnimInstance` |
| AnimBlueprint | ABP_ | `ABP_DJ01Character_Base` |
| AnimLayer | ABP_AnimLayer_ | `ABP_AnimLayer_Katana` |

---

## 📝 快速参考

### 初始化顺序

```
1. GameMode::InitGame
2. ExperienceManager::LoadExperience
3. GameFeatureActions 执行
4. Character::PossessedBy
5. PawnExtension::InitializeAbilitySystem
6. HeroComponent::InitializePlayerInput
7. OnPawnReadyToInitialize 广播
```

### ASC 获取方式

```cpp
// 从 Actor
UAbilitySystemComponent* ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(Actor);

// 从 PlayerState (推荐)
if (ADJ01PlayerState* PS = GetPlayerState<ADJ01PlayerState>())
{
    UDJ01AbilitySystemComponent* ASC = PS->GetDJ01AbilitySystemComponent();
}

// 从 AnimInstance
if (AActor* Owner = GetOwningActor())
{
    ASC = UAbilitySystemGlobals::GetAbilitySystemComponentFromActor(Owner);
}
```

### 技能激活

```cpp
// 通过 Tag
ASC->AbilityInputTagPressed(InputTag);

// 通过 Class
ASC->TryActivateAbilityByClass(AbilityClass);

// 通过 Handle
ASC->TryActivateAbility(AbilityHandle);
```

---

**文档版本**: v1.0  
**适用项目**: DJ01  
**维护**: 请在项目架构变更时更新此文档