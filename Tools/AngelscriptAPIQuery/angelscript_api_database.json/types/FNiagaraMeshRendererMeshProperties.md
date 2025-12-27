# FNiagaraMeshRendererMeshProperties

## 属性

### Mesh
- **类型**: `UStaticMesh`
- **描述**: The mesh to use when rendering this slot

### MeshParameterBinding
- **类型**: `FNiagaraParameterBinding`
- **描述**: Binding to supported mesh types.

### LODMode
- **类型**: `ENiagaraMeshLODMode`

### LODLevelBinding
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: Absolute LOD level to use

### LODBiasBinding
- **类型**: `FNiagaraParameterBindingWithValue`
- **描述**: LOD bias to apply to the LOD calculation.

### LODDistanceFactor
- **类型**: `float32`
- **描述**: Used in LOD calculation to modify the distance, i.e. increasing the value will make lower poly LODs transition closer to the camera.

### bUseLODRange
- **类型**: `bool`
- **描述**: When enabled you can restrict the LOD range we consider for LOD calculation.
This can be useful to reduce the performance impact, as it reduces the number of draw calls required.

### LODRange
- **类型**: `FIntVector2`
- **描述**: Used to restrict the range of LODs we include when dynamically calculating the LOD level.

### Scale
- **类型**: `FVector`
- **描述**: Scale of the mesh

### Rotation
- **类型**: `FRotator`
- **描述**: Rotation of the mesh

### PivotOffset
- **类型**: `FVector`
- **描述**: Offset of the mesh pivot

### PivotOffsetSpace
- **类型**: `ENiagaraMeshPivotOffsetSpace`
- **描述**: What space is the pivot offset in?

## 方法

### opAssign
```angelscript
FNiagaraMeshRendererMeshProperties& opAssign(FNiagaraMeshRendererMeshProperties Other)
```

