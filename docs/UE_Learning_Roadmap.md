# 🎮 UE 游戏客户端开发 - 求职必学知识路线图

> **目标**: 以获得 UE 游戏客户端开发工作为导向  
> **基础**: 配合 DJ01 项目边学边练  
> **创建日期**: 2025-12-19

---

## 📋 目录

1. [岗位要求分析](#1-岗位要求分析)
2. [知识优先级总览](#2-知识优先级总览)
3. [Phase 1: 必备基础](#3-phase-1-必备基础-4-6周)
4. [Phase 2: Gameplay 核心](#4-phase-2-gameplay-核心-4-6周)
5. [Phase 3: GAS 技能系统](#5-phase-3-gas-技能系统-4-8周)
6. [Phase 4: 动画与表现](#6-phase-4-动画与表现-3-4周)
7. [Phase 5: AI 与网络](#7-phase-5-ai-与网络-4-6周)
8. [Phase 6: 图形学入门](#8-phase-6-图形学入门-持续学习)
9. [面试准备](#9-面试准备)
10. [学习资源汇总](#10-学习资源汇总)

---

## 1. 岗位要求分析

### 1.1 常见 JD 关键词提取

根据主流游戏公司 (腾讯/网易/米哈游/莉莉丝等) UE 客户端岗位要求：

| 要求频率 | 技能点 | 优先级 |
|----------|--------|--------|
| ⭐⭐⭐⭐⭐ | C++ 扎实基础 | P0 |
| ⭐⭐⭐⭐⭐ | UE 框架理解 (Actor/Component/GameMode) | P0 |
| ⭐⭐⭐⭐⭐ | Gameplay 开发经验 | P0 |
| ⭐⭐⭐⭐ | GAS 技能系统 | P1 |
| ⭐⭐⭐⭐ | 动画系统 | P1 |
| ⭐⭐⭐ | AI 行为树 | P2 |
| ⭐⭐⭐ | UI (UMG/Slate) | P2 |
| ⭐⭐⭐ | 网络同步 | P2 |
| ⭐⭐ | 性能优化 | P3 |
| ⭐⭐ | 渲染/Shader | P3 |

### 1.2 岗位分类与侧重

```
┌─────────────────────────────────────────────────────────┐
│                    UE 客户端开发                         │
├─────────────────┬─────────────────┬────────────────────┤
│   战斗/技能向    │    系统框架向    │     表现/TA向      │
├─────────────────┼─────────────────┼────────────────────┤
│ GAS 深度        │ 架构设计        │ 动画系统           │
│ 战斗系统        │ 性能优化        │ 材质/Shader        │
│ AI 行为         │ 网络同步        │ 特效/Niagara       │
│ 动画集成        │ 工具开发        │ 渲染管线           │
└─────────────────┴─────────────────┴────────────────────┘
         ↑ 推荐从这里切入 (与 DJ01 项目契合)
```

---

## 2. 知识优先级总览

```
P0 必会 ─────────────────────────────────────────────────────────────
│
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  │ C++ 核心    │  │ UE C++ 基础 │  │ Actor 体系  │  │ 角色控制    │
│  │ (语法/STL)  │  │ (宏/反射)   │  │ (组件化)    │  │ (Pawn/PC)   │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
│
P1 核心竞争力 ───────────────────────────────────────────────────────
│
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  │ GAS 系统    │  │ 动画系统    │  │ 输入系统    │  │ GameMode   │
│  │ (技能/属性) │  │ (ABP/蒙太奇)│  │ (Enhanced)  │  │ (游戏规则) │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
│
P2 加分项 ───────────────────────────────────────────────────────────
│
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  │ AI 行为树   │  │ 网络同步    │  │ UI (UMG)    │  │ 碰撞/物理   │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
│
P3 进阶方向 ─────────────────────────────────────────────────────────
│
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  │ 性能优化    │  │ 材质/Shader │  │ Niagara     │  │ 源码阅读    │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

---

## 3. Phase 1: 必备基础 (4-6周)

### 3.1 C++ 核心 (2周)

> **目标**: 能读懂 UE 源码，写出规范的游戏代码

#### 必学知识点

| 知识点 | 重要程度 | 学习内容 | 验证标准 |
|--------|----------|----------|----------|
| 类与继承 | ⭐⭐⭐⭐⭐ | 构造/析构顺序、虚函数表、多态 | 能解释虚函数调用机制 |
| 内存管理 | ⭐⭐⭐⭐⭐ | new/delete、智能指针、RAII | 能避免内存泄漏 |
| STL 容器 | ⭐⭐⭐⭐⭐ | vector/map/unordered_map 实现原理 | 知道何时用哪种容器 |
| 模板基础 | ⭐⭐⭐⭐ | 函数模板、类模板、模板特化 | 能读懂 TArray/TMap |
| Lambda | ⭐⭐⭐⭐ | 捕获列表、闭包原理 | 能用于回调和委托 |
| 右值引用 | ⭐⭐⭐ | 移动语义、完美转发 | 理解 MoveTemp |

#### 面试高频题

```cpp
// 1. 虚函数相关
class Base {
public:
    virtual void Foo() { cout << "Base"; }
    void Bar() { cout << "Base::Bar"; }
};
class Derived : public Base {
public:
    void Foo() override { cout << "Derived"; }
    void Bar() { cout << "Derived::Bar"; }
};
// 问: Base* p = new Derived(); p->Foo(); p->Bar(); 输出什么？

// 2. 智能指针
// 问: shared_ptr 循环引用如何解决？weak_ptr 原理？

// 3. 内存布局
// 问: 一个包含虚函数的类，sizeof 是多少？为什么？
```

#### 学习资源

- 📖 《Effective C++》- 必读经典
- 📖 《C++ Primer》- 查阅工具书
- 🎬 侯捷 C++ 系列视频

#### 学习验证

- [ ] 能手写智能指针简单实现
- [ ] 能解释虚函数表结构
- [ ] 能分析常见内存问题 (泄漏/野指针/循环引用)

---

### 3.2 UE C++ 基础 (2周)

> **目标**: 理解 UE 的 C++ 扩展机制

#### 必学知识点

| 知识点 | 重要程度 | 学习内容 | 验证标准 |
|--------|----------|----------|----------|
| UCLASS 宏 | ⭐⭐⭐⭐⭐ | 反射注册、类说明符 | 知道各说明符作用 |
| UPROPERTY 宏 | ⭐⭐⭐⭐⭐ | 属性说明符、GC 标记 | 能正确配置属性 |
| UFUNCTION 宏 | ⭐⭐⭐⭐⭐ | BlueprintCallable/Native/Event | 能设计 BP/C++ 接口 |
| UObject 系统 | ⭐⭐⭐⭐⭐ | CDO、反射、序列化 | 理解对象创建流程 |
| 智能指针 | ⭐⭐⭐⭐ | TSharedPtr/TWeakPtr/TUniquePtr | 与标准库的区别 |
| 容器类 | ⭐⭐⭐⭐ | TArray/TMap/TSet 特性 | 能选择合适容器 |
| 委托 | ⭐⭐⭐⭐ | 单播/多播委托、动态委托 | 能实现事件系统 |
| 日志与断言 | ⭐⭐⭐ | UE_LOG/check/ensure | 能调试问题 |

#### UE 特有概念

```cpp
// 1. 反射宏
UCLASS(Blueprintable, BlueprintType)
class MYGAME_API UMyObject : public UObject
{
    GENERATED_BODY()  // 必须！生成反射代码
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
    float Health;
    
    UFUNCTION(BlueprintCallable, Category = "Combat")
    void TakeDamage(float Damage);
};

// 2. 委托
DECLARE_DELEGATE_OneParam(FOnHealthChanged, float);  // 单播
DECLARE_MULTICAST_DELEGATE_OneParam(FOnDeath, AActor*);  // 多播
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnLevelUp);  // 蓝图可用

// 3. 对象创建
UMyObject* Obj = NewObject<UMyObject>(Outer);  // UObject
AActor* Actor = GetWorld()->SpawnActor<AMyActor>(Location, Rotation);  // Actor
```

#### 学习资源

- 📖 UE 官方文档: Programming with C++
- 📖 UE 官方: Unreal Object Handling
- 🔗 项目参考: `Source/DJ01/` 下所有 .h 文件

#### 学习验证

- [ ] 能解释 GENERATED_BODY() 的作用
- [ ] 能说出 UPROPERTY() 常用说明符
- [ ] 能手写一个带委托的简单类

---

### 3.3 项目结构与编译 (1周)

> **目标**: 能独立创建和管理 UE C++ 项目

| 知识点 | 学习内容 |
|--------|----------|
| 模块系统 | .Build.cs、模块依赖、Public/Private 目录 |
| 编译流程 | UBT/UHT、头文件包含规则 |
| 项目配置 | .uproject、Config 文件夹 |
| 插件系统 | .uplugin、Game Features |

#### 学习验证

- [ ] 能创建新模块并正确配置依赖
- [ ] 理解 MYGAME_API 宏的作用
- [ ] 能排查常见编译错误

---

## 4. Phase 2: Gameplay 核心 (4-6周)

### 4.1 Actor 与 Component (2周)

> **目标**: 深入理解 UE 的 Actor-Component 架构

#### 必学知识点

| 知识点 | 重要程度 | 学习内容 |
|--------|----------|----------|
| Actor 生命周期 | ⭐⭐⭐⭐⭐ | Constructor → PostInitializeComponents → BeginPlay → Tick → EndPlay |
| Component 类型 | ⭐⭐⭐⭐⭐ | SceneComponent vs ActorComponent |
| 组件注册 | ⭐⭐⭐⭐ | RegisterComponent、组件依赖 |
| 组件化设计 | ⭐⭐⭐⭐ | 职责分离、组件通信 |
| Actor 复制 | ⭐⭐⭐ | SpawnActor、Actor 池 |

#### Actor 生命周期详解

```
┌──────────────────────────────────────────────────────────┐
│                    Actor 生命周期                         │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  1. Constructor (CDO 创建)                               │
│     ↓ 设置默认值、创建组件                                │
│                                                          │
│  2. PostInitializeComponents()                           │
│     ↓ 所有组件已初始化                                    │
│                                                          │
│  3. BeginPlay()                                          │
│     ↓ 游戏开始，可以安全访问其他 Actor                     │
│                                                          │
│  4. Tick(DeltaTime)                                      │
│     ↓ 每帧更新                                           │
│                                                          │
│  5. EndPlay(EndPlayReason)                               │
│     ↓ Actor 销毁前                                       │
│                                                          │
│  6. Destructor                                           │
│     └ GC 回收                                            │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

#### 项目对照学习

```
阅读顺序:
1. Source/DJ01/Character/Public/DJ01Character.h
2. Source/DJ01/Character/Public/DJ01PawnExtensionComponent.h
3. Source/DJ01/Character/Public/DJ01HeroComponent.h

思考:
- 为什么 HeroComponent 不在构造函数中创建？
- PawnExtensionComponent 的职责是什么？
```

---

### 4.2 Pawn 与 Character (1.5周)

> **目标**: 掌握角色控制的核心机制

#### 必学知识点

| 知识点 | 重要程度 | 学习内容 |
|--------|----------|----------|
| Pawn 基础 | ⭐⭐⭐⭐⭐ | 控制器分离、Possess/UnPossess |
| Character 特性 | ⭐⭐⭐⭐⭐ | CharacterMovementComponent |
| 移动组件 | ⭐⭐⭐⭐⭐ | 移动模式、物理交互 |
| 控制器 | ⭐⭐⭐⭐ | PlayerController vs AIController |

#### 关键类继承链

```
AActor
  └── APawn
        ├── ADefaultPawn (简单 Pawn)
        └── ACharacter
              └── ADJ01Character (你的项目)
                    └── ADJ01CharacterWithAbilities

AController
  ├── APlayerController
  │     └── ADJ01PlayerController
  └── AAIController
        └── ADJ01AIController (待实现)
```

#### 移动组件核心概念

```cpp
// 移动模式
enum EMovementMode
{
    MOVE_Walking,   // 地面行走
    MOVE_Falling,   // 下落
    MOVE_Flying,    // 飞行
    MOVE_Swimming,  // 游泳
    MOVE_Custom     // 自定义 (如爬墙、滑翔)
};

// 常用接口
CharacterMovement->MaxWalkSpeed = 600.f;
CharacterMovement->JumpZVelocity = 420.f;
CharacterMovement->SetMovementMode(MOVE_Flying);
```

---

### 4.3 GameMode 与 GameState (1周)

> **目标**: 理解游戏规则管理

| 知识点 | 学习内容 |
|--------|----------|
| GameMode | 游戏规则 (仅服务器)、玩家生成、比赛流程 |
| GameState | 游戏状态 (复制到客户端)、分数、时间 |
| PlayerState | 玩家状态 (复制)、名字、队伍、分数 |
| WorldSettings | 关卡设置、默认 GameMode |

#### 项目对照

```
阅读:
- Source/DJ01/System/Public/DJ01GameMode.h
- Source/DJ01/System/Public/DJ01GameState.h  
- Source/DJ01/Player/Public/DJ01PlayerState.h
- Source/DJ01/Experience/ (Experience 系统)
```

---

### 4.4 输入系统 (1周)

> **目标**: 掌握 UE5 Enhanced Input System

| 知识点 | 学习内容 |
|--------|----------|
| Input Action | 输入动作资产、Value Type |
| Input Mapping Context | 输入映射、优先级 |
| Input Modifiers | 输入修改器 (死区、缩放) |
| Input Triggers | 触发条件 (按下、释放、长按) |
| 绑定到 GAS | 通过 Tag 触发技能 |

#### 项目对照

```
阅读:
- Source/DJ01/Input/Public/DJ01InputConfig.h
- Source/DJ01/Input/Public/DJ01InputComponent.h
- Source/DJ01/Character/Public/DJ01HeroComponent.h (输入绑定部分)
```

---

## 5. Phase 3: GAS 技能系统 (4-8周)

> **这是 UE 动作游戏的核心竞争力，务必深入理解**

### 5.1 GAS 核心概念 (2周)

#### 必学知识点

| 知识点 | 重要程度 | 学习内容 |
|--------|----------|----------|
| AbilitySystemComponent | ⭐⭐⭐⭐⭐ | ASC 结构、Owner vs Avatar |
| GameplayAbility | ⭐⭐⭐⭐⭐ | 技能激活/结束、实例化策略 |
| GameplayEffect | ⭐⭐⭐⭐⭐ | 属性修改、Duration、Stacking |
| AttributeSet | ⭐⭐⭐⭐⭐ | 属性定义、Clamp、响应变化 |
| GameplayTags | ⭐⭐⭐⭐⭐ | 层级 Tag、条件查询 |
| GameplayCue | ⭐⭐⭐⭐ | 技能表现、音效、特效 |
| Ability Tasks | ⭐⭐⭐⭐ | 异步任务、等待输入/动画 |

#### GAS 架构图

```
┌────────────────────────────────────────────────────────────────┐
│                   Gameplay Ability System                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              AbilitySystemComponent (ASC)                 │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │  │
│  │  │ Abilities   │  │ Attributes  │  │ GameplayTags│       │  │
│  │  │ (技能列表)   │  │ (属性集)     │  │ (状态标签)  │       │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘       │  │
│  │  ┌─────────────┐  ┌─────────────┐                        │  │
│  │  │ Active GEs  │  │ Cooldowns   │                        │  │
│  │  │ (激活效果)   │  │ (冷却)       │                        │  │
│  │  └─────────────┘  └─────────────┘                        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
│  触发流程:                                                      │
│  Input → ASC.TryActivateAbility → GA.ActivateAbility           │
│       → GA.ApplyGameplayEffect → AttributeSet.Modify           │
│       → GameplayCue (表现)                                      │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

#### 项目对照学习

```
核心阅读顺序:
1. Source/DJ01/AbilitySystem/AbilitySystem_Architecture.md (架构文档)
2. Source/DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h
3. Source/DJ01/AbilitySystem/Abilities/Public/DJ01GameplayAbility.h
4. Source/DJ01/AbilitySystem/Attributes/ (属性集)
```

---

### 5.2 GameplayAbility 深入 (1.5周)

| 知识点 | 学习内容 |
|--------|----------|
| 激活策略 | OnInputPressed/OnSpawn/OnGiven |
| 实例化策略 | NonInstanced/InstancedPerActor/InstancedPerExecution |
| Cost & Cooldown | 消耗与冷却 GE |
| Ability Tags | BlockedTags/CancelTags/ActivationRequiredTags |
| Targeting | 目标选择、TargetData |

#### 技能激活流程

```
TryActivateAbility()
    │
    ├── CanActivateAbility()
    │     ├── CheckCost() - 检查消耗
    │     ├── CheckCooldown() - 检查冷却
    │     └── CheckTagRequirements() - 检查 Tag
    │
    ├── ActivateAbility()
    │     ├── CommitAbility() - 扣除消耗/启动CD
    │     ├── [执行技能逻辑]
    │     └── EndAbility()
    │
    └── [失败] → OnActivateFailed()
```

---

### 5.3 GameplayEffect 深入 (1.5周)

| 知识点 | 学习内容 |
|--------|----------|
| Duration 类型 | Instant/Duration/Infinite |
| Modifier 类型 | Add/Multiply/Override |
| Execution 计算 | ExecutionCalculation 自定义公式 |
| Stacking | 叠加规则、叠加上限 |
| Conditional GE | 基于 Tag 的条件应用 |

#### Modifier vs Execution

```cpp
// Modifier - 简单属性修改
// 适合: 固定加减、百分比修改
Modifiers:
  - Attribute: Health
  - ModOp: Add
  - Magnitude: -50

// Execution - 复杂计算
// 适合: 伤害公式、多属性交互
class UDamageExecution : public UGameplayEffectExecutionCalculation
{
    // 捕获攻击者的 AttackPower
    // 捕获目标的 Defense
    // 计算: Damage = AttackPower * Multiplier - Defense
    // 输出: 修改目标 Health
};
```

---

### 5.4 AttributeSet 深入 (1周)

| 知识点 | 学习内容 |
|--------|----------|
| 属性定义 | FGameplayAttributeData、ATTRIBUTE_ACCESSORS 宏 |
| PreAttributeChange | 值变化前 (Clamp) |
| PostGameplayEffectExecute | GE 执行后 (响应伤害/治疗) |
| 属性复制 | GetLifetimeReplicatedProps、OnRep 函数 |

#### 项目参考

```
阅读:
- Source/DJ01/AbilitySystem/Attributes/Public/DJ01AttributeMacros.h (三层属性宏)
- Source/DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h
- Tools/AttributeGenerator/ (属性生成器工具)
```

---

### 5.5 GAS 实践任务

| 任务 | 涉及知识点 | 难度 |
|------|------------|------|
| 实现一个简单近战攻击 | GA + Montage + Hit Detection | ⭐⭐ |
| 实现 Buff/Debuff 系统 | GE Duration + Tag | ⭐⭐ |
| 实现伤害计算系统 | Execution + Attributes | ⭐⭐⭐ |
| 实现技能连招 | GA Combo + AbilityTask | ⭐⭐⭐ |
| 实现护盾系统 | 属性层级 + GE 条件 | ⭐⭐⭐ |

---

## 6. Phase 4: 动画与表现 (3-4周)

### 6.1 动画系统基础 (1.5周)

| 知识点 | 重要程度 | 学习内容 |
|--------|----------|----------|
| Skeleton & Mesh | ⭐⭐⭐⭐⭐ | 骨骼结构、蒙皮 |
| Animation Blueprint | ⭐⭐⭐⭐⭐ | 状态机、EventGraph |
| Blend Space | ⭐⭐⭐⭐ | 1D/2D 混合空间 |
| Animation Montage | ⭐⭐⭐⭐⭐ | Section、Slot、通知 |
| AnimNotify | ⭐⭐⭐⭐⭐ | Notify 点、Notify State |
| IK (Inverse Kinematics) | ⭐⭐⭐ | Foot IK、Hand IK |

### 6.2 动画蓝图结构

```
┌────────────────────────────────────────────────────────────┐
│                   Animation Blueprint                       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    Event Graph                        │  │
│  │  - 接收角色数据 (速度、方向等)                          │  │
│  │  - 更新动画变量                                        │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    Anim Graph                         │  │
│  │  ┌──────────┐    ┌──────────┐    ┌──────────┐        │  │
│  │  │State    ├────►│ Blend   ├────►│  Output  │        │  │
│  │  │Machine  │    │ Nodes   │    │  Pose    │        │  │
│  │  └──────────┘    └──────────┘    └──────────┘        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 6.3 与 GAS 集成

| 场景 | 实现方式 |
|------|----------|
| 技能播放动画 | GA 中调用 PlayMontage AbilityTask |
| 动画触发伤害 | AnimNotify 发送 GameplayEvent |
| 动画结束反馈 | AbilityTask 等待 Montage 结束 |
| 状态驱动动画 | ABP 读取 GameplayTags |

### 6.4 项目对照

```
阅读:
- Source/DJ01/Animation/DJ01AnimInstance.h
- Source/DJ01/Animation/AnimNotifies/ (连招通知)
- docs/Now/Animation/ (动画系统文档)
```

---

## 7. Phase 5: AI 与网络 (4-6周)

### 7.1 AI 系统 (2-3周)

| 知识点 | 重要程度 | 学习内容 |
|--------|----------|----------|
| AI Controller | ⭐⭐⭐⭐⭐ | AI 控制器、Possess |
| Behavior Tree | ⭐⭐⭐⭐⭐ | Composite/Task/Decorator/Service |
| Blackboard | ⭐⭐⭐⭐ | 数据存储、键值类型 |
| EQS | ⭐⭐⭐ | 环境查询、Generator/Test |
| AI Perception | ⭐⭐⭐⭐ | 视觉/听觉感知、刺激源 |
| Navigation | ⭐⭐⭐ | NavMesh、路径查找 |

#### 行为树节点类型

```
行为树节点类型:
├── Composite (组合节点)
│   ├── Selector - 选择执行 (OR)
│   ├── Sequence - 顺序执行 (AND)
│   └── Parallel - 并行执行
│
├── Task (任务节点)
│   ├── Move To - 移动到目标
│   ├── Wait - 等待
│   └── Custom Task - 自定义任务
│
├── Decorator (装饰器)
│   ├── Blackboard Check - 条件检查
│   ├── Cooldown - 冷却
│   └── Loop - 循环
│
└── Service (服务)
    ├── Update Blackboard - 更新数据
    └── Check Conditions - 检查条件
```

### 7.2 网络同步基础 (2-3周)

| 知识点 | 重要程度 | 学习内容 |
|--------|----------|----------|
| Replication 基础 | ⭐⭐⭐⭐ | UPROPERTY(Replicated)、OnRep |
| RPC 调用 | ⭐⭐⭐⭐ | Server/Client/NetMulticast |
| 所有权 | ⭐⭐⭐⭐ | Owner、Connection |
| 预测与回滚 | ⭐⭐⭐ | Client Prediction |
| GAS 网络 | ⭐⭐⭐⭐ | ASC Owner、技能预测 |

---

## 8. Phase 6: 图形学入门 (持续学习)

> **优先级较低，但对求职有加分作用**

### 8.1 学习路线

```
入门阶段 (1-2月)
│
├── 理解渲染管线
│   └── 顶点处理 → 光栅化 → 片元处理 → 输出
│
├── 材质编辑器
│   └── 节点式编辑、PBR 参数
│
└── 基础光照
    └── 光源类型、阴影

进阶阶段 (2-3月)
│
├── Shader 入门
│   └── HLSL 基础、Custom Node
│
├── 后处理
│   └── Bloom、DOF、Color Grading
│
└── Niagara 特效
    └── 粒子系统、GPU 粒子

深入阶段 (长期)
│
├── 渲染源码
│   └── Deferred/Forward、RDG
│
├── Lumen/Nanite
│   └── 全局光照、虚拟几何体
│
└── 自定义渲染特性
    └── RenderPass、SceneViewExtension
```

### 8.2 推荐学习资源

| 资源 | 内容 | 难度 |
|------|------|------|
| LearnOpenGL | 图形学入门经典 | ⭐⭐ |
| Games101 | 计算机图形学入门 | ⭐⭐ |
| Games202 | 高级渲染技术 | ⭐⭐⭐ |
| 《Real-Time Rendering》 | 渲染圣经 | ⭐⭐⭐⭐ |
| Ben Cloward YouTube | UE 材质教程 | ⭐⭐ |

---

## 9. 面试准备

### 9.1 高频面试题

#### C++ 基础

1. 虚函数原理？多态如何实现？
2. 智能指针种类及使用场景？
3. 移动语义与完美转发？
4. 内存对齐原则？

#### UE 基础

1. Actor 生命周期？
2. UObject 反射系统原理？
3. GC 机制？如何避免对象被错误回收？
4. 蓝图与 C++ 如何交互？

#### Gameplay

1. 角色移动组件原理？
2. Enhanced Input 相比旧版优势？
3. GameMode 与 GameState 区别？
4. 如何设计可扩展的技能系统？

#### GAS

1. ASC 的 Owner 与 Avatar 区别？
2. GameplayEffect 的 Duration 类型？
3. Execution 与 Modifier 的区别和使用场景？
4. GameplayTag 的作用和设计思路？
5. 如何处理技能冷却？

### 9.2 项目准备

```
DJ01 项目亮点提炼:

1. 架构设计
   - 基于 Lyra 的模块化架构
   - Experience 系统实现玩法配置化
   - GameFeatureActions 动态功能注入

2. 技能系统
   - 完整的 GAS 技能框架
   - 三层属性系统 (Base/Flat/Percent)
   - 数据驱动的伤害计算
   - 元素弱点系统

3. 工具链
   - GAS 代码生成器 (提效工具开发经验)
   - 可视化配置系统

4. 可演示的功能
   - 基础战斗流程
   - 伤害计算验证
   - 连招系统
```

### 9.3 简历建议

```
## 项目经历

### DJ01 - UE5 动作 RPG (个人项目)

**技术栈**: Unreal Engine 5 / C++ / GAS / Lyra 架构

**项目描述**:
基于 Lyra Starter Game 架构开发的动作 RPG 游戏，实现了完整的战斗系统框架。

**核心贡献**:
- 设计并实现了基于 GAS 的技能系统，支持技能组合、属性交互、元素克制
- 实现三层属性系统 (Base/Flat/Percent)，支持灵活的数值策划配置
- 开发 GAS 代码生成工具，将属性/标签配置效率提升 10 倍
- 设计 Experience 系统，实现游戏模式的配置化管理

**技术亮点**:
- 深入理解 UE5 Gameplay 框架和 GAS 系统
- 具备工具链开发能力
- 代码规范，文档完善
```

---

## 10. 学习资源汇总

### 10.1 官方资源

| 资源 | 链接 | 用途 |
|------|------|------|
| UE 官方文档 | docs.unrealengine.com | 查阅 API |
| UE Learning | dev.epicgames.com/community/learning | 系统学习 |
| Lyra 项目 | Epic Games Launcher | 架构参考 |

### 10.2 社区资源

| 资源 | 链接 | 用途 |
|------|------|------|
| GASDocumentation | github.com/tranek/GASDocumentation | GAS 学习 |
| Unreal Slackers Discord | unrealslackers.org | 问答社区 |
| 知乎 UE 专栏 | - | 中文教程 |
| B站 UE 教程 | - | 视频学习 |

### 10.3 书籍推荐

| 书籍 | 用途 | 优先级 |
|------|------|--------|
| 《Effective C++》 | C++ 进阶 | ⭐⭐⭐⭐⭐ |
| 《Game Programming Patterns》 | 游戏设计模式 | ⭐⭐⭐⭐ |
| 《Real-Time Rendering》 | 图形学 | ⭐⭐⭐ |

### 10.4 项目内文档

| 文档 | 路径 | 内容 |
|------|------|------|
| 架构指南 | `docs/Now/Architecture_Guide.md` | 整体架构 |
| GAS 架构 | `Source/DJ01/AbilitySystem/AbilitySystem_Architecture.md` | 技能系统 |
| 动画系统 | `docs/Now/Animation/` | 动画设计 |
| 相机系统 | `Source/DJ01/Camera/Docs/README.md` | 相机实现 |

---

## 附录: 学习进度检查表

### Phase 1 检查项
- [ ] 能解释虚函数表原理
- [ ] 能说明 UPROPERTY 常用说明符
- [ ] 理解 UObject 反射机制
- [ ] 能创建 UE C++ 类并正确配置

### Phase 2 检查项
- [ ] 能说明 Actor 生命周期
- [ ] 理解 Pawn/Controller 分离设计
- [ ] 能使用 Enhanced Input 配置输入
- [ ] 理解 GameMode/GameState 职责

### Phase 3 检查项
- [ ] 能说明 ASC 的 Owner/Avatar 概念
- [ ] 能实现基础 GameplayAbility
- [ ] 能配置 GameplayEffect
- [ ] 理解 AttributeSet 的 Pre/Post 方法
- [ ] 能使用 GameplayTags 设计系统

### Phase 4 检查项
- [ ] 能创建 Animation Blueprint
- [ ] 能使用 Montage 和 Notify
- [ ] 理解动画与 GAS 的集成方式

### Phase 5 检查项
- [ ] 能创建基础行为树
- [ ] 理解网络复制基础概念
- [ ] 能说明 RPC 类型区别

---

**文档版本**: v1.0  
**创建日期**: 2025-12-19  
**目标**: UE 游戏客户端开发求职

*"代码是最好的老师，项目是最好的面试官"*