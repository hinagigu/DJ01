# __CachedAnimData

## 方法

### StateMachine_GetGlobalWeight
```angelscript
float32 StateMachine_GetGlobalWeight(UAnimInstance InAnimInstance, FCachedAnimStateData CachedAnimStateData)
```
Returns the weight of a state, relative to the graph (specified in the provided FCachedAnimStateData)

### StateMachine_GetLocalWeight
```angelscript
float32 StateMachine_GetLocalWeight(UAnimInstance InAnimInstance, FCachedAnimStateData CachedAnimStateData)
```
Returns the weight of a state, relative to its state machine (specified in the provided FCachedAnimStateData)

### StateMachine_IsStateRelevant
```angelscript
bool StateMachine_IsStateRelevant(UAnimInstance InAnimInstance, FCachedAnimStateData CachedAnimStateData)
```
Returns whether a state is relevant (specified in the provided FCachedAnimStateData)

