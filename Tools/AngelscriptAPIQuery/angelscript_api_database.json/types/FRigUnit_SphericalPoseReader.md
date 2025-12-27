# FRigUnit_SphericalPoseReader

* Outputs a float value between 0-1 based off of the driver item's rotation in a specified region.

## 属性

### OutputParam
- **类型**: `float32`
- **描述**: The normalized output parameter; ranges from 0 (when outside yellow region) to 1 (in the green region) and smoothly blends from 0-1 in the yellow region.

### DriverItem
- **类型**: `FRigElementKey`

### DriverAxis
- **类型**: `FVector`

### RotationOffset
- **类型**: `FVector`

### ActiveRegionSize
- **类型**: `float32`

### ActiveRegionScaleFactors
- **类型**: `FRegionScaleFactors`

### FalloffSize
- **类型**: `float32`

### FalloffRegionScaleFactors
- **类型**: `FRegionScaleFactors`

### FlipWidthScaling
- **类型**: `bool`

### FlipHeightScaling
- **类型**: `bool`

### OptionalParentItem
- **类型**: `FRigElementKey`

### Debug
- **类型**: `FSphericalPoseReaderDebugSettings`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_SphericalPoseReader& opAssign(FRigUnit_SphericalPoseReader Other)
```

