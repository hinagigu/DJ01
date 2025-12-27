# FBlendSpaceTriangle

This is the runtime representation of a triangle. Each triangle stores its vertices etc in normalized space,
with an index to the original samples.

## 属性

### SampleIndices
- **类型**: `int`
- **描述**: Indices into the samples

### Vertices
- **类型**: `FVector2D`
- **描述**: The vertices are in the normalized space - i.e. in the range 0-1.

## 方法

### opAssign
```angelscript
FBlendSpaceTriangle& opAssign(FBlendSpaceTriangle Other)
```

