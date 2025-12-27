# FPlayerMappableKeyQueryOptions

Options when querying what keys are mapped to a specific action on the player mappable
key profile.

## 属性

### MappingName
- **类型**: `FName`

### KeyToMatch
- **类型**: `FKey`

### SlotToMatch
- **类型**: `EPlayerMappableKeySlot`

### RequiredDeviceType
- **类型**: `EHardwareDevicePrimaryType`

### RequiredDeviceFlags
- **类型**: `int`

### bMatchBasicKeyTypes
- **类型**: `bool`

### bMatchKeyAxisType
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FPlayerMappableKeyQueryOptions& opAssign(FPlayerMappableKeyQueryOptions Other)
```

