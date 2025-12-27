# FMovieSceneDynamicBinding

Data for a dynamic binding endpoint call.

## 属性

### PayloadVariables
- **类型**: `TMap<FName,FMovieSceneDynamicBindingPayloadVariable>`
- **描述**: Array of payload variables to be added to the generated function

### ResolveParamsPinName
- **类型**: `FName`
- **描述**: Pin name for passing the resolve params

### WeakEndpoint
- **类型**: `TWeakObjectPtr<UObject>`
- **描述**: Endpoint node in the sequence director

## 方法

### opAssign
```angelscript
FMovieSceneDynamicBinding& opAssign(FMovieSceneDynamicBinding Other)
```

