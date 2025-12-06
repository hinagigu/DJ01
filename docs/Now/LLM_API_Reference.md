# DJ01 项目 API 快速参考

> **用途**: 本文档专为 LLM 交互设计，提供最小化的 API 表面信息。
> **项目类型**: UE5 RPG 游戏 | **架构基础**: Lyra Starter Game

---

## 1. 核心模块概览

| 模块 | 职责 | 入口类 |
|------|------|--------|
| AbilitySystem | GAS技能系统 | `UDJ01AbilitySystemComponent` |
| Character | 角色与Pawn | `ADJ01Character`, `UDJ01PawnExtensionComponent` |
| Experience | 游戏模式加载 | `UDJ01ExperienceDefinition`, `UDJ01ExperienceManagerComponent` |
| Input | 增强输入系统 | `UDJ01InputConfig`, `UDJ01InputComponent` |
| Camera | 模块化相机 | `UDJ01CameraComponent`, `UDJ01CameraMode` |
| Player | 玩家控制器/状态 | `ADJ01PlayerController`, `ADJ01PlayerState` |
| Team | 阵营关系 | `UDJ01TeamSubsystem`, `IDJ01TeamAgentInterface` |
| GameFeatureActions | 模块化功能注入 | `UGameFeatureAction_AddAbilities` |

---

## 2. AbilitySystem 模块

### 2.1 核心类

```cpp
// ASC - 技能系统组件
class UDJ01AbilitySystemComponent : public UAbilitySystemComponent
  void AbilityInputTagPressed(FGameplayTag InputTag)   // 输入按下
  void AbilityInputTagReleased(FGameplayTag InputTag)  // 输入释放
  void ProcessAbilityInput(float DeltaTime, bool bGamePaused) // 每帧处理
  void CancelAbilitiesWithActivationGroup(EDJ01AbilityActivationGroup) // 取消激活组

// 技能基类
class UDJ01GameplayAbility : public UGameplayAbility
  EDJ01AbilityActivationPolicy ActivationPolicy  // OnInputTriggered|WhileInputActive|OnSpawn
  EDJ01AbilityActivationGroup ActivationGroup    // Independent|Exclusive_Replaceable|Exclusive_Blocking
  TArray<UDJ01AbilityCost*> AdditionalCosts      // 额外消耗

// 技能集 (DataAsset)
class UDJ01AbilitySet : public UPrimaryDataAsset
  void GiveToAbilitySystem(ASC*, OutHandles*, SourceObject)  // 批量授予技能
```

### 2.2 属性集

```cpp
// 生存属性
class UDJ01HealthSet : public UDJ01AttributeSetBase
  FGameplayAttributeData Health, MaxHealth  // 生命值
  FGameplayAttributeData Mana, MaxMana      // 魔法值
  FGameplayAttributeData Stamina, MaxStamina // 体力值
  FGameplayAttributeData Healing            // 治疗量(Meta)

// 战斗属性
class UDJ01CombatSet : public UDJ01AttributeSetBase
  FGameplayAttributeData AttackPower, Defense       // 攻防
  FGameplayAttributeData CriticalRate, CriticalDamage // 暴击
  FGameplayAttributeData FireAffinity/Resistance    // 火系
  FGameplayAttributeData IceAffinity/Resistance     // 冰系
  FGameplayAttributeData LightningAffinity/Resistance // 雷系
  FGameplayAttributeData BaseDamage, IncomingDamage // 伤害(Meta)
```

### 2.3 激活策略枚举

```cpp
enum class EDJ01AbilityActivationPolicy : uint8
  OnInputTriggered  // 按键触发
  WhileInputActive  // 持续按住
  OnSpawn           // 自动激活

enum class EDJ01AbilityActivationGroup : uint8
  Independent          // 独立运行
  Exclusive_Replaceable // 可被替换
  Exclusive_Blocking    // 阻塞其他
```

---

## 3. Character 模块

### 3.1 核心类

```cpp
// 角色基类
class ADJ01Character : public AModularCharacter, IAbilitySystemInterface
  UDJ01PawnExtensionComponent* PawnExtComponent  // 生命周期管理
  UDJ01CameraComponent* CameraComponent          // 相机组件

// Pawn扩展组件 - 管理初始化状态机
class UDJ01PawnExtensionComponent : public UPawnComponent
  void SetPawnData(const UDJ01PawnData*)  // 设置Pawn数据
  void InitializeAbilitySystem(ASC*, AActor* OwnerActor)
  void HandleControllerChanged()          // Controller变更回调
  void CheckDefaultInitialization()       // 检查初始化状态
  // 状态: Spawned → DataAvailable → DataInitialized → GameplayReady

// 英雄组件 - 处理玩家输入 (通过GFD动态添加)
class UDJ01HeroComponent : public UPawnComponent
  void InitializePlayerInput(UInputComponent*)
  void Input_AbilityInputTagPressed(FGameplayTag)
  void Input_AbilityInputTagReleased(FGameplayTag)

// Pawn数据 (DataAsset)
class UDJ01PawnData : public UPrimaryDataAsset
  TSubclassOf<APawn> PawnClass
  TArray<UDJ01AbilitySet*> AbilitySets
  UDJ01InputConfig* InputConfig
  TSubclassOf<UDJ01CameraMode> DefaultCameraMode
```

---

## 4. Experience 模块

### 4.1 核心类

```cpp
// Experience定义 (DataAsset)
class UDJ01ExperienceDefinition : public UPrimaryDataAsset
  TArray<FString> GameFeaturesToEnable        // 要启用的GF插件
  UDJ01PawnData* DefaultPawnData              // 默认Pawn数据
  TArray<UGameFeatureAction*> Actions         // 激活时执行的Action
  TArray<UDJ01ExperienceActionSet*> ActionSets // Action集合

// Experience管理组件 (附加到GameState)
class UDJ01ExperienceManagerComponent : public UGameStateComponent
  void ServerSetCurrentExperience(FPrimaryAssetId)  // 设置Experience
  void CallOrRegister_OnExperienceLoaded(Delegate)  // 加载完成回调
  bool IsExperienceLoaded() const
  const UDJ01ExperienceDefinition* GetCurrentExperienceChecked()
  // 状态: Unloaded → Loading → LoadingGameFeatures → ExecutingActions → Loaded

// 蓝图异步节点
class UAsyncAction_ExperienceReady : public UCancellableAsyncAction
  static UAsyncAction_ExperienceReady* WaitForExperienceReady(WorldContext)
  FOnExperienceReady OnReady  // 完成委托
```

---

## 5. Input 模块

### 5.1 核心类

```cpp
// 输入配置 (DataAsset)
class UDJ01InputConfig : public UDataAsset
  TArray<FDJ01InputAction> NativeInputActions   // 原生输入(移动等)
  TArray<FDJ01InputAction> AbilityInputActions  // 技能输入

// 输入动作映射
struct FDJ01InputAction
  UInputAction* InputAction
  FGameplayTag InputTag

// 增强输入组件
class UDJ01InputComponent : public UEnhancedInputComponent
  void BindNativeAction(Config, Tag, TriggerEvent, Object, Func)
  void BindAbilityActions(Config, Object, PressedFunc, ReleasedFunc)
```

---

## 6. Camera 模块

### 6.1 核心类

```cpp
// 相机组件
class UDJ01CameraComponent : public UCameraComponent
  void PushCameraMode(TSubclassOf<UDJ01CameraMode>)
  TSubclassOf<UDJ01CameraMode> DetermineCameraModeDelegate

// 相机模式基类
class UDJ01CameraMode : public UObject
  FDJ01CameraModeView View  // 位置/旋转/FOV
  float BlendTime, BlendWeight
  virtual void UpdateView(float DeltaTime)

// 第三人称相机
class UDJ01CameraMode_ThirdPerson : public UDJ01CameraMode
  UCurveVector* TargetOffsetCurve
  bool bPreventPenetration
```

---

## 7. Team 模块

### 7.1 核心类

```cpp
// 队伍代理接口
class IDJ01TeamAgentInterface
  void SetGenericTeamId(FGenericTeamId)
  FGenericTeamId GetGenericTeamId() const
  FOnDJ01TeamIndexChanged OnTeamChanged  // 队伍变更委托

// 队伍子系统
class UDJ01TeamSubsystem : public UWorldSubsystem
  bool CanCauseDamage(AActor* Instigator, AActor* Target)
  EDJ01TeamComparison CompareTeams(A, B, OptionalTeamID)  // 比较关系
  EDJ01TeamComparison CompareTeams(TeamA, TeamB)

// 队伍关系
enum class EDJ01TeamComparison : uint8
  OnSameTeam      // 同队
  DifferentTeams  // 敌对
  InvalidArgument // 无效
```

---

## 8. GameFeatureActions

### 8.1 可用Actions

```cpp
// 添加技能
class UGameFeatureAction_AddAbilities : public UGameFeatureAction_WorldActionBase
  TArray<FGameFeatureAbilitiesEntry> AbilitiesList
  // Entry: ActorClass + AbilitySets + Attributes + InputConfigs

// 添加输入绑定
class UGameFeatureAction_AddInputBinding : public UGameFeatureAction_WorldActionBase
  TArray<TSoftObjectPtr<UDJ01InputConfig>> InputConfigs

// 添加输入上下文映射
class UGameFeatureAction_AddInputContextMapping : public UGameFeatureAction_WorldActionBase
  TArray<FInputMappingContextAndPriority> InputMappings

// 添加UI组件
class UGameFeatureAction_AddWidgets : public UGameFeatureAction_WorldActionBase
  TArray<FDJ01HUDElementEntry> Widgets
  TArray<FDJ01HUDLayoutRequest> Layout
```

---

## 9. 重要Gameplay Tags

```cpp
// 定义位置: Source/DJ01/System/Public/DJ01GameplayTags.h
struct FDJ01GameplayTags
  // 输入标签
  FGameplayTag InputTag_Move
  FGameplayTag InputTag_Look_Mouse
  FGameplayTag InputTag_Jump
  FGameplayTag InputTag_Crouch
  FGameplayTag InputTag_Sprint
  
  // 技能激活状态
  FGameplayTag Ability_ActivateFail_*
  
  // 游戏事件
  FGameplayTag GameplayEvent_*
```

---

## 10. 常用代码模式

### 10.1 获取ASC

```cpp
// 从Actor获取
UDJ01AbilitySystemComponent* ASC = Actor->FindComponentByClass<UDJ01AbilitySystemComponent>();
// 或通过接口
if (IAbilitySystemInterface* ASI = Cast<IAbilitySystemInterface>(Actor))
    UAbilitySystemComponent* ASC = ASI->GetAbilitySystemComponent();
```

### 10.2 等待Experience加载

```cpp
// C++
ExperienceComponent->CallOrRegister_OnExperienceLoaded(
    FOnDJ01ExperienceLoaded::FDelegate::CreateUObject(this, &ThisClass::OnExperienceLoaded));

// 蓝图: 使用 WaitForExperienceReady 异步节点
```

### 10.3 授予技能集

```cpp
FDJ01AbilitySet_GrantedHandles Handles;
AbilitySet->GiveToAbilitySystem(ASC, &Handles, SourceObject);
// 移除时
Handles.TakeFromAbilitySystem(ASC);
```

---

## 11. 文件路径速查

| 功能 | 路径 |
|------|------|
| ASC | `Source/DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h` |
| 技能基类 | `Source/DJ01/AbilitySystem/Abilities/Public/DJ01GameplayAbility.h` |
| 属性集 | `Source/DJ01/AbilitySystem/Attributes/DJ01HealthSet.h` |
| 角色 | `Source/DJ01/Character/Public/DJ01Character.h` |
| PawnData | `Source/DJ01/Character/Public/DJ01PawnData.h` |
| Experience | `Source/DJ01/Experience/Public/DJ01ExperienceDefinition.h` |
| 输入配置 | `Source/DJ01/Input/Public/DJ01InputConfig.h` |
| 相机模式 | `Source/DJ01/Camera/Public/DJ01CameraMode.h` |
| 队伍系统 | `Source/DJ01/Team/Public/DJ01TeamSubsystem.h` |
| Gameplay Tags | `Source/DJ01/System/Public/DJ01GameplayTags.h` |
| GF Actions | `Source/GameFeatureActions/` |

---

**文档版本**: v1.0 | **更新日期**: 2025