# 第一章：动画资产准备

> **预计耗时**: 2小时  
> **前置要求**: 已阅读 [00_Overview.md](./00_Overview.md)  
> **本章目标**: 制作攻击蒙太奇，配置 AnimNotify，设置连招窗口

---

## 📋 本章任务清单

- [ ] 理解项目动画资产结构
- [ ] 创建第一个攻击蒙太奇 (Katana Combo A - 第一段)
- [ ] 配置 AnimNotifyState_ComboWindow (连招窗口)
- [ ] 配置 AnimNotify 触发点 (伤害、特效)
- [ ] 批量制作完整连招序列 (4段)

---

## 1.1 动画资产目录结构

### 当前资源位置

```
Content/Characters/AnimationAssets/
├── DynamicKatanaAnims/              ← 刀 (推荐首选)
│   ├── ComboA/
│   │   ├── Katana_Attack_A1.uasset
│   │   ├── Katana_Attack_A2.uasset
│   │   ├── Katana_Attack_A3.uasset
│   │   └── Katana_Attack_A4.uasset
│   ├── ComboB/
│   ├── ComboC/
│   ├── ComboD/
│   ├── Hit_Reactions/
│   └── Movement/
│
├── DynamicSwordAndShield/           ← 剑盾
│   ├── ComboA/
│   ├── ComboB/
│   ├── Block/
│   └── Dodge/
│
├── TwinSwordAnims/                  ← 双刀
│   ├── ComboA/
│   ├── Block/
│   └── Dodge/
│
└── HandsomeSwordCombatAnims/        ← 单手剑
    └── Various attack anims
```

### 建议的蒙太奇资产目录

```
Content/Characters/Heroes/HeroAnimations/Montages/
├── Katana/
│   ├── AM_Katana_ComboA_1.uasset
│   ├── AM_Katana_ComboA_2.uasset
│   ├── AM_Katana_ComboA_3.uasset
│   └── AM_Katana_ComboA_4.uasset
├── SwordAndShield/
└── TwinSword/
```

---

## 1.2 创建攻击蒙太奇

### 步骤 1: 找到源动画

1. 在内容浏览器中导航到:
   ```
   Content/Characters/AnimationAssets/DynamicKatanaAnims/ComboA/
   ```

2. 找到 `Katana_Attack_A1` 动画序列

### 步骤 2: 创建蒙太奇

1. **右键** `Katana_Attack_A1` → **Create** → **Create AnimMontage**

2. 重命名为 `AM_Katana_ComboA_1`

3. 移动到目标目录:
   ```
   Content/Characters/Heroes/HeroAnimations/Montages/Katana/
   ```

### 步骤 3: 配置蒙太奇

打开蒙太奇，进行以下设置:

#### 3.1 设置 Slot

在 Montage 面板中:
- **Slot Name**: `DefaultGroup.UpperBody` (或你定义的攻击 Slot)

> 💡 **Slot 选择指南**:
> - `UpperBody`: 仅上半身动画，下半身可保持移动
> - `FullBody`: 全身动画，用于需要完整控制的攻击
> - 后续我们会在 ABP 中配置对应的 Slot Node

#### 3.2 添加 Section

蒙太奇默认有一个 `Default` Section，我们需要确认其设置:

1. 在时间轴上方的 **Sections** 轨道
2. 确保 Section 覆盖整个动画

---

## 1.3 配置连招窗口 (ComboWindow)

ComboGraph 插件提供了 `UAnimNotifyState_ComboWindow`，用于定义连招输入窗口。

### 步骤 1: 添加 ComboWindow NotifyState

1. 在蒙太奇时间轴下方的 **Notifies** 轨道
2. **右键** → **Add Notify State** → **Combo Window**

### 步骤 2: 调整窗口时机

拖动 NotifyState 的起止点:

```
时间轴示意:
|----[动画播放]----------------------|
        |=====ComboWindow=====|
        ↑                     ↑
      开窗时机              关窗时机
      (约40%)               (约80%)
```

**推荐参数**:
| 攻击段数 | 开窗时机 | 关窗时机 | 说明 |
|---------|---------|---------|------|
| 第1段 | 40% | 85% | 窗口较大，方便衔接 |
| 第2段 | 45% | 80% | 略微收紧 |
| 第3段 | 50% | 85% | 中等窗口 |
| 第4段 | - | - | 最后一段无需窗口 |

### 步骤 3: 配置 ComboWindow 属性

选中 ComboWindow NotifyState，在 Details 面板配置:

| 属性 | 值 | 说明 |
|------|-----|------|
| **Combo Window Tag** | `Ability.ComboWindow.Light` | 标识窗口类型 |
| **bTriggerOnStart** | true | 窗口开始时触发 |
| **bTriggerOnEnd** | true | 窗口结束时触发 |

> 💡 **Combo Window Tag 用途**:  
> ComboGraph 节点可以指定 "仅在特定窗口内接受输入"  
> 例如: 轻攻击只在 `Light` 窗口接受，重攻击需要 `Heavy` 窗口

---

## 1.4 配置攻击触发点

### AnimNotify 类型选择

| Notify 类型 | 用途 | 触发方式 |
|-------------|------|---------|
| `ANS_ComboWindow` | 连招输入窗口 | State (时间段) |
| `AN_PlaySound` | 攻击音效 | 单点 |
| `ANS_TrailEffect` | 武器拖尾 | State |
| `AN_HitCheck` (自定义) | 伤害检测 | 单点或State |

### 步骤 1: 添加音效 Notify

1. **右键 Notifies 轨道** → **Add Notify** → **Play Sound**
2. 放置在攻击挥砍的瞬间
3. 配置 Sound 属性

### 步骤 2: 添加伤害检测点

有两种方式处理伤害:

#### 方式 A: 使用 GameplayEvent (推荐)

1. **Add Notify** → **Send Gameplay Event**
2. 配置:
   - **Event Tag**: `Event.Montage.DamageWindow.Start`

这个事件会被 ComboGraph 或 Ability 捕获，触发伤害检测逻辑。

#### 方式 B: 使用自定义 Notify (高级)

创建 `UAnimNotify_MeleeHitCheck`:
- 在 Notify 触发时执行碰撞检测
- 对命中目标应用 GameplayEffect

### 步骤 3: 添加武器拖尾

1. **Add Notify State** → **Trail**
2. 配置:
   - **PSTemplate**: 选择拖尾粒子
   - **First Socket Name**: `WeaponBase`
   - **Second Socket Name**: `WeaponTip`

---

## 1.5 完整蒙太奇示例

以下是配置完成后的蒙太奇时间轴示意:

```
AM_Katana_ComboA_1 时间轴:

[Section: Default]
|====================动画播放====================|

[Slot: UpperBody]

[Notifies]
                    ▼ PlaySound (挥砍声)
|----[Trail拖尾]-------------------------|
          |=====ComboWindow=====|
                 ▼ SendGameplayEvent (伤害检测)
```

### Notify 时间点参考

| Notify | 时间点 | 说明 |
|--------|-------|------|
| Trail Start | 20% | 武器开始移动 |
| PlaySound | 35% | 挥砍瞬间 |
| ComboWindow Start | 40% | 可接受下一段输入 |
| DamageEvent | 45% | 伤害判定点 |
| ComboWindow End | 85% | 输入窗口关闭 |
| Trail End | 60% | 拖尾结束 |

---

## 1.6 批量制作连招序列

### 任务清单

为 Katana ComboA 制作完整的4段连招:

| 蒙太奇 | 源动画 | 状态 |
|--------|-------|------|
| `AM_Katana_ComboA_1` | `Katana_Attack_A1` | ⬜ 待制作 |
| `AM_Katana_ComboA_2` | `Katana_Attack_A2` | ⬜ 待制作 |
| `AM_Katana_ComboA_3` | `Katana_Attack_A3` | ⬜ 待制作 |
| `AM_Katana_ComboA_4` | `Katana_Attack_A4` | ⬜ 待制作 |

### 批量制作步骤

1. **重复 1.2-1.5** 的步骤为每个动画创建蒙太奇

2. **注意事项**:
   - 第4段 (最后一段) **不需要** ComboWindow
   - 每段的伤害时间点需要根据动画调整
   - 可以复制第一个蒙太奇的 Notify 配置，然后调整时间

### 快速复制技巧

1. 创建好第一个蒙太奇后，打开它
2. 在 Notifies 轨道选中所有 Notify
3. **Ctrl+C** 复制
4. 打开第二个蒙太奇
5. **Ctrl+V** 粘贴
6. 调整各 Notify 的时间点

---

## 1.7 Root Motion 设置

### 什么是 Root Motion?

Root Motion 是将动画中角色的位移应用到实际角色移动的技术。

**适用场景**:
- 冲刺攻击 (角色向前移动)
- 重击 (大幅度位移)
- 翻滚闪避

### 启用 Root Motion

> ⚠️ **重要**: Root Motion 设置在 **源动画序列** 中，不是在蒙太奇中！

#### 步骤 1: 配置源动画序列

打开 **Animation Sequence**（如 `Katana_Attack_A1`），在 Asset Details 面板:

| 属性 | 推荐值 | 说明 |
|------|--------|------|
| **Enable Root Motion** | ✅ | 启用动画位移提取 |
| **Force Root Lock** | ☐ | 通常不勾选 |
| **Root Motion Root Lock** | `Anim First Frame` | 锁定根骨骼到第一帧位置，防止滑步 |

#### 步骤 2: 蒙太奇自动继承

蒙太奇会自动从源动画序列继承 Root Motion 数据，无需额外设置。

#### Root Motion Root Lock 选项说明

| 选项 | 效果 |
|------|------|
| `Ref Pose` | 锁定到参考姿势（T-Pose）位置 |
| `Anim First Frame` | 🌟 锁定到动画第一帧位置（推荐） |
| `Zero` | 锁定到世界原点 |

> 💡 **推荐 `Anim First Frame`**: 确保角色从当前位置开始移动，避免"瞬移"或"滑步"

---

## 1.8 验证蒙太奇

### 在 Persona 中预览

1. 双击打开蒙太奇
2. 在预览面板点击 **Play**
3. 检查:
   - [ ] 动画正确播放
   - [ ] Notify 在正确时间触发 (查看输出日志)
   - [ ] ComboWindow 时机合理

### 在编辑器中测试

1. 创建一个测试 Ability 或蓝图
2. 调用 `PlayMontage` 播放蒙太奇
3. 观察:
   - [ ] Slot 是否正确
   - [ ] 动画是否与其他动画正确混合

---

## 1.9 下一步

完成本章后，你应该有:

✅ 4个 Katana ComboA 蒙太奇 (`AM_Katana_ComboA_1` ~ `4`)  
✅ 每个蒙太奇配置了 ComboWindow (除最后一段)  
✅ 每个蒙太奇配置了基本的 Notify (声音、伤害事件)

---

## 📚 参考资源

### 相关文件

- **ComboWindow 源码**: `Plugins/ComboGraph/Source/ComboGraph/Public/Notifies/ComboGraphANS_ComboWindow.h`
- **项目 Notify 配置**: (待创建)

### 扩展阅读

- [UE5 Animation Montage 官方文档](https://docs.unrealengine.com/5.0/en-US/animation-montage-in-unreal-engine/)
- [Root Motion 官方文档](https://docs.unrealengine.com/5.0/en-US/root-motion-in-unreal-engine/)

---

👉 **[进入第二章：动画蓝图设计](./02_AnimBlueprint.md)**