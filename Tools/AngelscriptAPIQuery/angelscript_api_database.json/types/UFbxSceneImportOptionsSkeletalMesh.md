# UFbxSceneImportOptionsSkeletalMesh

**继承自**: `UObject`

## 属性

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

### AnimationLength
- **类型**: `EFBXAnimationLengthImportType`
- **描述**: Type of asset to import from the FBX file

### FrameImportRange
- **类型**: `FInt32Interval`
- **描述**: Frame range used when Set Range is used in Animation Length

### bUseDefaultSampleRate
- **类型**: `bool`
- **描述**: If enabled, samples all animation curves to 30 FPS

### CustomSampleRate
- **类型**: `int`
- **描述**: Sample fbx animation data at the specified sample rate, 0 find automaticaly the best sample rate

### bSnapToClosestFrameBoundary
- **类型**: `bool`
- **描述**: If enabled, snaps the animation to the closest frame boundary using the import sampling rate

### bImportCustomAttribute
- **类型**: `bool`
- **描述**: If true, import node attributes as either Animation Curves or Animation Attributes

### bDeleteExistingCustomAttributeCurves
- **类型**: `bool`
- **描述**: If true, all previous node attributes imported as Animation Curves will be deleted when doing a re-import.

### bDeleteExistingNonCurveCustomAttributes
- **类型**: `bool`
- **描述**: If true, all previous node attributes imported as Animation Attributes will be deleted when doing a re-import.

### bPreserveLocalTransform
- **类型**: `bool`
- **描述**: Type of asset to import from the FBX file

### bDeleteExistingMorphTargetCurves
- **类型**: `bool`
- **描述**: Type of asset to import from the FBX file

### bUpdateSkeletonReferencePose
- **类型**: `bool`

### bCreatePhysicsAsset
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

### bImportAnimations
- **类型**: `bool`

