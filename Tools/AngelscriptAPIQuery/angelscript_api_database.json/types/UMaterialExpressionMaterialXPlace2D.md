# UMaterialExpressionMaterialXPlace2D

**继承自**: `UMaterialExpression`

Transform incoming UV texture coordinates from one 2D frame of reference to another.
operationorder (integer enum): the order in which to perform the transform operations.
"0" or "SRT" performs -pivot, scale, rotate, translate, +pivot as per the original
implementation matching the behavior of certain DCC packages, and "1" or "TRS" performs
-pivot, translate, rotate, scale, +pivot which does not introduce texture shear.
Default is 0 "SRT" for backward compatibility.

## 属性

### ConstRotationAngle
- **类型**: `float32`
- **描述**: only used if RotationAngle is not hooked up

### ConstCoordinate
- **类型**: `uint8`
- **描述**: only used if Coordinates is not hooked up

