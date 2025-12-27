# UFbxSkeletalMeshImportData

**继承自**: `UFbxMeshImportData`

Import data and options used when importing a static mesh from fbx
Notes:
- Meta data ImportType i.e.       meta = (ImportType = "SkeletalMesh|GeoOnly")
    - SkeletalMesh : the property will be shown when importing skeletalmesh
    - GeoOnly: The property will be hide if we import skinning only
    - RigOnly: The property will be hide if we import geo only
    - RigAndGeo: The property will be show only if we import both skinning and geometry, it will be hiden otherwise

## 属性

### ImportContentType
- **类型**: `EFBXImportContentType`
- **描述**: Filter the content we want to import from the incoming FBX skeletal mesh.

### VertexColorImportOption
- **类型**: `EVertexColorImportOption`

### VertexOverrideColor
- **类型**: `FColor`

### ThresholdPosition
- **类型**: `float32`
- **描述**: Threshold to compare vertex position equality.

### ThresholdTangentNormal
- **类型**: `float32`
- **描述**: Threshold to compare normal, tangent or bi-normal equality.

### ThresholdUV
- **类型**: `float32`
- **描述**: Threshold to compare UV equality.

### MorphThresholdPosition
- **类型**: `float32`
- **描述**: Threshold to compare vertex position equality when computing morph target deltas.

### bUpdateSkeletonReferencePose
- **类型**: `bool`

### bUseT0AsRefPose
- **类型**: `bool`

### bPreserveSmoothingGroups
- **类型**: `bool`

### bKeepSectionsSeparate
- **类型**: `bool`

### bImportMeshesInBoneHierarchy
- **类型**: `bool`

### bImportMorphTargets
- **类型**: `bool`

### bImportVertexAttributes
- **类型**: `bool`

