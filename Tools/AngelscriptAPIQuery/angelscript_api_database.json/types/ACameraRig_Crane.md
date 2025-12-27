# ACameraRig_Crane

**继承自**: `AActor`

A simple rig for simulating crane-like camera movements.

## 属性

### CranePitch
- **类型**: `float32`

### CraneYaw
- **类型**: `float32`

### CraneArmLength
- **类型**: `float32`

### bLockMountPitch
- **类型**: `bool`

### bLockMountYaw
- **类型**: `bool`

### TransformComponent
- **类型**: `USceneComponent`
- **描述**: Root component to give the whole actor a transform.

### CraneYawControl
- **类型**: `USceneComponent`
- **描述**: Component to control Yaw.

### CranePitchControl
- **类型**: `USceneComponent`
- **描述**: Component to control Pitch.

### CraneCameraMount
- **类型**: `USceneComponent`
- **描述**: Component to define the attach point for cameras.

