# 代码实现清单

> **目的**：汇总所有需要实现的类和文件，提供明确的验收标准和实现顺序。

---

## 总览

| Phase | 模块 | 类数量 | 预计工时 |
|-------|------|--------|---------|
| Phase 1 | 网络基础架构 | 4 | 5天 |
| Phase 2 | GAS 战斗同步 | 5 | 7天 |
| Phase 3 | AI 大模型集成 | 5 | 7天 |
| Phase 4 | 演示场景集成 | 5 | 5天 |
| **合计** | - | **19** | **24天** |

---

## Phase 1: 网络基础架构

### 1.1 分布式类型定义

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01DistributedTypes.h` | ⬜ 待实现 | 服务器信息、消息类型等结构体 |

**验收标准**：
- [ ] `FDJ01ServerInfo` 结构体包含 ServerId, Address, Port, CurrentLoad, MaxCapacity
- [ ] `FDJ01BrokerMessage` 结构体包含 MessageType, Payload, SenderId, TargetId
- [ ] 所有结构体支持蓝图读写

**代码位置**：`Source/DJ01/Network/Public/DJ01DistributedTypes.h`

---

### 1.2 Master Server 子系统

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01MasterServer.h` | ⬜ 待实现 | Master Server 头文件 |
| `DJ01MasterServer.cpp` | ⬜ 待实现 | Master Server 实现 |

**验收标准**：
- [ ] 继承自 `UGameInstanceSubsystem`
- [ ] 实现 `RegisterServer()` 服务器注册
- [ ] 实现 `GetBestServer()` 负载均衡选择
- [ ] 实现 `RequestJoinScene()` 场景分配
- [ ] 维护 `TMap<FString, FDJ01ServerInfo>` 服务器列表
- [ ] 单元测试覆盖率 > 80%

**代码位置**：`Source/DJ01/Network/Public/DJ01MasterServer.h`

---

### 1.3 Message Broker 子系统

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01MessageBroker.h` | ⬜ 待实现 | Message Broker 头文件 |
| `DJ01MessageBroker.cpp` | ⬜ 待实现 | Message Broker 实现 |

**验收标准**：
- [ ] 继承自 `UGameInstanceSubsystem`
- [ ] 实现 `Subscribe()` 订阅主题
- [ ] 实现 `Unsubscribe()` 取消订阅
- [ ] 实现 `Publish()` 发布消息
- [ ] 实现 `RouteMessage()` 消息路由
- [ ] 支持跨服务器消息转发
- [ ] 消息队列最大容量可配置

**代码位置**：`Source/DJ01/Network/Public/DJ01MessageBroker.h`

---

### 1.4 网络管理器

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01NetworkManager.h` | ⬜ 待实现 | 网络连接管理 |
| `DJ01NetworkManager.cpp` | ⬜ 待实现 | 网络连接实现 |

**验收标准**：
- [ ] 管理客户端与服务器连接
- [ ] 实现连接状态监控
- [ ] 实现断线重连逻辑
- [ ] 网络延迟统计

**代码位置**：`Source/DJ01/Network/Public/DJ01NetworkManager.h`

---

## Phase 2: GAS 战斗同步

### 2.1 预测类型定义

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01PredictionTypes.h` | ⬜ 待实现 | 预测相关结构体 |

**验收标准**：
- [ ] `FDJ01AbilitySnapshot` 包含预测键、时间戳、位置、目标
- [ ] `FDJ01AbilityResult` 包含成功标志、错误原因、修正数据
- [ ] 支持网络序列化

**代码位置**：`Source/DJ01/AbilitySystem/Public/DJ01PredictionTypes.h`

---

### 2.2 扩展 AbilitySystemComponent

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01AbilitySystemComponent.h` | ⬜ 待实现 | ASC 扩展头文件 |
| `DJ01AbilitySystemComponent.cpp` | ⬜ 待实现 | ASC 扩展实现 |

**验收标准**：
- [ ] 继承自 `UAbilitySystemComponent`
- [ ] 实现 `CreatePrediction()` 创建预测快照
- [ ] 实现 `ServerValidatePrediction()` 服务端验证 (Server RPC)
- [ ] 实现 `ClientReceivePredictionResult()` 客户端回调 (Client RPC)
- [ ] 实现 `ExecuteRollback()` 回滚逻辑
- [ ] `OnPredictionRejected` 委托可在蓝图绑定
- [ ] 预测队列自动清理

**代码位置**：`Source/DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h`

---

### 2.3 伤害执行计算

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01DamageExecution.h` | ⬜ 待实现 | 伤害计算头文件 |
| `DJ01DamageExecution.cpp` | ⬜ 待实现 | 伤害计算实现 |

**验收标准**：
- [ ] 继承自 `UGameplayEffectExecutionCalculation`
- [ ] 捕获 Attack, Defense, Health 属性
- [ ] 实现伤害公式：`FinalDamage = Attack * (100 / (100 + Defense))`
- [ ] 支持暴击、格挡修正（可选）
- [ ] 伤害值最小为 1

**代码位置**：`Source/DJ01/AbilitySystem/Public/DJ01DamageExecution.h`

---

### 2.4 近战技能基类

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01GameplayAbility_Melee.h` | ⬜ 待实现 | 近战技能头文件 |
| `DJ01GameplayAbility_Melee.cpp` | ⬜ 待实现 | 近战技能实现 |

**验收标准**：
- [ ] 继承自 `UGameplayAbility`
- [ ] 配置：攻击范围、攻击角度、伤害 GE
- [ ] 实现扇形范围命中检测
- [ ] 集成客户端预测流程
- [ ] 支持动画 Montage 播放

**代码位置**：`Source/DJ01/AbilitySystem/Public/DJ01GameplayAbility_Melee.h`

---

### 2.5 远程技能基类

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01GameplayAbility_Ranged.h` | ⬜ 待实现 | 远程技能头文件 |
| `DJ01GameplayAbility_Ranged.cpp` | ⬜ 待实现 | 远程技能实现 |

**验收标准**：
- [ ] 继承自 `UGameplayAbility`
- [ ] 配置：射程、弹道速度、伤害 GE
- [ ] 实现射线/抛物线命中检测
- [ ] 弹道同步（Projectile Replication）
- [ ] 支持预瞄准预测

**代码位置**：`Source/DJ01/AbilitySystem/Public/DJ01GameplayAbility_Ranged.h`

---

## Phase 3: AI 大模型集成

### 3.1 AI 类型定义

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01AITypes.h` | ⬜ 待实现 | AI 相关结构体 |

**验收标准**：
- [ ] `FDJ01LLMRequestConfig` 包含 Endpoint, APIKey, Model, Temperature, MaxTokens
- [ ] `FDJ01LLMMessage` 包含 Role, Content
- [ ] `FDJ01LLMResponse` 包含 bSuccess, Content, ErrorMessage, TokensUsed
- [ ] `FDJ01AICombatDecision` 包含 ActionType, Target, SkillId, Confidence
- [ ] `FDJ01NPCPersonality` 包含 Name, PersonalityDesc, Backstory, CombatStyle

**代码位置**：`Source/DJ01/AI/Public/DJ01AITypes.h`

---

### 3.2 LLM 通信子系统

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01LLMSubsystem.h` | ⬜ 待实现 | LLM 子系统头文件 |
| `DJ01LLMSubsystem.cpp` | ⬜ 待实现 | LLM 子系统实现 |

**验收标准**：
- [ ] 继承自 `UGameInstanceSubsystem`
- [ ] 实现 `SendChatRequest()` 发送聊天请求
- [ ] 实现 `SendSimpleRequest()` 简单单轮对话
- [ ] 支持 OpenAI 兼容 API 格式
- [ ] 异步回调 `FOnLLMResponseReceived`
- [ ] 并发请求限流（最大 5 个）
- [ ] 从配置文件读取 API 密钥
- [ ] 请求超时处理

**代码位置**：`Source/DJ01/AI/Public/DJ01LLMSubsystem.h`

---

### 3.3 AI 大脑组件

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01AIBrainComponent.h` | ⬜ 待实现 | AI 大脑组件头文件 |
| `DJ01AIBrainComponent.cpp` | ⬜ 待实现 | AI 大脑组件实现 |

**验收标准**：
- [ ] 继承自 `UActorComponent`
- [ ] 实现 `RequestCombatDecision()` 请求战斗决策
- [ ] 实现 `RequestDialogueResponse()` 请求对话响应
- [ ] 构建战斗态势描述（自身状态、敌人列表、可用技能）
- [ ] 解析 LLM JSON 响应为结构体
- [ ] 对话历史记录管理
- [ ] 失败时的默认行为

**代码位置**：`Source/DJ01/AI/Public/DJ01AIBrainComponent.h`

---

### 3.4 行为树 LLM 决策任务

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01BTTask_LLMDecision.h` | ⬜ 待实现 | BT 决策任务头文件 |
| `DJ01BTTask_LLMDecision.cpp` | ⬜ 待实现 | BT 决策任务实现 |

**验收标准**：
- [ ] 继承自 `UBTTaskNode`
- [ ] 实现 `ExecuteTask()` 发起 LLM 请求
- [ ] 实现 `AbortTask()` 清理回调
- [ ] 输出到黑板：ActionType, TargetActor, SkillId
- [ ] 潜伏任务（等待异步响应）

**代码位置**：`Source/DJ01/AI/Public/DJ01BTTask_LLMDecision.h`

---

### 3.5 行为树 LLM 对话任务

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01BTTask_LLMDialogue.h` | ⬜ 待实现 | BT 对话任务头文件 |
| `DJ01BTTask_LLMDialogue.cpp` | ⬜ 待实现 | BT 对话任务实现 |

**验收标准**：
- [ ] 继承自 `UBTTaskNode`
- [ ] 从黑板读取玩家消息
- [ ] 输出到黑板：对话响应文本
- [ ] 触发 UI 更新事件

**代码位置**：`Source/DJ01/AI/Public/DJ01BTTask_LLMDialogue.h`

---

## Phase 4: 演示场景集成

### 4.1 Demo GameMode

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01DemoGameMode.h` | ⬜ 待实现 | GameMode 头文件 |
| `DJ01DemoGameMode.cpp` | ⬜ 待实现 | GameMode 实现 |

**验收标准**：
- [ ] 管理玩家登录/登出
- [ ] 分配玩家出生点
- [ ] 生成 AI NPC
- [ ] 匹配倒计时逻辑
- [ ] 竞技场重置

**代码位置**：`Source/DJ01/Demo/Public/DJ01DemoGameMode.h`

---

### 4.2 调试 HUD

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01DemoHUD.h` | ⬜ 待实现 | HUD 头文件 |
| `DJ01DemoHUD.cpp` | ⬜ 待实现 | HUD 实现 |

**验收标准**：
- [ ] 显示网络统计（Ping、丢包率）
- [ ] 显示预测状态
- [ ] 显示 AI 决策日志
- [ ] 可通过命令开关

**代码位置**：`Source/DJ01/Demo/Public/DJ01DemoHUD.h`

---

### 4.3 竞技场管理器

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01ArenaManager.h` | ⬜ 待实现 | 竞技场管理器头文件 |
| `DJ01ArenaManager.cpp` | ⬜ 待实现 | 竞技场管理器实现 |

**验收标准**：
- [ ] 状态机：Idle → Countdown → InProgress → Finished
- [ ] 边界检测
- [ ] 状态同步（Replicated）

**代码位置**：`Source/DJ01/Demo/Public/DJ01ArenaManager.h`

---

### 4.4 Demo NPC 基类

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01DemoNPC.h` | ⬜ 待实现 | NPC 基类头文件 |
| `DJ01DemoNPC.cpp` | ⬜ 待实现 | NPC 基类实现 |

**验收标准**：
- [ ] 集成 AIBrainComponent
- [ ] 集成 AbilitySystemComponent
- [ ] 处理战斗决策回调
- [ ] 处理对话响应回调
- [ ] 初始化默认技能

**代码位置**：`Source/DJ01/Demo/Public/DJ01DemoNPC.h`

---

### 4.5 Demo Player Controller

| 文件 | 状态 | 说明 |
|------|------|------|
| `DJ01DemoPlayerController.h` | ⬜ 待实现 | 控制器头文件 |
| `DJ01DemoPlayerController.cpp` | ⬜ 待实现 | 控制器实现 |

**验收标准**：
- [ ] 输入处理
- [ ] 对话 UI 交互
- [ ] 调试命令支持

**代码位置**：`Source/DJ01/Demo/Public/DJ01DemoPlayerController.h`

---

## 蓝图资产清单

| 资产 | 类型 | 依赖 | 状态 |
|------|------|------|------|
| `BP_DemoGameMode` | GameMode | DJ01DemoGameMode | ⬜ 待创建 |
| `BP_DemoNPC_Guard` | Character | DJ01DemoNPC | ⬜ 待创建 |
| `BP_DemoNPC_Challenger` | Character | DJ01DemoNPC | ⬜ 待创建 |
| `BP_DemoNPC_Dialogue` | Character | DJ01DemoNPC | ⬜ 待创建 |
| `BT_GuardAI` | BehaviorTree | BTTask_LLMDecision | ⬜ 待创建 |
| `BT_ChallengerAI` | BehaviorTree | BTTask_LLMDecision | ⬜ 待创建 |
| `WBP_DialoguePanel` | Widget | - | ⬜ 待创建 |
| `WBP_DebugHUD` | Widget | - | ⬜ 待创建 |
| `DemoArena` | Map | All above | ⬜ 待创建 |

---

## 配置文件清单

| 文件 | 说明 | 状态 |
|------|------|------|
| `Config/DefaultGame.ini` | LLM API 配置 | ⬜ 待配置 |

**需添加内容**：
```ini
[DJ01.LLM]
Endpoint=https://api.openai.com/v1/chat/completions
APIKey=sk-your-api-key
Model=gpt-4
Temperature=0.7
MaxTokens=256
TimeoutSeconds=10.0

[DJ01.Network]
MaxPredictionLatency=200.0
MaxConcurrentPredictions=10
```

---

## 模块依赖配置

在 `DJ01.Build.cs` 中添加依赖：

```csharp
PublicDependencyModuleNames.AddRange(new string[] 
{ 
    "Core", 
    "CoreUObject", 
    "Engine", 
    "InputCore",
    "GameplayAbilities",
    "GameplayTags",
    "GameplayTasks",
    "AIModule",
    "NavigationSystem",
    "HTTP",
    "Json",
    "JsonUtilities"
});
```

---

## 实现优先级

### 第一周：网络基础 (Phase 1)
1. ⬜ DJ01DistributedTypes.h
2. ⬜ DJ01MasterServer.h/.cpp
3. ⬜ DJ01MessageBroker.h/.cpp
4. ⬜ DJ01NetworkManager.h/.cpp
5. ⬜ 单元测试

### 第二周：战斗同步 (Phase 2)
1. ⬜ DJ01PredictionTypes.h
2. ⬜ DJ01AbilitySystemComponent.h/.cpp
3. ⬜ DJ01DamageExecution.h/.cpp
4. ⬜ DJ01GameplayAbility_Melee.h/.cpp
5. ⬜ DJ01GameplayAbility_Ranged.h/.cpp
6. ⬜ 多客户端测试

### 第三周：AI 集成 (Phase 3)
1. ⬜ DJ01AITypes.h
2. ⬜ DJ01LLMSubsystem.h/.cpp
3. ⬜ DJ01AIBrainComponent.h/.cpp
4. ⬜ DJ01BTTask_LLMDecision.h/.cpp
5. ⬜ DJ01BTTask_LLMDialogue.h/.cpp
6. ⬜ API 集成测试

### 第四周：演示集成 (Phase 4)
1. ⬜ DJ01DemoGameMode.h/.cpp
2. ⬜ DJ01DemoHUD.h/.cpp
3. ⬜ DJ01ArenaManager.h/.cpp
4. ⬜ DJ01DemoNPC.h/.cpp
5. ⬜ 蓝图资产创建
6. ⬜ 演示地图搭建
7. ⬜ 完整流程测试

---

## 验收总清单

### 功能验收
- [ ] 两个客户端能稳定连接并进行对战
- [ ] 技能释放有明显的预测效果（无需等待服务端）
- [ ] 服务端能正确验证并驳回非法预测
- [ ] AI NPC 能根据战斗态势做出合理决策
- [ ] AI NPC 能进行有上下文的角色扮演对话
- [ ] 调试 HUD 能清晰展示网络和 AI 状态

### 性能验收
- [ ] 60fps 基准下帧率波动 < 5fps
- [ ] 网络延迟 < 100ms 时无明显卡顿
- [ ] LLM 响应时间 < 3秒
- [ ] 10分钟连续运行无内存泄漏

### 代码质量验收
- [ ] 所有公共 API 有注释
- [ ] 关键函数有日志输出
- [ ] 无编译警告（W4 级别）
- [ ] 核心模块单元测试覆盖率 > 70%

---

## 快速开始命令

```bash
# 1. 生成项目文件
cd D:\UnrealProjects\DJ01
"C:\Program Files\Epic Games\UE_5.x\Engine\Build\BatchFiles\GenerateProjectFiles.bat" DJ01.uproject

# 2. 编译项目
"C:\Program Files\Epic Games\UE_5.x\Engine\Build\BatchFiles\Build.bat" DJ01 Win64 Development

# 3. 运行编辑器
"C:\Program Files\Epic Games\UE_5.x\Engine\Binaries\Win64\UnrealEditor.exe" D:\UnrealProjects\DJ01\DJ01.uproject

# 4. 启动多客户端测试
# 在编辑器中：Play → Net Mode: Play As Listen Server → Number of Players: 2
```

---

**文档生成完毕！开始按顺序实现各个模块。** 🚀