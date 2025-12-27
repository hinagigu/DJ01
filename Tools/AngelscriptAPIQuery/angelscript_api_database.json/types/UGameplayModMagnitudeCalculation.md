# UGameplayModMagnitudeCalculation

**继承自**: `UGameplayEffectCalculation`

Class used to perform custom gameplay effect modifier calculations, either via blueprint or native code

## 属性

### bAllowNonNetAuthorityDependencyRegistration
- **类型**: `bool`
- **描述**: Whether the calculation allows non-net authorities to register the external dependency multi-cast delegate or not; Effectively
whether clients are allowed to perform the custom calculation themselves or not

@Note:       This is an advanced use case that should only be enabled under very specific circumstances. This is designed for games
                     that are utilizing network dormancy and may want to trust the client to update non-gameplay critical attributes client-side without
                     causing a network dormancy flush. Usage of this flag is *NOT* compatible with attribute capture within the calculation and will trigger
                     an ensure if used in tandem. Clients are incapable of performing custom calculations that require attribute captures. In general,
                     if your game is not using network dormancy, this should always remain disabled.

@Note:       If enabling this for a custom calculation, be sure that the external delegate is sourced from something guaranteed to be on the client to avoid
                     timing issues. As an example, binding to a delegate on a GameState is potentially unreliable, as the client reference to that actor may not be
                     available during registration.

## 方法

### CalculateBaseMagnitude
```angelscript
float32 CalculateBaseMagnitude(FGameplayEffectSpec Spec)
```
Calculate the base magnitude of the gameplay effect modifier, given the specified spec. Note that the owning spec def can still modify this base value
with a coeffecient and pre/post multiply adds. see FCustomCalculationBasedFloat::CalculateMagnitude for details.

@param Spec  Gameplay effect spec to use to calculate the magnitude with

@return Computed magnitude of the modifier

### GetSetByCallerMagnitudeByName
```angelscript
float32 GetSetByCallerMagnitudeByName(FGameplayEffectSpec EffectSpec, FName MagnitudeName)
```
Extracts the Set by Caller Magnitude from a Gameplay Effect Spec

@param EffectSpec The Gameplay Effect Spec to get the info from
@param MagnitudeName The effect name to query

@return The magnitude value if found, zero otherwise

### GetSetByCallerMagnitudeByTag
```angelscript
float32 GetSetByCallerMagnitudeByTag(FGameplayEffectSpec EffectSpec, FGameplayTag Tag)
```
Extracts the Set by Caller Magnitude from a Gameplay Effect Spec

@param EffectSpec The Gameplay Effect Spec to get the info from
@param Tag The effect tag to query

@return The magnitude value if found, zero otherwise

### GetSourceActorTags
```angelscript
FGameplayTagContainer GetSourceActorTags(FGameplayEffectSpec EffectSpec)
```
Returns the source actor tags from a Gameplay Effect Spec

@param EffectSpec The Gameplay Effect Spec to get the info from

@return Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

### GetSourceAggregatedTags
```angelscript
FGameplayTagContainer GetSourceAggregatedTags(FGameplayEffectSpec EffectSpec)
```
Copies and returns the source aggregated tags from a Gameplay Effect Spec

@param EffectSpec The Gameplay Effect Spec to get the info from

@return Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

### GetSourceSpecTags
```angelscript
FGameplayTagContainer GetSourceSpecTags(FGameplayEffectSpec EffectSpec)
```
Returns the source spec tags from a Gameplay Effect Spec

@param EffectSpec The Gameplay Effect Spec to get the info from

@return Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

### GetTargetActorTags
```angelscript
FGameplayTagContainer GetTargetActorTags(FGameplayEffectSpec EffectSpec)
```
Returns the target actor tags from a Gameplay Effect Spec
Useful for Modifier Magnitude Calculations

@param EffectSpec The Gameplay Effect Spec to get the info from

@return Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

### GetTargetAggregatedTags
```angelscript
FGameplayTagContainer GetTargetAggregatedTags(FGameplayEffectSpec EffectSpec)
```
Copies and returns the target aggregated tags from a Gameplay Effect Spec

@param EffectSpec The Gameplay Effect Spec to get the info from

@return Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

### GetTargetSpecTags
```angelscript
FGameplayTagContainer GetTargetSpecTags(FGameplayEffectSpec EffectSpec)
```
Returns the target spec tags from a Gameplay Effect Spec
Useful for Modifier Magnitude Calculations

@param EffectSpec The Gameplay Effect Spec to get the info from

@return Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

### GetCapturedAttributeMagnitude
```angelscript
float32 GetCapturedAttributeMagnitude(FGameplayEffectSpec EffectSpec, FGameplayAttribute Attribute, FGameplayTagContainer SourceTags, FGameplayTagContainer TargetTags)
```
Gets the captured magnitude value for the given Attribute
For this to work correctly, the Attribute needs to be added to the Relevant Attributes to Capture array

@param EffectSpec The Gameplay Effect Spec to get the info from
@param Attribute The attribute to query

@return The magnitude value if found, zero otherwise

