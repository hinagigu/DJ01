# FPhysAssetCreateParams

Parameters for PhysicsAsset creation

## 属性

### MinBoneSize
- **类型**: `float32`
- **描述**: Bones that are shorter than this value will be ignored for body creation

### MinWeldSize
- **类型**: `float32`
- **描述**: Bones that are smaller than this value will be merged together for body creation

### GeomType
- **类型**: `EPhysAssetFitGeomType`
- **描述**: The geometry type that should be used when creating bodies

### VertWeight
- **类型**: `EPhysAssetFitVertWeight`
- **描述**: How vertices are mapped to bones when approximating them with bodies

### bAutoOrientToBone
- **类型**: `bool`
- **描述**: Whether to automatically orient the created bodies to their corresponding bones

### bCreateConstraints
- **类型**: `bool`
- **描述**: Whether to create constraints between adjacent created bodies

### bWalkPastSmall
- **类型**: `bool`
- **描述**: Whether to skip small bones entirely (rather than merge them with adjacent bones)

### bBodyForAll
- **类型**: `bool`
- **描述**: Forces creation of a body for each bone

### bDisableCollisionsByDefault
- **类型**: `bool`
- **描述**: Whether to disable collision of body with other bodies on creation

### AngularConstraintMode
- **类型**: `EAngularConstraintMotion`
- **描述**: The type of angular constraint to create between bodies

### HullCount
- **类型**: `int`
- **描述**: When creating multiple convex hulls, the maximum number that will be created.

### MaxHullVerts
- **类型**: `int`
- **描述**: When creating convex hulls, the maximum verts that should be created

### LevelSetResolution
- **类型**: `int`
- **描述**: When creating level sets, the grid resolution to use

### LatticeResolution
- **类型**: `int`
- **描述**: When creating skinned level sets, the embedding grid resolution to use

## 方法

### opAssign
```angelscript
FPhysAssetCreateParams& opAssign(FPhysAssetCreateParams Other)
```

