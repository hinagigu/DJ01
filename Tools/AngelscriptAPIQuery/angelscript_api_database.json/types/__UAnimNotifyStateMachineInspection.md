# __UAnimNotifyStateMachineInspection

## 方法

### IsTriggeredByState
```angelscript
bool IsTriggeredByState(FAnimNotifyEventReference EventReference, UAnimInstance AnimInstance, FName StateName)
```
Get whether a state with the given name in any state machine triggered the notify

@param EventReference         The event to inspect
@param MeshComp                       The skeletal mesh that contains the animation instance that produced the event
@param StateName                      The name of a state to test

### IsTriggeredByStateInStateMachine
```angelscript
bool IsTriggeredByStateInStateMachine(FAnimNotifyEventReference EventReference, UAnimInstance AnimInstance, FName StateMachineName, FName StateName)
```
Get whether a particular state in a specific state machine triggered the notify

@param EventReference         The event to inspect
@param MeshComp                       The skeletal mesh that contains the animation instance that produced the event
@param StateMachineName       The name of a state machine to test
@param StateName                      The name of a state to test

### IsTriggeredByStateMachine
```angelscript
bool IsTriggeredByStateMachine(FAnimNotifyEventReference EventReference, UAnimInstance AnimInstance, FName StateMachineName)
```
Get whether the notify was triggered from the specified state machine

@param EventReference            The event to inspect
@param MeshComp                  The skeletal mesh that contains the animation instance that produced the event
@param StateMachineName  The Name of a state machine to test

