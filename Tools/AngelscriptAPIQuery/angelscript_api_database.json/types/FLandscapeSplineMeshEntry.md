# FLandscapeSplineMeshEntry

## 属性

### Mesh
- **类型**: `UStaticMesh`
- **描述**: Mesh to use on the spline

### MaterialOverrides
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`
- **描述**: Overrides mesh's materials

### CenterAdjust
- **类型**: `FVector2D`
- **描述**: Tweak to center the mesh correctly on the spline

### Scale
- **类型**: `FVector`
- **描述**: Scale of the spline mesh, (Z=Forwards)

### ForwardAxis
- **类型**: `ESplineMeshAxis`
- **描述**: Chooses the forward axis for the spline mesh orientation

### UpAxis
- **类型**: `ESplineMeshAxis`
- **描述**: Chooses the up axis for the spline mesh orientation

### bCenterH
- **类型**: `bool`

### bScaleToWidth
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FLandscapeSplineMeshEntry& opAssign(FLandscapeSplineMeshEntry Other)
```

