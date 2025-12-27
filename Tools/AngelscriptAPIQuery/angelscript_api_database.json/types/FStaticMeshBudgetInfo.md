# FStaticMeshBudgetInfo

## 属性

### LodGroupName
- **类型**: `FName`
- **描述**: The name of the LOD group we will use for this budget.

### MinimumExtent
- **类型**: `float`
- **描述**: The minimum volume extent to assign this budget info. We will compare the mesh bounding box extent to this value.

## 方法

### opAssign
```angelscript
FStaticMeshBudgetInfo& opAssign(FStaticMeshBudgetInfo Other)
```

