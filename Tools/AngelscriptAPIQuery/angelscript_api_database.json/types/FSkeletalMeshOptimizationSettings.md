# FSkeletalMeshOptimizationSettings

FSkeletalMeshOptimizationSettings - The settings used to optimize a skeletal mesh LOD.

## 属性

### TerminationCriterion
- **类型**: `SkeletalMeshTerminationCriterion`
- **描述**: The method to use when optimizing the skeletal mesh LOD

### NumOfTrianglesPercentage
- **类型**: `float32`
- **描述**: The percentage of triangles to retain as a ratio, e.g. 0.1 indicates 10 percent

### NumOfVertPercentage
- **类型**: `float32`
- **描述**: The percentage of vertices to retain as a ratio, e.g. 0.1 indicates 10 percent

### MaxNumOfTriangles
- **类型**: `uint`
- **描述**: The maximum number of triangles to retain

### MaxNumOfVerts
- **类型**: `uint`
- **描述**: The maximum number of vertices to retain

### MaxNumOfTrianglesPercentage
- **类型**: `uint`
- **描述**: The maximum number of triangles to retain when using percentage termination criterion.

### MaxNumOfVertsPercentage
- **类型**: `uint`
- **描述**: The maximum number of vertices to retain when using percentage termination criterion.

### MaxDeviationPercentage
- **类型**: `float32`
- **描述**: If ReductionMethod equals MaxDeviation this value is the maximum deviation from the base mesh as a percentage of the bounding sphere.
In code, it ranges from [0, 1]. In the editor UI, it ranges from [0, 100]

### ReductionMethod
- **类型**: `SkeletalMeshOptimizationType`
- **描述**: The method to use when optimizing the skeletal mesh LOD

### SilhouetteImportance
- **类型**: `SkeletalMeshOptimizationImportance`
- **描述**: How important the shape of the geometry is.

### TextureImportance
- **类型**: `SkeletalMeshOptimizationImportance`
- **描述**: How important texture density is.

### ShadingImportance
- **类型**: `SkeletalMeshOptimizationImportance`
- **描述**: How important shading quality is.

### SkinningImportance
- **类型**: `SkeletalMeshOptimizationImportance`
- **描述**: How important skinning quality is.

### WeldingThreshold
- **类型**: `float32`
- **描述**: The welding threshold distance. Vertices under this distance will be welded.

### NormalsThreshold
- **类型**: `float32`
- **描述**: If the angle between two triangles are above this value, the normals will not be
      smooth over the edge between those two triangles. Set in degrees. This is only used when bRecalcNormals is set to true

### MaxBonesPerVertex
- **类型**: `int`
- **描述**: Maximum number of bones that can be assigned to each vertex.

### VolumeImportance
- **类型**: `float32`
- **描述**: Default value of 1 attempts to preserve volume.  Smaller values will loose volume by flattening curved surfaces, and larger values will accentuate curved surfaces.

### BaseLOD
- **类型**: `int`
- **描述**: Base LOD index to generate this LOD. By default, we generate from LOD 0

### bRemapMorphTargets
- **类型**: `bool`

### bRecalcNormals
- **类型**: `bool`

### bEnforceBoneBoundaries
- **类型**: `bool`

### bMergeCoincidentVertBones
- **类型**: `bool`

### bLockEdges
- **类型**: `bool`

### bLockColorBounaries
- **类型**: `bool`

### bImproveTrianglesForCloth
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FSkeletalMeshOptimizationSettings& opAssign(FSkeletalMeshOptimizationSettings Other)
```

