# UNiagaraDataInterfaceGrid2D

**继承自**: `UNiagaraDataInterfaceRWBase`

## 属性

### ClearBeforeNonIterationStage
- **类型**: `bool`
- **描述**: Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
and accumulate values.

### NumCellsX
- **类型**: `int`
- **描述**: Number of cells in X

### NumCellsY
- **类型**: `int`
- **描述**: Number of cells in Y

### NumCellsMaxAxis
- **类型**: `int`
- **描述**: Number of cells on the longest axis

### NumAttributes
- **类型**: `int`
- **描述**: Number of Attributes

### SetGridFromMaxAxis
- **类型**: `bool`
- **描述**: Set grid resolution according to longest axis

### WorldBBoxSize
- **类型**: `FVector2D`
- **描述**: World size of the grid

