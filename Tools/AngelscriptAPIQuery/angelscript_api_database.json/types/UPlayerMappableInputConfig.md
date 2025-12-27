# UPlayerMappableInputConfig

**继承自**: `UPrimaryDataAsset`

UPlayerMappableInputConfig

This represents one set of Player Mappable controller/keymappings. You can use this input config to create
the default mappings for your player to start with in your game. It provides an easy way to get only the player
mappable key actions, and it can be used to add multiple UInputMappingContext's at once to the player.

Populate this data asset with Input Mapping Contexts that have player mappable actions in them.

## 属性

### ConfigDisplayName
- **类型**: `FText`

### bIsDeprecated
- **类型**: `bool`

### Contexts
- **类型**: `TMap<TObjectPtr<UInputMappingContext>,int>`

### ConfigName
- **类型**: `FName`

### Metadata
- **类型**: `UObject`

## 方法

### GetConfigName
```angelscript
FName GetConfigName()
```

### GetDisplayName
```angelscript
FText GetDisplayName()
```

### GetKeysBoundToAction
```angelscript
TArray<FEnhancedActionKeyMapping> GetKeysBoundToAction(const UInputAction InAction)
```
Returns all the keys mapped to a specific Input Action in this mapping config.

### GetMappingByName
```angelscript
FEnhancedActionKeyMapping GetMappingByName(FName MappingName)
```
Returns the action key mapping for the mapping that matches the given name

### GetMappingContexts
```angelscript
TMap<TObjectPtr<UInputMappingContext>,int> GetMappingContexts()
```
Return all the Input Mapping contexts that

### GetMetadata
```angelscript
UObject GetMetadata()
```
Get all the player mappable keys in this config.

### GetPlayerMappableKeys
```angelscript
TArray<FEnhancedActionKeyMapping> GetPlayerMappableKeys()
```
Get all the player mappable keys in this config.

### IsDeprecated
```angelscript
bool IsDeprecated()
```

### ResetToDefault
```angelscript
void ResetToDefault()
```
Resets this mappable config to use the keys

