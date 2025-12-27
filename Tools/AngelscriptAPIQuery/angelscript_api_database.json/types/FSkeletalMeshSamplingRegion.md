# FSkeletalMeshSamplingRegion

Defined a named region on a mesh that will have associated triangles and bones for fast sampling at each enabled LOD.

## 属性

### Name
- **类型**: `FName`
- **描述**: Name of this region that users will reference.

### LODIndex
- **类型**: `int`
- **描述**: The LOD of the mesh that this region applies to.

### MaterialFilters
- **类型**: `TArray<FSkeletalMeshSamplingRegionMaterialFilter>`
- **描述**: Filters to determine which triangles to include in this region based on material.

### BoneFilters
- **类型**: `TArray<FSkeletalMeshSamplingRegionBoneFilter>`
- **描述**: Filters to determine which triangles and bones to include in this region based on bone.

### bSupportUniformlyDistributedSampling
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FSkeletalMeshSamplingRegion& opAssign(FSkeletalMeshSamplingRegion Other)
```

