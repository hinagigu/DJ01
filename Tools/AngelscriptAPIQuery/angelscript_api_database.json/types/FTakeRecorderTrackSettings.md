# FTakeRecorderTrackSettings

## 属性

### MatchingActorClass
- **类型**: `FSoftClassPath`
- **描述**: The Actor class to create movie scene tracks for.

### DefaultPropertyTracks
- **类型**: `TArray<FTakeRecorderPropertyTrackSettings>`
- **描述**: List of property names for which movie scene tracks will be created automatically.

### ExcludePropertyTracks
- **类型**: `TArray<FTakeRecorderPropertyTrackSettings>`
- **描述**: List of property names for which movie scene tracks will NOT be created automatically.

## 方法

### opAssign
```angelscript
FTakeRecorderTrackSettings& opAssign(FTakeRecorderTrackSettings Other)
```

