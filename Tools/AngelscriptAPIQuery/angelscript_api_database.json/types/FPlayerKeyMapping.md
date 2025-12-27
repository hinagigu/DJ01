# FPlayerKeyMapping

Represents a single key mapping that is set by the player

## 属性

### MappingName
- **类型**: `FName`
- **描述**: The name of the mapping for this key

### DisplayName
- **类型**: `FText`
- **描述**: Localized display name of this mapping

### DisplayCategory
- **类型**: `FText`
- **描述**: Localized display category of this mapping

### Slot
- **类型**: `EPlayerMappableKeySlot`
- **描述**: What slot this key is mapped to

### DefaultKey
- **类型**: `FKey`
- **描述**: The default key that this mapping was set to in its input mapping context

### CurrentKey
- **类型**: `FKey`
- **描述**: The key that the player has mapped to

### HardwareDeviceId
- **类型**: `FHardwareDeviceIdentifier`
- **描述**: An optional Hardware Device specifier for this mapping

### AssociatedInputAction
- **类型**: `const UInputAction`
- **描述**: The input action associated with this player key mapping

### bIsDirty
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FPlayerKeyMapping& opAssign(FPlayerKeyMapping Other)
```

