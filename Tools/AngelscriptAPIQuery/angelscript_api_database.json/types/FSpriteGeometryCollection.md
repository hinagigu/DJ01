# FSpriteGeometryCollection

## 属性

### Shapes
- **类型**: `TArray<FSpriteGeometryShape>`
- **描述**: List of shapes

### GeometryType
- **类型**: `ESpritePolygonMode`
- **描述**: The geometry type (automatic / manual)

### PixelsPerSubdivisionX
- **类型**: `int`
- **描述**: Size of a single subdivision (in pixels) in X (for Diced mode)

### PixelsPerSubdivisionY
- **类型**: `int`
- **描述**: Size of a single subdivision (in pixels) in Y (for Diced mode)

### bAvoidVertexMerging
- **类型**: `bool`
- **描述**: Experimental: Hint to the triangulation routine that extra vertices should be preserved

### AlphaThreshold
- **类型**: `float32`
- **描述**: Alpha threshold for a transparent pixel (range 0..1, anything equal or below this value will be considered unimportant)

### DetailAmount
- **类型**: `float32`
- **描述**: Amount to detail to consider when shrink-wrapping (range 0..1, 0 = low detail, 1 = high detail)

### SimplifyEpsilon
- **类型**: `float32`
- **描述**: This is the threshold below which multiple vertices will be merged together when doing shrink-wrapping.  Higher values result in fewer vertices.

## 方法

### opAssign
```angelscript
FSpriteGeometryCollection& opAssign(FSpriteGeometryCollection Other)
```

