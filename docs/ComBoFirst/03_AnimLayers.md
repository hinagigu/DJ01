# 第三章：动画层系统

> **预计耗时**: 2小时  
> **前置要求**: 已完成 [02_AnimBlueprint.md](./02_AnimBlueprint.md)  
> **本章目标**: 创建武器动画层蓝图，实现运行时切换机制

---

## 📋 本章任务清单

- [ ] 理解动画层接口 (ALI) 系统
- [ ] 创建第一个武器动画层 (ALB_Katana)
- [ ] 实现各动画层函数
- [ ] 配置武器切换机制
- [ ] 创建其他武器动画层

---

## 3.1 动画层系统概述

### 什么是动画层接口 (Animation Layer Interface)?

动画层接口是 UE5 提供的一种机制，允许动画蓝图定义可被"覆盖"的函数。

**核心思想**:
- **主 ABP**: 定义"我需要一个 Idle 动画"
- **链接层 ABP**: 定义"这是刀的 Idle 动画" / "这是剑盾的 Idle 动画"
- **运行时**: 根据装备切换具体实现

### 架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                    IALI_DJ01AnimLayers                          │
│                       (C++ 接口)                                 │
│                                                                  │
│   ┌───────────────────────────────────────────────────────┐    │
│   │  BlueprintImplementableEvent                           │    │
│   │  + FullBody_IdleState() → FPoseLink                   │    │
│   │  + FullBody_MovingState() → FPoseLink                 │    │
│   │  + FullBody_JumpStartState() → FPoseLink              │    │
│   │  + FullBody_FallLoopState() → FPoseLink               │    │
│   │  + FullBody_LandState() → FPoseLink                   │    │
│   │  + UpperBody_Overlay() → FPoseLink                    │    │
│   └───────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                    implements│
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   ALB_Katana    │  │ ALB_SwordShield │  │  ALB_TwinSword  │
│                 │  │                 │  │                 │
│  IdleState()    │  │  IdleState()    │  │  IdleState()    │
│  = 刀待机动画   │  │  = 剑盾待机     │  │  = 双刀待机     │
│                 │  │                 │  │                 │
│  MovingState()  │  │  MovingState()  │  │  MovingState()  │
│  = 刀移动混合   │  │  = 剑盾移动     │  │  = 双刀移动     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## 3.2 创建武器动画层蓝图

### 步骤 1: 创建蓝图

1. 在内容浏览器中导航到:
   ```
   Content/Characters/Heroes/HeroAnimations/AnimLayers/
   ```
   (如不存在则创建此目录)

2. **右键** → **Animation** → **Animation Blueprint**

3. 在弹窗中:
   - **Parent Class**: `AnimInstance` (或 `UDJ01AnimInstance`)
   - **Target Skeleton**: 选择你的角色骨架

4. 命名为 `ALB_Katana`

### 步骤 2: 添加接口

1. 打开 `ALB_Katana`
2. 进入 **Class Settings**
3. 在 **Interfaces** → **Implemented Interfaces** 中点击 **Add**
4. 搜索并添加 `ALI_DJ01AnimLayers`

### 步骤 3: 确认函数出现

添加接口后，在 **My Blueprint** 面板的 **Functions** 下应该出现:
- `FullBody_IdleState` (Interface)
- `FullBody_MovingState` (Interface)
- ... 等接口函数

---

## 3.3 实现动画层函数

### 3.3.1 实现 FullBody_IdleState

1. 双击 `FullBody_IdleState` 进入图表
2. 添加动画序列节点:
   ```
   [Sequence Player: Katana_Idle] ──→ [Return Node]
   ```

3. 配置 Sequence Player:
   - **Sequence**: 选择 `Katana_Idle` 动画
   - **Loop Animation**: ✅

### 3.3.2 实现 FullBody_MovingState

移动状态通常使用 BlendSpace 来混合不同速度的动画:

1. 双击 `FullBody_MovingState`
2. 添加 BlendSpace 节点:
   ```
   [BlendSpace: BS_Katana_Locomotion]
        │
        ├── Speed (输入参数)
        │
        ▼
   [Return Node]
   ```

### 创建 BlendSpace (如果尚未存在)

1. **右键** → **Animation** → **Blend Space 1D**
2. 选择骨架
3. 命名为 `BS_Katana_Locomotion`
4. 配置:
   - **Axis Settings**:
     - Horizontal Axis: `Speed`, Range: 0 ~ 600
   - **Sample Points**:
     - 0: `Katana_Idle`
     - 150: `Katana_Walk`
     - 600: `Katana_Run`

### 3.3.3 跳跃相关函数

#### FullBody_JumpStartState
```
[Sequence Player: Katana_JumpStart] ──→ [Return Node]
```
- **Loop Animation**: ❌ (不循环)

#### FullBody_FallLoopState
```
[Sequence Player: Katana_FallLoop] ──→ [Return Node]
```
- **Loop Animation**: ✅

#### FullBody_LandState
```
[Sequence Player: Katana_Land] ──→ [Return Node]
```
- **Loop Animation**: ❌

---

## 3.4 获取变量

动画层蓝图需要访问主 ABP 的变量 (如 GroundSpeed):

### 方法 1: 通过 Property Access (推荐)

1. 在动画图表中添加 **Property Access** 节点
2. 配置路径: `Get Owning Component → Get Owner → ...`

### 方法 2: 通过 Get Linked Anim Layer Instance

```
[Get Linked Anim Layer Instance By Class]
    │
    ├── Class: ABP_DJ01Character_Base
    │
    ▼
[Get GroundSpeed] ──→ [使用变量]
```

### 方法 3: 在链接层中声明同名变量

在 `ALB_Katana` 中声明:
```cpp
UPROPERTY(BlueprintReadOnly)
float GroundSpeed;
```

然后在 EventGraph 中同步:
```
Event Blueprint Update Animation
    │
    ▼
[Get Owning Actor] → [Get Velocity] → [Vector Length XY] → [Set GroundSpeed]
```

---

## 3.5 完整的 ALB_Katana 示例

### AnimGraph 结构

虽然大部分逻辑在接口函数中，但有时需要额外的 AnimGraph:

```
ALB_Katana AnimGraph:

[Input Pose] ──→ [Output Pose]
    │
    └──→ (可选: 添加全局修改，如 IK 调整)
```

> 💡 **注意**: 链接层蓝图的 AnimGraph 通常很简单，主要逻辑在接口函数中

### 函数实现概览

| 函数 | 实现 |
|------|------|
| `FullBody_IdleState` | Sequence: `Katana_Idle` |
| `FullBody_MovingState` | BlendSpace1D: `BS_Katana_Locomotion` |
| `FullBody_JumpStartState` | Sequence: `Katana_JumpStart` |
| `FullBody_FallLoopState` | Sequence: `Katana_FallLoop` |
| `FullBody_LandState` | Sequence: `Katana_Land` |
| `UpperBody_Overlay` | (暂时返回空 Pose) |

---

## 3.6 配置武器切换机制

### 切换函数调用

在角色蓝图或 C++ 中:

```cpp
// 获取 Mesh 组件的 AnimInstance
UAnimInstance* AnimInstance = Mesh->GetAnimInstance();

// 链接武器动画层
AnimInstance->LinkAnimClassLayers(ALB_Katana::StaticClass());
```

蓝图版本:
```
[Get Mesh] → [Get Anim Instance] → [Link Anim Class Layers]
                                          │
                                          └── New Class: ALB_Katana
```

### 切换时机

| 时机 | 触发方式 |
|------|---------|
| **游戏开始** | BeginPlay 中根据默认武器链接 |
| **装备武器** | 装备系统触发 |
| **拾取武器** | 拾取逻辑触发 |

### 示例: 角色蓝图中的武器切换

```
Custom Event: OnWeaponEquipped
    │
    ├── Input: WeaponType (Enum)
    │
    ▼
[Switch on WeaponType]
    │
    ├── Katana ──→ [Link Anim Class Layers: ALB_Katana]
    ├── SwordShield ──→ [Link Anim Class Layers: ALB_SwordShield]
    └── TwinSword ──→ [Link Anim Class Layers: ALB_TwinSword]
```

---

## 3.7 创建其他武器动画层

### 任务清单

| 动画层 | 武器类型 | 状态 |
|--------|---------|------|
| `ALB_Katana` | 刀 | ⬜ 待创建 |
| `ALB_SwordShield` | 剑盾 | ⬜ 待创建 |
| `ALB_TwinSword` | 双刀 | ⬜ 待创建 |
| `ALB_Unarmed` | 空手/默认 | ⬜ 待创建 |

### 复用技巧

1. **创建基础模板**:
   - 完成 `ALB_Katana` 后
   - 复制为 `ALB_SwordShield`
   - 修改引用的动画资产

2. **使用动画重定向**:
   - 如果不同武器可以共用部分动画
   - 使用 Retarget 从一套动画生成另一套

---

## 3.8 调试动画层

### 显示当前链接的层

在控制台:
```
ShowDebug Animation
```

在输出中查找 "Linked Anim Layers" 信息。

### 检查函数是否被调用

1. 在接口函数实现中添加 Print 节点
2. 运行游戏查看输出

### 常见问题排查

| 问题 | 可能原因 | 解决方案 |
|------|---------|---------|
| 动画不切换 | 未调用 LinkAnimClassLayers | 检查切换逻辑 |
| 动画错误 | 链接层引用了错误的动画 | 检查 Sequence Player 设置 |
| T-Pose | 接口函数未实现 | 确保所有函数都有返回值 |
| 变量不同步 | 链接层获取不到主 ABP 变量 | 使用 Property Access 或同步更新 |

---

## 3.9 高级: 动画层组合

### 上半身覆盖

当需要在移动时播放上半身攻击:

1. 在主 ABP 中配置 Layered Blend:
   ```
   [LocomotionSM Output]
          │
          ▼
   [Layered Blend per Bone]
          │
          ├── Base: LocomotionSM 输出
          │
          └── Layer 1: UpperBody_Overlay()
                  │
                  └── Blend Mask: Spine 以上
   ```

2. 在链接层中实现 `UpperBody_Overlay()`:
   ```
   [Slot 'UpperBody'] ──→ [Return Node]
   ```

### 效果

- 下半身: 继续播放移动动画
- 上半身: 播放攻击蒙太奇

---

## 3.10 验证清单

### 单个动画层验证

- [ ] ALB 蓝图无编译错误
- [ ] 所有接口函数已实现
- [ ] 动画引用正确

### 切换机制验证

- [ ] 游戏开始时链接正确的默认层
- [ ] 切换武器时动画层正确更新
- [ ] 切换过渡平滑（无明显跳变）

### 运行时验证

- [ ] 各武器的 Idle 动画正确
- [ ] 各武器的移动混合正确
- [ ] 跳跃动画序列完整

---

## 3.11 下一步

完成本章后，你应该有:

✅ 至少一个完整的武器动画层 (`ALB_Katana`)  
✅ 理解动画层接口的工作原理  
✅ 实现了武器切换机制  
✅ (可选) 多个武器的动画层蓝图

接下来我们将配置 GameplayTags 和 BindingSet，为技能系统做准备。

---

👉 **[进入第四章：Tags 与 BindingSet](./04_TagsAndBindings.md)**