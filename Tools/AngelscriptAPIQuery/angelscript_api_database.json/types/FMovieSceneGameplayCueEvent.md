# FMovieSceneGameplayCueEvent

## 方法

### opAssign
```angelscript
FMovieSceneGameplayCueEvent& opAssign(FMovieSceneGameplayCueEvent Other)
```

### IsBound
```angelscript
bool IsBound()
```

### GetUObject
```angelscript
UObject GetUObject()
```

### GetFunctionName
```angelscript
FName GetFunctionName()
```

### Clear
```angelscript
void Clear()
```

### BindUFunction
```angelscript
void BindUFunction(UObject Object, FName FunctionName)
```

### Execute
```angelscript
void Execute(AActor Target, FGameplayTag GameplayTag, const FGameplayCueParameters&in Parameters, EGameplayCueEvent Event)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(AActor Target, FGameplayTag GameplayTag, const FGameplayCueParameters&in Parameters, EGameplayCueEvent Event)
```

