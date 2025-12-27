# AGeometryCollectionRenderLevelSetActor

**继承自**: `AActor`

AGeometryCollectionRenderLevelSetActor
An actor representing the collection of data necessary to
render volumes.  This references a ray marching material, which
is used internally by a post process component blendable.  This
is a workflow that can be improved with a deeper implementation
in the future if we decide to.  Note that behavior with multiple
render level set actors isn't currently supported very well,
but could be improved in the future

## 属性

### TargetVolumeTexture
- **类型**: `UVolumeTexture`

### RayMarchMaterial
- **类型**: `UMaterial`

### SurfaceTolerance
- **类型**: `float32`

### Isovalue
- **类型**: `float32`

### Enabled
- **类型**: `bool`

### RenderVolumeBoundingBox
- **类型**: `bool`

