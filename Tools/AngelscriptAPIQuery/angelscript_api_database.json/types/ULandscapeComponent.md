# ULandscapeComponent

**继承自**: `UPrimitiveComponent`

## 属性

### SectionBaseX
- **类型**: `int`
- **描述**: X offset from global components grid origin (in quads)

### SectionBaseY
- **类型**: `int`
- **描述**: Y offset from global components grid origin (in quads)

### OverrideMaterial
- **类型**: `UMaterialInterface`

### OverrideHoleMaterial
- **类型**: `UMaterialInterface`

### PerLODOverrideMaterials
- **类型**: `TArray<FLandscapePerLODMaterialOverride>`

### CollisionMipLevel
- **类型**: `int`
- **描述**: Heightfield mipmap used to generate collision

### SimpleCollisionMipLevel
- **类型**: `int`
- **描述**: Heightfield mipmap used to generate simple collision

### NegativeZBoundsExtension
- **类型**: `float32`
- **描述**: Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example
Extension value in the negative Z axis, positive value increases bound size

### PositiveZBoundsExtension
- **类型**: `float32`
- **描述**: Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example
Extension value in the positive Z axis, positive value increases bound size

### StaticLightingResolution
- **类型**: `float32`
- **描述**: StaticLightingResolution overriding per component, default value 0 means no overriding

### LightingLODBias
- **类型**: `int`
- **描述**: LOD level Bias to use when lighting building via lightmass, -1 Means automatic LOD calculation based on ForcedLOD + LODBias

### LayerAllowList
- **类型**: `TArray<TObjectPtr<ULandscapeLayerInfoObject>>`
- **描述**: List of layers allowed to be painted on this component

### ForcedLOD
- **类型**: `int`

### LODBias
- **类型**: `int`

## 方法

### EditorGetPaintLayerWeightAtLocation
```angelscript
float32 EditorGetPaintLayerWeightAtLocation(FVector InLocation, ULandscapeLayerInfoObject PaintLayer)
```
Gets the landscape paint layer weight value at the given position using LandscapeLayerInfo . Returns 0 in case it fails.

### EditorGetPaintLayerWeightByNameAtLocation
```angelscript
float32 EditorGetPaintLayerWeightByNameAtLocation(FVector InLocation, FName InPaintLayerName)
```
Gets the landscape paint layer weight value at the given position using layer name. Returns 0 in case it fails.

### GetMaterialInstanceDynamic
```angelscript
UMaterialInstanceDynamic GetMaterialInstanceDynamic(int InIndex)
```
Gets the landscape material instance dynamic for this component

### SetForcedLOD
```angelscript
void SetForcedLOD(int InForcedLOD)
```

### SetLODBias
```angelscript
void SetLODBias(int InLODBias)
```

