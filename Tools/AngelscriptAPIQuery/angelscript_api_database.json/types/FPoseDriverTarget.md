# FPoseDriverTarget

Information about each target in the PoseDriver

## 属性

### BoneTransforms
- **类型**: `TArray<FPoseDriverTransform>`
- **描述**: Translation of this target

### TargetRotation
- **类型**: `FRotator`
- **描述**: Rotation of this target

### TargetScale
- **类型**: `float32`
- **描述**: Scale applied to this target's function - a larger value will activate this target sooner

### DistanceMethod
- **类型**: `ERBFDistanceMethod`
- **描述**: Override for the distance method to use for each target

### FunctionType
- **类型**: `ERBFFunctionType`
- **描述**: Override for the function method to use for each target

### bApplyCustomCurve
- **类型**: `bool`
- **描述**: If we should apply a custom curve mapping to how this target activates

### CustomCurve
- **类型**: `FRichCurve`
- **描述**: Custom curve mapping to apply if bApplyCustomCurve is true

### DrivenName
- **类型**: `FName`
- **描述**: Name of item to drive - depends on DriveOutput setting.
If DriveOutput is DrivePoses, this should be the name of a pose in the assigned PoseAsset
If DriveOutput is DriveCurves, this is the name of the curve (morph target, material param etc) to drive

### bIsHidden
- **类型**: `bool`
- **描述**: If we should hide this pose from the UI

## 方法

### opAssign
```angelscript
FPoseDriverTarget& opAssign(FPoseDriverTarget Other)
```

