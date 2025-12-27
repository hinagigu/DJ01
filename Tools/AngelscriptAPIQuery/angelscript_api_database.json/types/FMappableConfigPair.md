# FMappableConfigPair

A container to organize potentially unloaded player mappable configs to their CommonUI input type

## 属性

### Config
- **类型**: `TSoftObjectPtr<UPlayerMappableInputConfig>`

### Type
- **类型**: `ECommonInputType`
- **描述**: The type of config that this is. Useful for filtering out configs by the current input device
for things like the settings screen, or if you only want to apply this config when a certain
input type is being used.

### DependentPlatformTraits
- **类型**: `FGameplayTagContainer`
- **描述**: Container of platform traits that must be set in order for this input to be activated.

If the platform does not have one of the traits specified it can still be registered, but cannot
be activated.

### ExcludedPlatformTraits
- **类型**: `FGameplayTagContainer`
- **描述**: If the current platform has any of these traits, then this config will not be actived.

### bShouldActivateAutomatically
- **类型**: `bool`
- **描述**: If true, then this input config will be activated when it's associated Game Feature is activated.
This is normally the desirable behavior

## 方法

### opAssign
```angelscript
FMappableConfigPair& opAssign(FMappableConfigPair Other)
```

