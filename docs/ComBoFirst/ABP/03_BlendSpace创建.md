# 03. BlendSpace 创建

> **预计耗时**: 30 分钟  
> **前置条件**: 已完成 02_状态机设计

---

## 🎯 本章目标

创建移动 BlendSpace，实现：

1. ✅ 4方向移动动画混合 (前/后/左/右)
2. ✅ 速度驱动的 Idle → Walk → Jog 过渡
3. ✅ 平滑的方向转换

---

## 📚 BlendSpace 类型选择

> ⚠️ **UE 5.x 重要变化**: Blend Space 1D 已被废弃，现在只有 **Blend Space (2D)**。

| 使用方式 | 轴配置 | 适用场景 |
|---------|--------|---------|
| **双轴模式** | Direction + Speed | 有完整方向动画时 (推荐) |
| **单轴模式** | 只用 Speed 轴 | 只有前进动画时 |

### 推荐方案：双轴 BlendSpace

项目已有完整的 4 方向动画 (Pistol/Rifle/Unarmed)，使用 **Direction + Speed** 双轴：

```
        Speed (Y轴)
          ▲
    600   │  Jog_B    Jog_L    Jog_F    Jog_R    Jog_B
          │
    200   │  Walk_B   Walk_L   Walk_F   Walk_R   Walk_B
          │
      0   │  Idle     Idle     Idle     Idle     Idle
          └────────────────────────────────────────────→ Direction (X轴)
              -180     -90       0       90      180
               (后)    (左)    (前)     (右)     (后)
```

### 可用动画资产

| 武器类型 | 路径 | Walk | Jog | 跳跃 |
|---------|------|------|-----|------|
| **Pistol** | `Locomotion/Pistol/` | ✅ F/B/L/R | ✅ F/B/L/R | ✅ |
| **Rifle** | `Locomotion/Rifle/` | ✅ F/B/L/R | ✅ F/B/L/R | ✅ |
| **Unarmed** | `Locomotion/Unarmed/` | ✅ F/B/L/R | ✅ F/B/L/R | ✅ |

> 💡 已有现成 BlendSpace 可参考：`BS_MM_Unarmed_Jog_Walk.uasset`

```
┌─────────────────────────────────────────┐
│            BlendSpace 2D                 │
│                                          │
│     Direction                            │
│        ▲                                 │
│   -180 │  FL   F   FR                   │
│        │   L  Idle  R                   │
│    180 │  BL   B   BR                   │
│        └────────────────→ Speed         │
│            0    150   600               │
└─────────────────────────────────────────┘
```

---

## 📝 创建 BlendSpace (双轴模式 - 推荐)

### Step 1: 创建资产

1. **在内容浏览器中导航到**:
   ```
   Content/Characters/Heroes/HeroAnimations/BlendSpaces/
   ```
   (如果没有这个文件夹，请创建)

2. **右键 → Animation → Blend Space**

3. **选择骨骼**: 你的角色骨骼

4. **命名为**: `BS_Pistol_Locomotion` (或 `BS_Rifle_Locomotion` 等)

5. **双击打开**

---

### Step 2: 配置轴

在 **Asset Details** 面板 (右侧) 的 **Axis Settings** 中：

**Horizontal Axis (水平轴 - 方向)**:
- Name: `Direction`
- Minimum Axis Value: `-180`
- Maximum Axis Value: `180`
- Number of Grid Divisions: `4`

**Vertical Axis (垂直轴 - 速度)**:
- Name: `Speed`
- Minimum Axis Value: `0`
- Maximum Axis Value: `600`
- Number of Grid Divisions: `2`

---

### Step 3: 添加动画样本 (以 Pistol 为例)

动画路径: `Content/Characters/Heroes/Mannequin_Mesh/Animations/Locomotion/Pistol/`

**布局示意图**:

```
Speed (Y)
    ▲
600 │  Jog_Bwd   Jog_Left   Jog_Fwd   Jog_Right   Jog_Bwd
    │
200 │  Walk_Bwd  Walk_Left  Walk_Fwd  Walk_Right  Walk_Bwd  
    │
  0 │  Idle      Idle       Idle      Idle        Idle
    └─────────────────────────────────────────────────────→ Direction (X)
        -180      -90         0         90        180
        (后)      (左)       (前)       (右)       (后)
```

**具体动画位置**:

| 位置 (Dir, Speed) | 动画文件 |
|-------------------|----------|
| (0, 0) | `MM_Pistol_Idle_Hipfire` |
| (0, 200) | `MM_Pistol_Walk_Fwd` |
| (0, 600) | `MM_Pistol_Jog_Fwd` |
| (-90, 0) | `MM_Pistol_Idle_Hipfire` |
| (-90, 200) | `MM_Pistol_Walk_Left` |
| (-90, 600) | `MM_Pistol_Jog_Left` |
| (90, 0) | `MM_Pistol_Idle_Hipfire` |
| (90, 200) | `MM_Pistol_Walk_Right` |
| (90, 600) | `MM_Pistol_Jog_Right` |
| (180, 0) | `MM_Pistol_Idle_Hipfire` |
| (180, 200) | `MM_Pistol_Walk_Bwd` |
| (180, 600) | `MM_Pistol_Jog_Bwd` |
| (-180, 0) | `MM_Pistol_Idle_Hipfire` |
| (-180, 200) | `MM_Pistol_Walk_Bwd` |
| (-180, 600) | `MM_Pistol_Jog_Bwd` |

> 💡 **注意**：-180 和 180 使用相同动画 (都是后退)，形成循环

**添加方式**:
1. 从内容浏览器拖动动画到 BlendSpace 编辑器网格
2. 放置到对应的 (Direction, Speed) 位置
3. 可以按住 Ctrl 微调位置

---

### Step 4: 调整混合参数

在 **Blend Space → Sample Interpolation** 设置中：

- **Interpolation Time**: `0.15` (混合响应时间)
- **Target Weight Interpolation Speed Per Sec**: `5.0`

---

## 📝 其他武器 BlendSpace

复制上述步骤创建其他武器的 BlendSpace：

| BlendSpace 名称 | 动画路径 |
|-----------------|----------|
| `BS_Rifle_Locomotion` | `Locomotion/Rifle/MM_Rifle_*` |
| `BS_Unarmed_Locomotion` | `Locomotion/Unarmed/MM_Unarmed_*` |

> 💡 或者直接复制 `BS_MM_Unarmed_Jog_Walk.uasset` 作为模板修改

---

## 🔧 C++ 变量支持

`MoveDirection` 变量已在 C++ 中自动计算：

```cpp
// DJ01AnimInstance.h
UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
float GroundSpeed = 0.0f;

UPROPERTY(BlueprintReadOnly, Category = "Character State Data|Physics")
float MoveDirection = 0.0f;  // -180 到 180
```

```cpp
// DJ01AnimInstance.cpp - NativeUpdateAnimation 中
GroundSpeed = CharMoveComp->Velocity.Size2D();

if (GroundSpeed > 1.0f)
{
    const FVector Velocity = CharMoveComp->Velocity;
    const FRotator ActorRotation = Character->GetActorRotation();
    MoveDirection = CalculateDirection(Velocity, ActorRotation);
}
```

---

## 🔧 在动画蓝图中使用

### 在状态机 Moving 状态中使用 BlendSpace

**方式一：直接在状态中使用**

```
[BS_Pistol_Locomotion] ← Direction: [MoveDirection]
         │              ← Speed: [GroundSpeed]
         ▼
[Output Animation Pose]
```

**方式二：在动画层实现中使用 (推荐)**

```
// ABP_AnimLayer_Pistol 的 Ranged_MovingState 实现
[BS_Pistol_Locomotion] ← Direction: [MoveDirection]
         │              ← Speed: [GroundSpeed]
         ▼
[Return Node]
```

### 连接步骤

1. 在 AnimGraph 中右键搜索你创建的 BlendSpace 名称
2. 拖出 **Direction** 引脚 → 连接 `MoveDirection` 变量
3. 拖出 **Speed** 引脚 → 连接 `GroundSpeed` 变量
4. 输出连接到 State Result 或 Return Node

---

## 🎨 BlendSpace 预览

在 BlendSpace 编辑器中：

1. **拖动预览点**: 在网格上拖动绿色预览点
2. **查看混合结果**: 右侧预览窗口显示混合动画
3. **调整权重**: 确保过渡平滑

---

## ✅ 完成检查清单

- [ ] 创建了 BlendSpace 资产 (`BS_Pistol_Locomotion` 等)
- [ ] 配置了双轴: Direction (-180~180) + Speed (0~600)
- [ ] 添加了所有方向的动画样本 (F/B/L/R × Idle/Walk/Jog)
- [ ] -180 和 180 位置使用相同后退动画
- [ ] 预览混合效果平滑
- [ ] C++ 已有 `MoveDirection` 变量 (自动计算)

---

## ⚠️ 常见问题

### Q: BlendSpace 中动画不显示？

**A**: 确保：
1. 动画使用相同骨骼
2. 动画已导入且有效
3. 检查资产是否损坏

### Q: 移动时动画跳变？

**A**: 
1. 增加 Interpolation Time (如 0.2)
2. 检查动画样本位置是否正确
3. 确保动画循环设置正确

### Q: 没有足够的方向动画？

**A**: 
1. 使用 BlendSpace 1D + Root Motion Warping
2. 或使用 AimOffset 处理方向
3. 或镜像现有动画

---

## 📞 下一步

BlendSpace 完成！接下来实现动画层接口，让状态机能正确调用这些动画。

👉 **[进入第四章：动画层接口实现](./04_动画层接口实现.md)**