# FSplineMeshParams

Structure that holds info about spline, passed to renderer to deform UStaticMesh.
Also used by Lightmass, so be sure to update Lightmass::FSplineMeshParams and the static lighting code if this changes!

## 属性

### StartPos
- **类型**: `FVector`
- **描述**: Start location of spline, in component space.

### StartTangent
- **类型**: `FVector`
- **描述**: Start tangent of spline, in component space.

### StartScale
- **类型**: `FVector2D`
- **描述**: X and Y scale applied to mesh at start of spline.

### StartRoll
- **类型**: `float32`
- **描述**: Roll around spline applied at start, in radians.

### StartOffset
- **类型**: `FVector2D`
- **描述**: Starting offset of the mesh from the spline, in component space.

### EndPos
- **类型**: `FVector`
- **描述**: End location of spline, in component space.

### EndScale
- **类型**: `FVector2D`
- **描述**: X and Y scale applied to mesh at end of spline.

### EndTangent
- **类型**: `FVector`
- **描述**: End tangent of spline, in component space.

### EndRoll
- **类型**: `float32`
- **描述**: Roll around spline applied at end, in radians.

### EndOffset
- **类型**: `FVector2D`
- **描述**: Ending offset of the mesh from the spline, in component space.

### NaniteClusterBoundsScale
- **类型**: `float32`
- **描述**: How much to scale the calculated culling bounds of Nanite clusters after deformation.
NOTE: This should only be set greater than 1.0 if it fixes visible issues with clusters being
incorrectly culled.

## 方法

### opAssign
```angelscript
FSplineMeshParams& opAssign(FSplineMeshParams Other)
```

