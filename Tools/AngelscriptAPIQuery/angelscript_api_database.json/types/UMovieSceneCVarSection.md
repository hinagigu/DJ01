# UMovieSceneCVarSection

**继承自**: `UMovieSceneSection`

A CVar section is responsible for applying a user-supplied value to the specified cvar, and then restoring the previous value after the section ends.

## 属性

### ConsoleVariableCollections
- **类型**: `TArray<FMovieSceneConsoleVariableCollection>`
- **描述**: Array of console variable preset assets that this track should operate on

### ConsoleVariables
- **类型**: `FMovieSceneCVarOverrides`
- **描述**: The name of the console variable and the value, separated by ' ' or '=', ie: "foo.bar=1" or "foo.bar 1".

## 方法

### GetString
```angelscript
FString GetString()
```

### SetFromString
```angelscript
void SetFromString(FString InString)
```

