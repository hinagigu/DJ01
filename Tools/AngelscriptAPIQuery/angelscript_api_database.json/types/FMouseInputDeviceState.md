# FMouseInputDeviceState

Current State of a physical Mouse device at a point in time.

## 属性

### Left
- **类型**: `FDeviceButtonState`
- **描述**: State of the left mouse button

### Middle
- **类型**: `FDeviceButtonState`
- **描述**: State of the middle mouse button

### Right
- **类型**: `FDeviceButtonState`
- **描述**: State of the right mouse button

### WheelDelta
- **类型**: `float32`
- **描述**: Change in 'ticks' of the mouse wheel since last state event

### Position2D
- **类型**: `FVector2D`
- **描述**: Current 2D position of the mouse, in application-defined coordinate system

### Delta2D
- **类型**: `FVector2D`
- **描述**: Change in 2D mouse position from last state event

### WorldRay
- **类型**: `FRay`
- **描述**: Ray into current 3D scene at current 2D mouse position

## 方法

### opAssign
```angelscript
FMouseInputDeviceState& opAssign(FMouseInputDeviceState Other)
```

