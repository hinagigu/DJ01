# FGameplayEffectCustomExecutionParameters

Struct representing parameters for a custom gameplay effect execution. Should not be held onto via reference, used just for the scope of the execution

## 方法

### AttemptCalculateCapturedAttributeBaseValue
```angelscript
bool AttemptCalculateCapturedAttributeBaseValue(FGameplayEffectAttributeCaptureDefinition InCaptureDef, float32& OutBaseValue)
```
Attempts to calculate the base value of a captured attribute given the specified parameters. Can fail if the gameplay spec doesn't have
a valid capture for the attribute.

@param InCaptureDef  Attribute definition to attempt to calculate the base value of
@param OutBaseValue  [OUT] Computed base value

@return True if the base value was successfully calculated, false if it was not

### AttemptCalculateCapturedAttributeBonusMagnitude
```angelscript
bool AttemptCalculateCapturedAttributeBonusMagnitude(FGameplayEffectAttributeCaptureDefinition InCaptureDef, FGameplayEffectExecutionParameters InParams, float32& OutBonusMagnitude)
```
Attempts to calculate the bonus magnitude of a captured attribute given the specified parameters. Can fail if the gameplay spec doesn't have
a valid capture for the attribute.

@param InCaptureDef          Attribute definition to attempt to calculate the bonus magnitude of
@param InEvalParams          Parameters to evaluate the attribute under
@param OutBonusMagnitude     [OUT] Computed bonus magnitude

@return True if the bonus magnitude was successfully calculated, false if it was not

### AttemptCalculateCapturedAttributeMagnitude
```angelscript
bool AttemptCalculateCapturedAttributeMagnitude(FGameplayEffectAttributeCaptureDefinition InCaptureDef, FGameplayEffectExecutionParameters InParams, float32& OutMagnitude)
```
Attempts to calculate the magnitude of a captured attribute given the specified parameters. Can fail if the gameplay spec doesn't have
a valid capture for the attribute.

@param InCaptureDef  Attribute definition to attempt to calculate the magnitude of
@param InEvalParams  Parameters to evaluate the attribute under
@param OutMagnitude  [OUT] Computed magnitude

@return True if the magnitude was successfully calculated, false if it was not

### AttemptCalculateCapturedAttributeMagnitudeWithBase
```angelscript
bool AttemptCalculateCapturedAttributeMagnitudeWithBase(FGameplayEffectAttributeCaptureDefinition InCaptureDef, FGameplayEffectExecutionParameters InParams, float32 InBaseValue, float32& OutMagnitude)
```
Attempts to calculate the magnitude of a captured attribute given the specified parameters, including a starting base value.
Can fail if the gameplay spec doesn't have a valid capture for the attribute.

@param InCaptureDef  Attribute definition to attempt to calculate the magnitude of
@param InEvalParams  Parameters to evaluate the attribute under
@param InBaseValue   Base value to evaluate the attribute under
@param OutMagnitude  [OUT] Computed magnitude

@return True if the magnitude was successfully calculated, false if it was not

### AttemptCalculateTransientAggregatorMagnitude
```angelscript
void AttemptCalculateTransientAggregatorMagnitude(FGameplayTag InAggregatorIdentifier, FGameplayEffectExecutionParameters InParams, float32& OutMagnitude)
```
Attempts to calculate the magnitude of a transient aggregator given the specified parameters.

@param InAggregatorIdentifier Tag identifying the transient aggregator to attempt to calculate the magnitude of
@param InParams                               Parameters to evaluate the aggregator under
@param OutMagnitude                   [OUT] Computed magnitude

### GetIgnoreHandles
```angelscript
TArray<FActiveGameplayEffectHandle> GetIgnoreHandles()
```

### GetOwningSpec
```angelscript
FGameplayEffectSpec GetOwningSpec()
```
Simple accessor to owning gameplay spec

### GetOwningSpecForPreExecuteMod
```angelscript
FGameplayEffectSpec& GetOwningSpecForPreExecuteMod()
```
Non const access. Be careful with this, especially when modifying a spec after attribute capture.

### GetPassedInTags
```angelscript
FGameplayTagContainer GetPassedInTags()
```
Simple accessor to the Passed In Tags to this execution

### GetSourceAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetSourceAbilitySystemComponent()
```
Simple accessor to source ability system component (could be null!)

### GetTargetAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetTargetAbilitySystemComponent()
```
Simple accessor to target ability system component

### opAssign
```angelscript
FGameplayEffectCustomExecutionParameters& opAssign(FGameplayEffectCustomExecutionParameters Other)
```

