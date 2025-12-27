# FBrushToolRadius

FBrushToolRadius is used to define the size of 3D "brushes" used in (eg) sculpting tools.
The brush size can be defined in various ways.

## 属性

### SizeType
- **类型**: `EBrushToolSizeType`
- **描述**: Specify the type of brush size currently in use

### AdaptiveSize
- **类型**: `float32`
- **描述**: Adaptive brush size is used to interpolate between an object-specific minimum and maximum brush size

### WorldRadius
- **类型**: `float32`
- **描述**: World brush size is a dimension in world coordinates

## 方法

### opAssign
```angelscript
FBrushToolRadius& opAssign(FBrushToolRadius Other)
```

