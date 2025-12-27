# __AbilitySystem

## 方法

### AbilityTargetDataFromActor
```angelscript
FGameplayAbilityTargetDataHandle AbilityTargetDataFromActor(AActor Actor)
```
Creates single actor target data

### AbilityTargetDataFromActorArray
```angelscript
FGameplayAbilityTargetDataHandle AbilityTargetDataFromActorArray(TArray<AActor> ActorArray, bool OneTargetPerHandle)
```
Creates actor array target data

### AbilityTargetDataFromHitResult
```angelscript
FGameplayAbilityTargetDataHandle AbilityTargetDataFromHitResult(FHitResult HitResult)
```
Creates a target data with a single hit result

### AbilityTargetDataFromLocations
```angelscript
FGameplayAbilityTargetDataHandle AbilityTargetDataFromLocations(FGameplayAbilityTargetingLocationInfo SourceLocation, FGameplayAbilityTargetingLocationInfo TargetLocation)
```
Creates a target data with a source and destination location

### AddAssetTag
```angelscript
FGameplayEffectSpecHandle AddAssetTag(FGameplayEffectSpecHandle SpecHandle, FGameplayTag NewGameplayTag)
```
Adds NewGameplayTag to this instance of the effect

### AddAssetTags
```angelscript
FGameplayEffectSpecHandle AddAssetTags(FGameplayEffectSpecHandle SpecHandle, FGameplayTagContainer NewGameplayTags)
```
Adds NewGameplayTags to this instance of the effect

### AddGrantedTag
```angelscript
FGameplayEffectSpecHandle AddGrantedTag(FGameplayEffectSpecHandle SpecHandle, FGameplayTag NewGameplayTag)
```
This instance of the effect will now grant NewGameplayTag to the object that this effect is applied to

### AddGrantedTags
```angelscript
FGameplayEffectSpecHandle AddGrantedTags(FGameplayEffectSpecHandle SpecHandle, FGameplayTagContainer NewGameplayTags)
```
This instance of the effect will now grant NewGameplayTags to the object that this effect is applied to

### AddLooseGameplayTags
```angelscript
bool AddLooseGameplayTags(AActor Actor, FGameplayTagContainer GameplayTags, bool bShouldReplicate)
```
Manually adds a set of tags to a given actor, and optionally replicates them.

### AppendTargetDataHandle
```angelscript
FGameplayAbilityTargetDataHandle AppendTargetDataHandle(FGameplayAbilityTargetDataHandle TargetHandle, FGameplayAbilityTargetDataHandle HandleToAdd)
```
Copies targets from HandleToAdd to TargetHandle

### AssignSetByCallerMagnitude
```angelscript
FGameplayEffectSpecHandle AssignSetByCallerMagnitude(FGameplayEffectSpecHandle SpecHandle, FName DataName, float32 Magnitude)
```
Sets a raw name Set By Caller magnitude value, the tag version should normally be used

### AssignTagSetByCallerMagnitude
```angelscript
FGameplayEffectSpecHandle AssignTagSetByCallerMagnitude(FGameplayEffectSpecHandle SpecHandle, FGameplayTag DataTag, float32 Magnitude)
```
Sets a gameplay tag Set By Caller magnitude value

### BreakGameplayCueParameters
```angelscript
void BreakGameplayCueParameters(FGameplayCueParameters Parameters, float32& NormalizedMagnitude, float32& RawMagnitude, FGameplayEffectContextHandle& EffectContext, FGameplayTag& MatchedTagName, FGameplayTag& OriginalTag, FGameplayTagContainer& AggregatedSourceTags, FGameplayTagContainer& AggregatedTargetTags, FVector& Location, FVector& Normal, AActor& Instigator, AActor& EffectCauser, UObject& SourceObject, UPhysicalMaterial& PhysicalMaterial, int& GameplayEffectLevel, int& AbilityLevel, USceneComponent& TargetAttachComponent, bool& bReplicateLocationWhenUsingMinimalRepProxy)
```
Native break, to avoid having to deal with quantized vector types

### CloneSpecHandle
```angelscript
FGameplayEffectSpecHandle CloneSpecHandle(AActor InNewInstigator, AActor InEffectCauser, FGameplayEffectSpecHandle GameplayEffectSpecHandle_Clone)
```
Create a spec handle, cloning another

### DoesGameplayCueMeetTagRequirements
```angelscript
bool DoesGameplayCueMeetTagRequirements(FGameplayCueParameters Parameters, FGameplayTagRequirements SourceTagReqs, FGameplayTagRequirements TargetTagReqs)
```
Returns true if the aggregated source and target tags from the effect spec meets the tag requirements

### DoesTargetDataContainActor
```angelscript
bool DoesTargetDataContainActor(FGameplayAbilityTargetDataHandle TargetData, int Index, AActor Actor)
```
Returns true if the given TargetData has the actor passed in targeted

### EffectContextAddHitResult
```angelscript
void EffectContextAddHitResult(FGameplayEffectContextHandle EffectContext, FHitResult HitResult, bool bReset)
```
Adds a hit result to the effect context

### EffectContextGetEffectCauser
```angelscript
AActor EffectContextGetEffectCauser(FGameplayEffectContextHandle EffectContext)
```
Gets the physical actor that caused the effect, possibly a projectile or weapon

### EffectContextGetHitResult
```angelscript
FHitResult EffectContextGetHitResult(FGameplayEffectContextHandle EffectContext)
```
Extracts a hit result from the effect context if it is set

### EffectContextGetInstigatorActor
```angelscript
AActor EffectContextGetInstigatorActor(FGameplayEffectContextHandle EffectContext)
```
Gets the instigating actor (that holds the ability system component) of the EffectContext

### EffectContextGetOrigin
```angelscript
FVector EffectContextGetOrigin(FGameplayEffectContextHandle EffectContext)
```
Gets the location the effect originated from

### EffectContextGetOriginalInstigatorActor
```angelscript
AActor EffectContextGetOriginalInstigatorActor(FGameplayEffectContextHandle EffectContext)
```
Gets the original instigator actor that started the chain of events to cause this effect

### EffectContextGetSourceObject
```angelscript
UObject EffectContextGetSourceObject(FGameplayEffectContextHandle EffectContext)
```
Gets the source object of the effect.

### EffectContextHasHitResult
```angelscript
bool EffectContextHasHitResult(FGameplayEffectContextHandle EffectContext)
```
Returns true if there is a valid hit result inside the effect context

### EffectContextIsInstigatorLocallyControlled
```angelscript
bool EffectContextIsInstigatorLocallyControlled(FGameplayEffectContextHandle EffectContext)
```
Returns true if the ability system component that instigated this is locally controlled

### EffectContextIsValid
```angelscript
bool EffectContextIsValid(FGameplayEffectContextHandle EffectContext)
```
Returns true if this context has ever been initialized

### EffectContextSetOrigin
```angelscript
void EffectContextSetOrigin(FGameplayEffectContextHandle EffectContext, FVector Origin)
```
Sets the location the effect originated from

### EqualEqual_ActiveGameplayEffectHandle
```angelscript
bool EqualEqual_ActiveGameplayEffectHandle(FActiveGameplayEffectHandle A, FActiveGameplayEffectHandle B)
```
Equality operator for two Active Gameplay Effect Handles

### EqualEqual_GameplayAbilitySpecHandle
```angelscript
bool EqualEqual_GameplayAbilitySpecHandle(FGameplayAbilitySpecHandle A, FGameplayAbilitySpecHandle B)
```
Equality operator for two Gameplay Ability Spec Handles

### EqualEqual_GameplayAttributeGameplayAttribute
```angelscript
bool EqualEqual_GameplayAttributeGameplayAttribute(FGameplayAttribute AttributeA, FGameplayAttribute AttributeB)
```
Simple equality operator for gameplay attributes

### EvaluateAttributeValueWithTags
```angelscript
float32 EvaluateAttributeValueWithTags(UAbilitySystemComponent AbilitySystem, FGameplayAttribute Attribute, FGameplayTagContainer SourceTags, FGameplayTagContainer TargetTags, bool& bSuccess)
```
Returns the value of Attribute from the ability system component AbilitySystem after evaluating it with source and target tags. bSuccess indicates the success or failure of this operation.

### EvaluateAttributeValueWithTagsAndBase
```angelscript
float32 EvaluateAttributeValueWithTagsAndBase(UAbilitySystemComponent AbilitySystem, FGameplayAttribute Attribute, FGameplayTagContainer SourceTags, FGameplayTagContainer TargetTags, float32 BaseValue, bool& bSuccess)
```
Returns the value of Attribute from the ability system component AbilitySystem after evaluating it with source and target tags using the passed in base value instead of the real base value. bSuccess indicates the success or failure of this operation.

### FilterTargetData
```angelscript
FGameplayAbilityTargetDataHandle FilterTargetData(FGameplayAbilityTargetDataHandle TargetDataHandle, FGameplayTargetDataFilterHandle ActorFilterClass)
```
Create a new target data handle with filtration performed on the data

### GetAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetAbilitySystemComponent(AActor Actor)
```
Tries to find an ability system component on the actor, will use AbilitySystemInterface or fall back to a component search

### GetActiveGameplayEffectDebugString
```angelscript
FString GetActiveGameplayEffectDebugString(FActiveGameplayEffectHandle ActiveHandle)
```
Returns a debug string for display

### GetActiveGameplayEffectExpectedEndTime
```angelscript
float32 GetActiveGameplayEffectExpectedEndTime(FActiveGameplayEffectHandle ActiveHandle)
```
Returns the expected end time (when we think the GE will expire) for a given GameplayEffect (note someone could remove or change it before that happens!)

### GetActiveGameplayEffectRemainingDuration
```angelscript
float32 GetActiveGameplayEffectRemainingDuration(FActiveGameplayEffectHandle ActiveHandle)
```
Returns the total duration for a given GameplayEffect, basically ExpectedEndTime - Current Time

### GetActiveGameplayEffectStackCount
```angelscript
int GetActiveGameplayEffectStackCount(FActiveGameplayEffectHandle ActiveHandle)
```
Returns current stack count of an active Gameplay Effect. Will return 0 if the GameplayEffect is no longer valid.

### GetActiveGameplayEffectStackLimitCount
```angelscript
int GetActiveGameplayEffectStackLimitCount(FActiveGameplayEffectHandle ActiveHandle)
```
Returns stack limit count of an active Gameplay Effect. Will return 0 if the GameplayEffect is no longer valid.

### GetActiveGameplayEffectStartTime
```angelscript
float32 GetActiveGameplayEffectStartTime(FActiveGameplayEffectHandle ActiveHandle)
```
Returns the start time (time which the GE was added) for a given GameplayEffect

### GetActiveGameplayEffectTotalDuration
```angelscript
float32 GetActiveGameplayEffectTotalDuration(FActiveGameplayEffectHandle ActiveHandle)
```
Returns the total duration for a given GameplayEffect

### GetActorByIndex
```angelscript
AActor GetActorByIndex(FGameplayCueParameters Parameters, int Index)
```
Returns actor stored in the Effect Context used by this cue

### GetActorCount
```angelscript
int GetActorCount(FGameplayCueParameters Parameters)
```
Returns number of actors stored in the Effect Context used by this cue

### GetActorsFromTargetData
```angelscript
TArray<AActor> GetActorsFromTargetData(FGameplayAbilityTargetDataHandle TargetData, int Index)
```
Returns all actors targeted, for a given index

### GetAllActorsFromTargetData
```angelscript
TArray<AActor> GetAllActorsFromTargetData(FGameplayAbilityTargetDataHandle TargetData)
```
Returns all actors targeted

### GetDataCountFromTargetData
```angelscript
int GetDataCountFromTargetData(FGameplayAbilityTargetDataHandle TargetData)
```
Returns number of target data objects, not necessarily number of distinct targets

### GetDebugStringFromGameplayAttribute
```angelscript
FString GetDebugStringFromGameplayAttribute(FGameplayAttribute Attribute)
```
Returns FString representation of a gameplay attribute's set class and name, in the form of AttrSetName.AttrName (or just AttrName if not part of a set).

### GetEffectContext
```angelscript
FGameplayEffectContextHandle GetEffectContext(FGameplayEffectSpecHandle SpecHandle)
```
Gets the GameplayEffectSpec's effect context handle

### GetFloatAttribute
```angelscript
float32 GetFloatAttribute(const AActor Actor, FGameplayAttribute Attribute, bool& bSuccessfullyFoundAttribute)
```
Returns the value of Attribute from the ability system component belonging to Actor.

### GetFloatAttributeBase
```angelscript
float32 GetFloatAttributeBase(const AActor Actor, FGameplayAttribute Attribute, bool& bSuccessfullyFoundAttribute)
```
Returns the base value of Attribute from the ability system component belonging to Actor.

### GetFloatAttributeBaseFromAbilitySystemComponent
```angelscript
float32 GetFloatAttributeBaseFromAbilitySystemComponent(const UAbilitySystemComponent AbilitySystemComponent, FGameplayAttribute Attribute, bool& bSuccessfullyFoundAttribute)
```
Returns the base value of Attribute from the ability system component AbilitySystemComponent.

### GetFloatAttributeFromAbilitySystemComponent
```angelscript
float32 GetFloatAttributeFromAbilitySystemComponent(const UAbilitySystemComponent AbilitySystem, FGameplayAttribute Attribute, bool& bSuccessfullyFoundAttribute)
```
Returns the value of Attribute from the ability system component AbilitySystem.

### GetGameplayAbilityFromSpecHandle
```angelscript
const UGameplayAbility GetGameplayAbilityFromSpecHandle(UAbilitySystemComponent AbilitySystem, FGameplayAbilitySpecHandle AbilitySpecHandle, bool& bIsInstance)
```
Provides the Gameplay Ability object associated with an Ability Spec Handle
This can be either an instanced ability, or in the case of shared abilities, the Class Default Object

@param AbilitySpec The Gameplay Ability Spec you want to get the object from
@param bIsInstance Set to true if this is an instanced ability instead of a shared CDO

@return Pointer to the Gameplay Ability object

### GetGameplayCueDirection
```angelscript
bool GetGameplayCueDirection(AActor TargetActor, FGameplayCueParameters Parameters, FVector& Direction)
```
Gets the best normalized effect direction for this gameplay cue. This is useful for effects that require the direction of an enemy attack. Returns true if a valid direction could be calculated.

### GetGameplayCueEndLocationAndNormal
```angelscript
bool GetGameplayCueEndLocationAndNormal(AActor TargetActor, FGameplayCueParameters Parameters, FVector& Location, FVector& Normal)
```
Gets the best end location and normal for this gameplay cue. If there is hit result data, it will return this. Otherwise it will return the target actor's location/rotation. If none of this is available, it will return false.

### GetGameplayEffectAssetTags
```angelscript
FGameplayTagContainer GetGameplayEffectAssetTags(TSubclassOf<UGameplayEffect> EffectClass)
```
Returns all tags that the Gameplay Effect *has* (that denote the GE Asset itself) and *does not* grant to any Actor.

### GetGameplayEffectFromActiveEffectHandle
```angelscript
const UGameplayEffect GetGameplayEffectFromActiveEffectHandle(FActiveGameplayEffectHandle ActiveHandle)
```
Returns the Gameplay Effect CDO from an active handle.
This reference should be considered read only,
but you can use it to read additional Gameplay Effect info, such as icon, description, etc.

### GetGameplayEffectGrantedTags
```angelscript
FGameplayTagContainer GetGameplayEffectGrantedTags(TSubclassOf<UGameplayEffect> EffectClass)
```
Returns all tags that the Gameplay Effect grants to the target Actor

### GetGameplayEffectUIData
```angelscript
const UGameplayEffectUIData GetGameplayEffectUIData(TSubclassOf<UGameplayEffect> EffectClass, TSubclassOf<UGameplayEffectUIData> DataType)
```
Returns the UI data for a gameplay effect class (if any)

### GetHitResult
```angelscript
FHitResult GetHitResult(FGameplayCueParameters Parameters)
```
Returns a hit result stored in the effect context if valid

### GetHitResultFromTargetData
```angelscript
FHitResult GetHitResultFromTargetData(FGameplayAbilityTargetDataHandle HitResult, int Index)
```
Returns the hit result for a given index if it exists

### GetInstigatorActor
```angelscript
AActor GetInstigatorActor(FGameplayCueParameters Parameters)
```
Gets the instigating actor (that holds the ability system component) of the GameplayCue

### GetInstigatorTransform
```angelscript
FTransform GetInstigatorTransform(FGameplayCueParameters Parameters)
```
Gets instigating world location

### GetModifiedAttributeMagnitude
```angelscript
float32 GetModifiedAttributeMagnitude(FGameplayEffectSpecHandle SpecHandle, FGameplayAttribute Attribute)
```
Gets the magnitude of change for an attribute on an APPLIED GameplayEffectSpec.

### GetOrigin
```angelscript
FVector GetOrigin(FGameplayCueParameters Parameters)
```
Gets instigating world location

### GetTargetDataEndPoint
```angelscript
FVector GetTargetDataEndPoint(FGameplayAbilityTargetDataHandle TargetData, int Index)
```
Returns the end point for a given index if it exists

### GetTargetDataEndPointTransform
```angelscript
FTransform GetTargetDataEndPointTransform(FGameplayAbilityTargetDataHandle TargetData, int Index)
```
Returns the end point transform for a given index if it exists

### GetTargetDataOrigin
```angelscript
FTransform GetTargetDataOrigin(FGameplayAbilityTargetDataHandle TargetData, int Index)
```
Returns the origin for a given index if it exists

### HasHitResult
```angelscript
bool HasHitResult(FGameplayCueParameters Parameters)
```
Checks if the effect context has a hit reslt stored inside

### IsInstigatorLocallyControlled
```angelscript
bool IsInstigatorLocallyControlled(FGameplayCueParameters Parameters)
```
Returns true if the ability system component that spawned this cue is locally controlled

### IsInstigatorLocallyControlledPlayer
```angelscript
bool IsInstigatorLocallyControlledPlayer(FGameplayCueParameters Parameters)
```
Returns true if the ability system component that spawned this cue is locally controlled and a player

### IsValid
```angelscript
bool IsValid(FGameplayAttribute Attribute)
```
Returns true if the attribute actually exists

### MakeFilterHandle
```angelscript
FGameplayTargetDataFilterHandle MakeFilterHandle(FGameplayTargetDataFilter Filter, AActor FilterActor)
```
Create a handle for filtering target data, filling out all fields

### MakeGameplayCueParameters
```angelscript
FGameplayCueParameters MakeGameplayCueParameters(float32 NormalizedMagnitude, float32 RawMagnitude, FGameplayEffectContextHandle EffectContext, FGameplayTag MatchedTagName, FGameplayTag OriginalTag, FGameplayTagContainer AggregatedSourceTags, FGameplayTagContainer AggregatedTargetTags, FVector Location, FVector Normal, AActor Instigator, AActor EffectCauser, UObject SourceObject, UPhysicalMaterial PhysicalMaterial, int GameplayEffectLevel, int AbilityLevel, USceneComponent TargetAttachComponent, bool bReplicateLocationWhenUsingMinimalRepProxy)
```
Native make, to avoid having to deal with quantized vector types

### MakeSpecHandle
```angelscript
FGameplayEffectSpecHandle MakeSpecHandle(UGameplayEffect InGameplayEffect, AActor InInstigator, AActor InEffectCauser, float32 InLevel)
```
Create a spec handle, filling out all fields

### NotEqual_ActiveGameplayEffectHandle
```angelscript
bool NotEqual_ActiveGameplayEffectHandle(FActiveGameplayEffectHandle A, FActiveGameplayEffectHandle B)
```
Inequality operator for two Active Gameplay Effect Handles

### NotEqual_GameplayAbilitySpecHandle
```angelscript
bool NotEqual_GameplayAbilitySpecHandle(FGameplayAbilitySpecHandle A, FGameplayAbilitySpecHandle B)
```
Inequality operator for two Gameplay Ability Spec Handles

### NotEqual_GameplayAttributeGameplayAttribute
```angelscript
bool NotEqual_GameplayAttributeGameplayAttribute(FGameplayAttribute AttributeA, FGameplayAttribute AttributeB)
```
Simple inequality operator for gameplay attributes

### RemoveLooseGameplayTags
```angelscript
bool RemoveLooseGameplayTags(AActor Actor, FGameplayTagContainer GameplayTags, bool bShouldReplicate)
```
Manually removes a set of tags from a given actor, with optional replication.

### SendGameplayEventToActor
```angelscript
void SendGameplayEventToActor(AActor Actor, FGameplayTag EventTag, FGameplayEventData Payload)
```
This function can be used to trigger an ability on the actor in question with useful payload data.

### SetDuration
```angelscript
FGameplayEffectSpecHandle SetDuration(FGameplayEffectSpecHandle SpecHandle, float32 Duration)
```
Manually sets the duration on a specific effect

### SetStackCount
```angelscript
FGameplayEffectSpecHandle SetStackCount(FGameplayEffectSpecHandle SpecHandle, int StackCount)
```
Sets the GameplayEffectSpec's StackCount to the specified amount (prior to applying)

### SetStackCountToMax
```angelscript
FGameplayEffectSpecHandle SetStackCountToMax(FGameplayEffectSpecHandle SpecHandle)
```
Sets the GameplayEffectSpec's StackCount to the max stack count defined in the GameplayEffect definition

### TargetDataHasActor
```angelscript
bool TargetDataHasActor(FGameplayAbilityTargetDataHandle TargetData, int Index)
```
Returns true if the given TargetData has at least 1 actor targeted

### TargetDataHasEndPoint
```angelscript
bool TargetDataHasEndPoint(FGameplayAbilityTargetDataHandle TargetData, int Index)
```
Returns true if the target data has an end point

### TargetDataHasHitResult
```angelscript
bool TargetDataHasHitResult(FGameplayAbilityTargetDataHandle HitResult, int Index)
```
Returns true if the target data has a hit result

### TargetDataHasOrigin
```angelscript
bool TargetDataHasOrigin(FGameplayAbilityTargetDataHandle TargetData, int Index)
```
Returns true if the target data has an origin

