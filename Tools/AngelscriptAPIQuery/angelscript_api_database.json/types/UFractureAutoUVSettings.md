# UFractureAutoUVSettings

**继承自**: `UFractureToolSettings`

Settings for UV layout and texture baking on the geometry collection *

## 属性

### UVChannel
- **类型**: `FString`
- **描述**: Which UV channel to use for layout and baking

### ProjectionScale
- **类型**: `FVector`
- **描述**: The scale factor to use for UV box projection

### bAutoFitToBounds
- **类型**: `bool`
- **描述**: Set the scale factor for UV box projection based on the bounding box of the geometry

### bUniformProjectionScale
- **类型**: `bool`
- **描述**: Ensure the projection scale is the same on each axis, either by repeating the X Axis scale, or using the max box dimension if Auto Fit to Bounds is selected.

### ProjectionUVOffset
- **类型**: `FVector2D`
- **描述**: UV Offset to apply after UV box projection

### bCenterAtPivot
- **类型**: `bool`
- **描述**: Optionally center the UV projection around the object pivot

### TargetFaces
- **类型**: `ETargetFaces`
- **描述**: Choose whether to target internal faces, or a custom selection

### MaterialIDs
- **类型**: `TArray<int>`
- **描述**: Custom selection of material IDs to target for texturing

### Resolution
- **类型**: `EAutoUVTextureResolution`
- **描述**: The pixel resolution of the generated map

### GutterSize
- **类型**: `int`
- **描述**: Approximate space to leave between UV islands, measured in texels

### bPromptToSave
- **类型**: `bool`
- **描述**: Whether to prompt user for an asset name for each generated texture, or automatically place them next to the source Geometry Collections

### bReplaceExisting
- **类型**: `bool`
- **描述**: Whether to allow the new texture to overwrite an existing texture

### BakeTextureType
- **类型**: `ETextureType`
- **描述**: Which standard set of texture channels to bake

### bDistToOuter
- **类型**: `bool`
- **描述**: Bake the distance to the external surface to a texture channel (red)

### bAmbientOcclusion
- **类型**: `bool`
- **描述**: Bake the ambient occlusion of each bone (considered separately) to a texture channel (green)

### bSmoothedCurvature
- **类型**: `bool`
- **描述**: Bake a smoothed curvature metric to a texture channel (blue)
Specifically, this is the mean curvature of a smoothed copy of each fractured piece, baked back to the respective fracture piece
Note that this attribute is relatively expensive to compute

### MaxDistance
- **类型**: `float`
- **描述**: Max distance to search for the outer mesh surface

### OcclusionRays
- **类型**: `int`
- **描述**: Number of occlusion rays

### OcclusionBlurRadius
- **类型**: `float`
- **描述**: Pixel Radius of Gaussian Blur Kernel applied to AO map (0 will apply no blur)

### CurvatureBlurRadius
- **类型**: `float`
- **描述**: Pixel Radius of Gaussian Blur Kernel applied to Curvature map (0 will apply no blur)

### VoxelResolution
- **类型**: `int`
- **描述**: Voxel resolution of smoothed shape representation

### SmoothingIterations
- **类型**: `int`
- **描述**: Amount of smoothing iterations to apply before computing curvature

### ThicknessFactor
- **类型**: `float`
- **描述**: Distance to search for correspondence between fractured shape and smoothed shape, as factor of voxel size

### MaxCurvature
- **类型**: `float`
- **描述**: Curvatures in the range [-MaxCurvature, MaxCurvature] will be mapped from [0,1]. Values outside that range will be clamped

