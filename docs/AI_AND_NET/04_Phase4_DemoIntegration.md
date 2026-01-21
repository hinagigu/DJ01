# Phase 4: 演示场景集成

> **目标**：将 Phase 1-3 的所有系统整合到一个可展示的 Demo 场景中，展示网络同步与 AI 智能的协同工作。

---

## 4.1 演示场景设计

### 4.1.1 场景概述

**「智能竞技场」Demo** - 一个展示分布式网络和 AI 决策能力的技术演示场景。

```
┌─────────────────────────────────────────────────────────────┐
│                      Demo 场景布局                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│    ┌─────────┐                           ┌─────────┐       │
│    │ 玩家1   │                           │ 玩家2   │       │
│    │ 出生点  │                           │ 出生点  │       │
│    └────┬────┘                           └────┬────┘       │
│         │                                     │             │
│         ▼           ┌─────────────┐           ▼             │
│    ┌─────────┐     │   中央      │     ┌─────────┐         │
│    │ AI NPC  │────▶│   竞技场    │◀────│ AI NPC  │         │
│    │ (守卫)  │     │             │     │ (挑战者)│         │
│    └─────────┘     └─────────────┘     └─────────┘         │
│                           │                                 │
│                           ▼                                 │
│                    ┌─────────────┐                          │
│                    │  对话 NPC   │                          │
│                    │ (LLM 驱动)  │                          │
│                    └─────────────┘                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4.1.2 演示要素

| 功能点 | 展示内容 | 技术亮点 |
|-------|---------|---------|
| **多人同步** | 2名玩家实时对战 | 客户端预测 + 服务端权威 |
| **无缝迁移** | 玩家跨场景传送 | Master Server 分配 + Broker 消息转发 |
| **AI 战斗** | NPC 智能战斗决策 | LLM 实时生成战术 |
| **AI 对话** | NPC 角色扮演对话 | 上下文记忆 + 个性化回复 |
| **状态可视化** | 网络延迟/预测状态 | 调试 HUD |

---

## 4.2 文件结构规划

```
Source/DJ01/
├── Demo/
│   ├── Public/
│   │   ├── DJ01DemoGameMode.h           // Demo 专用 GameMode
│   │   ├── DJ01DemoPlayerController.h   // Demo 玩家控制器
│   │   ├── DJ01DemoHUD.h                // 调试信息 HUD
│   │   ├── DJ01ArenaManager.h           // 竞技场管理器
│   │   └── DJ01DemoNPC.h                // Demo NPC 基类
│   └── Private/
│       ├── DJ01DemoGameMode.cpp
│       ├── DJ01DemoPlayerController.cpp
│       ├── DJ01DemoHUD.cpp
│       ├── DJ01ArenaManager.cpp
│       └── DJ01DemoNPC.cpp
│
Content/
├── Demo/
│   ├── Maps/
│   │   └── DemoArena.umap              // 演示地图
│   ├── Blueprints/
│   │   ├── BP_DemoGameMode.uasset
│   │   ├── BP_DemoNPC_Guard.uasset     // 守卫 NPC
│   │   ├── BP_DemoNPC_Challenger.uasset // 挑战者 NPC
│   │   └── BP_DemoNPC_Dialogue.uasset  // 对话 NPC
│   ├── BehaviorTrees/
│   │   ├── BT_GuardAI.uasset
│   │   └── BT_ChallengerAI.uasset
│   └── UI/
│       ├── WBP_DebugHUD.uasset
│       └── WBP_DialoguePanel.uasset
```

---

## 4.3 核心代码实现

### 4.3.1 Demo GameMode

```cpp
// DJ01DemoGameMode.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "DJ01DemoGameMode.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnPlayerJoinedArena, APlayerController*, PC, int32, SlotIndex);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnArenaMatchStarted, float, CountdownTime);

/**
 * Demo 演示场景的 GameMode
 * 管理玩家匹配、NPC 生成和演示流程
 */
UCLASS()
class DJ01_API ADJ01DemoGameMode : public AGameModeBase
{
    GENERATED_BODY()

public:
    ADJ01DemoGameMode();

    //~ Begin AGameModeBase Interface
    virtual void BeginPlay() override;
    virtual void PostLogin(APlayerController* NewPlayer) override;
    virtual void Logout(AController* Exiting) override;
    //~ End AGameModeBase Interface

    // ========== 竞技场管理 ==========

    /** 开始匹配倒计时 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Demo")
    void StartMatchCountdown(float CountdownSeconds = 5.0f);

    /** 结束当前对战 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Demo")
    void EndCurrentMatch();

    /** 重置竞技场 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Demo")
    void ResetArena();

    // ========== 事件 ==========

    UPROPERTY(BlueprintAssignable, Category = "DJ01|Demo")
    FOnPlayerJoinedArena OnPlayerJoinedArena;

    UPROPERTY(BlueprintAssignable, Category = "DJ01|Demo")
    FOnArenaMatchStarted OnArenaMatchStarted;

    // ========== 配置 ==========

    /** 玩家出生点（按槽位索引） */
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Demo")
    TArray<FTransform> PlayerSpawnPoints;

    /** AI NPC 生成配置 */
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Demo")
    TArray<TSubclassOf<APawn>> NPCClasses;

    /** NPC 生成点 */
    UPROPERTY(EditDefaultsOnly, Category = "DJ01|Demo")
    TArray<FTransform> NPCSpawnPoints;

protected:
    /** 生成 AI NPC */
    void SpawnAINPCs();

    /** 分配玩家槽位 */
    int32 AssignPlayerSlot(APlayerController* PC);

private:
    // 当前在场玩家
    UPROPERTY()
    TArray<APlayerController*> ActivePlayers;

    // 生成的 NPC
    UPROPERTY()
    TArray<APawn*> SpawnedNPCs;

    // 匹配是否进行中
    bool bMatchInProgress = false;
};
```

---

### 4.3.2 Demo GameMode 实现

```cpp
// DJ01DemoGameMode.cpp
#include "DJ01DemoGameMode.h"
#include "DJ01DemoPlayerController.h"
#include "GameFramework/PlayerStart.h"
#include "Kismet/GameplayStatics.h"
#include "Engine/World.h"

ADJ01DemoGameMode::ADJ01DemoGameMode()
{
    // 默认使用自定义控制器
    PlayerControllerClass = ADJ01DemoPlayerController::StaticClass();

    // 默认出生点配置
    PlayerSpawnPoints.Add(FTransform(FRotator::ZeroRotator, FVector(-500, 0, 100)));
    PlayerSpawnPoints.Add(FTransform(FRotator(0, 180, 0), FVector(500, 0, 100)));
}

void ADJ01DemoGameMode::BeginPlay()
{
    Super::BeginPlay();

    // 服务端生成 AI NPC
    if (HasAuthority())
    {
        SpawnAINPCs();
    }

    UE_LOG(LogTemp, Log, TEXT("[DJ01 Demo] GameMode BeginPlay. Authority: %d"), HasAuthority());
}

void ADJ01DemoGameMode::PostLogin(APlayerController* NewPlayer)
{
    Super::PostLogin(NewPlayer);

    if (!NewPlayer) return;

    // 分配槽位
    int32 SlotIndex = AssignPlayerSlot(NewPlayer);

    // 设置出生位置
    if (PlayerSpawnPoints.IsValidIndex(SlotIndex))
    {
        if (APawn* Pawn = NewPlayer->GetPawn())
        {
            Pawn->SetActorTransform(PlayerSpawnPoints[SlotIndex]);
        }
    }

    ActivePlayers.Add(NewPlayer);
    OnPlayerJoinedArena.Broadcast(NewPlayer, SlotIndex);

    UE_LOG(LogTemp, Log, TEXT("[DJ01 Demo] Player %s joined at slot %d"), 
           *NewPlayer->GetName(), SlotIndex);

    // 检查是否可以开始匹配
    if (ActivePlayers.Num() >= 2 && !bMatchInProgress)
    {
        StartMatchCountdown(5.0f);
    }
}

void ADJ01DemoGameMode::Logout(AController* Exiting)
{
    Super::Logout(Exiting);

    if (APlayerController* PC = Cast<APlayerController>(Exiting))
    {
        ActivePlayers.Remove(PC);
    }
}

int32 ADJ01DemoGameMode::AssignPlayerSlot(APlayerController* PC)
{
    // 找到第一个空闲槽位
    for (int32 i = 0; i < PlayerSpawnPoints.Num(); i++)
    {
        bool bSlotTaken = false;
        for (APlayerController* ExistingPC : ActivePlayers)
        {
            // 简化逻辑：按加入顺序分配
        }
        if (!bSlotTaken)
        {
            return i;
        }
    }
    return ActivePlayers.Num() % PlayerSpawnPoints.Num();
}

void ADJ01DemoGameMode::StartMatchCountdown(float CountdownSeconds)
{
    bMatchInProgress = true;
    OnArenaMatchStarted.Broadcast(CountdownSeconds);

    // 倒计时后正式开始
    FTimerHandle TimerHandle;
    GetWorld()->GetTimerManager().SetTimer(
        TimerHandle,
        [this]()
        {
            UE_LOG(LogTemp, Log, TEXT("[DJ01 Demo] Match started!"));
            // 可在此触发 NPC 进入战斗模式
        },
        CountdownSeconds,
        false);
}

void ADJ01DemoGameMode::EndCurrentMatch()
{
    bMatchInProgress = false;
    UE_LOG(LogTemp, Log, TEXT("[DJ01 Demo] Match ended."));
}

void ADJ01DemoGameMode::ResetArena()
{
    EndCurrentMatch();

    // 重置玩家位置
    for (int32 i = 0; i < ActivePlayers.Num(); i++)
    {
        if (ActivePlayers[i] && PlayerSpawnPoints.IsValidIndex(i))
        {
            if (APawn* Pawn = ActivePlayers[i]->GetPawn())
            {
                Pawn->SetActorTransform(PlayerSpawnPoints[i]);
            }
        }
    }

    // 重置 NPC
    for (APawn* NPC : SpawnedNPCs)
    {
        if (NPC)
        {
            // TODO: 重置 NPC 状态
        }
    }
}

void ADJ01DemoGameMode::SpawnAINPCs()
{
    for (int32 i = 0; i < NPCClasses.Num() && i < NPCSpawnPoints.Num(); i++)
    {
        if (NPCClasses[i])
        {
            FActorSpawnParameters SpawnParams;
            SpawnParams.SpawnCollisionHandlingOverride = ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButAlwaysSpawn;

            APawn* NPC = GetWorld()->SpawnActor<APawn>(
                NPCClasses[i],
                NPCSpawnPoints[i].GetLocation(),
                NPCSpawnPoints[i].Rotator(),
                SpawnParams);

            if (NPC)
            {
                SpawnedNPCs.Add(NPC);
                UE_LOG(LogTemp, Log, TEXT("[DJ01 Demo] Spawned NPC: %s"), *NPC->GetName());
            }
        }
    }
}
```

---

### 4.3.3 调试 HUD

```cpp
// DJ01DemoHUD.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/HUD.h"
#include "DJ01DemoHUD.generated.h"

/**
 * Demo 调试 HUD
 * 显示网络状态、预测信息和 AI 决策日志
 */
UCLASS()
class DJ01_API ADJ01DemoHUD : public AHUD
{
    GENERATED_BODY()

public:
    ADJ01DemoHUD();

    //~ Begin AHUD Interface
    virtual void DrawHUD() override;
    //~ End AHUD Interface

    /** 添加 AI 决策日志 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Debug")
    void AddAIDecisionLog(const FString& NPCName, const FString& Decision);

    /** 是否显示调试信息 */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "DJ01|Debug")
    bool bShowDebugInfo = true;

protected:
    /** 绘制网络状态 */
    void DrawNetworkStats();

    /** 绘制预测状态 */
    void DrawPredictionStats();

    /** 绘制 AI 日志 */
    void DrawAILogs();

private:
    // AI 决策日志（最近 10 条）
    TArray<FString> AIDecisionLogs;
    static constexpr int32 MaxLogCount = 10;
};
```

```cpp
// DJ01DemoHUD.cpp
#include "DJ01DemoHUD.h"
#include "Engine/Canvas.h"
#include "GameFramework/PlayerController.h"
#include "Net/UnrealNetwork.h"

ADJ01DemoHUD::ADJ01DemoHUD()
{
}

void ADJ01DemoHUD::DrawHUD()
{
    Super::DrawHUD();

    if (!bShowDebugInfo) return;

    DrawNetworkStats();
    DrawPredictionStats();
    DrawAILogs();
}

void ADJ01DemoHUD::DrawNetworkStats()
{
    if (!Canvas) return;

    float X = 20.0f;
    float Y = 50.0f;
    float LineHeight = 18.0f;

    // 标题
    Canvas->SetDrawColor(FColor::Cyan);
    Canvas->DrawText(GEngine->GetSmallFont(), TEXT("=== Network Stats ==="), X, Y);
    Y += LineHeight;

    // 获取网络信息
    if (APlayerController* PC = GetOwningPlayerController())
    {
        if (UNetConnection* Connection = PC->GetNetConnection())
        {
            // Ping
            float Ping = Connection->AvgLag * 1000.0f;
            Canvas->SetDrawColor(Ping < 50 ? FColor::Green : (Ping < 100 ? FColor::Yellow : FColor::Red));
            Canvas->DrawText(GEngine->GetSmallFont(), 
                           FString::Printf(TEXT("Ping: %.1f ms"), Ping), X, Y);
            Y += LineHeight;

            // 丢包率
            float PacketLoss = Connection->InPacketsLost / FMath::Max(1.0f, (float)Connection->InTotalPackets) * 100.0f;
            Canvas->SetDrawColor(FColor::White);
            Canvas->DrawText(GEngine->GetSmallFont(),
                           FString::Printf(TEXT("Packet Loss: %.1f%%"), PacketLoss), X, Y);
            Y += LineHeight;
        }

        // 服务器/客户端标识
        Canvas->SetDrawColor(FColor::White);
        FString RoleText = PC->HasAuthority() ? TEXT("Role: SERVER") : TEXT("Role: CLIENT");
        Canvas->DrawText(GEngine->GetSmallFont(), RoleText, X, Y);
    }
}

void ADJ01DemoHUD::DrawPredictionStats()
{
    if (!Canvas) return;

    float X = 20.0f;
    float Y = 150.0f;
    float LineHeight = 18.0f;

    Canvas->SetDrawColor(FColor::Yellow);
    Canvas->DrawText(GEngine->GetSmallFont(), TEXT("=== Prediction Stats ==="), X, Y);
    Y += LineHeight;

    // TODO: 从 DJ01AbilitySystemComponent 获取预测状态
    Canvas->SetDrawColor(FColor::White);
    Canvas->DrawText(GEngine->GetSmallFont(), TEXT("Pending Predictions: 0"), X, Y);
    Y += LineHeight;
    Canvas->DrawText(GEngine->GetSmallFont(), TEXT("Last Rollback: None"), X, Y);
}

void ADJ01DemoHUD::DrawAILogs()
{
    if (!Canvas || AIDecisionLogs.Num() == 0) return;

    float X = Canvas->SizeX - 400.0f;
    float Y = 50.0f;
    float LineHeight = 16.0f;

    Canvas->SetDrawColor(FColor::Magenta);
    Canvas->DrawText(GEngine->GetSmallFont(), TEXT("=== AI Decision Log ==="), X, Y);
    Y += LineHeight;

    Canvas->SetDrawColor(FColor::White);
    for (const FString& Log : AIDecisionLogs)
    {
        Canvas->DrawText(GEngine->GetSmallFont(), Log, X, Y);
        Y += LineHeight;
    }
}

void ADJ01DemoHUD::AddAIDecisionLog(const FString& NPCName, const FString& Decision)
{
    FString LogEntry = FString::Printf(TEXT("[%s] %s"), *NPCName, *Decision);
    AIDecisionLogs.Insert(LogEntry, 0);

    while (AIDecisionLogs.Num() > MaxLogCount)
    {
        AIDecisionLogs.Pop();
    }
}
```

---

### 4.3.4 竞技场管理器

```cpp
// DJ01ArenaManager.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "DJ01ArenaManager.generated.h"

UENUM(BlueprintType)
enum class EDJ01ArenaState : uint8
{
    Idle,           // 等待玩家
    Countdown,      // 倒计时中
    InProgress,     // 对战进行中
    Finished        // 对战结束
};

DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnArenaStateChanged, EDJ01ArenaState, NewState);

/**
 * 竞技场管理器
 * 负责管理竞技场的状态、边界和战斗逻辑
 */
UCLASS()
class DJ01_API ADJ01ArenaManager : public AActor
{
    GENERATED_BODY()

public:
    ADJ01ArenaManager();

    //~ Begin AActor Interface
    virtual void BeginPlay() override;
    virtual void Tick(float DeltaTime) override;
    //~ End AActor Interface

    // ========== 状态管理 ==========

    UFUNCTION(BlueprintCallable, Category = "DJ01|Arena")
    void SetArenaState(EDJ01ArenaState NewState);

    UFUNCTION(BlueprintPure, Category = "DJ01|Arena")
    EDJ01ArenaState GetArenaState() const { return CurrentState; }

    UPROPERTY(BlueprintAssignable, Category = "DJ01|Arena")
    FOnArenaStateChanged OnArenaStateChanged;

    // ========== 边界检测 ==========

    /** 检查位置是否在竞技场内 */
    UFUNCTION(BlueprintPure, Category = "DJ01|Arena")
    bool IsInsideArena(const FVector& Location) const;

    /** 将位置限制在竞技场内 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|Arena")
    FVector ClampToArenaBounds(const FVector& Location) const;

    // ========== 配置 ==========

    /** 竞技场中心 */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "DJ01|Arena")
    FVector ArenaCenter = FVector::ZeroVector;

    /** 竞技场半径 */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "DJ01|Arena")
    float ArenaRadius = 1000.0f;

    /** 边界警告距离 */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "DJ01|Arena")
    float BoundaryWarningDistance = 200.0f;

protected:
    /** 检查所有参与者是否越界 */
    void CheckBoundaries();

private:
    UPROPERTY(ReplicatedUsing=OnRep_ArenaState)
    EDJ01ArenaState CurrentState = EDJ01ArenaState::Idle;

    UFUNCTION()
    void OnRep_ArenaState();

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
};
```

---

### 4.3.5 Demo NPC 基类

```cpp
// DJ01DemoNPC.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "DJ01AITypes.h"
#include "DJ01DemoNPC.generated.h"

/**
 * Demo 场景 NPC 基类
 * 集成了 AI 大脑组件和战斗能力
 */
UCLASS()
class DJ01_API ADJ01DemoNPC : public ACharacter
{
    GENERATED_BODY()

public:
    ADJ01DemoNPC();

    //~ Begin AActor Interface
    virtual void BeginPlay() override;
    //~ End AActor Interface

    // ========== AI 组件 ==========

    /** AI 大脑组件 */
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "DJ01|AI")
    class UDJ01AIBrainComponent* AIBrainComponent;

    /** 技能系统组件 */
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "DJ01|Abilities")
    class UDJ01AbilitySystemComponent* AbilitySystemComponent;

    // ========== 配置 ==========

    /** NPC 角色类型 */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "DJ01|NPC")
    FString NPCRole = TEXT("Guard"); // Guard, Challenger, Dialogue

    /** 初始技能列表 */
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DJ01|Abilities")
    TArray<TSubclassOf<class UGameplayAbility>> InitialAbilities;

protected:
    /** 初始化技能 */
    void InitializeAbilities();

    /** 处理战斗决策 */
    UFUNCTION()
    void HandleCombatDecision(const FDJ01AICombatDecision& Decision);

    /** 处理对话响应 */
    UFUNCTION()
    void HandleDialogueResponse(const FString& Response);

    /** 执行攻击动作 */
    void ExecuteAttack(AActor* Target);

    /** 执行技能 */
    void ExecuteSkill(const FString& SkillId, AActor* Target);

    /** 执行防御姿态 */
    void ExecuteDefend();

    /** 执行逃跑 */
    void ExecuteFlee();
};
```

---

## 4.4 行为树配置

### 4.4.1 守卫 AI 行为树结构

```
BT_GuardAI
├── Selector
│   ├── Sequence [Patrol Mode]
│   │   ├── Decorator: BB.ThreatLevel < 0.3
│   │   ├── Task: BTTask_MoveTo (Patrol Point)
│   │   └── Task: Wait (3-5 sec)
│   │
│   └── Sequence [Combat Mode]
│       ├── Decorator: BB.ThreatLevel >= 0.3
│       ├── Task: DJ01BTTask_LLMDecision
│       │   └── Output → BB.NextAction, BB.Target
│       ├── Selector [Execute Action]
│       │   ├── Sequence [Attack]
│       │   │   ├── Decorator: BB.NextAction == "Attack"
│       │   │   └── Task: BTTask_UseAbility (BasicAttack)
│       │   ├── Sequence [Skill]
│       │   │   ├── Decorator: BB.NextAction == "Skill"
│       │   │   └── Task: BTTask_UseAbility (BB.SkillId)
│       │   └── Sequence [Defend]
│       │       ├── Decorator: BB.NextAction == "Defend"
│       │       └── Task: BTTask_UseAbility (DefensiveStance)
│       └── Task: Wait (0.5 sec)
```

### 4.4.2 黑板键配置

| 键名 | 类型 | 说明 |
|-----|------|------|
| `ThreatLevel` | Float | 威胁等级 (0-1) |
| `NextAction` | String | LLM 决策的下一步动作 |
| `TargetActor` | Object | 目标 Actor |
| `SkillId` | String | 使用的技能 ID |
| `PatrolIndex` | Int | 当前巡逻点索引 |

---

## 4.5 UI 配置

### 4.5.1 对话面板 Widget

```
WBP_DialoguePanel
├── Canvas Panel
│   ├── Background (Border)
│   │   ├── NPC Name Text
│   │   ├── Dialogue Scroll Box
│   │   │   └── Dialogue Text Block (动态生成)
│   │   ├── Input Text Box
│   │   └── Send Button
│   └── Loading Indicator (Throbber)
```

### 4.5.2 调试 HUD Widget

```
WBP_DebugHUD
├── Canvas Panel
│   ├── Network Stats Panel (左上)
│   │   ├── Ping Display
│   │   ├── Packet Loss Display
│   │   └── Role Display
│   ├── Prediction Stats Panel (左中)
│   │   ├── Pending Count
│   │   └── Rollback History
│   └── AI Log Panel (右侧)
│       └── Scrolling Log Text
```

---

## 4.6 实现步骤清单

| 序号 | 任务 | 文件/资产 | 依赖 |
|-----|------|----------|------|
| 4.1 | 创建 Demo GameMode | `DJ01DemoGameMode.h/.cpp` | Phase 1-3 |
| 4.2 | 创建调试 HUD | `DJ01DemoHUD.h/.cpp` | 无 |
| 4.3 | 创建竞技场管理器 | `DJ01ArenaManager.h/.cpp` | 无 |
| 4.4 | 创建 Demo NPC 基类 | `DJ01DemoNPC.h/.cpp` | Phase 2, 3 |
| 4.5 | 创建演示地图 | `DemoArena.umap` | 无 |
| 4.6 | 配置 GameMode 蓝图 | `BP_DemoGameMode` | 4.1 |
| 4.7 | 创建守卫 NPC 蓝图 | `BP_DemoNPC_Guard` | 4.4 |
| 4.8 | 创建挑战者 NPC 蓝图 | `BP_DemoNPC_Challenger` | 4.4 |
| 4.9 | 创建对话 NPC 蓝图 | `BP_DemoNPC_Dialogue` | 4.4 |
| 4.10 | 配置守卫行为树 | `BT_GuardAI` | Phase 3 |
| 4.11 | 配置挑战者行为树 | `BT_ChallengerAI` | Phase 3 |
| 4.12 | 创建对话 UI | `WBP_DialoguePanel` | Phase 3 |
| 4.13 | 创建调试 UI | `WBP_DebugHUD` | 4.2 |
| 4.14 | 集成测试 | - | 4.1-4.13 |

---

## 4.7 演示脚本

### 4.7.1 演示流程

```
1. [0:00-0:30] 场景介绍
   - 展示分布式架构图
   - 说明技术栈：UE5 + GAS + LLM

2. [0:30-2:00] 网络同步演示
   - 两个客户端窗口并排显示
   - 演示技能释放的客户端预测
   - 故意制造高延迟，展示预测回滚

3. [2:00-4:00] AI 战斗演示
   - 与 AI 守卫进行战斗
   - 展示调试 HUD 中的 AI 决策日志
   - 说明 LLM 是如何做出战术决策的

4. [4:00-5:30] AI 对话演示
   - 与对话 NPC 进行交互
   - 展示上下文记忆能力
   - 展示不同性格 NPC 的回复差异

5. [5:30-6:00] 技术总结
   - 回顾架构设计
   - 展示代码结构
   - Q&A
```

### 4.7.2 调试命令

```
// 控制台命令
DJ01.ShowDebugHUD 1          // 显示调试信息
DJ01.SimulateLatency 200     // 模拟 200ms 延迟
DJ01.ForcePredictionReject   // 强制下一次预测被驳回
DJ01.SetAIVerbose 1          // 开启 AI 决策详细日志
DJ01.ResetArena              // 重置竞技场
```

---

## 4.8 测试验证点

### 功能测试
1. **多人连接**：两个客户端能正常连接并看到对方
2. **技能同步**：技能释放在所有客户端正确显示
3. **AI 对战**：NPC 能根据战斗情况做出合理决策
4. **对话系统**：NPC 对话有上下文记忆且符合角色设定

### 性能测试
1. **帧率稳定**：60fps 基准下波动 < 5fps
2. **LLM 延迟**：响应时间 < 2秒，有 loading 提示
3. **网络带宽**：稳态流量 < 50KB/s

### 压力测试
1. **快速操作**：连续快速释放技能不崩溃
2. **长时间运行**：10分钟连续对战无内存泄漏

---

## 4.9 下一步

完成所有 Phase 后，请查阅 [05_CodeChecklist.md](./05_CodeChecklist.md) 获取完整的代码实现清单和验收标准。