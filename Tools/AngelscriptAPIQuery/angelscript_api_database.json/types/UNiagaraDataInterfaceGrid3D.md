# UNiagaraDataInterfaceGrid3D

**继承自**: `UNiagaraDataInterfaceRWBase`

## 属性

### ClearBeforeNonIterationStage
- **类型**: `bool`
- **描述**: Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
and accumulate values.

### NumCells
- **类型**: `FIntVector`
- **描述**: Number of cells

### CellSize
- **类型**: `float32`
- **描述**: World space size of a cell

### NumCellsMaxAxis
- **类型**: `int`
- **描述**: Number of cells on the longest axis

### SetResolutionMethod
- **类型**: `ESetResolutionMethod`
- **描述**: Method for setting the grid resolution

### WorldBBoxSize
- **类型**: `FVector`
- **描述**: World size of the grid

