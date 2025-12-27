# UMovieSceneDataLayerSection

**继承自**: `UMovieSceneSection`

## 属性

### bFlushOnActivated
- **类型**: `bool`
- **描述**: Determine if we need to flush level streaming when the data layers are activated. May result in a hitch.

### bFlushOnUnload
- **类型**: `bool`
- **描述**: Determine if we need to flush level streaming when the data layers unloads.

### bPerformGCOnUnload
- **类型**: `bool`
- **描述**: Determine if we need to perform a GC when the data layers unloads.

## 方法

### GetDataLayerAssets
```angelscript
TArray<UDataLayerAsset> GetDataLayerAssets()
```

### GetDataLayers
```angelscript
TArray<FActorDataLayer> GetDataLayers()
```

### GetDesiredState
```angelscript
EDataLayerRuntimeState GetDesiredState()
```

### GetFlushOnActivated
```angelscript
bool GetFlushOnActivated()
```

### GetFlushOnUnload
```angelscript
bool GetFlushOnUnload()
```

### GetPerformGCOnUnload
```angelscript
bool GetPerformGCOnUnload()
```

### GetPrerollState
```angelscript
EDataLayerRuntimeState GetPrerollState()
```

### SetDataLayerAssets
```angelscript
void SetDataLayerAssets(TArray<UDataLayerAsset> InDataLayerAssets)
```

### SetDataLayers
```angelscript
void SetDataLayers(TArray<FActorDataLayer> InDataLayers)
```

### SetDesiredState
```angelscript
void SetDesiredState(EDataLayerRuntimeState InDesiredState)
```

### SetFlushOnActivated
```angelscript
void SetFlushOnActivated(bool bFlushOnActivated)
```

### SetFlushOnUnload
```angelscript
void SetFlushOnUnload(bool bFlushOnUnload)
```

### SetPerformGCOnUnload
```angelscript
void SetPerformGCOnUnload(bool bPerformGCOnUnload)
```

### SetPrerollState
```angelscript
void SetPrerollState(EDataLayerRuntimeState InPrerollState)
```

