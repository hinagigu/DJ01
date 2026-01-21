# ABP 架构总览

> **版本**: 1.0  
> **创建日期**: 2026-01-11  
> **目标**: 理解 Lyra 风格动画蓝图架构，掌握 InPlace vs RootMotion 选择策略

---

## 📚 动画蓝图文档目录

| 序号 | 文档 | 内容 | 预计耗时 |
|------|------|------|---------|
| 00 | [本文档](./00_ABP架构总览.md) | 架构总览、InPlace vs RootMotion | 15分钟 |
| 01 | [创建主动画蓝图](./01_创建主动画蓝图.md) | ABP_DJ01Character_Base 创建 | 45分钟 |
| 02 | [状态机设计](./02_状态机设计.md) | Locomotion 状态机完整配置 | 1小时 |
| 03 | [BlendSpace创建](./03_BlendSpace创建.md) | 移动混合空间制作 | 30分钟 |
| 04 | [动画层接口实现](./04_动画层接口实现.md) | 主ABP调用ALI接口 | 45分钟 |
| 05 | [武器动画层创建](./05_武器动画层创建.md) | ABP_AnimLayer_Katana 制作 | 1小时 |
| 06 | [BindingSet集成](./06_BindingSet集成.md) | GAS属性同步到ABP | 30分钟 |
| 07 | [动画层切换](./07_动画层切换.md) | 运行时切换武器动画 | 30分钟 |

**总预计耗时**: 约 5 小时

---

## 🏗️ Lyra 风格动画架构

### 架构图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      ABP_DJ01Character_Base                              │
│                      (主动画蓝图 - 继承 UDJ01AnimInstance)               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐│
│  │  EventGraph                                                         ││
│  │  • InitializeWithAbilitySystem() ← 绑定 GAS                        ││
│  │  • 事件处理                                                         ││
│  └────────────────────────────────────────────────────────────────────┘│
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐│
│  │  AnimGraph                                                          ││
│  │                                                                      ││
│  │  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐ ││
│  │  │ Locomotion   │───→│ UpperBody    │───→│ DefaultSlot          │ ││
│  │  │ StateMachine │    │ Overlay      │    │ (Montage播放)         │ ││
│  │  └──────┬───────┘    └──────────────┘    └──────────────────────┘ ││
│  │         │                                           │               ││
│  │         │        ┌──────────────────────────────────┘               ││
│  │         │        │                                                   ││
│  │         ▼        ▼                                                   ││
│  │  ┌────────────────────┐                                             ││
│  │  │   Output Pose      │                                             ││
│  │  └────────────────────┘                                             ││
│  └────────────────────────────────────────────────────────────────────┘│
│                                                                          │
│  ╔════════════════════════════════════════════════════════════════════╗│
│  ║  实现接口: IALI_DJ01AnimLayers                                      ║│
│  ║  • FullBody_IdleState()     → 调用链接层的 Idle                     ║│
│  ║  • FullBody_MovingState()   → 调用链接层的 Move                     ║│
│  ║  • FullBody_JumpStartState() → 调用链接层的 Jump                    ║│
│  ╚════════════════════════════════════════════════════════════════════╝│
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ LinkAnimClassLayers()
                                    ▼
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ ABP_AnimLayer   │      │ ABP_AnimLayer   │      │ ABP_AnimLayer   │
│ _Unarmed        │      │ _Katana         │      │ _SwordShield    │
│                 │      │                 │      │                 │
│ 实现接口:        │      │ 实现接口:        │      │ 实现接口:        │
│ FullBody_Idle   │      │ FullBody_Idle   │      │ FullBody_Idle   │
│ FullBody_Move   │      │ FullBody_Move   │      │ FullBody_Move   │
│ ...             │      │ ...             │      │ ...             │
└─────────────────┘      └─────────────────┘      └─────────────────┘
     空手待机               刀待机                  剑盾待机
     空手移动               刀移动                  剑盾移动
```

### 核心概念

| 概念 | 说明 |
|------|------|
| **主动画蓝图** | 包含状态机骨架，通过接口函数调用具体动画 |
| **动画层接口 (ALI)** | C++ 定义的接口，声明所有动画函数 |
| **武器动画层** | 实现接口，提供具体武器的动画内容 |
| **LinkAnimClassLayers** | 运行时切换动画层的核心函数 |

---

## 🎯 InPlace vs RootMotion 完全指南

### 什么是 RootMotion？

**RootMotion** = 动画数据中包含了根骨骼的位移信息，播放动画时角色会随之移动。

```
帧 0:  角色在 (0, 0, 0)
帧 10: 角色在 (50, 0, 0)    ← 动画驱动位移
帧 20: 角色在 (100, 0, 0)
```

**InPlace** = 动画在原地播放，位移需要代码单独处理。

```
帧 0:  角色在 (0, 0, 0)     ← 动画播放
帧 10: 角色在 (0, 0, 0)     ← 位置不变
帧 20: 角色在 (0, 0, 0)     ← CharacterMovement 单独控制位置
```

### 选择决策树

```
                      ┌─────────────────────┐
                      │ 这个动画需要位移吗？ │
                      └──────────┬──────────┘
                                 │
                     ┌───────────┴───────────┐
                     │                       │
                    不需要                   需要
                     │                       │
                     ▼                       ▼
              ┌──────────┐         ┌─────────────────────┐
              │ InPlace  │         │ 位移需要精确控制吗？ │
              └──────────┘         └──────────┬──────────┘
                                              │
                                  ┌───────────┴───────────┐
                                  │                       │
                                 是的                    不需要
                                  │                       │
                                  ▼                       ▼
                           ┌────────────┐          ┌──────────┐
                           │ RootMotion │          │ InPlace  │
                           │ 动画驱动    │          │ +代码推力 │
                           └────────────┘          └──────────┘
```

### DJ01 项目推荐配置

#### 移动系统 (Locomotion)

| 状态 | 动画类型 | 来源文件夹 | 原因 |
|------|---------|-----------|------|
| **Idle** | InPlace | `*/InPlace/Idle/` 或任意 | 静止状态无需位移 |
| **Walk/Run** | ✅ **InPlace** | `*/InPlace/Walk/` | 速度由 CharacterMovement 的 MaxWalkSpeed 控制 |
| **Jump Start** | InPlace | 任意 | 起跳力由引擎物理处理 |
| **Fall Loop** | InPlace | 任意 | 空中物理由引擎处理 |
| **Land** | InPlace | 任意 | 落地后恢复控制 |

#### 攻击系统 (Combat)

| 状态 | 动画类型 | 来源文件夹 | 原因 |
|------|---------|-----------|------|
| **普通攻击** | ✅ **RootMotion** | `*/RootMotion/Attack/` | 攻击时前冲感需要与动画同步 |
| **连招攻击** | ✅ **RootMotion** | `*/RootMotion/Attack/Combo*` | 每段连招的位移距离由动画精确控制 |
| **重攻击** | ✅ **RootMotion** | `*/RootMotion/Attack/` | 大位移需要精确匹配动画 |
| **翻滚/闪避** | ✅ **RootMotion** | `*/RootMotion/Dodge/` | 闪避距离需要一致性 |

#### 受击系统 (Hit Reaction)

| 状态 | 动画类型 | 原因 |
|------|---------|------|
| **轻微受击** | InPlace + Impulse | 小击退用代码 AddImpulse 即可 |
| **重击击飞** | ✅ **RootMotion** | 大击退需要与动画匹配 |
| **死亡倒地** | ✅ **RootMotion** | 倒地动画需要精确位移 |

### 项目动画资产分析

```
Content/Characters/AnimationAssets/DynamicKatanaAnims/
├── InPlace/                    ← Locomotion 使用
│   ├── ComboAttack/            ← 可用于边移动边攻击
│   │   └── Anim_DK_Combo_A_IP.uasset
│   ├── Hit/
│   │   └── Anim_DK_Hit_Back_IP.uasset
│   └── Walk/                   ← BlendSpace 用这些！
│       ├── Anim_DK_Walk_B_IP.uasset
│       ├── Anim_DK_Walk_F_IP.uasset
│       ├── Anim_DK_Walk_L_IP.uasset
│       └── Anim_DK_Walk_R_IP.uasset
│
└── RootMotion/                 ← 攻击蒙太奇使用
    ├── Attack/                 ← 连招系统用这些！
    │   ├── Anim_DK_Combo_A_RM.uasset
    │   ├── Anim_DK_Combo_A01_RM.uasset
    │   └── ...
    ├── Hit/
    │   └── ...
    ├── Idle/
    │   └── ...
    └── Walk/                   ← 可选：带位移的移动
```

### RootMotion 配置步骤

1. **动画序列设置**
   - 打开动画序列 (如 `Anim_DK_Combo_A01_RM`)
   - 确认 `Enable Root Motion` = ✅

2. **蒙太奇设置**
   - 创建蒙太奇后，打开 Asset Details
   - `Root Motion Root Lock` = `Anim First Frame` (推荐)
   - 这样根骨骼会锁定在第一帧位置，防止"滑步"

3. **AnimInstance 设置**（二选一）
   
   **方式 A：C++ 代码设置（推荐）**
   - 在 `UDJ01AnimInstance` 构造函数中：
   ```cpp
   RootMotionMode = ERootMotionMode::RootMotionFromMontagesOnly;
   ```
   
   **方式 B：动画蓝图 Class Defaults 设置**
   - 打开动画蓝图 → Class Defaults
   - 搜索 `Root Motion Mode`
   - 设置为 `Root Motion from Montages Only`
   
   > ⚠️ **注意**：此设置在 AnimInstance 上，不是 CharacterMovementComponent！

4. **效果说明**
   - 普通移动（BlendSpace）→ CharacterMovement 控制位移
   - 攻击蒙太奇（Montage）→ RootMotion 控制位移
   - Montage Slot 会自动应用 RootMotion，AnimGraph 无需特殊处理

---

## 📁 资产命名规范

### 动画蓝图

```
ABP_                           前缀
   └── DJ01Character_Base      主动画蓝图
   └── AnimLayer_Katana        刀动画层
   └── AnimLayer_SwordShield   剑盾动画层
   └── AnimLayer_Unarmed       空手动画层
```

### 动画蒙太奇

```
AM_                            前缀 (Animation Montage)
   └── Katana_Combo_A1         刀连招A第1段
   └── Katana_Combo_A2         刀连招A第2段
   └── Katana_Dodge            刀闪避
```

### BlendSpace

```
BS_                            前缀 (Blend Space)
   └── Katana_Locomotion       刀移动混合空间
   └── Unarmed_Locomotion      空手移动混合空间
```

---

## ✅ 准备工作检查清单

开始制作动画蓝图前，请确认：

- [ ] 理解了 InPlace vs RootMotion 的区别
- [ ] 确认了项目中动画资产的 IP/RM 分类
- [ ] 明确了要使用的武器类型 (建议从 Katana 开始)
- [ ] 已阅读 `ALI_DJ01AnimLayers.h` 了解接口函数

---

## 📞 下一步

架构已清晰，让我们开始创建第一个动画蓝图！

👉 **[进入第一章：创建主动画蓝图](./01_创建主动画蓝图.md)**