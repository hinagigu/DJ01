# UPlanarReflectionComponent

**继承自**: `USceneCaptureComponent`

UPlanarReflectionComponent

## 属性

### NormalDistortionStrength
- **类型**: `float32`
- **描述**: Controls the strength of normals when distorting the planar reflection.

### PrefilterRoughness
- **类型**: `float32`
- **描述**: The roughness value to prefilter the planar reflection texture with, useful for hiding low resolution.  Larger values have larger GPU cost.

### PrefilterRoughnessDistance
- **类型**: `float32`
- **描述**: The distance at which the prefilter roughness value will be achieved.

### ScreenPercentage
- **类型**: `int`
- **描述**: Downsample percent, can be used to reduce GPU time rendering the planar reflection.

### ExtraFOV
- **类型**: `float32`
- **描述**: Additional FOV used when rendering to the reflection texture.
This is useful when normal distortion is causing reads outside the reflection texture.
Larger values increase rendering thread and GPU cost, as more objects and triangles have to be rendered into the planar reflection.

### DistanceFromPlaneFadeoutStart
- **类型**: `float32`
- **描述**: Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection.

### DistanceFromPlaneFadeoutEnd
- **类型**: `float32`
- **描述**: Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection.

### AngleFromPlaneFadeStart
- **类型**: `float32`
- **描述**: Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection.

### AngleFromPlaneFadeEnd
- **类型**: `float32`
- **描述**: Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection.

### bShowPreviewPlane
- **类型**: `bool`

### bRenderSceneTwoSided
- **类型**: `bool`
- **描述**: Whether to render the scene as two-sided, which can be useful to hide artifacts where normal distortion would read 'under' an object that has been clipped by the reflection plane.
With this setting enabled, the backfaces of a mesh would be displayed in the clipped region instead of the background which is potentially a bright sky.
Be sure to add the water plane to HiddenActors if enabling this, as the water plane will now block the reflection.

