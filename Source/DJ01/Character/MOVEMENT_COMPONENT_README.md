# DJ01 角色移动组件设计文档

## 概述

`UDJ01CharacterMovementComponent` 是为 RPG 游戏优化的角色移动组件，相比 Lyra 的版本进行了简化，移除了射击游戏所需的复杂网络优化，保留了 RPG 游戏所需的核心功能。

## 设计理念

### 与 Lyra 的差异

| 特性 | Lyra | DJ01 (RPG) | 理由 |
|------|------|-----------|------|
| 加速度优化 | ✅ 压缩网络复制 | ❌ 使用默认 | RPG 移动较慢，不需要精细优化 |
| 地面检测 | ✅ 详细信息 | ✅ 简化版本 | 保留用于音效和特效 |
| GAS 集成 | ✅ 完整实现 | ⏸️ 预留接口 | 等待 GAS 系统实现 |
| 蹲伏跳跃 | ✅ 支持 | ❌ 使用默认 | RPG 较少使用 |
| 代码量 | 132 行 | ~180 行（含注释） | 更清晰易懂 |

### 核心原则

1. **简单优先**：只实现 RPG 必需的功能
2. **可扩展性**：预留 GAS 集成接口
3. **性能适中**：不过度优化，保持代码可读性
4. **易于维护**：详细注释，清晰的代码结构

## 功能特性

### 1. 地面信息检测

```cpp
const FDJ01CharacterGroundInfo& GetGroundInfo();
```

**用途：**
- 🔊 根据地面材质播放不同的脚步声（草地、石头、金属等）
- ✨ 根据地面类型生成粒子特效（灰尘、水花、雪花等）
- 🎮 检测特殊地面（岩浆、冰面、毒沼等）

**优化：**
- 自动缓存，同一帧内多次调用不会重复检测
- 在地面行走时使用引擎提供的地板信息（零开销）
- 在空中时才执行射线检测

**示例用法（蓝图）：**
```cpp
// 在 AnimNotify 或脚步声事件中
UDJ01CharacterMovementComponent* MoveComp = Character->FindComponentByClass<UDJ01CharacterMovementComponent>();
const FDJ01CharacterGroundInfo& GroundInfo = MoveComp->GetGroundInfo();

if (GroundInfo.GroundHitResult.PhysMaterial.IsValid())
{
    // 根据物理材质播放不同的声音
    UPhysicalMaterial* PhysMat = GroundInfo.GroundHitResult.PhysMaterial.Get();
    PlayFootstepSound(PhysMat);
}
```

### 2. RPG 优化的移动参数

```cpp
// 构造函数中的配置
MaxAcceleration = 1800.0f;              // 适中的加速度
BrakingDecelerationWalking = 1200.0f;   // 舒适的制动速度
bOrientRotationToMovement = true;       // 面向移动方向旋转
RotationRate = FRotator(0.0f, 540.0f, 0.0f); // 适中的旋转速度
```

**与 Lyra 的对比：**
- Lyra MaxAcceleration: 2400.0f（快节奏射击游戏）
- DJ01 MaxAcceleration: 1800.0f（适合 RPG 的节奏）

### 3. GAS 集成接口（待实现）

#### GetMaxSpeed() - 速度控制

```cpp
// 未来实现后的效果：
// Status.MovementStopped -> 0% 速度（定身、眩晕）
// Status.MovementSlowed -> 50% 速度（减速）
// Status.MovementHasted -> 150% 速度（加速）
```

**使用场景：**
- 🧊 冰冻、定身、石化：完全无法移动
- 🐌 减速 Debuff：降低移动速度
- ⚡ 加速 Buff：提高移动速度
- 🏃 疾跑技能：临时加速

#### GetDeltaRotation() - 旋转控制

```cpp
// 未来实现后的效果：
// Status.RotationLocked -> 锁定旋转（释放技能时）
```

**使用场景：**
- 🎯 锁定目标：释放定向技能时强制面向目标
- 🛡️ 格挡状态：格挡时锁定朝向
- 🎬 过场动画：播放动画时控制朝向

## 文件结构

```
Source/DJ01/Character/
├── Public/
│   ├── DJ01CharacterMovementComponent.h    # 移动组件头文件
│   └── DJ01Character.h                      # 角色类头文件
├── Private/
│   ├── DJ01CharacterMovementComponent.cpp  # 移动组件实现
│   └── DJ01Character.cpp                    # 角色类实现（已更新使用新组件）
└── MOVEMENT_COMPONENT_README.md            # 本文档
```

## 使用方法

### 在 C++ 中使用

```cpp
// 获取移动组件
UDJ01CharacterMovementComponent* MoveComp = Cast<UDJ01CharacterMovementComponent>(Character->GetCharacterMovement());

// 获取地面信息
const FDJ01CharacterGroundInfo& GroundInfo = MoveComp->GetGroundInfo();
UE_LOG(LogTemp, Log, TEXT("Distance to ground: %f"), GroundInfo.GroundDistance);

// 检查地面材质
if (GroundInfo.GroundHitResult.bBlockingHit)
{
    if (UPhysicalMaterial* PhysMat = GroundInfo.GroundHitResult.PhysMaterial.Get())
    {
        // 处理不同的物理材质
    }
}
```

### 在蓝图中使用

1. 获取角色的 Movement Component
2. 转换为 `DJ01CharacterMovementComponent`
3. 调用 `Get Ground Info` 节点
4. 从返回的结构体中获取地面信息

## 扩展指南

### 添加新的移动模式

如果需要添加冲刺、翻滚等自定义移动模式：

```cpp
// 1. 在头文件中添加自定义移动模式枚举
UENUM(BlueprintType)
enum class EDJ01CustomMovementMode : uint8
{
    CMOVE_Dodge      UMETA(DisplayName = "Dodge"),  // 翻滚闪避
    CMOVE_Sprint     UMETA(DisplayName = "Sprint"), // 冲刺
    CMOVE_MAX        UMETA(Hidden)
};

// 2. 重写 PhysCustom 函数
virtual void PhysCustom(float deltaTime, int32 Iterations) override;

// 3. 实现自定义移动逻辑
void UDJ01CharacterMovementComponent::PhysCustom(float deltaTime, int32 Iterations)
{
    if (CustomMovementMode == (uint8)EDJ01CustomMovementMode::CMOVE_Dodge)
    {
        PhysDodge(deltaTime, Iterations);
    }
    else
    {
        Super::PhysCustom(deltaTime, Iterations);
    }
}
```

### 集成 GAS

当准备实现 Gameplay Ability System 时：

1. 取消注释 `GetMaxSpeed()` 和 `GetDeltaRotation()` 函数
2. 定义游戏所需的 GameplayTag（在项目的 GameplayTags 定义文件中）
3. 创建对应的 GameplayEffect 来应用这些标签
4. 测试不同状态下的移动和旋转

## 调试工具

### 控制台变量

```
DJ01.Character.GroundTraceDistance [值]
```

用于调整地面检测的最大距离（单位：厘米），默认 500cm。

**用法示例：**
```
# 增加检测距离到 10 米
DJ01.Character.GroundTraceDistance 1000
```

### 可视化调试

建议在开发时启用以下调试功能：

```cpp
// 在 PlayerController 或调试类中
if (GEngine)
{
    UDJ01CharacterMovementComponent* MoveComp = Character->FindComponentByClass<UDJ01CharacterMovementComponent>();
    const FDJ01CharacterGroundInfo& GroundInfo = MoveComp->GetGroundInfo();
    
    // 显示地面距离
    GEngine->AddOnScreenDebugMessage(-1, 0.0f, FColor::Green, 
        FString::Printf(TEXT("Ground Distance: %.2f"), GroundInfo.GroundDistance));
    
    // 绘制地面检测射线
    if (GroundInfo.GroundHitResult.bBlockingHit)
    {
        DrawDebugLine(GetWorld(), 
            Character->GetActorLocation(), 
            GroundInfo.GroundHitResult.ImpactPoint, 
            FColor::Red, false, 0.1f, 0, 2.0f);
    }
}
```

## 常见问题

### Q: 为什么角色不朝向控制器方向旋转？

A: RPG 通常使用 `bOrientRotationToMovement = true`，角色会自动朝向移动方向。如果需要朝向控制器方向（如射击游戏），可以在 Character 中设置：
```cpp
bUseControllerRotationYaw = true;
DJ01MoveComp->bOrientRotationToMovement = false;
```

### Q: 如何实现疾跑功能？

A: 有两种方式：
1. **简单方式（不依赖 GAS）**：在移动组件中添加 `bSprinting` 变量，在 `GetMaxSpeed()` 中检查并返回加速后的速度
2. **推荐方式（使用 GAS）**：创建疾跑 Ability，应用带有 `Status.MovementHasted` 标签的 GameplayEffect

### Q: 地面检测的性能开销如何？

A: 非常低。在角色站在地面上时，直接使用引擎已经计算好的地板信息（零额外开销）。只有在空中时才会执行一次射线检测，且结果会缓存到当前帧结束。

## 未来计划

- [ ] 实现 GAS 集成的速度和旋转控制
- [ ] 添加冲刺/翻滚自定义移动模式
- [ ] 添加攀爬系统
- [ ] 添加游泳和飞行移动模式
- [ ] 性能分析和优化

## 参考资料

- [Unreal Engine CharacterMovementComponent 文档](https://docs.unrealengine.com/en-US/API/Runtime/Engine/GameFramework/UCharacterMovementComponent/)
- [Lyra Starter Game 源码分析](https://docs.unrealengine.com/en-US/lyra-sample-game-in-unreal-engine/)
- 项目内部文档：<a href="file:d:\UnrealProjects\DJ01\Source\DJ01\Character\README.md">Character 系统架构</a>