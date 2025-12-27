# UStaticMeshComponent

**继承自**: `UMeshComponent`

StaticMeshComponent is used to create an instance of a UStaticMesh.
A static mesh is a piece of geometry that consists of a static set of polygons.

@see https://docs.unrealengine.com/latest/INT/Engine/Content/Types/StaticMeshes/
@see UStaticMesh

## 属性

### MinLOD
- **类型**: `int`

### WireframeColorOverride
- **类型**: `FColor`

### OverriddenLightMapRes
- **类型**: `int`

### DistanceFieldIndirectShadowMinVisibility
- **类型**: `float32`

### StreamingDistanceMultiplier
- **类型**: `float32`

### LightmassSettings
- **类型**: `FLightmassPrimitiveSettings`
- **描述**: The Lightmass settings for this object.

### ForcedLodModel
- **类型**: `int`

### StaticMesh
- **类型**: `UStaticMesh`

### bForceNaniteForMasked
- **类型**: `bool`

### bDisallowNanite
- **类型**: `bool`

### bEvaluateWorldPositionOffset
- **类型**: `bool`

### bWorldPositionOffsetWritesVelocity
- **类型**: `bool`

### bEvaluateWorldPositionOffsetInRayTracing
- **类型**: `bool`

### WorldPositionOffsetDisableDistance
- **类型**: `int`

### bOverrideWireframeColor
- **类型**: `bool`

### bOverrideMinLOD
- **类型**: `bool`

### bDisallowMeshPaintPerInstance
- **类型**: `bool`

### bIgnoreInstanceForTextureStreaming
- **类型**: `bool`

### bOverrideLightMapRes
- **类型**: `bool`

### bCastDistanceFieldIndirectShadow
- **类型**: `bool`

### bOverrideDistanceFieldSelfShadowBias
- **类型**: `bool`

### bUseDefaultCollision
- **类型**: `bool`

### bSortTriangles
- **类型**: `bool`

### bReverseCulling
- **类型**: `bool`

### DistanceFieldSelfShadowBias
- **类型**: `float32`

## 方法

### GetInitialEvaluateWorldPositionOffset
```angelscript
bool GetInitialEvaluateWorldPositionOffset()
```
Get the initial value of bEvaluateWorldPositionOffset. This is the value when BeginPlay() was last called, or if UpdateInitialEvaluateWorldPositionOffset is called.

### GetLocalBounds
```angelscript
void GetLocalBounds(FVector& Min, FVector& Max)
```
Get Local bounds

### SetDistanceFieldSelfShadowBias
```angelscript
void SetDistanceFieldSelfShadowBias(float32 NewValue)
```
Sets the component's DistanceFieldSelfShadowBias.  bOverrideDistanceFieldSelfShadowBias must be enabled for this to have an effect.

### SetEvaluateWorldPositionOffset
```angelscript
void SetEvaluateWorldPositionOffset(bool NewValue)
```

### SetEvaluateWorldPositionOffsetInRayTracing
```angelscript
void SetEvaluateWorldPositionOffsetInRayTracing(bool NewValue)
```

### SetForceDisableNanite
```angelscript
void SetForceDisableNanite(bool bInForceDisableNanite)
```
Force disabling of Nanite rendering. When true, Will swap to the the fallback mesh instead.

### SetForcedLodModel
```angelscript
void SetForcedLodModel(int NewForcedLodModel)
```

### SetReverseCulling
```angelscript
void SetReverseCulling(bool ReverseCulling)
```
Set forced reverse culling

### SetStaticMesh
```angelscript
bool SetStaticMesh(UStaticMesh NewMesh)
```
Change the StaticMesh used by this instance.

### SetWorldPositionOffsetDisableDistance
```angelscript
void SetWorldPositionOffsetDisableDistance(int NewValue)
```

### UpdateInitialEvaluateWorldPositionOffset
```angelscript
void UpdateInitialEvaluateWorldPositionOffset()
```
This manually updates the initial value of bEvaluateWorldPositionOffset to be the current value.
    This is useful if the default value of bEvaluateWorldPositionOffset is changed after constructing
    the component.

