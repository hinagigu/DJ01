# UBTDecorator_BlueprintBase

**继承自**: `UBTDecorator`

Base class for blueprint based decorator nodes. Do NOT use it for creating native c++ classes!

Unlike task and services, decorator have two execution chains:
 ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
which makes automatic latent action cleanup impossible. Keep in mind, that
you HAVE TO verify is given chain is still active after resuming from any
latent action (like Delay, Timelines, etc).

Helper functions:
- IsDecoratorExecutionActive (true after ExecutionStart, until ExecutionFinish)
- IsDecoratorObserverActive (true after ObserverActivated, until ObserverDeactivated)

## 属性

### CustomDescription
- **类型**: `FString`

### bShowPropertyDetails
- **类型**: `bool`

### bCheckConditionOnlyBlackBoardChanges
- **类型**: `bool`

## 方法

### IsDecoratorExecutionActive
```angelscript
bool IsDecoratorExecutionActive()
```
check if decorator is part of currently active branch

### IsDecoratorObserverActive
```angelscript
bool IsDecoratorObserverActive()
```
check if decorator's observer is currently active

### PerformConditionCheck
```angelscript
bool PerformConditionCheck(AActor OwnerActor)
```
called when testing if underlying node can be executed, must call FinishConditionCheck
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### PerformConditionCheckAI
```angelscript
bool PerformConditionCheckAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveConditionCheck
    @see ReceiveConditionCheck for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ExecutionFinish
```angelscript
void ExecutionFinish(AActor OwnerActor, EBTNodeResult NodeResult)
```
called when execution of underlying node is finished
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ExecutionFinishAI
```angelscript
void ExecutionFinishAI(AAIController OwnerController, APawn ControlledPawn, EBTNodeResult NodeResult)
```
Alternative AI version of ReceiveExecutionFinish
    @see ReceiveExecutionFinish for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ExecutionStart
```angelscript
void ExecutionStart(AActor OwnerActor)
```
called on execution of underlying node
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ExecutionStartAI
```angelscript
void ExecutionStartAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveExecutionStart
    @see ReceiveExecutionStart for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ObserverActivated
```angelscript
void ObserverActivated(AActor OwnerActor)
```
called when observer is activated (flow controller)
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ObserverActivatedAI
```angelscript
void ObserverActivatedAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveObserverActivated
    @see ReceiveObserverActivated for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ObserverDeactivated
```angelscript
void ObserverDeactivated(AActor OwnerActor)
```
called when observer is deactivated (flow controller)
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ObserverDeactivatedAI
```angelscript
void ObserverDeactivatedAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveObserverDeactivated
    @see ReceiveObserverDeactivated for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### Tick
```angelscript
void Tick(AActor OwnerActor, float DeltaSeconds)
```
tick function
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### TickAI
```angelscript
void TickAI(AAIController OwnerController, APawn ControlledPawn, float DeltaSeconds)
```
Alternative AI version of ReceiveTick
    @see ReceiveTick for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

