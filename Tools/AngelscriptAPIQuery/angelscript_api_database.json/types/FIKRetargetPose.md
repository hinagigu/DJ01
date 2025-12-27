# FIKRetargetPose

## 属性

### RootTranslationOffset
- **类型**: `FVector`
- **描述**: a translational delta in GLOBAL space, applied only to the retarget root bone

### BoneRotationOffsets
- **类型**: `TMap<FName,FQuat>`
- **描述**: these are LOCAL-space rotation deltas to be applied to a bone to modify it's retarget pose

## 方法

### opAssign
```angelscript
FIKRetargetPose& opAssign(FIKRetargetPose Other)
```

