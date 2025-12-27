# FNiagaraGeometryCacheReference

## 属性

### GeometryCache
- **类型**: `UGeometryCache`
- **描述**: Reference to the geometry cache asset to use (if the user parameter binding is not set)

### GeometryCacheUserParamBinding
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Use the UGeometryCache bound to this user variable if it is set to a valid value. If this is bound to a valid value and GeometryCache is also set, GeometryCacheUserParamBinding wins.

### OverrideMaterials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`
- **描述**: The materials to be used instead of the GeometryCache's materials. If the GeometryCache requires more materials than exist in this array or any entry in this array is set to None, we will use the GeometryCache's existing material instead.

## 方法

### opAssign
```angelscript
FNiagaraGeometryCacheReference& opAssign(FNiagaraGeometryCacheReference Other)
```

