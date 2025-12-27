# UBTTask_BlueprintBase

**继承自**: `UBTTaskNode`

Base class for blueprint based task nodes. Do NOT use it for creating native c++ classes!

When task receives Abort event, all latent actions associated this instance are being removed.
This prevents from resuming activity started by Execute, but does not handle external events.
Please use them safely (unregister at abort) and call IsTaskExecuting() when in doubt.

## 属性

### TickInterval
- **类型**: `FIntervalCountdown`
- **描述**: If any of the Tick functions is implemented, how often should they be ticked.
    Values < 0 mean 'every tick'.

### CustomDescription
- **类型**: `FString`

### bShowPropertyDetails
- **类型**: `bool`

## 方法

### FinishAbort
```angelscript
void FinishAbort()
```
aborts task execution

### FinishExecute
```angelscript
void FinishExecute(bool bSuccess)
```
finishes task execution with Success or Fail result

### IsTaskAborting
```angelscript
bool IsTaskAborting()
```
check if task is currently being aborted

### IsTaskExecuting
```angelscript
bool IsTaskExecuting()
```
check if task is currently being executed

### Abort
```angelscript
void Abort(AActor OwnerActor)
```
if blueprint graph contains this event, task will stay active until FinishAbort is called
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### AbortAI
```angelscript
void AbortAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveAbort
    @see ReceiveAbort for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### Execute
```angelscript
void Execute(AActor OwnerActor)
```
entry point, task will stay active until FinishExecute is called.
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ExecuteAI
```angelscript
void ExecuteAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveExecute
     @see ReceiveExecute for more details
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
Alternative AI version of tick function.
    @see ReceiveTick for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### SetFinishOnMessage
```angelscript
void SetFinishOnMessage(FName MessageName)
```
task execution will be finished (with result 'Success') after receiving specified message

### SetFinishOnMessageWithId
```angelscript
void SetFinishOnMessageWithId(FName MessageName, int RequestID)
```
task execution will be finished (with result 'Success') after receiving specified message with indicated ID

