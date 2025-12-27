# ULandscapeLayerInfoObject

**继承自**: `UObject`

## 属性

### PhysMaterial
- **类型**: `UPhysicalMaterial`
- **描述**: Physical material to use when this layer is the predominant one at a given location. Note: this is ignored if the Landscape Physical Material node is used in the landscape material.

### Hardness
- **类型**: `float32`
- **描述**: Defines how much 'resistance' areas painted with this layer will offer to the Erosion tool. A hardness of 0 means the layer is fully affected by erosion, while 1 means fully unaffected.

### MinimumCollisionRelevanceWeight
- **类型**: `float32`
- **描述**: The minimum weight that needs to be painted for that layer to be picked up as the dominant physical layer.

### SplineFalloffModulationTexture
- **类型**: `UTexture2D`
- **描述**: Texture to modulate the Splines Falloff Layer Alpha

### SplineFalloffModulationColorMask
- **类型**: `ESplineModulationColorMask`
- **描述**: Defines which channel of the Spline Falloff Modulation Texture to use.

### SplineFalloffModulationTiling
- **类型**: `float32`
- **描述**: Defines the tiling to use when sampling the Spline Falloff Modulation Texture.

### SplineFalloffModulationBias
- **类型**: `float32`
- **描述**: Defines the offset to use when sampling the Spline Falloff Modulation Texture.

### SplineFalloffModulationScale
- **类型**: `float32`
- **描述**: Allows to scale the value sampled from the Spline Falloff Modulation Texture.

### LayerUsageDebugColor
- **类型**: `FLinearColor`
- **描述**: The color to use for layer usage debug

### bNoWeightBlend
- **类型**: `bool`

