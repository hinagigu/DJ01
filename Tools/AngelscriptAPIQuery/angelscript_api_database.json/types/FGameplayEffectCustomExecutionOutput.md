# FGameplayEffectCustomExecutionOutput

Struct representing the output of a custom gameplay effect execution.

## 方法

### AddOutputModifier
```angelscript
void AddOutputModifier(FGameplayModifierEvaluatedData InOutputMod)
```
Add the specified evaluated data to the execution's output modifiers

### AreGameplayCuesHandledManually
```angelscript
bool AreGameplayCuesHandledManually()
```
Accessor for determining if GameplayCue events have already been handled

### GetOutputModifiers
```angelscript
TArray<FGameplayModifierEvaluatedData> GetOutputModifiers()
```
Simple accessor to output modifiers of the execution

### GetOutputModifiersRef
```angelscript
TArray<FGameplayModifierEvaluatedData>& GetOutputModifiersRef()
```
Returns direct access to output modifiers of the execution (avoid copy)

### IsStackCountHandledManually
```angelscript
bool IsStackCountHandledManually()
```
Simple accessor for determining whether the execution has manually handled the stack count or not

### MarkConditionalGameplayEffectsToTrigger
```angelscript
void MarkConditionalGameplayEffectsToTrigger()
```
Mark that the execution wants conditional gameplay effects to trigger

### MarkGameplayCuesHandledManually
```angelscript
void MarkGameplayCuesHandledManually()
```
Mark that the execution wants conditional gameplay effects to trigger

### MarkStackCountHandledManually
```angelscript
void MarkStackCountHandledManually()
```
Mark that the execution has manually handled the stack count and the GE system should not attempt to automatically act upon it for emitted modifiers

### ShouldTriggerConditionalGameplayEffects
```angelscript
bool ShouldTriggerConditionalGameplayEffects()
```
Simple accessor for determining whether the execution wants conditional gameplay effects to trigger or not

### opAssign
```angelscript
FGameplayEffectCustomExecutionOutput& opAssign(FGameplayEffectCustomExecutionOutput Other)
```

