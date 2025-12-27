# UAnimBoneCompressionCodec_ACLCustom

**继承自**: `UAnimBoneCompressionCodec_ACLBase`

Uses the open source Animation Compression Library with custom settings suitable for debugging purposes.

## 属性

### RotationFormat
- **类型**: `ACLRotationFormat`
- **描述**: The rotation format to use.

### TranslationFormat
- **类型**: `ACLVectorFormat`
- **描述**: The translation format to use.

### ScaleFormat
- **类型**: `ACLVectorFormat`
- **描述**: The scale format to use.

### OptimizationTargets
- **类型**: `TArray<USkeletalMesh>`
- **描述**: The skeletal meshes used to estimate the skinning deformation during compression.

### KeyframeStrippingProportion
- **类型**: `FPerPlatformFloat`
- **描述**: The minimum proportion of keyframes that should be stripped.

### KeyframeStrippingThreshold
- **类型**: `FPerPlatformFloat`
- **描述**: The error threshold below which to strip keyframes. If a keyframe can be reconstructed with an error below the threshold, it is stripped.

