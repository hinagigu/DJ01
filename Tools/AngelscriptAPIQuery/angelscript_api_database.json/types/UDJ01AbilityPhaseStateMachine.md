# UDJ01AbilityPhaseStateMachine

**继承自**: `UObject`

技能阶段状态机

独立于技能类的状态机实现，负责管理技能的执行阶段。
技能类持有状态机实例，通过委托接收阶段变化通知。

使用方式：
1. 技能激活时调用 Initialize()
2. 状态机自动按配置推进阶段
3. 技能可以手动调用 TransitionToPhase() 控制阶段
4. 技能结束时调用 Shutdown()

## 属性

### OnPhaseChanged
- **类型**: `FOnAbilityPhaseChanged`

### OnPhaseEnter
- **类型**: `FOnAbilityPhaseEnter`

### OnPhaseExit
- **类型**: `FOnAbilityPhaseExit`

### OnFinished
- **类型**: `FOnPhaseStateMachineFinished`

### Config
- **类型**: `FDJ01AbilityPhaseConfig`
- **描述**: 阶段配置

## 方法

### CanCurrentPhaseBeInterrupted
```angelscript
bool CanCurrentPhaseBeInterrupted()
```
当前阶段是否可被打断

### CanCurrentPhaseCancelInto
```angelscript
bool CanCurrentPhaseCancelInto()
```
当前阶段是否可取消到其他技能

### GetCurrentPhase
```angelscript
EDJ01AbilityPhase GetCurrentPhase()
```
获取当前阶段

### GetCurrentPhaseRemainingTime
```angelscript
float32 GetCurrentPhaseRemainingTime()
```
获取当前阶段剩余时间

### GetPreviousPhase
```angelscript
EDJ01AbilityPhase GetPreviousPhase()
```
获取上一个阶段

### Initialize
```angelscript
void Initialize(UDJ01GameplayAbility InOwnerAbility, FDJ01AbilityPhaseConfig InConfig)
```
初始化状态机
@param InOwnerAbility - 拥有此状态机的技能
@param InConfig - 阶段配置

### IsRunning
```angelscript
bool IsRunning()
```
状态机是否正在运行

### Shutdown
```angelscript
void Shutdown()
```
关闭状态机（清理资源）

### SkipCurrentPhase
```angelscript
void SkipCurrentPhase()
```
跳过当前阶段（立即进入下一阶段）

### Start
```angelscript
void Start()
```
启动状态机（进入第一个阶段）

### TransitionToPhase
```angelscript
bool TransitionToPhase(EDJ01AbilityPhase NewPhase, bool bForce)
```
切换到指定阶段
@param NewPhase - 目标阶段
@param bForce - 是否强制转换（忽略验证）
@return 是否成功切换

