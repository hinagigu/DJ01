# FNiagaraDataChannelSearchParameters

Parameters used when retrieving a specific set of Data Channel Data to read or write.
Many Data Channel types will have multiple internal sets of data and these parameters control which the Channel should return to users for access.
An example of this would be the Islands Data Channel type which will subdivide the world and have a different set of data for each sub division.
It will return to users the correct data for their location based on these parameters.

## 属性

### OwningComponent
- **类型**: `USceneComponent`

### Location
- **类型**: `FVector`

### bOverrideLocation
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraDataChannelSearchParameters& opAssign(FNiagaraDataChannelSearchParameters Other)
```

