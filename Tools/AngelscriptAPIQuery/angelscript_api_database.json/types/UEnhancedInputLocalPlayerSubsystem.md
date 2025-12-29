# UEnhancedInputLocalPlayerSubsystem

**继承自**: `ULocalPlayerSubsystem`

Per local player input subsystem

## 属性

### ControlMappingsRebuiltDelegate
- **类型**: `FOnControlMappingsRebuilt__EnhancedInputLocalPlayerSubsystem`

## 方法

### AddMappingContext
```angelscript
void AddMappingContext(const UInputMappingContext MappingContext, int Priority, FModifyContextOptions Options)
```
Add a control mapping context.
@param MappingContext                A set of key to action mappings to apply to this player
@param Priority                              Higher priority mappings will be applied first and, if they consume input, will block lower priority mappings.
@param Options                               Options to consider when adding this mapping context.

### AddPlayerMappableConfig
```angelscript
void AddPlayerMappableConfig(const UPlayerMappableInputConfig Config, FModifyContextOptions Options)
```
Adds all the input mapping contexts inside of this mappable config.

### AddPlayerMappedKey
```angelscript
int AddPlayerMappedKey(FName MappingName, FKey NewKey, FModifyContextOptions Options)
```
Replace any currently applied mappings to this key mapping with the given new one.
Requests a rebuild of the player mappings.

@return The number of mappings that have been replaced

### AddPlayerMappedKeyInSlot
```angelscript
int AddPlayerMappedKeyInSlot(FName MappingName, FKey NewKey, FPlayerMappableKeySlot KeySlot, FModifyContextOptions Options)
```
Emplace or replace any currently applied key in KeySlot for mapping of MappingName.
Requests a rebuild of the player mappings.

@return The number of mappings that have been replaced

### ClearAllMappings
```angelscript
void ClearAllMappings()
```
Remove all applied mapping contexts.

### GetPlayerInput
```angelscript
UEnhancedPlayerInput GetPlayerInput()
```

### HasMappingContext
```angelscript
bool HasMappingContext(const UInputMappingContext MappingContext)
```
Check if a mapping context is applied to this subsystem's owner.
        // TODO: BlueprintPure would be nicer. Move into library?

### InjectInputForAction
```angelscript
void InjectInputForAction(const UInputAction Action, FInputActionValue RawValue, TArray<UInputModifier> Modifiers, TArray<UInputTrigger> Triggers)
```
Input simulation via injection. Runs modifiers and triggers delegates as if the input had come through the underlying input system as FKeys.
Applies action modifiers and triggers on top.

@param Action                The Input Action to set inject input for
@param RawValue              The value to set the action to
@param Modifiers             The modifiers to apply to the injected input.
@param Triggers              The triggers to apply to the injected input.

### InjectInputVectorForAction
```angelscript
void InjectInputVectorForAction(const UInputAction Action, FVector Value, TArray<UInputModifier> Modifiers, TArray<UInputTrigger> Triggers)
```
Input simulation via injection. Runs modifiers and triggers delegates as if the input had come through the underlying input system as FKeys.
Applies action modifiers and triggers on top.

@param Action                The Input Action to set inject input for
@param Value                 The value to set the action to (the type will be controlled by the Action)
@param Modifiers             The modifiers to apply to the injected input.
@param Triggers              The triggers to apply to the injected input.

### QueryKeysMappedToAction
```angelscript
TArray<FKey> QueryKeysMappedToAction(const UInputAction Action)
```
Returns the keys mapped to the given action in the active input mapping contexts.

### QueryMapKeyInActiveContextSet
```angelscript
EMappingQueryResult QueryMapKeyInActiveContextSet(const UInputMappingContext InputContext, const UInputAction Action, FKey Key, TArray<FMappingQueryIssue>& OutIssues, EMappingQueryIssue BlockingIssues)
```
= DefaultMappingIssues::StandardFatal

### QueryMapKeyInContextSet
```angelscript
EMappingQueryResult QueryMapKeyInContextSet(TArray<UInputMappingContext> PrioritizedActiveContexts, const UInputMappingContext InputContext, const UInputAction Action, FKey Key, TArray<FMappingQueryIssue>& OutIssues, EMappingQueryIssue BlockingIssues)
```
= DefaultMappingIssues::StandardFatal

### RemoveMappingContext
```angelscript
void RemoveMappingContext(const UInputMappingContext MappingContext, FModifyContextOptions Options)
```
Remove a specific control context.
This is safe to call even if the context is not applied.
@param MappingContext         Context to remove from the player
@param Options                        Options to consider when removing this input mapping context

### RemovePlayerMappableConfig
```angelscript
void RemovePlayerMappableConfig(const UPlayerMappableInputConfig Config, FModifyContextOptions Options)
```
Removes all the input mapping contexts inside of this mappable config.

### RemovePlayerMappedKey
```angelscript
int RemovePlayerMappedKey(FName MappingName, FModifyContextOptions Options)
```
Remove any player mappings with to the given action
Requests a rebuild of the player mappings.

@return The number of mappings that have been removed

### RemovePlayerMappedKeyInSlot
```angelscript
int RemovePlayerMappedKeyInSlot(FName MappingName, FPlayerMappableKeySlot KeySlot, FModifyContextOptions Options)
```
Removes player mapped key in the KeySlot for mapping of MappingName.
Requests a rebuild of the player mappings.

@return The number of mappings that have been removed

### RequestRebuildControlMappings
```angelscript
void RequestRebuildControlMappings(FModifyContextOptions Options, EInputMappingRebuildType RebuildType)
```
Flag player for reapplication of all mapping contexts at the end of this frame.
This is called automatically when adding or removing mappings contexts.

@param Options                Options to consider when removing this input mapping context

