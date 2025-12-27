# UDecalComponent

**继承自**: `USceneComponent`

A material that is rendered onto the surface of a mesh. A kind of 'bumper sticker' for a model.

@see https://docs.unrealengine.com/latest/INT/Engine/Actors/DecalActor
@see UDecalActor

## 属性

### DecalSize
- **类型**: `FVector`

### SortOrder
- **类型**: `int`

### FadeScreenSize
- **类型**: `float32`

### FadeStartDelay
- **类型**: `float32`

### FadeDuration
- **类型**: `float32`

### FadeInDuration
- **类型**: `float32`

### FadeInStartDelay
- **类型**: `float32`

### bDestroyOwnerAfterFade
- **类型**: `bool`

### DecalColor
- **类型**: `FLinearColor`

## 方法

### CreateDynamicMaterialInstance
```angelscript
UMaterialInstanceDynamic CreateDynamicMaterialInstance()
```
Utility to allocate a new Dynamic Material Instance, set its parent to the currently applied material, and assign it

### GetDecalMaterial
```angelscript
UMaterialInterface GetDecalMaterial()
```
Accessor for decal material

### GetFadeDuration
```angelscript
float32 GetFadeDuration()
```

### GetFadeInDuration
```angelscript
float32 GetFadeInDuration()
```

### GetFadeInStartDelay
```angelscript
float32 GetFadeInStartDelay()
```

### GetFadeStartDelay
```angelscript
float32 GetFadeStartDelay()
```

### SetDecalColor
```angelscript
void SetDecalColor(FLinearColor Color)
```
Sets the decal color.

### SetDecalMaterial
```angelscript
void SetDecalMaterial(UMaterialInterface NewDecalMaterial)
```
setting decal material on decal component. This will force the decal to reattach

### SetFadeIn
```angelscript
void SetFadeIn(float32 StartDelay, float32 Duration)
```

### SetFadeOut
```angelscript
void SetFadeOut(float32 StartDelay, float32 Duration, bool DestroyOwnerAfterFade)
```
Sets the decal's fade start time, duration and if the owning actor should be destroyed after the decal is fully faded out.
The default value of 0 for FadeStartDelay and FadeDuration makes the decal persistent. See DecalLifetimeOpacity material
node to control the look of "fading out."

@param StartDelay - Time in seconds to wait before beginning to fade out the decal.
@param Duration - Time in second for the decal to fade out.
@param DestroyOwnerAfterFade - Should the owning actor automatically be destroyed after it is completely faded out.

### SetFadeScreenSize
```angelscript
void SetFadeScreenSize(float32 NewFadeScreenSize)
```
Set the FadeScreenSize for this decal component

### SetSortOrder
```angelscript
void SetSortOrder(int Value)
```
Sets the sort order for the decal component. Higher values draw later (on top). This will force the decal to reattach

