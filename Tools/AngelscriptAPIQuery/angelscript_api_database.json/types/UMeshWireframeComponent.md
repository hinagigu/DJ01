# UMeshWireframeComponent

**继承自**: `UMeshComponent`

UMeshWireframeComponent draws a mesh wireframe as lines, with line color/thickness
varying depending on line type and the configuration settings.
Currently can draw:
   - all mesh edges
   - boundary edges
   - UV seam edges
   - Normal seam edges
   - Color seam edges

Client must provide a IMeshWireframeSourceProvider implementation that provides the
edge set, vertices, and edge type

## 属性

### LineDepthBias
- **类型**: `float32`
- **描述**: Depth bias of the lines, used to offset in depth to avoid z-fighting

### LineDepthBiasSizeScale
- **类型**: `float32`
- **描述**: Target-size depth bias scale. This is multiplied by LineDepthBias.
Client of UMeshWireframeComponent can set this if desired, eg to fraction of target object bounding box size, etc.

### ThicknessScale
- **类型**: `float32`
- **描述**: Scaling factor applied to the per-edge-type thicknesses defined below

### bEnableWireframe
- **类型**: `bool`
- **描述**: Wireframe properties

### WireframeColor
- **类型**: `FColor`

### WireframeThickness
- **类型**: `float32`

### bEnableBoundaryEdges
- **类型**: `bool`
- **描述**: Boundary Edge properties

### BoundaryEdgeColor
- **类型**: `FColor`

### BoundaryEdgeThickness
- **类型**: `float32`

### bEnableUVSeams
- **类型**: `bool`
- **描述**: UV seam properties

### UVSeamColor
- **类型**: `FColor`

### UVSeamThickness
- **类型**: `float32`

### bEnableNormalSeams
- **类型**: `bool`
- **描述**: normal seam properties

### NormalSeamColor
- **类型**: `FColor`

### NormalSeamThickness
- **类型**: `float32`

### bEnableTangentSeams
- **类型**: `bool`
- **描述**: tangent seam properties

### TangentSeamColor
- **类型**: `FColor`

### TangentSeamThickness
- **类型**: `float32`

### bEnableColorSeams
- **类型**: `bool`
- **描述**: color seam properties

### ColorSeamColor
- **类型**: `FColor`

### ColorSeamThickness
- **类型**: `float32`

