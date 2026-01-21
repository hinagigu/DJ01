# Phase 3: AI 大模型集成系统

> **目标**：将 LLM（大语言模型）API 集成到 UE5 中，实现 NPC 的智能对话和战斗决策，展示 AI 与游戏系统的深度融合。

---

## 3.1 核心目标

| 功能模块 | 说明 |
|---------|------|
| **LLM 通信层** | 异步 HTTP 调用大模型 API，支持流式响应 |
| **AI 决策组件** | 封装 NPC 的决策逻辑，桥接 LLM 与行为树 |
| **对话系统** | 基于上下文的 NPC 智能对话 |
| **战斗 AI** | LLM 辅助的战术决策（技能选择、目标优先级） |

---

## 3.2 文件结构规划

```
Source/DJ01/
├── AI/
│   ├── Public/
│   │   ├── DJ01LLMSubsystem.h           // LLM 通信子系统
│   │   ├── DJ01AIBrainComponent.h       // AI 大脑组件
│   │   ├── DJ01AITypes.h                // AI 相关类型定义
│   │   ├── DJ01BTTask_LLMDecision.h     // 行为树 LLM 决策任务
│   │   └── DJ01BTTask_LLMDialogue.h     // 行为树 LLM 对话任务
│   └── Private/
│       ├── DJ01LLMSubsystem.cpp
│       ├── DJ01AIBrainComponent.cpp
│       ├── DJ01BTTask_LLMDecision.cpp
│       └── DJ01BTTask_LLMDialogue.cpp
```

---

## 3.3 核心代码实现

### 3.3.1 AI 类型定义

```cpp
// DJ01AITypes.h
#pragma once

#include "CoreMinimal.h"
#include "DJ01AITypes.generated.h"

/**
 * LLM 请求配置
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01LLMRequestConfig
{
    GENERATED_BODY()

    // API 端点 URL
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    FString Endpoint = TEXT("https://api.openai.com/v1/chat/completions");

    // API 密钥（建议从配置文件读取）
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    FString APIKey;

    // 使用的模型
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    FString Model = TEXT("gpt-4");

    // 温度参数（0-1，越高越随机）
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    float Temperature = 0.7f;

    // 最大 Token 数
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    int32 MaxTokens = 256;

    // 请求超时时间（秒）
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    float TimeoutSeconds = 10.0f;
};

/**
 * LLM 聊天消息
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01LLMMessage
{
    GENERATED_BODY()

    // 角色: "system", "user", "assistant"
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    FString Role;

    // 内容
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "LLM")
    FString Content;
};

/**
 * LLM 响应结果
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01LLMResponse
{
    GENERATED_BODY()

    // 是否成功
    UPROPERTY(BlueprintReadOnly, Category = "LLM")
    bool bSuccess = false;

    // 响应内容
    UPROPERTY(BlueprintReadOnly, Category = "LLM")
    FString Content;

    // 错误信息
    UPROPERTY(BlueprintReadOnly, Category = "LLM")
    FString ErrorMessage;

    // 使用的 Token 数
    UPROPERTY(BlueprintReadOnly, Category = "LLM")
    int32 TokensUsed = 0;

    // 响应延迟（毫秒）
    UPROPERTY(BlueprintReadOnly, Category = "LLM")
    float LatencyMs = 0.0f;
};

/**
 * AI 战斗决策
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01AICombatDecision
{
    GENERATED_BODY()

    // 决策类型
    UPROPERTY(BlueprintReadOnly, Category = "AI")
    FString ActionType; // "Attack", "Defend", "Skill", "Flee", "Wait"

    // 目标 Actor
    UPROPERTY(BlueprintReadOnly, Category = "AI")
    TWeakObjectPtr<AActor> TargetActor = nullptr;

    // 使用的技能 ID（如果是 Skill 类型）
    UPROPERTY(BlueprintReadOnly, Category = "AI")
    FString SkillId;

    // 移动目标位置（如果需要移动）
    UPROPERTY(BlueprintReadOnly, Category = "AI")
    FVector MoveLocation = FVector::ZeroVector;

    // 决策置信度（0-1）
    UPROPERTY(BlueprintReadOnly, Category = "AI")
    float Confidence = 0.0f;

    // LLM 的推理说明（用于调试）
    UPROPERTY(BlueprintReadOnly, Category = "AI")
    FString Reasoning;
};

/**
 * NPC 性格配置
 */
USTRUCT(BlueprintType)
struct DJ01_API FDJ01NPCPersonality
{
    GENERATED_BODY()

    // NPC 名称
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI")
    FString Name = TEXT("Unknown");

    // 性格描述
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI", meta=(MultiLine=true))
    FString PersonalityDesc = TEXT("A neutral NPC.");

    // 背景故事
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI", meta=(MultiLine=true))
    FString Backstory;

    // 说话风格
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI")
    FString SpeakingStyle = TEXT("formal");

    // 战斗风格
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI")
    FString CombatStyle = TEXT("balanced"); // aggressive, defensive, balanced, tactical
};
```

---

### 3.3.2 LLM 通信子系统

```cpp
// DJ01LLMSubsystem.h
#pragma once

#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "DJ01AITypes.h"
#include "Interfaces/IHttpRequest.h"
#include "DJ01LLMSubsystem.generated.h"

DECLARE_DYNAMIC_DELEGATE_OneParam(FOnLLMResponseReceived, const FDJ01LLMResponse&, Response);

/**
 * LLM 大模型通信子系统
 * 管理所有与 LLM API 的通信，提供异步请求接口
 */
UCLASS()
class DJ01_API UDJ01LLMSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()

public:
    //~ Begin USubsystem Interface
    virtual void Initialize(FSubsystemCollectionBase& Collection) override;
    virtual void Deinitialize() override;
    //~ End USubsystem Interface

    /**
     * 发送聊天请求到 LLM
     * @param Messages 消息列表（包含上下文）
     * @param OnComplete 完成回调
     * @param Config 可选的自定义配置
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|LLM")
    void SendChatRequest(
        const TArray<FDJ01LLMMessage>& Messages,
        FOnLLMResponseReceived OnComplete,
        const FDJ01LLMRequestConfig& Config);

    /**
     * 发送简单单轮对话
     * @param SystemPrompt 系统提示词
     * @param UserMessage 用户消息
     * @param OnComplete 完成回调
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|LLM")
    void SendSimpleRequest(
        const FString& SystemPrompt,
        const FString& UserMessage,
        FOnLLMResponseReceived OnComplete);

    /**
     * 设置全局 API 配置
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|LLM")
    void SetGlobalConfig(const FDJ01LLMRequestConfig& NewConfig);

    /**
     * 获取当前配置
     */
    UFUNCTION(BlueprintPure, Category = "DJ01|LLM")
    FDJ01LLMRequestConfig GetGlobalConfig() const { return GlobalConfig; }

protected:
    /** 处理 HTTP 响应 */
    void HandleHttpResponse(
        FHttpRequestPtr Request,
        FHttpResponsePtr Response,
        bool bSuccess,
        FOnLLMResponseReceived OnComplete,
        float RequestStartTime);

    /** 解析 LLM 响应 JSON */
    FDJ01LLMResponse ParseLLMResponse(const FString& JsonString);

    /** 构建请求 JSON */
    FString BuildRequestJson(const TArray<FDJ01LLMMessage>& Messages, const FDJ01LLMRequestConfig& Config);

private:
    // 全局配置
    UPROPERTY()
    FDJ01LLMRequestConfig GlobalConfig;

    // 活跃请求计数（用于限流）
    int32 ActiveRequestCount = 0;

    // 最大并发请求数
    static constexpr int32 MaxConcurrentRequests = 5;
};
```

---

### 3.3.3 LLM 子系统实现

```cpp
// DJ01LLMSubsystem.cpp
#include "DJ01LLMSubsystem.h"
#include "HttpModule.h"
#include "Interfaces/IHttpResponse.h"
#include "Dom/JsonObject.h"
#include "Serialization/JsonReader.h"
#include "Serialization/JsonSerializer.h"
#include "Serialization/JsonWriter.h"
#include "Misc/ConfigCacheIni.h"

void UDJ01LLMSubsystem::Initialize(FSubsystemCollectionBase& Collection)
{
    Super::Initialize(Collection);

    // 从配置文件读取 API 密钥（安全做法）
    FString APIKey;
    if (GConfig->GetString(TEXT("DJ01.LLM"), TEXT("APIKey"), APIKey, GGameIni))
    {
        GlobalConfig.APIKey = APIKey;
    }

    // 读取其他配置
    FString Endpoint;
    if (GConfig->GetString(TEXT("DJ01.LLM"), TEXT("Endpoint"), Endpoint, GGameIni))
    {
        GlobalConfig.Endpoint = Endpoint;
    }

    UE_LOG(LogTemp, Log, TEXT("[DJ01 LLM] Subsystem initialized. Endpoint: %s"), *GlobalConfig.Endpoint);
}

void UDJ01LLMSubsystem::Deinitialize()
{
    Super::Deinitialize();
}

void UDJ01LLMSubsystem::SetGlobalConfig(const FDJ01LLMRequestConfig& NewConfig)
{
    GlobalConfig = NewConfig;
}

void UDJ01LLMSubsystem::SendChatRequest(
    const TArray<FDJ01LLMMessage>& Messages,
    FOnLLMResponseReceived OnComplete,
    const FDJ01LLMRequestConfig& Config)
{
    // 限流检查
    if (ActiveRequestCount >= MaxConcurrentRequests)
    {
        FDJ01LLMResponse ErrorResponse;
        ErrorResponse.bSuccess = false;
        ErrorResponse.ErrorMessage = TEXT("Too many concurrent requests");
        OnComplete.ExecuteIfBound(ErrorResponse);
        return;
    }

    // 合并配置（使用传入配置，缺失项用全局配置填充）
    FDJ01LLMRequestConfig FinalConfig = Config;
    if (FinalConfig.APIKey.IsEmpty()) FinalConfig.APIKey = GlobalConfig.APIKey;
    if (FinalConfig.Endpoint.IsEmpty()) FinalConfig.Endpoint = GlobalConfig.Endpoint;

    // 创建 HTTP 请求
    TSharedRef<IHttpRequest, ESPMode::ThreadSafe> HttpRequest = FHttpModule::Get().CreateRequest();
    HttpRequest->SetURL(FinalConfig.Endpoint);
    HttpRequest->SetVerb(TEXT("POST"));
    HttpRequest->SetHeader(TEXT("Content-Type"), TEXT("application/json"));
    HttpRequest->SetHeader(TEXT("Authorization"), FString::Printf(TEXT("Bearer %s"), *FinalConfig.APIKey));
    HttpRequest->SetTimeout(FinalConfig.TimeoutSeconds);

    // 构建请求体
    FString RequestBody = BuildRequestJson(Messages, FinalConfig);
    HttpRequest->SetContentAsString(RequestBody);

    // 记录开始时间
    float RequestStartTime = FPlatformTime::Seconds();

    // 绑定回调
    HttpRequest->OnProcessRequestComplete().BindUObject(
        this,
        &UDJ01LLMSubsystem::HandleHttpResponse,
        OnComplete,
        RequestStartTime);

    // 发送请求
    ActiveRequestCount++;
    HttpRequest->ProcessRequest();

    UE_LOG(LogTemp, Verbose, TEXT("[DJ01 LLM] Request sent. Active: %d"), ActiveRequestCount);
}

void UDJ01LLMSubsystem::SendSimpleRequest(
    const FString& SystemPrompt,
    const FString& UserMessage,
    FOnLLMResponseReceived OnComplete)
{
    TArray<FDJ01LLMMessage> Messages;

    FDJ01LLMMessage SystemMsg;
    SystemMsg.Role = TEXT("system");
    SystemMsg.Content = SystemPrompt;
    Messages.Add(SystemMsg);

    FDJ01LLMMessage UserMsg;
    UserMsg.Role = TEXT("user");
    UserMsg.Content = UserMessage;
    Messages.Add(UserMsg);

    SendChatRequest(Messages, OnComplete, GlobalConfig);
}

FString UDJ01LLMSubsystem::BuildRequestJson(const TArray<FDJ01LLMMessage>& Messages, const FDJ01LLMRequestConfig& Config)
{
    TSharedPtr<FJsonObject> RootObject = MakeShareable(new FJsonObject());
    RootObject->SetStringField(TEXT("model"), Config.Model);
    RootObject->SetNumberField(TEXT("temperature"), Config.Temperature);
    RootObject->SetNumberField(TEXT("max_tokens"), Config.MaxTokens);

    // 构建 messages 数组
    TArray<TSharedPtr<FJsonValue>> MessagesArray;
    for (const FDJ01LLMMessage& Msg : Messages)
    {
        TSharedPtr<FJsonObject> MsgObject = MakeShareable(new FJsonObject());
        MsgObject->SetStringField(TEXT("role"), Msg.Role);
        MsgObject->SetStringField(TEXT("content"), Msg.Content);
        MessagesArray.Add(MakeShareable(new FJsonValueObject(MsgObject)));
    }
    RootObject->SetArrayField(TEXT("messages"), MessagesArray);

    // 序列化为字符串
    FString OutputString;
    TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&OutputString);
    FJsonSerializer::Serialize(RootObject.ToSharedRef(), Writer);

    return OutputString;
}

void UDJ01LLMSubsystem::HandleHttpResponse(
    FHttpRequestPtr Request,
    FHttpResponsePtr Response,
    bool bSuccess,
    FOnLLMResponseReceived OnComplete,
    float RequestStartTime)
{
    ActiveRequestCount--;

    FDJ01LLMResponse LLMResponse;
    LLMResponse.LatencyMs = (FPlatformTime::Seconds() - RequestStartTime) * 1000.0f;

    if (!bSuccess || !Response.IsValid())
    {
        LLMResponse.bSuccess = false;
        LLMResponse.ErrorMessage = TEXT("HTTP request failed");
        OnComplete.ExecuteIfBound(LLMResponse);
        return;
    }

    int32 ResponseCode = Response->GetResponseCode();
    if (ResponseCode != 200)
    {
        LLMResponse.bSuccess = false;
        LLMResponse.ErrorMessage = FString::Printf(TEXT("HTTP %d: %s"), ResponseCode, *Response->GetContentAsString());
        OnComplete.ExecuteIfBound(LLMResponse);
        return;
    }

    // 解析响应
    LLMResponse = ParseLLMResponse(Response->GetContentAsString());
    LLMResponse.LatencyMs = (FPlatformTime::Seconds() - RequestStartTime) * 1000.0f;

    OnComplete.ExecuteIfBound(LLMResponse);
}

FDJ01LLMResponse UDJ01LLMSubsystem::ParseLLMResponse(const FString& JsonString)
{
    FDJ01LLMResponse Result;

    TSharedPtr<FJsonObject> JsonObject;
    TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(JsonString);

    if (!FJsonSerializer::Deserialize(Reader, JsonObject) || !JsonObject.IsValid())
    {
        Result.bSuccess = false;
        Result.ErrorMessage = TEXT("Failed to parse JSON response");
        return Result;
    }

    // 检查错误
    if (JsonObject->HasField(TEXT("error")))
    {
        const TSharedPtr<FJsonObject>* ErrorObject;
        if (JsonObject->TryGetObjectField(TEXT("error"), ErrorObject))
        {
            Result.bSuccess = false;
            Result.ErrorMessage = (*ErrorObject)->GetStringField(TEXT("message"));
            return Result;
        }
    }

    // 解析 choices
    const TArray<TSharedPtr<FJsonValue>>* ChoicesArray;
    if (JsonObject->TryGetArrayField(TEXT("choices"), ChoicesArray) && ChoicesArray->Num() > 0)
    {
        const TSharedPtr<FJsonObject>* FirstChoice = nullptr;
        if ((*ChoicesArray)[0]->TryGetObject(FirstChoice))
        {
            const TSharedPtr<FJsonObject>* MessageObject = nullptr;
            if ((*FirstChoice)->TryGetObjectField(TEXT("message"), MessageObject))
            {
                Result.Content = (*MessageObject)->GetStringField(TEXT("content"));
                Result.bSuccess = true;
            }
        }
    }

    // 解析 token 使用量
    const TSharedPtr<FJsonObject>* UsageObject;
    if (JsonObject->TryGetObjectField(TEXT("usage"), UsageObject))
    {
        Result.TokensUsed = (*UsageObject)->GetIntegerField(TEXT("total_tokens"));
    }

    return Result;
}
```

---

### 3.3.4 AI 大脑组件

```cpp
// DJ01AIBrainComponent.h
#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "DJ01AITypes.h"
#include "DJ01AIBrainComponent.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnCombatDecisionMade, const FDJ01AICombatDecision&, Decision);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnDialogueResponseReady, const FString&, Response);

/**
 * AI 大脑组件
 * 负责管理 NPC 的智能决策，桥接 LLM 与游戏逻辑
 */
UCLASS(ClassGroup=(DJ01), meta=(BlueprintSpawnableComponent))
class DJ01_API UDJ01AIBrainComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UDJ01AIBrainComponent();

    //~ Begin UActorComponent Interface
    virtual void BeginPlay() override;
    //~ End UActorComponent Interface

    // ========== 战斗决策 API ==========

    /**
     * 请求战斗决策
     * 根据当前战斗态势，让 LLM 决定下一步行动
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|AI")
    void RequestCombatDecision();

    /**
     * 战斗决策完成事件
     */
    UPROPERTY(BlueprintAssignable, Category = "DJ01|AI")
    FOnCombatDecisionMade OnCombatDecisionMade;

    // ========== 对话 API ==========

    /**
     * 请求对话响应
     * @param PlayerMessage 玩家发送的消息
     */
    UFUNCTION(BlueprintCallable, Category = "DJ01|AI")
    void RequestDialogueResponse(const FString& PlayerMessage);

    /**
     * 对话响应就绪事件
     */
    UPROPERTY(BlueprintAssignable, Category = "DJ01|AI")
    FOnDialogueResponseReady OnDialogueResponseReady;

    // ========== 配置 ==========

    /** NPC 性格配置 */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "DJ01|AI")
    FDJ01NPCPersonality Personality;

    /** 对话历史记录最大长度 */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "DJ01|AI")
    int32 MaxDialogueHistory = 10;

    /** 是否正在等待响应 */
    UFUNCTION(BlueprintPure, Category = "DJ01|AI")
    bool IsWaitingForResponse() const { return bWaitingForResponse; }

protected:
    /** 构建战斗决策的系统提示词 */
    FString BuildCombatSystemPrompt();

    /** 构建战斗态势描述 */
    FString BuildCombatSituation();

    /** 解析战斗决策响应 */
    FDJ01AICombatDecision ParseCombatDecision(const FString& LLMResponse);

    /** 构建对话系统提示词 */
    FString BuildDialogueSystemPrompt();

    /** 处理 LLM 战斗决策响应 */
    UFUNCTION()
    void HandleCombatDecisionResponse(const FDJ01LLMResponse& Response);

    /** 处理 LLM 对话响应 */
    UFUNCTION()
    void HandleDialogueResponse(const FDJ01LLMResponse& Response);

private:
    // LLM 子系统引用
    UPROPERTY()
    class UDJ01LLMSubsystem* LLMSubsystem = nullptr;

    // 对话历史
    UPROPERTY()
    TArray<FDJ01LLMMessage> DialogueHistory;

    // 是否正在等待响应
    bool bWaitingForResponse = false;
};
```

---

### 3.3.5 AI 大脑组件实现

```cpp
// DJ01AIBrainComponent.cpp
#include "DJ01AIBrainComponent.h"
#include "DJ01LLMSubsystem.h"
#include "GameFramework/Character.h"
#include "Kismet/GameplayStatics.h"

UDJ01AIBrainComponent::UDJ01AIBrainComponent()
{
    PrimaryComponentTick.bCanEverTick = false;
}

void UDJ01AIBrainComponent::BeginPlay()
{
    Super::BeginPlay();

    // 获取 LLM 子系统
    if (UGameInstance* GI = UGameplayStatics::GetGameInstance(this))
    {
        LLMSubsystem = GI->GetSubsystem<UDJ01LLMSubsystem>();
    }

    if (!LLMSubsystem)
    {
        UE_LOG(LogTemp, Error, TEXT("[DJ01 AIBrain] Failed to get LLMSubsystem!"));
    }
}

// ==================== 战斗决策 ====================

void UDJ01AIBrainComponent::RequestCombatDecision()
{
    if (!LLMSubsystem || bWaitingForResponse)
    {
        return;
    }

    bWaitingForResponse = true;

    FString SystemPrompt = BuildCombatSystemPrompt();
    FString Situation = BuildCombatSituation();

    FOnLLMResponseReceived Callback;
    Callback.BindDynamic(this, &UDJ01AIBrainComponent::HandleCombatDecisionResponse);

    LLMSubsystem->SendSimpleRequest(SystemPrompt, Situation, Callback);
}

FString UDJ01AIBrainComponent::BuildCombatSystemPrompt()
{
    return FString::Printf(TEXT(
        "You are an AI controlling an NPC named %s in a combat game.\n"
        "Combat Style: %s\n"
        "Personality: %s\n\n"
        "Based on the combat situation, decide the next action.\n"
        "Respond in JSON format:\n"
        "{\n"
        "  \"action\": \"Attack|Defend|Skill|Flee|Wait\",\n"
        "  \"target_index\": 0,\n"
        "  \"skill_id\": \"skill_name_if_using_skill\",\n"
        "  \"confidence\": 0.8,\n"
        "  \"reasoning\": \"brief explanation\"\n"
        "}"
    ), *Personality.Name, *Personality.CombatStyle, *Personality.PersonalityDesc);
}

FString UDJ01AIBrainComponent::BuildCombatSituation()
{
    // 收集当前战斗态势
    FString Situation = TEXT("Current Combat Situation:\n");

    // 自身状态
    if (AActor* Owner = GetOwner())
    {
        Situation += FString::Printf(TEXT("- Self HP: 70%%\n")); // TODO: 从 AttributeSet 获取
        Situation += FString::Printf(TEXT("- Self Position: %s\n"), *Owner->GetActorLocation().ToString());
    }

    // 敌人列表 (简化示例)
    Situation += TEXT("Enemies:\n");
    Situation += TEXT("  [0] Player - HP: 80%%, Distance: 500 units, Stance: Aggressive\n");

    // 可用技能
    Situation += TEXT("Available Skills:\n");
    Situation += TEXT("  - basic_attack (no cooldown)\n");
    Situation += TEXT("  - heavy_strike (ready)\n");
    Situation += TEXT("  - defensive_stance (ready)\n");

    return Situation;
}

void UDJ01AIBrainComponent::HandleCombatDecisionResponse(const FDJ01LLMResponse& Response)
{
    bWaitingForResponse = false;

    if (!Response.bSuccess)
    {
        UE_LOG(LogTemp, Warning, TEXT("[DJ01 AIBrain] Combat decision failed: %s"), *Response.ErrorMessage);
        
        // 失败时使用默认行为
        FDJ01AICombatDecision DefaultDecision;
        DefaultDecision.ActionType = TEXT("Attack");
        DefaultDecision.Confidence = 0.5f;
        DefaultDecision.Reasoning = TEXT("Fallback decision due to LLM failure");
        OnCombatDecisionMade.Broadcast(DefaultDecision);
        return;
    }

    FDJ01AICombatDecision Decision = ParseCombatDecision(Response.Content);
    OnCombatDecisionMade.Broadcast(Decision);

    UE_LOG(LogTemp, Log, TEXT("[DJ01 AIBrain] Decision: %s (%.0f%% confidence) - %s"),
           *Decision.ActionType, Decision.Confidence * 100, *Decision.Reasoning);
}

FDJ01AICombatDecision UDJ01AIBrainComponent::ParseCombatDecision(const FString& LLMResponse)
{
    FDJ01AICombatDecision Decision;

    // 解析 JSON
    TSharedPtr<FJsonObject> JsonObject;
    TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(LLMResponse);

    if (FJsonSerializer::Deserialize(Reader, JsonObject) && JsonObject.IsValid())
    {
        Decision.ActionType = JsonObject->GetStringField(TEXT("action"));
        Decision.SkillId = JsonObject->GetStringField(TEXT("skill_id"));
        Decision.Confidence = JsonObject->GetNumberField(TEXT("confidence"));
        Decision.Reasoning = JsonObject->GetStringField(TEXT("reasoning"));

        // 解析目标索引（需要转换为实际 Actor）
        int32 TargetIndex = JsonObject->GetIntegerField(TEXT("target_index"));
        // TODO: 根据索引查找实际目标 Actor
    }
    else
    {
        // JSON 解析失败，使用默认值
        Decision.ActionType = TEXT("Wait");
        Decision.Confidence = 0.3f;
        Decision.Reasoning = TEXT("Failed to parse LLM response");
    }

    return Decision;
}

// ==================== 对话系统 ====================

void UDJ01AIBrainComponent::RequestDialogueResponse(const FString& PlayerMessage)
{
    if (!LLMSubsystem || bWaitingForResponse)
    {
        return;
    }

    bWaitingForResponse = true;

    // 添加玩家消息到历史
    FDJ01LLMMessage UserMsg;
    UserMsg.Role = TEXT("user");
    UserMsg.Content = PlayerMessage;
    DialogueHistory.Add(UserMsg);

    // 限制历史长度
    while (DialogueHistory.Num() > MaxDialogueHistory)
    {
        DialogueHistory.RemoveAt(0);
    }

    // 构建完整消息列表
    TArray<FDJ01LLMMessage> Messages;

    // 系统提示词
    FDJ01LLMMessage SystemMsg;
    SystemMsg.Role = TEXT("system");
    SystemMsg.Content = BuildDialogueSystemPrompt();
    Messages.Add(SystemMsg);

    // 添加对话历史
    Messages.Append(DialogueHistory);

    FOnLLMResponseReceived Callback;
    Callback.BindDynamic(this, &UDJ01AIBrainComponent::HandleDialogueResponse);

    LLMSubsystem->SendChatRequest(Messages, Callback, LLMSubsystem->GetGlobalConfig());
}

FString UDJ01AIBrainComponent::BuildDialogueSystemPrompt()
{
    return FString::Printf(TEXT(
        "You are %s, an NPC in a fantasy RPG game.\n"
        "Personality: %s\n"
        "Backstory: %s\n"
        "Speaking Style: %s\n\n"
        "Respond in character. Keep responses concise (1-3 sentences).\n"
        "Do not break character or mention that you are an AI."
    ), *Personality.Name, *Personality.PersonalityDesc, *Personality.Backstory, *Personality.SpeakingStyle);
}

void UDJ01AIBrainComponent::HandleDialogueResponse(const FDJ01LLMResponse& Response)
{
    bWaitingForResponse = false;

    if (!Response.bSuccess)
    {
        UE_LOG(LogTemp, Warning, TEXT("[DJ01 AIBrain] Dialogue failed: %s"), *Response.ErrorMessage);
        OnDialogueResponseReady.Broadcast(TEXT("..."));
        return;
    }

    // 添加助手回复到历史
    FDJ01LLMMessage AssistantMsg;
    AssistantMsg.Role = TEXT("assistant");
    AssistantMsg.Content = Response.Content;
    DialogueHistory.Add(AssistantMsg);

    OnDialogueResponseReady.Broadcast(Response.Content);
}
```

---

### 3.3.6 行为树决策任务

```cpp
// DJ01BTTask_LLMDecision.h
#pragma once

#include "CoreMinimal.h"
#include "BehaviorTree/BTTaskNode.h"
#include "DJ01AITypes.h"
#include "DJ01BTTask_LLMDecision.generated.h"

/**
 * 行为树任务：请求 LLM 战斗决策
 * 这是一个潜伏任务（Latent），会等待 LLM 响应后完成
 */
UCLASS()
class DJ01_API UDJ01BTTask_LLMDecision : public UBTTaskNode
{
    GENERATED_BODY()

public:
    UDJ01BTTask_LLMDecision();

    //~ Begin UBTTaskNode Interface
    virtual EBTNodeResult::Type ExecuteTask(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory) override;
    virtual EBTNodeResult::Type AbortTask(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory) override;
    virtual FString GetStaticDescription() const override;
    //~ End UBTTaskNode Interface

protected:
    /** 输出决策类型的黑板键 */
    UPROPERTY(EditAnywhere, Category = "Blackboard")
    FBlackboardKeySelector ActionTypeKey;

    /** 输出目标的黑板键 */
    UPROPERTY(EditAnywhere, Category = "Blackboard")
    FBlackboardKeySelector TargetActorKey;

    /** 输出技能 ID 的黑板键 */
    UPROPERTY(EditAnywhere, Category = "Blackboard")
    FBlackboardKeySelector SkillIdKey;

private:
    /** 处理决策结果 */
    UFUNCTION()
    void OnDecisionMade(const FDJ01AICombatDecision& Decision);

    // 缓存的行为树组件
    UPROPERTY()
    UBehaviorTreeComponent* CachedOwnerComp = nullptr;
};
```

```cpp
// DJ01BTTask_LLMDecision.cpp
#include "DJ01BTTask_LLMDecision.h"
#include "DJ01AIBrainComponent.h"
#include "AIController.h"
#include "BehaviorTree/BlackboardComponent.h"

UDJ01BTTask_LLMDecision::UDJ01BTTask_LLMDecision()
{
    NodeName = TEXT("Request LLM Combat Decision");
    bNotifyTick = false;
    bNotifyTaskFinished = true;
}

EBTNodeResult::Type UDJ01BTTask_LLMDecision::ExecuteTask(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory)
{
    // 获取 AI 控制器和被控制的 Pawn
    AAIController* AIController = OwnerComp.GetAIOwner();
    if (!AIController)
    {
        return EBTNodeResult::Failed;
    }

    APawn* ControlledPawn = AIController->GetPawn();
    if (!ControlledPawn)
    {
        return EBTNodeResult::Failed;
    }

    // 获取 AI 大脑组件
    UDJ01AIBrainComponent* BrainComp = ControlledPawn->FindComponentByClass<UDJ01AIBrainComponent>();
    if (!BrainComp)
    {
        UE_LOG(LogTemp, Warning, TEXT("[DJ01 BT] No AIBrainComponent found on %s"), *ControlledPawn->GetName());
        return EBTNodeResult::Failed;
    }

    // 如果已经在等待响应，直接返回
    if (BrainComp->IsWaitingForResponse())
    {
        return EBTNodeResult::InProgress;
    }

    // 缓存组件引用
    CachedOwnerComp = &OwnerComp;

    // 绑定回调
    BrainComp->OnCombatDecisionMade.AddDynamic(this, &UDJ01BTTask_LLMDecision::OnDecisionMade);

    // 发起请求
    BrainComp->RequestCombatDecision();

    return EBTNodeResult::InProgress;
}

EBTNodeResult::Type UDJ01BTTask_LLMDecision::AbortTask(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory)
{
    // 清理回调
    if (AAIController* AIController = OwnerComp.GetAIOwner())
    {
        if (APawn* Pawn = AIController->GetPawn())
        {
            if (UDJ01AIBrainComponent* BrainComp = Pawn->FindComponentByClass<UDJ01AIBrainComponent>())
            {
                BrainComp->OnCombatDecisionMade.RemoveDynamic(this, &UDJ01BTTask_LLMDecision::OnDecisionMade);
            }
        }
    }

    return EBTNodeResult::Aborted;
}

void UDJ01BTTask_LLMDecision::OnDecisionMade(const FDJ01AICombatDecision& Decision)
{
    if (!CachedOwnerComp)
    {
        return;
    }

    // 移除回调
    if (AAIController* AIController = CachedOwnerComp->GetAIOwner())
    {
        if (APawn* Pawn = AIController->GetPawn())
        {
            if (UDJ01AIBrainComponent* BrainComp = Pawn->FindComponentByClass<UDJ01AIBrainComponent>())
            {
                BrainComp->OnCombatDecisionMade.RemoveDynamic(this, &UDJ01BTTask_LLMDecision::OnDecisionMade);
            }
        }
    }

    // 将决策结果写入黑板
    UBlackboardComponent* Blackboard = CachedOwnerComp->GetBlackboardComponent();
    if (Blackboard)
    {
        Blackboard->SetValueAsString(ActionTypeKey.SelectedKeyName, Decision.ActionType);
        Blackboard->SetValueAsObject(TargetActorKey.SelectedKeyName, Decision.TargetActor.Get());
        Blackboard->SetValueAsString(SkillIdKey.SelectedKeyName, Decision.SkillId);
    }

    // 完成任务
    FinishLatentTask(*CachedOwnerComp, EBTNodeResult::Succeeded);
}

FString UDJ01BTTask_LLMDecision::GetStaticDescription() const
{
    return FString::Printf(TEXT("Request LLM decision -> %s, %s"),
                           *ActionTypeKey.SelectedKeyName.ToString(),
                           *TargetActorKey.SelectedKeyName.ToString());
}
```

---

## 3.4 实现步骤清单

| 序号 | 任务 | 文件 | 依赖 |
|-----|------|------|------|
| 3.1 | 创建 AI 类型定义 | `DJ01AITypes.h` | 无 |
| 3.2 | 实现 LLM 子系统头文件 | `DJ01LLMSubsystem.h` | 3.1 |
| 3.3 | 实现 LLM 子系统逻辑 | `DJ01LLMSubsystem.cpp` | 3.2 |
| 3.4 | 实现 AI 大脑组件头文件 | `DJ01AIBrainComponent.h` | 3.1 |
| 3.5 | 实现 AI 大脑组件逻辑 | `DJ01AIBrainComponent.cpp` | 3.2, 3.4 |
| 3.6 | 实现行为树决策任务 | `DJ01BTTask_LLMDecision.h/.cpp` | 3.4 |
| 3.7 | 实现行为树对话任务 | `DJ01BTTask_LLMDialogue.h/.cpp` | 3.4 |
| 3.8 | 配置 API 密钥 | `Config/DefaultGame.ini` | 无 |

---

## 3.5 配置文件示例

在 `Config/DefaultGame.ini` 中添加：

```ini
[DJ01.LLM]
; 注意：实际部署时应从环境变量或加密存储获取
Endpoint=https://api.openai.com/v1/chat/completions
APIKey=your-api-key-here
Model=gpt-4
Temperature=0.7
MaxTokens=256
```

---

## 3.6 测试验证点

### 单元测试
1. **JSON 构建**：验证 `BuildRequestJson` 输出格式正确
2. **响应解析**：验证各种 LLM 响应格式的解析
3. **错误处理**：验证网络错误、超时、API 错误的处理

### 集成测试
1. **端到端对话**：NPC 能够根据性格配置进行角色扮演对话
2. **战斗决策**：NPC 能够根据战斗态势做出合理决策
3. **行为树集成**：决策结果正确写入黑板并触发后续行为

### 性能测试
1. **延迟测量**：记录 LLM 响应延迟，确保 UI 有 loading 状态
2. **并发限制**：验证超过最大并发数时的限流行为

---

## 3.7 下一步

完成 Phase 3 后，继续阅读 [04_Phase4_DemoIntegration.md](./04_Phase4_DemoIntegration.md) 进行最终演示场景集成。