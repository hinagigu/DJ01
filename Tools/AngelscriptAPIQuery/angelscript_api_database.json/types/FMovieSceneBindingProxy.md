# FMovieSceneBindingProxy

Movie Scene Binding Proxy represents the binding ID (an FGuid) and the corresponding sequence that it relates to.
This is primarily used for scripting where there is no support for FMovieSceneSequenceID and use cases where
managing multiple bindings with their corresponding sequences is necessary.

## 属性

### BindingID
- **类型**: `FGuid`

### Sequence
- **类型**: `UMovieSceneSequence`

## 方法

### opAssign
```angelscript
FMovieSceneBindingProxy& opAssign(FMovieSceneBindingProxy Other)
```

