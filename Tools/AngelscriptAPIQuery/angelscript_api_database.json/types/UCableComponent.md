# UCableComponent

**继承自**: `UMeshComponent`

Component that allows you to specify custom triangle mesh geometry

## 属性

### bAttachStart
- **类型**: `bool`

### bAttachEnd
- **类型**: `bool`

### AttachEndToSocketName
- **类型**: `FName`
- **描述**: Socket name on the AttachEndTo component to attach to

### EndLocation
- **类型**: `FVector`

### CableLength
- **类型**: `float32`

### NumSegments
- **类型**: `int`

### SubstepTime
- **类型**: `float32`

### SolverIterations
- **类型**: `int`

### bEnableStiffness
- **类型**: `bool`

### bUseSubstepping
- **类型**: `bool`

### bSkipCableUpdateWhenNotVisible
- **类型**: `bool`

### bSkipCableUpdateWhenNotOwnerRecentlyRendered
- **类型**: `bool`

### bEnableCollision
- **类型**: `bool`

### CollisionFriction
- **类型**: `float32`

### CableForce
- **类型**: `FVector`

### CableGravityScale
- **类型**: `float32`

### CableWidth
- **类型**: `float32`

### NumSides
- **类型**: `int`

### TileMaterial
- **类型**: `float32`

## 方法

### GetAttachedActor
```angelscript
AActor GetAttachedActor()
```
Gets the Actor that the cable is attached to *

### GetAttachedComponent
```angelscript
USceneComponent GetAttachedComponent()
```
Gets the specific USceneComponent that the cable is attached to *

### GetCableParticleLocations
```angelscript
void GetCableParticleLocations(TArray<FVector>& Locations)
```
Get array of locations of particles (in world space) making up the cable simulation.

### SetAttachEndTo
```angelscript
void SetAttachEndTo(AActor Actor, FName ComponentProperty, FName SocketName)
```
Attaches the end of the cable to a specific Component within an Actor *

### SetAttachEndToComponent
```angelscript
void SetAttachEndToComponent(USceneComponent Component, FName SocketName)
```
Attaches the end of the cable to a specific Component *

