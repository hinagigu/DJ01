# UDJ01CameraMode

**继承自**: `UObject`

UDJ01CameraMode

     Base class for all camera modes.

## 属性

### CameraTypeTag
- **类型**: `FGameplayTag`
- **描述**: A tag that can be queried by gameplay code that cares when a kind of camera mode is active
without having to ask about a specific mode (e.g., when aiming downsights to get more accuracy)

### FieldOfView
- **类型**: `float32`
- **描述**: The horizontal field of view (in degrees).

### ViewPitchMin
- **类型**: `float32`
- **描述**: Minimum view pitch (in degrees).

### ViewPitchMax
- **类型**: `float32`
- **描述**: Maximum view pitch (in degrees).

### BlendTime
- **类型**: `float32`
- **描述**: How long it takes to blend in this mode.

### BlendFunction
- **类型**: `EDJ01CameraModeBlendFunction`
- **描述**: Function used for blending.

### BlendExponent
- **类型**: `float32`
- **描述**: Exponent used by blend functions to control the shape of the curve.

