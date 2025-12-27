# FRotationRetargetingInfo

The FRotationRetargetingInfo is used to provide all of the
settings required to perform rotational retargeting on a single
transform.

## 属性

### bEnabled
- **类型**: `bool`
- **描述**: Set to true this enables retargeting

### Source
- **类型**: `FTransform`
- **描述**: The source transform of the frame of reference. The rotation is made relative to this space

### Target
- **类型**: `FTransform`
- **描述**: The target transform to project the rotation. In most cases this is the same as Source

### RotationComponent
- **类型**: `ERotationComponent`
- **描述**: The rotation component to perform retargeting with

### TwistAxis
- **类型**: `FVector`
- **描述**: In case the rotation component is SwingAngle or TwistAngle this vector is used as the twist axis

### bUseAbsoluteAngle
- **类型**: `bool`
- **描述**: If set to true the angle will be always positive, thus resulting in mirrored rotation both ways

### SourceMinimum
- **类型**: `float32`
- **描述**: The minimum value of the source angle in degrees

### SourceMaximum
- **类型**: `float32`
- **描述**: The maximum value of the source angle in degrees

### TargetMinimum
- **类型**: `float32`
- **描述**: The minimum value of the target angle in degrees (can be the same as SourceMinimum)

### TargetMaximum
- **类型**: `float32`
- **描述**: The target value of the target angle in degrees (can be the same as SourceMaximum)

### EasingType
- **类型**: `EEasingFuncType`
- **描述**: The easing to use - pick linear if you don't want to apply any easing

### CustomCurve
- **类型**: `FRuntimeFloatCurve`
- **描述**: Custom curve mapping to apply if bApplyCustomCurve is true

### bFlipEasing
- **类型**: `bool`
- **描述**: If set to true the interpolation value for the easing will be flipped (1.0 - Value)

### EasingWeight
- **类型**: `float32`
- **描述**: The amount of easing to apply (value should be 0.0 to 1.0)

### bClamp
- **类型**: `bool`
- **描述**: If set to true the value for the easing will be clamped between 0.0 and 1.0

## 方法

### opAssign
```angelscript
FRotationRetargetingInfo& opAssign(FRotationRetargetingInfo Other)
```

