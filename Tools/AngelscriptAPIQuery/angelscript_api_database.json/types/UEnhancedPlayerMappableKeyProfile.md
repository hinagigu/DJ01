# UEnhancedPlayerMappableKeyProfile

**继承自**: `UObject`

Represents one "Profile" that a user can have for their player mappable keys

## 属性

### ProfileIdentifier
- **类型**: `FGameplayTag`

### OwningUserId
- **类型**: `FPlatformUserId`
- **描述**: The platform user id of the owning Local Player of this profile.

### PlayerMappedKeys
- **类型**: `TMap<FName,FKeyMappingRow>`

### DisplayName
- **类型**: `FText`

## 方法

### DoesMappingPassQueryOptions
```angelscript
bool DoesMappingPassQueryOptions(FPlayerKeyMapping PlayerMapping, FPlayerMappableKeyQueryOptions Options)
```
Returns true if the given player key mapping passes the query filter provided.

### DumpProfileToLog
```angelscript
void DumpProfileToLog()
```
A helper function to print out all the current profile settings to the log.

### GetMappedKeysInRow
```angelscript
int GetMappedKeysInRow(FName MappingName, TArray<FKey>& OutKeys)
```
OUT

### GetMappingNamesForKey
```angelscript
int GetMappingNamesForKey(FKey InKey, TArray<FName>& OutMappingNames)
```
OUT

### GetPlayerMappingRows
```angelscript
TMap<FName,FKeyMappingRow> GetPlayerMappingRows()
```
Get all known key mappings for this profile.

This returns a map of "Mapping Name" -> Player Mappings to that name

### GetProfileDisplayName
```angelscript
FText GetProfileDisplayName()
```
Get the localized display name for this profile

### GetProfileIdentifer
```angelscript
FGameplayTag GetProfileIdentifer()
```

### FindKeyMapping
```angelscript
void FindKeyMapping(FPlayerKeyMapping& OutKeyMapping, FMapPlayerKeyArgs InArgs)
```

### QueryPlayerMappedKeys
```angelscript
int QueryPlayerMappedKeys(FPlayerMappableKeyQueryOptions Options, TArray<FKey>& OutKeys)
```
OUT

### ResetMappingToDefault
```angelscript
void ResetMappingToDefault(FName InMappingName)
```
Resets every player key mapping to this mapping back to it's default value

### ResetToDefault
```angelscript
void ResetToDefault()
```
Resets all the key mappings in this profile to their default value from their Input Mapping Context.

### SetDisplayName
```angelscript
void SetDisplayName(FText NewDisplayName)
```

### ToString
```angelscript
FString ToString()
```
Returns a string that can be used to debug the current key mappings.

