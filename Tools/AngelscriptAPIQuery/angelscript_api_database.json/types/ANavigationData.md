# ANavigationData

**继承自**: `AActor`

Represents abstract Navigation Data (sub-classed as NavMesh, NavGraph, etc)
Used as a common interface for all navigation types handled by NavigationSystem

## 属性

### RuntimeGeneration
- **类型**: `ERuntimeGenerationType`
- **描述**: Navigation data runtime generation options

### ObservedPathsTickInterval
- **类型**: `float32`
- **描述**: all observed paths will be processed every ObservedPathsTickInterval seconds

### bEnableDrawing
- **类型**: `bool`

### bForceRebuildOnLoad
- **类型**: `bool`

### bAutoDestroyWhenNoNavigation
- **类型**: `bool`

### bCanBeMainNavData
- **类型**: `bool`

