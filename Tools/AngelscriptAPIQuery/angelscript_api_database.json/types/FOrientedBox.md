# FOrientedBox

Structure for arbitrarily oriented boxes (i.e. not necessarily axis-aligned).
@note The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\OrientedBox.h

## 属性

### Center
- **类型**: `FVector`
- **描述**: Holds the center of the box.

### AxisX
- **类型**: `FVector`
- **描述**: Holds the x-axis vector of the box. Must be a unit vector.

### AxisY
- **类型**: `FVector`
- **描述**: Holds the y-axis vector of the box. Must be a unit vector.

### AxisZ
- **类型**: `FVector`
- **描述**: Holds the z-axis vector of the box. Must be a unit vector.

### ExtentX
- **类型**: `float`
- **描述**: Holds the extent of the box along its x-axis.

### ExtentY
- **类型**: `float`
- **描述**: Holds the extent of the box along its y-axis.

### ExtentZ
- **类型**: `float`
- **描述**: Holds the extent of the box along its z-axis.

## 方法

### opAssign
```angelscript
FOrientedBox& opAssign(FOrientedBox Other)
```

