# FInputDeviceRay

FInputDeviceRay represents a 3D ray created based on an input device.
If the device is a 2D input device like a mouse, then the ray may
have an associated 2D screen position.

## 属性

### WorldRay
- **类型**: `FRay`
- **描述**: 3D ray in 3D scene, in world coordinates

### bHas2D
- **类型**: `bool`
- **描述**: If true, WorldRay has 2D device position coordinates

### ScreenPosition
- **类型**: `FVector2D`
- **描述**: 2D device position coordinates associated with the ray

## 方法

### opAssign
```angelscript
FInputDeviceRay& opAssign(FInputDeviceRay Other)
```

