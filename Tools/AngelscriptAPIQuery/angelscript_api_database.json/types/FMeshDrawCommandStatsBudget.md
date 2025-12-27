# FMeshDrawCommandStatsBudget

Description of a stat category used in the MeshDrawCommandStats system.

## 属性

### CategoryName
- **类型**: `FName`
- **描述**: Category name.

### LinkedStatNames
- **类型**: `TArray<FName>`
- **描述**: Stat names that will match this category name.

### PrimitiveBudget
- **类型**: `int`
- **描述**: The category primitive budget. This is the maximum triangles expected, post-culling, summed across all passes.

### Collection
- **类型**: `int`
- **描述**: The collection which contains this budget.

### Passes
- **类型**: `TArray<FName>`
- **描述**: Which passes contribute to this budget.

## 方法

### opAssign
```angelscript
FMeshDrawCommandStatsBudget& opAssign(FMeshDrawCommandStatsBudget Other)
```

