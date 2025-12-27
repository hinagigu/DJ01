# FAnimNode_CopyPoseFromMesh

Simple controller to copy a bone's transform to another one.

## 属性

### SourceMeshComponent
- **类型**: `TWeakObjectPtr<USkeletalMeshComponent>`
- **描述**: This is used by default if it's valid

### bCopyCustomAttributes
- **类型**: `bool`

### RootBoneToCopy
- **类型**: `FName`

### bUseAttachedParent
- **类型**: `bool`

### bCopyCurves
- **类型**: `bool`

### bUseMeshPose
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_CopyPoseFromMesh& opAssign(FAnimNode_CopyPoseFromMesh Other)
```

