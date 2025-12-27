# FMovieSceneBindingOverrideData

Movie scene binding override data

## 属性

### ObjectBindingId
- **类型**: `FMovieSceneObjectBindingID`
- **描述**: Specifies the object binding to override.

### Object
- **类型**: `TSoftObjectPtr<UObject>`
- **描述**: Specifies the object to override the binding with.

### bOverridesDefault
- **类型**: `bool`
- **描述**: Specifies whether the default assignment should remain bound (false) or if this should completely override the default binding (true).

## 方法

### opAssign
```angelscript
FMovieSceneBindingOverrideData& opAssign(FMovieSceneBindingOverrideData Other)
```

