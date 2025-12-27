# FAnimNode_RetargetPoseFromMesh

## 属性

### SourceMeshComponent
- **类型**: `TWeakObjectPtr<USkeletalMeshComponent>`
- **描述**: The Skeletal Mesh Component to retarget animation from. Assumed to be animated and tick BEFORE this anim instance.

### bUseAttachedParent
- **类型**: `bool`

### IKRetargeterAsset
- **类型**: `UIKRetargeter`

### CustomRetargetProfile
- **类型**: `FRetargetProfile`

### bSuppressWarnings
- **类型**: `bool`

### bCopyCurves
- **类型**: `bool`

### LODThreshold
- **类型**: `int`

### LODThresholdForIK
- **类型**: `int`

## 方法

### opAssign
```angelscript
FAnimNode_RetargetPoseFromMesh& opAssign(FAnimNode_RetargetPoseFromMesh Other)
```

