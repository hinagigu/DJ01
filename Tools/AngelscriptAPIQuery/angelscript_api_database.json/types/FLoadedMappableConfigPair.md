# FLoadedMappableConfigPair

A container to organize loaded player mappable configs to their CommonUI input type

## 属性

### Config
- **类型**: `const UPlayerMappableInputConfig`
- **描述**: The player mappable input config that should be applied to the Enhanced Input subsystem

### Type
- **类型**: `ECommonInputType`
- **描述**: The type of device that this mapping config should be applied to

### bIsActive
- **类型**: `bool`
- **描述**: If this config is currently active. A config is marked as active when it's owning GFA is active

## 方法

### opAssign
```angelscript
FLoadedMappableConfigPair& opAssign(FLoadedMappableConfigPair Other)
```

