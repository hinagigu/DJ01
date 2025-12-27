# UInputAction

**继承自**: `UDataAsset`

An Input Action is a logical representation of something the user can do, such as "Jump" or "Crouch".
These are what your gameplay code binds to in order to listen for input state changes. For most scenarios
your gameplay code should be listening for the "Triggered" event on an input action. This will allow
for the most scalable and customizable input configuration because you can add different triggers
for each key mapping in the Input Mapping Context.

They are the conceptual equivalent to "Action" and "Axis" mapping names from the Legacy Input System.

Note: These are instanced per player (via FInputActionInstance)

## 属性

### ActionDescription
- **类型**: `FText`

### bTriggerWhenPaused
- **类型**: `bool`

### bConsumeInput
- **类型**: `bool`

### bConsumesActionAndAxisMappings
- **类型**: `bool`

### bReserveAllMappings
- **类型**: `bool`

### TriggerEventsThatConsumeLegacyKeys
- **类型**: `int`

### ValueType
- **类型**: `EInputActionValueType`

### AccumulationBehavior
- **类型**: `EInputActionAccumulationBehavior`

### Triggers
- **类型**: `TArray<TObjectPtr<UInputTrigger>>`

### Modifiers
- **类型**: `TArray<TObjectPtr<UInputModifier>>`

### PlayerMappableKeySettings
- **类型**: `UPlayerMappableKeySettings`

