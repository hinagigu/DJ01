# FGenerateStaticMeshLODProcess_PreprocessSettings

## 属性

### FilterGroupLayer
- **类型**: `FName`
- **描述**: Group layer to use for filtering out detail before processing

### ThickenWeightMapName
- **类型**: `FName`
- **描述**: Weight map used during mesh thickening

### ThickenAmount
- **类型**: `float32`
- **描述**: Amount to thicken the mesh prior to Solidifying. The thicken weight map values are multiplied by this value.
Thickening is primarily intended to repair shape erosion that can occur when using the Solidify Mesh Generators.

## 方法

### opAssign
```angelscript
FGenerateStaticMeshLODProcess_PreprocessSettings& opAssign(FGenerateStaticMeshLODProcess_PreprocessSettings Other)
```

