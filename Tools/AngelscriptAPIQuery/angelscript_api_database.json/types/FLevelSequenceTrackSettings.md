# FLevelSequenceTrackSettings

## 属性

### MatchingActorClass
- **类型**: `FSoftClassPath`
- **描述**: The Actor class to create movie scene tracks for.

### DefaultTracks
- **类型**: `TArray<FSoftClassPath>`
- **描述**: List of movie scene track classes to be added automatically.

### ExcludeDefaultTracks
- **类型**: `TArray<FSoftClassPath>`
- **描述**: List of movie scene track classes not to be added automatically.

### DefaultPropertyTracks
- **类型**: `TArray<FLevelSequencePropertyTrackSettings>`
- **描述**: List of property names for which movie scene tracks will be created automatically.

### ExcludeDefaultPropertyTracks
- **类型**: `TArray<FLevelSequencePropertyTrackSettings>`
- **描述**: List of property names for which movie scene tracks will not be created automatically.

## 方法

### opAssign
```angelscript
FLevelSequenceTrackSettings& opAssign(FLevelSequenceTrackSettings Other)
```

