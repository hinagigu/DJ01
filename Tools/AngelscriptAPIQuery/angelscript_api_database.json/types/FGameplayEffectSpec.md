# FGameplayEffectSpec

GameplayEffect Specification. Tells us:
    -What UGameplayEffect (const data)
    -What Level
 -Who instigated

FGameplayEffectSpec is modifiable. We start with initial conditions and modifications be applied to it. In this sense, it is stateful/mutable but it
is still distinct from an FActiveGameplayEffect which in an applied instance of an FGameplayEffectSpec.

## 属性

### Def
- **类型**: `const UGameplayEffect`

### SetByCallerNameMagnitudes
- **类型**: `TMap<FName,float32>`

### SetByCallerTagMagnitudes
- **类型**: `TMap<FGameplayTag,float32>`

## 方法

### AddDynamicAssetTag
```angelscript
void AddDynamicAssetTag(FGameplayTag TagToAdd)
```

### AppendDynamicAssetTags
```angelscript
void AppendDynamicAssetTags(FGameplayTagContainer ContainerToAdd)
```

### ApplyExecutorModifiersForDefinition
```angelscript
void ApplyExecutorModifiersForDefinition(UClass CalculationClass, FGameplayEffectAttributeCaptureDefinition InCaptureDef, float32& ValueToModify)
```

### CalculateModifiedDuration
```angelscript
float32 CalculateModifiedDuration()
```
Helper function that returns the duration after applying relevant modifiers from the source and target ability system components

### CalculateModifierMagnitudes
```angelscript
void CalculateModifierMagnitudes()
```
Fills out the modifier magnitudes inside the Modifier Specs

### CaptureAttributeDataFromTarget
```angelscript
void CaptureAttributeDataFromTarget(UAbilitySystemComponent TargetAbilitySystemComponent)
```

### GetAllAssetTags
```angelscript
FGameplayTagContainer GetAllAssetTags()
```

### GetAllGrantedTags
```angelscript
FGameplayTagContainer GetAllGrantedTags()
```

### GetCapturedSourceTags
```angelscript
FAngelscriptTagContainerAggregator GetCapturedSourceTags()
```

### GetCapturedTargetTags
```angelscript
FAngelscriptTagContainerAggregator GetCapturedTargetTags()
```

### GetChanceToApplyToTarget
```angelscript
float32 GetChanceToApplyToTarget()
```

### GetCompletedSourceAttributeCapture
```angelscript
int GetCompletedSourceAttributeCapture()
```

### GetCompletedTargetAttributeCapture
```angelscript
int GetCompletedTargetAttributeCapture()
```

### GetContext
```angelscript
FGameplayEffectContextHandle GetContext()
```

### GetDuration
```angelscript
float32 GetDuration()
```

### GetDurationLocked
```angelscript
int GetDurationLocked()
```

### GetDynamicAssetTags
```angelscript
FGameplayTagContainer GetDynamicAssetTags()
```

### GetDynamicGrantedTags
```angelscript
FGameplayTagContainer GetDynamicGrantedTags()
```

### GetGrantedAbilitySpecs
```angelscript
TArray<FGameplayAbilitySpecDef> GetGrantedAbilitySpecs()
```

### GetLevel
```angelscript
float32 GetLevel()
```

### GetModifiedAttributeMagnitude
```angelscript
float32 GetModifiedAttributeMagnitude(FGameplayAttribute Attribute)
```

### GetModifierMagnitude
```angelscript
float32 GetModifierMagnitude(int ModifierIdx, bool bFactorInStackCount)
```

### GetPeriod
```angelscript
float32 GetPeriod()
```

### GetSetByCallerMagnitude
```angelscript
float32 GetSetByCallerMagnitude(FGameplayTag DataTag, bool bWarnIfNotFound, float32 DefaultIfNotFound)
```

### GetStackCount
```angelscript
int GetStackCount()
```

### PrintAll
```angelscript
void PrintAll()
```

### RecaptureAttributeDataForClone
```angelscript
void RecaptureAttributeDataForClone(UAbilitySystemComponent OriginalASC, UAbilitySystemComponent NewASC)
```
Recapture attributes from source and target for cloning

### RecaptureSourceActorTags
```angelscript
void RecaptureSourceActorTags()
```
Recaptures source actor tags of this spec without modifying anything else

### SetByCallerMagnitude
```angelscript
void SetByCallerMagnitude(FGameplayTag DataTag, float32 Magnitude)
```

### SetContext
```angelscript
void SetContext(FGameplayEffectContextHandle NewEffectContextHandle)
```

### SetLevel
```angelscript
void SetLevel(float32 InLevel)
```

### SetupAttributeCaptureDefinitions
```angelscript
void SetupAttributeCaptureDefinitions()
```
Helper function to initialize all of the capture definitions required by the spec

### ToSimpleString
```angelscript
FString ToSimpleString()
```

### opAssign
```angelscript
FGameplayEffectSpec& opAssign(FGameplayEffectSpec Other)
```

