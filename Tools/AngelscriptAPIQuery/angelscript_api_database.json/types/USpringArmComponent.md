# USpringArmComponent

**继承自**: `USceneComponent`

This component tries to maintain its children at a fixed distance from the parent,
but will retract the children if there is a collision, and spring back when there is no collision.

Example: Use as a 'camera boom' or 'selfie stick' to keep the follow camera for a player from colliding into the world.

## 属性

### TargetArmLength
- **类型**: `float32`

### SocketOffset
- **类型**: `FVector`

### TargetOffset
- **类型**: `FVector`

### ProbeSize
- **类型**: `float32`

### ProbeChannel
- **类型**: `ECollisionChannel`

### CameraLagSpeed
- **类型**: `float32`

### CameraRotationLagSpeed
- **类型**: `float32`

### CameraLagMaxTimeStep
- **类型**: `float32`

### CameraLagMaxDistance
- **类型**: `float32`

### bDoCollisionTest
- **类型**: `bool`

### bUsePawnControlRotation
- **类型**: `bool`

### bInheritPitch
- **类型**: `bool`

### bInheritYaw
- **类型**: `bool`

### bInheritRoll
- **类型**: `bool`

### bEnableCameraLag
- **类型**: `bool`

### bEnableCameraRotationLag
- **类型**: `bool`

### bUseCameraLagSubstepping
- **类型**: `bool`

### bDrawDebugLagMarkers
- **类型**: `bool`

### bClampToMaxPhysicsDeltaTime
- **类型**: `bool`

## 方法

### GetTargetRotation
```angelscript
FRotator GetTargetRotation()
```
Get the target rotation we inherit, used as the base target for the boom rotation.
This is derived from attachment to our parent and considering the UsePawnControlRotation and absolute rotation flags.

### GetUnfixedCameraPosition
```angelscript
FVector GetUnfixedCameraPosition()
```
Get the position where the camera should be without applying the Collision Test displacement

### IsCollisionFixApplied
```angelscript
bool IsCollisionFixApplied()
```
Is the Collision Test displacement being applied?

