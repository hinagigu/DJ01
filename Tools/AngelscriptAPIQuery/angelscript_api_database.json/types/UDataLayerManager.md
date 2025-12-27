# UDataLayerManager

**继承自**: `UObject`

## 属性

### OnDataLayerInstanceRuntimeStateChanged
- **类型**: `FOnDataLayerInstanceRuntimeStateChanged`

## 方法

### GetDataLayerInstanceEffectiveRuntimeState
```angelscript
EDataLayerRuntimeState GetDataLayerInstanceEffectiveRuntimeState(const UDataLayerInstance InDataLayerInstance)
```

### GetDataLayerInstanceFromAsset
```angelscript
const UDataLayerInstance GetDataLayerInstanceFromAsset(const UDataLayerAsset InDataLayerAsset)
```

### GetDataLayerInstanceFromName
```angelscript
const UDataLayerInstance GetDataLayerInstanceFromName(FName InDataLayerInstanceName)
```

### GetDataLayerInstanceRuntimeState
```angelscript
EDataLayerRuntimeState GetDataLayerInstanceRuntimeState(const UDataLayerInstance InDataLayerInstance)
```

### GetDataLayerInstances
```angelscript
TArray<UDataLayerInstance> GetDataLayerInstances()
```

### SetDataLayerInstanceRuntimeState
```angelscript
bool SetDataLayerInstanceRuntimeState(const UDataLayerInstance InDataLayerInstance, EDataLayerRuntimeState InState, bool bInIsRecursive)
```

### SetDataLayerRuntimeState
```angelscript
bool SetDataLayerRuntimeState(const UDataLayerAsset InDataLayerAsset, EDataLayerRuntimeState InState, bool bInIsRecursive)
```

