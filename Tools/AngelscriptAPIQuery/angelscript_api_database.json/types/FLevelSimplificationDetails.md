# FLevelSimplificationDetails

## 属性

### bCreatePackagePerAsset
- **类型**: `bool`
- **描述**: Whether to create separate packages for each generated asset. All in map package otherwise

### DetailsPercentage
- **类型**: `float32`
- **描述**: Percentage of details for static mesh proxy

### StaticMeshMaterialSettings
- **类型**: `FMaterialProxySettings`
- **描述**: Landscape material simplification

### bOverrideLandscapeExportLOD
- **类型**: `bool`

### LandscapeExportLOD
- **类型**: `int`
- **描述**: Landscape LOD to use for static mesh generation, when not specified 'Max LODLevel' from landscape actor will be used

### LandscapeMaterialSettings
- **类型**: `FMaterialProxySettings`
- **描述**: Landscape material simplification

### bBakeFoliageToLandscape
- **类型**: `bool`
- **描述**: Whether to bake foliage into landscape static mesh texture

### bBakeGrassToLandscape
- **类型**: `bool`
- **描述**: Whether to bake grass into landscape static mesh texture

## 方法

### opAssign
```angelscript
FLevelSimplificationDetails& opAssign(FLevelSimplificationDetails Other)
```

