# UPhysicsHandleComponent

**继承自**: `UActorComponent`

Utility object for moving physics objects around.

## 属性

### bSoftAngularConstraint
- **类型**: `bool`

### bSoftLinearConstraint
- **类型**: `bool`

### bInterpolateTarget
- **类型**: `bool`

### LinearDamping
- **类型**: `float32`

### LinearStiffness
- **类型**: `float32`

### AngularDamping
- **类型**: `float32`

### AngularStiffness
- **类型**: `float32`

### InterpolationSpeed
- **类型**: `float32`

## 方法

### GetGrabbedComponent
```angelscript
UPrimitiveComponent GetGrabbedComponent()
```
Returns the currently grabbed component, or null if nothing is grabbed.

### GetTargetLocationAndRotation
```angelscript
void GetTargetLocationAndRotation(FVector& TargetLocation, FRotator& TargetRotation)
```
Get the current location and rotation

### GrabComponentAtLocation
```angelscript
void GrabComponentAtLocation(UPrimitiveComponent Component, FName InBoneName, FVector GrabLocation)
```
Grab the specified component at a given location. Does NOT constraint rotation which means the handle will pivot about GrabLocation.

### GrabComponentAtLocationWithRotation
```angelscript
void GrabComponentAtLocationWithRotation(UPrimitiveComponent Component, FName InBoneName, FVector Location, FRotator Rotation)
```
Grab the specified component at a given location and rotation. Constrains rotation.

### ReleaseComponent
```angelscript
void ReleaseComponent()
```
Release the currently held component

### SetAngularDamping
```angelscript
void SetAngularDamping(float32 NewAngularDamping)
```
Set angular damping

### SetAngularStiffness
```angelscript
void SetAngularStiffness(float32 NewAngularStiffness)
```
Set angular stiffness

### SetInterpolationSpeed
```angelscript
void SetInterpolationSpeed(float32 NewInterpolationSpeed)
```
Set interpolation speed

### SetLinearDamping
```angelscript
void SetLinearDamping(float32 NewLinearDamping)
```
Set linear damping

### SetLinearStiffness
```angelscript
void SetLinearStiffness(float32 NewLinearStiffness)
```
Set linear stiffness

### SetTargetLocation
```angelscript
void SetTargetLocation(FVector NewLocation)
```
Set the target location

### SetTargetLocationAndRotation
```angelscript
void SetTargetLocationAndRotation(FVector NewLocation, FRotator NewRotation)
```
Set target location and rotation

### SetTargetRotation
```angelscript
void SetTargetRotation(FRotator NewRotation)
```
Set the target rotation

