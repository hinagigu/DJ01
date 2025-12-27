# UAnimBoneCompressionCodec_ACLDatabase

**继承自**: `UAnimBoneCompressionCodec_ACLBase`

Uses the open source Animation Compression Library with default settings and database support.
The referenced database can be used to strip the least important keyframes on a per platform basis
or they can be streamed in/out on demand through Blueprint or C++.

## 属性

### DatabaseAsset
- **类型**: `UAnimationCompressionLibraryDatabase`
- **描述**: The database asset that will hold the compressed animation data.

### OptimizationTargets
- **类型**: `TArray<TObjectPtr<USkeletalMesh>>`
- **描述**: The skeletal meshes used to estimate the skinning deformation during compression.

