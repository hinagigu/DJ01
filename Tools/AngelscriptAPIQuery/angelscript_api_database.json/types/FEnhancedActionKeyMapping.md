# FEnhancedActionKeyMapping

Defines a mapping between a key activation and the resulting enhanced action
An key could be a button press, joystick axis movement, etc.
An enhanced action could be MoveForward, Jump, Fire, etc.

## 属性

### Triggers
- **类型**: `TArray<TObjectPtr<UInputTrigger>>`

### Modifiers
- **类型**: `TArray<TObjectPtr<UInputModifier>>`

### Action
- **类型**: `const UInputAction`

### Key
- **类型**: `FKey`

### SettingBehavior
- **类型**: `EPlayerMappableKeySettingBehaviors`
- **描述**: Defines which Player Mappable Key Setting to use for a Action Key Mapping.

### PlayerMappableKeySettings
- **类型**: `UPlayerMappableKeySettings`
- **描述**: Used to expose this mapping or to opt-out of settings completely.

## 方法

### opAssign
```angelscript
FEnhancedActionKeyMapping& opAssign(FEnhancedActionKeyMapping Other)
```

