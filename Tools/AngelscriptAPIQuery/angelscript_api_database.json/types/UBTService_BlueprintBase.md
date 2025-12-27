# UBTService_BlueprintBase

**继承自**: `UBTService`

Base class for blueprint based service nodes. Do NOT use it for creating native c++ classes!

When service receives Deactivation event, all latent actions associated this instance are being removed.
This prevents from resuming activity started by Activation, but does not handle external events.
Please use them safely (unregister at abort) and call IsServiceActive() when in doubt.

## 属性

### CustomDescription
- **类型**: `FString`

### bShowPropertyDetails
- **类型**: `bool`

### bShowEventDetails
- **类型**: `bool`

## 方法

### IsServiceActive
```angelscript
bool IsServiceActive()
```
check if service is currently being active

### Activation
```angelscript
void Activation(AActor OwnerActor)
```
service became active
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### ActivationAI
```angelscript
void ActivationAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveActivation function.
    @see ReceiveActivation for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### Deactivation
```angelscript
void Deactivation(AActor OwnerActor)
```
service became inactive
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### DeactivationAI
```angelscript
void DeactivationAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveDeactivation function.
    @see ReceiveDeactivation for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### SearchStart
```angelscript
void SearchStart(AActor OwnerActor)
```
task search enters branch of tree
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

### SearchStartAI
```angelscript
void SearchStartAI(AAIController OwnerController, APawn ControlledPawn)
```
Alternative AI version of ReceiveSearchStart function.
    @see ReceiveSearchStart for more details
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
Alternative AI version of ReceiveTick function.
    @see ReceiveTick for more details
    @Note that if both generic and AI event versions are implemented only the more
    suitable one will be called, meaning the AI version if called for AI, generic one otherwise

