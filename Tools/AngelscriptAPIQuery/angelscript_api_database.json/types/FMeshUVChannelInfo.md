# FMeshUVChannelInfo

The world size for each texcoord mapping. Used by the texture streaming.

## 属性

### bOverrideDensities
- **类型**: `bool`
- **描述**: Whether this values was set manually or is auto generated.

### LocalUVDensities
- **类型**: `float32`
- **描述**: The UV density in the mesh, before any transform scaling, in world unit per UV.
This value represents the length taken to cover a full UV unit.

## 方法

### opAssign
```angelscript
FMeshUVChannelInfo& opAssign(FMeshUVChannelInfo Other)
```

