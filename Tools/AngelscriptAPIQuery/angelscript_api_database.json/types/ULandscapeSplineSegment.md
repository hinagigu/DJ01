# ULandscapeSplineSegment

**继承自**: `UObject`

## 属性

### Connections
- **类型**: `FLandscapeSplineSegmentConnection`
- **描述**: Directly editable data:

### LayerName
- **类型**: `FName`
- **描述**: Name of blend layer to paint when applying spline to landscape
If "none", no layer is painted

### SplineMeshes
- **类型**: `TArray<FLandscapeSplineMeshEntry>`
- **描述**: Spline meshes from this list are used in random order along the spline.

### RandomSeed
- **类型**: `int`
- **描述**: Random seed used for choosing which order to use spline meshes. Ignored if only one mesh is set.

### LDMaxDrawDistance
- **类型**: `float32`
- **描述**: Max draw distance for all the mesh pieces used in this spline

### TranslucencySortPriority
- **类型**: `int`
- **描述**: Translucent objects with a lower sort priority draw behind objects with a higher priority.
Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.
This setting is also used to sort objects being drawn into a runtime virtual texture.

Ignored if the object is not translucent.  The default priority is zero.
Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.

### CustomDepthStencilWriteMask
- **类型**: `ERendererStencilMask`
- **描述**: Mask used for stencil buffer writes.

### CustomDepthStencilValue
- **类型**: `int`
- **描述**: Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)

### RuntimeVirtualTextures
- **类型**: `TArray<TObjectPtr<URuntimeVirtualTexture>>`
- **描述**: Array of runtime virtual textures into which we draw the spline segment.
The material also needs to be set up to output to a virtual texture.

### VirtualTextureLodBias
- **类型**: `int`
- **描述**: Lod bias for rendering to runtime virtual texture.

### VirtualTextureCullMips
- **类型**: `int`
- **描述**: Number of lower mips in the runtime virtual texture to skip for rendering this primitive.
Larger values reduce the effective draw distance in the runtime virtual texture.
This culling method doesn't take into account primitive size or virtual texture size.

### VirtualTextureMainPassMaxDrawDistance
- **类型**: `float32`
- **描述**: Desired cull distance in the main pass if we are rendering to both the virtual texture AND the main pass. A value of 0 has no effect.

### VirtualTextureRenderPassType
- **类型**: `ERuntimeVirtualTextureMainPassType`
- **描述**: Controls if this component draws in the main pass as well as in the virtual texture.

### BodyInstance
- **类型**: `FBodyInstance`

### bRaiseTerrain
- **类型**: `bool`

### bLowerTerrain
- **类型**: `bool`

### bCastShadow
- **类型**: `bool`

### bHiddenInGame
- **类型**: `bool`

### bPlaceSplineMeshesInStreamingLevels
- **类型**: `bool`

### bRenderCustomDepth
- **类型**: `bool`

