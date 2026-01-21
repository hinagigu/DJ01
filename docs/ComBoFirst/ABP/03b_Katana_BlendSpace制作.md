# 03b. Katana BlendSpace 制作指南

> **预计耗时**: 15 分钟  
> **前置条件**: 动画已重定向到项目骨架
> **本章产出**: `BS_Katana_Locomotion` BlendSpace

---

## 🎯 目标

创建一个 **2D BlendSpace**，实现 Katana 持刀状态下的 8 方向移动混合。

---

## 📦 动画资源清单

### 资源路径 (重定向后)

```
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/
```

> 📁 文件系统路径: `Content/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/`

### Idle 动画

| 动画文件 | 用途 | 搜索关键词 |
|----------|------|-----------|
| `Idle/Anim_KT3_Idle_RM` | 待机 | `KT3_Idle` |

### Walk 动画 (8 方向)

| 动画文件 | 方向 | Direction 值 | 搜索关键词 |
|----------|------|-------------|-----------|
| `Locomotion/Anim_KT3_Walk_F_RM` | 前 | 0 | `KT3_Walk_F` |
| `Locomotion/Anim_KT3_Walk_FL_RM` | 左前 | -45 | `KT3_Walk_FL` |
| `Locomotion/Anim_KT3_Walk_L_RM` | 左 | -90 | `KT3_Walk_L` |
| `Locomotion/Anim_KT3_Walk_BL_RM` | 左后 | -135 | `KT3_Walk_BL` |
| `Locomotion/Anim_KT3_Walk_B_RM` | 后 | ±180 | `KT3_Walk_B` |
| `Locomotion/Anim_KT3_Walk_BR_RM` | 右后 | 135 | `KT3_Walk_BR` |
| `Locomotion/Anim_KT3_Walk_R_RM` | 右 | 90 | `KT3_Walk_R` |
| `Locomotion/Anim_KT3_Walk_FR_RM` | 右前 | 45 | `KT3_Walk_FR` |

### Run 动画 (8 方向)

| 动画文件 | 方向 | Direction 值 | 搜索关键词 |
|----------|------|-------------|-----------|
| `Locomotion/Anim_KT3_Run_F_RM` | 前 | 0 | `KT3_Run_F` |
| `Locomotion/Anim_KT3_Run_FL_RM` | 左前 | -45 | `KT3_Run_FL` |
| `Locomotion/Anim_KT3_Run_L_RM` | 左 | -90 | `KT3_Run_L` |
| `Locomotion/Anim_KT3_Run_BL_RM` | 左后 | -135 | `KT3_Run_BL` |
| `Locomotion/Anim_KT3_Run_B_RM` | 后 | ±180 | `KT3_Run_B` |
| `Locomotion/Anim_KT3_Run_BR_RM` | 右后 | 135 | `KT3_Run_BR` |
| `Locomotion/Anim_KT3_Run_R_RM` | 右 | 90 | `KT3_Run_R` |
| `Locomotion/Anim_KT3_Run_FR_RM` | 右前 | 45 | `KT3_Run_FR` |

> ⚠️ **注意**: 如果有 `_RM1` 后缀的版本，那可能是重定向后的版本，优先使用那些！

---

## 📝 Step 1: 创建 BlendSpace

1. **导航到目标文件夹**:
   ```
   /Game/Characters/Heroes/HeroAnimations/BlendSpaces/
   ```
   (如果没有这个文件夹，请创建)

2. **右键 → Animation → Blend Space**

3. **选择骨骼**: 选择你角色使用的骨骼
   - 搜索 `SK_Mannequin` 或你项目的骨骼名称

4. **命名**: `BS_Katana_Locomotion`

5. **双击打开**

> 💡 **搜索技巧**: 在 Content Browser 搜索栏输入动画名称时，使用 `/Game/Characters/Heroes/HeroAnimations/` 作为路径过滤

---

## 📝 Step 2: 配置轴参数

在 **Asset Details** 面板中设置：

### Horizontal Axis (水平轴 - Direction)

| 属性 | 值 |
|------|-----|
| **Name** | `Direction` |
| **Minimum Axis Value** | `-180` |
| **Maximum Axis Value** | `180` |
| **Number of Grid Divisions** | `8` |

### Vertical Axis (垂直轴 - Speed)

| 属性 | 值 |
|------|-----|
| **Name** | `Speed` |
| **Minimum Axis Value** | `0` |
| **Maximum Axis Value** | `600` |
| **Number of Grid Divisions** | `2` |

```
┌─────────────────────────────────────────────────────────────────┐
│  BlendSpace 轴配置预览                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Speed (Y)                                                       │
│    ▲                                                             │
│600 ┼─────────────────────────────────────────────  Run 层       │
│    │                                                             │
│    │                                                             │
│200 ┼─────────────────────────────────────────────  Walk 层      │
│    │                                                             │
│    │                                                             │
│  0 ┼─────────────────────────────────────────────  Idle 层      │
│    └────┼────┼────┼────┼────┼────┼────┼────┼────→ Direction (X) │
│       -180 -135 -90  -45   0   45   90  135  180                │
│        (B)  (BL) (L) (FL) (F) (FR) (R) (BR) (B)                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 Step 3: 添加动画样本点

### 方法 A: 搜索并拖拽 (推荐)

1. 在 **BlendSpace 编辑器底部** 有 Asset Browser 面板

2. **在搜索栏输入关键词**:
   - 搜索 `KT3_Idle` 找到 Idle 动画
   - 搜索 `KT3_Walk_F` 找到前进 Walk 动画
   - 以此类推...

3. **拖拽到网格对应位置**

4. **微调坐标**: 
   - 选中样本点
   - 在右侧 Details 面板精确设置 X/Y 值

### 方法 B: 使用 Analyzer 自动放置

1. 点击 BlendSpace 空白处
2. 在 Details 面板找到 **Analysis Properties**
3. 设置 Horizontal Axis 为 `Locomotion Orientation`
4. 设置 Vertical Axis 为 `Locomotion Speed`
5. 拖入动画，系统自动计算位置

> 💡 **搜索过滤**: 可以在搜索栏输入 `KT3` 快速过滤出所有 Katana V3 动画

---

## 📝 Step 4: 放置所有动画

### 完整放置表

按照下表放置每个动画到对应坐标：

| 动画文件 | Direction (X) | Speed (Y) | 位置说明 |
|----------|---------------|-----------|----------|
| **Idle 层 (Speed = 0)** ||||
| `Anim_KT3_Idle_RM` | 0 | 0 | 中心待机 |
| `Anim_KT3_Idle_RM` | -180 | 0 | 左边界 (复用) |
| `Anim_KT3_Idle_RM` | 180 | 0 | 右边界 (复用) |
| **Walk 层 (Speed = 200)** ||||
| `Anim_KT3_Walk_F_RM` | 0 | 200 | 前走 |
| `Anim_KT3_Walk_FL_RM` | -45 | 200 | 左前走 |
| `Anim_KT3_Walk_L_RM` | -90 | 200 | 左走 |
| `Anim_KT3_Walk_BL_RM` | -135 | 200 | 左后走 |
| `Anim_KT3_Walk_B_RM` | -180 | 200 | 后走 (左边界) |
| `Anim_KT3_Walk_B_RM` | 180 | 200 | 后走 (右边界) |
| `Anim_KT3_Walk_BR_RM` | 135 | 200 | 右后走 |
| `Anim_KT3_Walk_R_RM` | 90 | 200 | 右走 |
| `Anim_KT3_Walk_FR_RM` | 45 | 200 | 右前走 |
| **Run 层 (Speed = 600)** ||||
| `Anim_KT3_Run_F_RM` | 0 | 600 | 前跑 |
| `Anim_KT3_Run_FL_RM` | -45 | 600 | 左前跑 |
| `Anim_KT3_Run_L_RM` | -90 | 600 | 左跑 |
| `Anim_KT3_Run_BL_RM` | -135 | 600 | 左后跑 |
| `Anim_KT3_Run_B_RM` | -180 | 600 | 后跑 (左边界) |
| `Anim_KT3_Run_B_RM` | 180 | 600 | 后跑 (右边界) |
| `Anim_KT3_Run_BR_RM` | 135 | 600 | 右后跑 |
| `Anim_KT3_Run_R_RM` | 90 | 600 | 右跑 |
| `Anim_KT3_Run_FR_RM` | 45 | 600 | 右前跑 |

### 可视化布局

```
┌─────────────────────────────────────────────────────────────────┐
│  BlendSpace 动画布局                                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Speed                                                           │
│    ▲                                                             │
│    │                                                             │
│600 │  Run_B  Run_BL  Run_L  Run_FL  Run_F  Run_FR  Run_R  Run_BR  Run_B
│    │    ●───────●───────●───────●───────●───────●───────●───────●───────●
│    │                                                             │
│    │                                                             │
│200 │  Walk_B Walk_BL Walk_L Walk_FL Walk_F Walk_FR Walk_R Walk_BR Walk_B
│    │    ●───────●───────●───────●───────●───────●───────●───────●───────●
│    │                                                             │
│    │                                                             │
│  0 │  Idle   Idle   Idle   Idle   Idle   Idle   Idle   Idle   Idle
│    │    ●───────●───────●───────●───────●───────●───────●───────●───────●
│    │                                                             │
│    └────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼────→
│       -180   -135    -90    -45     0     45     90    135    180
│                                                                  │
│  Direction                                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> ⚠️ **重要**: -180 和 180 位置使用**相同的动画** (Walk_B/Run_B)，确保方向循环无缝！

---

## 📝 Step 5: 配置混合参数

在 **Asset Details** 面板中：

### Blend Parameters

| 属性 | 推荐值 | 说明 |
|------|--------|------|
| **Target Weight Interpolation Speed Per Sec** | `5.0` | 动画混合速度 |

### Sample Interpolation

| 属性 | 推荐值 | 说明 |
|------|--------|------|
| **Interpolation Time** | `0.0` | 插值时间 (0 = 即时响应) |

### Axis Settings

确保两个轴的 **Snap to Grid** 已启用，方便精确放置。

---

## 📝 Step 6: 预览测试

1. **在 BlendSpace 编辑器底部**:
   - 可以看到预览窗口

2. **按住 Ctrl + 鼠标拖动**:
   - 在网格上移动查看混合效果

3. **检查项**:
   - [ ] 各方向切换是否平滑
   - [ ] Walk 和 Run 之间过渡是否自然
   - [ ] 边界 (-180/180) 是否无缝

4. **保存**: Ctrl + S

---

## 📝 Step 7: 在动画蓝图中使用

在 `ABP_AnimLayer_Katana` 的 `Melee_MovingState` 函数中：

```
┌─────────────────────────────────────────────────────────────────┐
│  Melee_MovingState 实现                                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [BlendSpace Player]                                            │
│      │                                                           │
│      ├── BlendSpace: BS_Katana_Locomotion                       │
│      │                                                           │
│      ├── X (Direction): ←── [MoveDirection] (来自 C++)          │
│      │                                                           │
│      └── Y (Speed): ←────── [GroundSpeed] (来自 C++)            │
│                │                                                 │
│                ▼                                                 │
│         [Output Pose]                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 节点连接

1. 右键 → 搜索 **BlendSpace Player**
2. 选择 `BS_Katana_Locomotion`
3. 连接输入:
   - `X (Direction)` ← 拖出引脚 → Get `MoveDirection`
   - `Y (Speed)` ← 拖出引脚 → Get `GroundSpeed`
4. 输出连接到 Return Node

---

## ✅ 完成检查清单

- [ ] 创建了 `BS_Katana_Locomotion` BlendSpace
- [ ] 设置了 Horizontal Axis: Direction (-180 ~ 180)
- [ ] 设置了 Vertical Axis: Speed (0 ~ 600)
- [ ] 放置了 Idle 动画 (3个点: -180, 0, 180)
- [ ] 放置了 Walk 动画 (9个点)
- [ ] 放置了 Run 动画 (9个点)
- [ ] -180 和 180 使用相同的后退动画
- [ ] 预览测试各方向混合正常
- [ ] 保存资产

---

## 📋 快速查找清单

### 搜索关键词与坐标对照表

在 BlendSpace 的 Asset Browser 中搜索以下关键词，拖到对应坐标：

```
=== Idle 层 (Y=0) ===
搜索: KT3_Idle     → 拖到 (0, 0)
搜索: KT3_Idle     → 拖到 (-180, 0)   [同一个动画]
搜索: KT3_Idle     → 拖到 (180, 0)    [同一个动画]

=== Walk 层 (Y=200) ===
搜索: KT3_Walk_F   → 拖到 (0, 200)    [注意不要选到 FL/FR]
搜索: KT3_Walk_FL  → 拖到 (-45, 200)
搜索: KT3_Walk_L   → 拖到 (-90, 200)  [注意不要选到 BL/FL]
搜索: KT3_Walk_BL  → 拖到 (-135, 200)
搜索: KT3_Walk_B   → 拖到 (-180, 200) [注意不要选到 BL/BR]
搜索: KT3_Walk_B   → 拖到 (180, 200)  [同一个动画]
搜索: KT3_Walk_BR  → 拖到 (135, 200)
搜索: KT3_Walk_R   → 拖到 (90, 200)   [注意不要选到 BR/FR]
搜索: KT3_Walk_FR  → 拖到 (45, 200)

=== Run 层 (Y=600) ===
搜索: KT3_Run_F    → 拖到 (0, 600)    [注意不要选到 FL/FR]
搜索: KT3_Run_FL   → 拖到 (-45, 600)
搜索: KT3_Run_L    → 拖到 (-90, 600)  [注意不要选到 BL/FL]
搜索: KT3_Run_BL   → 拖到 (-135, 600)
搜索: KT3_Run_B    → 拖到 (-180, 600) [注意不要选到 BL/BR]
搜索: KT3_Run_B    → 拖到 (180, 600)  [同一个动画]
搜索: KT3_Run_BR   → 拖到 (135, 600)
搜索: KT3_Run_R    → 拖到 (90, 600)   [注意不要选到 BR/FR]
搜索: KT3_Run_FR   → 拖到 (45, 600)
```

**总计: 21 个样本点**

### 动画文件完整路径

如需精确查找，完整路径如下：

```
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Idle/Anim_KT3_Idle_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_F_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_FL_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_L_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_BL_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_B_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_BR_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_R_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Walk_FR_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_F_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_FL_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_L_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_BL_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_B_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_BR_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_R_RM
/Game/Characters/Heroes/HeroAnimations/DynamicKatanaAnimsV3/RootMotion/Locomotion/Anim_KT3_Run_FR_RM
```

> 💡 **提示**: 如果搜索结果有 `_RM` 和 `_RM1` 两个版本，选择对应你角色骨架的那个版本。

---

## 📞 下一步

BlendSpace 创建完成后，继续创建 Katana 动画层：

👉 **[返回第五章：武器动画层创建](./05_武器动画层创建.md)**