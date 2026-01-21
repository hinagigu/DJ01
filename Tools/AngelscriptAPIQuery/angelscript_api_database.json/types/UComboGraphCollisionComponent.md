# UComboGraphCollisionComponent

**继承自**: `UActorComponent`

Actor Component providing basic collision detection mechanism for registered meshes using traces.

It implements simple logic for hit detection not meant to replace more robust solutions such as Combat Components or AGR Pro (Combat Manager in v4).

Rather to provide a quick and easy way to handle collision for those not having or not willing to use aforementioned plugins, or not having a game-specific custom collision system already in place.

Registered meshes can be Static or Skeletal meshes, this component relies on Sockets attached to those primitives to draw traces for each socket.

No sub-stepping is involved, we simply draw traces for each frame checking for collisions between last frame position and current frame position for a given socket.

## 属性

### bDebug
- **类型**: `bool`

### bShouldLogHits
- **类型**: `bool`

### TraceColor
- **类型**: `FLinearColor`

### TraceHitColor
- **类型**: `FLinearColor`

### DebugDrawTime
- **类型**: `float32`

### TraceRadius
- **类型**: `float32`

### bTraceComplex
- **类型**: `bool`

### CollisionTraceChannel
- **类型**: `ETraceTypeQuery`

### ActorTypesToIgnore
- **类型**: `TArray<TSubclassOf<AActor>>`

### CollisionProfilesToIgnore
- **类型**: `TArray<FName>`

### OnHitRegistered
- **类型**: `FComboGraphOnHitRegisteredDelegate__ComboGraphCollisionComponent`

### OnTraceStart
- **类型**: `FComboGraphSimpleDelegate__ComboGraphCollisionComponent`

### OnTraceEnd
- **类型**: `FComboGraphSimpleDelegate__ComboGraphCollisionComponent`

## 方法

### RegisterCollisionMesh
```angelscript
void RegisterCollisionMesh(UPrimitiveComponent InMesh)
```
Use this method to push a Static or Skeletal mesh into the registered meshes to consider for collision checks.

Meant to be called at least once either on Owner's Actor BeginPlay or with this component OnComponentActivated event.

### UnregisterCollisionMesh
```angelscript
void UnregisterCollisionMesh(UPrimitiveComponent InMesh)
```
Use this method to remove a Static or Skeletal mesh from the registered meshes

