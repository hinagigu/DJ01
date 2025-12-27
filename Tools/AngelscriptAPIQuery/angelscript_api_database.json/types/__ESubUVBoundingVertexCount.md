# __ESubUVBoundingVertexCount

More bounding vertices results in reduced overdraw, but adds more triangle overhead.
The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,
and when the particles using the texture will be few and large.

## 属性

### BVC_FourVertices
- **类型**: `ESubUVBoundingVertexCount`

### BVC_EightVertices
- **类型**: `ESubUVBoundingVertexCount`

### BVC_MAX
- **类型**: `ESubUVBoundingVertexCount`

