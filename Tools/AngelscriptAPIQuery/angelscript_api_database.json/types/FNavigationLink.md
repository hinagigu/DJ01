# FNavigationLink

## 属性

### Left
- **类型**: `FVector`

### Right
- **类型**: `FVector`

### LeftProjectHeight
- **类型**: `float32`
- **描述**: if greater than 0 nav system will attempt to project navlink's start point on geometry below

### MaxFallDownLength
- **类型**: `float32`
- **描述**: if greater than 0 nav system will attempt to project navlink's end point on geometry below

### SnapRadius
- **类型**: `float32`

### SnapHeight
- **类型**: `float32`

### SupportedAgents
- **类型**: `FNavAgentSelector`
- **描述**: restrict area only to specified agents

### Description
- **类型**: `FString`
- **描述**: this is an editor-only property to put descriptions in navlinks setup, to be able to identify it easier

### Direction
- **类型**: `ENavLinkDirection`

### AreaClass
- **类型**: `TSubclassOf<UNavAreaBase>`
- **描述**: Area type of this link (empty = default)

### bUseSnapHeight
- **类型**: `bool`

### bSnapToCheapestArea
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNavigationLink& opAssign(FNavigationLink Other)
```

