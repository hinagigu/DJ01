# FSkeletalMeshLODGroupSettings

## 属性

### ScreenSize
- **类型**: `FPerPlatformFloat`
- **描述**: The screen sizes to use for the respective LOD level

### LODHysteresis
- **类型**: `float32`
- **描述**: Used to avoid 'flickering' when on LOD boundary. Only taken into account when moving from complex->simple.

### BoneFilterActionOption
- **类型**: `EBoneFilterActionOption`
- **描述**: Bones which should be removed from the skeleton for the LOD level

### BoneList
- **类型**: `TArray<FBoneFilter>`
- **描述**: Bones which should be removed from the skeleton for the LOD level

### BonesToPrioritize
- **类型**: `TArray<FName>`
- **描述**: Bones which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.

### SectionsToPrioritize
- **类型**: `TArray<int>`
- **描述**: Sections which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.

### WeightOfPrioritization
- **类型**: `float32`
- **描述**: How much to consideration to give BonesToPrioritize and SectionsToPrioritize.  The weight is an additional vertex simplification penalty where 0 means nothing.

### BakePose
- **类型**: `UAnimSequence`
- **描述**: Pose which should be used to reskin vertex influences for which the bones will be removed in this LOD level, uses ref-pose by default

### ReductionSettings
- **类型**: `FSkeletalMeshOptimizationSettings`
- **描述**: The optimization settings to use for the respective LOD level

### bAllowMeshDeformer
- **类型**: `bool`
- **描述**: Whether a Mesh Deformer applied to the mesh asset or Skinned Mesh Component should be used on this LOD or not

## 方法

### opAssign
```angelscript
FSkeletalMeshLODGroupSettings& opAssign(FSkeletalMeshLODGroupSettings Other)
```

