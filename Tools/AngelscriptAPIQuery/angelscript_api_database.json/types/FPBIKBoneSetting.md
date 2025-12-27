# FPBIKBoneSetting

## 属性

### Bone
- **类型**: `FName`
- **描述**: The Bone that these settings will be applied to.

### RotationStiffness
- **类型**: `float32`
- **描述**: Range is 0 to 1 (Default is 0). At higher values, the bone will resist rotating (forcing other bones to compensate).

### PositionStiffness
- **类型**: `float32`
- **描述**: Range is 0 to 1 (Default is 0). At higher values, the bone will resist translational motion (forcing other bones to compensate).

### X
- **类型**: `EPBIKLimitType`
- **描述**: Limit the rotation angle of the bone on the X axis.
Free: can rotate freely in this axis.
Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
Locked: no rotation is allowed in this axis (will remain at reference pose angle).

### MinX
- **类型**: `float32`
- **描述**: Range is -180 to 0 (Default is 0). Degrees of rotation in the negative X direction to allow when joint is in "Limited" mode.

### MaxX
- **类型**: `float32`
- **描述**: Range is 0 to 180 (Default is 0). Degrees of rotation in the positive X direction to allow when joint is in "Limited" mode.

### Y
- **类型**: `EPBIKLimitType`
- **描述**: Limit the rotation angle of the bone on the Y axis.
Free: can rotate freely in this axis.
Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
Locked: no rotation is allowed in this axis (will remain at input pose angle).

### MinY
- **类型**: `float32`
- **描述**: Range is -180 to 0 (Default is 0). Degrees of rotation in the negative Y direction to allow when joint is in "Limited" mode.

### MaxY
- **类型**: `float32`
- **描述**: Range is 0 to 180 (Default is 0). Degrees of rotation in the positive Y direction to allow when joint is in "Limited" mode.

### Z
- **类型**: `EPBIKLimitType`
- **描述**: Limit the rotation angle of the bone on the Z axis.
Free: can rotate freely in this axis.
Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
Locked: no rotation is allowed in this axis (will remain at input pose angle).

### MinZ
- **类型**: `float32`
- **描述**: Range is -180 to 0 (Default is 0). Degrees of rotation in the negative Z direction to allow when joint is in "Limited" mode.

### MaxZ
- **类型**: `float32`
- **描述**: Range is 0 to 180 (Default is 0). Degrees of rotation in the positive Z direction to allow when joint is in "Limited" mode.

### bUsePreferredAngles
- **类型**: `bool`
- **描述**: When true, this bone will "prefer" to rotate in the direction specified by the Preferred Angles when the chain it belongs to is compressed.
Preferred Angles should be the first method used to fix bones that bend in the wrong direction (rather than limits).
The resulting angles can be visualized on their own by temporarily setting the Solver iterations to 0 and moving the effectors.

### PreferredAngles
- **类型**: `FVector`
- **描述**: The local Euler angles (in degrees) used to rotate this bone when the chain it belongs to is squashed.
This happens by moving the effector at the tip of the chain towards the root of the chain.
This can be used to coerce knees and elbows to bend in the anatomically "correct" direction without resorting to limits (which may require more iterations to converge).

## 方法

### opAssign
```angelscript
FPBIKBoneSetting& opAssign(FPBIKBoneSetting Other)
```

