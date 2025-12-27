# FSkeletalMeshLODInfo

Struct containing information for a particular LOD level, such as materials and info for when to use it.

## 属性

### ScreenSize
- **类型**: `FPerPlatformFloat`
- **描述**: ScreenSize to display this LOD.
The screen size is based around the projected diameter of the bounding
sphere of the model. i.e. 0.5 means half the screen's maximum dimension.

### LODHysteresis
- **类型**: `float32`
- **描述**: Used to avoid 'flickering' when on LOD boundary. Only taken into account when moving from complex->simple.

### BuildSettings
- **类型**: `FSkeletalMeshBuildSettings`
- **描述**: build settings to apply when building render data.

### ReductionSettings
- **类型**: `FSkeletalMeshOptimizationSettings`
- **描述**: Reduction settings to apply when building render data.

### BonesToRemove
- **类型**: `TArray<FBoneReference>`
- **描述**: Bones which should be removed from the skeleton for the LOD level

### BonesToPrioritize
- **类型**: `TArray<FBoneReference>`
- **描述**: Bones which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.

### SectionsToPrioritize
- **类型**: `TArray<FSectionReference>`
- **描述**: Sections which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.

### WeightOfPrioritization
- **类型**: `float32`
- **描述**: How much to consideration to give BonesToPrioritize and SectionsToPrioritize.  The weight is an additional vertex simplification penalty where 0 means nothing.

### BakePose
- **类型**: `UAnimSequence`
- **描述**: Pose which should be used to reskin vertex influences for which the bones will be removed in this LOD level, uses ref-pose by default

### BakePoseOverride
- **类型**: `UAnimSequence`
- **描述**: This is used when you are sharing the LOD settings, but you'd like to override the BasePose. This precedes prior to BakePose

### SkinCacheUsage
- **类型**: `ESkinCacheUsage`
- **描述**: How this LOD uses the skin cache feature. Auto will defer to the default project global option. If Support Ray Tracing is enabled on the mesh, will imply Enabled

### MorphTargetPositionErrorTolerance
- **类型**: `float32`
- **描述**: The Morph target position error tolerance in microns. Larger values result in better compression and lower memory footprint, but also lower quality.

### VertexAttributes
- **类型**: `TArray<FSkeletalMeshVertexAttributeInfo>`
- **描述**: List of vertex attributes to include for rendering and what type they should be

### bAllowCPUAccess
- **类型**: `bool`

### bBuildHalfEdgeBuffers
- **类型**: `bool`

### bAllowMeshDeformer
- **类型**: `bool`

### bSupportUniformlyDistributedSampling
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FSkeletalMeshLODInfo& opAssign(FSkeletalMeshLODInfo Other)
```

