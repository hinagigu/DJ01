# FRadialBoxSettings

## 属性

### StartingAngle
- **类型**: `float32`
- **描述**: At what angle will we place the first element of the wheel?

### bDistributeItemsEvenly
- **类型**: `bool`
- **描述**: Distribute Items evenly in the whole circle. Checking this option ignores AngleBetweenItems

### AngleBetweenItems
- **类型**: `float32`
- **描述**: Amount of Euler degrees that separate each item. Only used when bDistributeItemsEvenly is false

### SectorCentralAngle
- **类型**: `float32`
- **描述**: If we need a section of a radial (for example half-a-radial) we can define a central angle < 360 (180 in case of half-a-radial). Used when bDistributeItemsEvenly is enabled.

## 方法

### opAssign
```angelscript
FRadialBoxSettings& opAssign(FRadialBoxSettings Other)
```

