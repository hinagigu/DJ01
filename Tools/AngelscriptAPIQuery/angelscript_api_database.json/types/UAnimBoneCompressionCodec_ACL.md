# UAnimBoneCompressionCodec_ACL

**继承自**: `UAnimBoneCompressionCodec_ACLBase`

Uses the open source Animation Compression Library with default settings suitable for general purpose animations.

## 属性

### OptimizationTargets
- **类型**: `TArray<TObjectPtr<USkeletalMesh>>`
- **描述**: The skeletal meshes used to estimate the skinning deformation during compression.

### KeyframeStrippingProportion
- **类型**: `FPerPlatformFloat`
- **描述**: The minimum proportion of keyframes that should be stripped.

### KeyframeStrippingThreshold
- **类型**: `FPerPlatformFloat`
- **描述**: The error threshold below which to strip keyframes. If a keyframe can be reconstructed with an error below the threshold, it is stripped.

