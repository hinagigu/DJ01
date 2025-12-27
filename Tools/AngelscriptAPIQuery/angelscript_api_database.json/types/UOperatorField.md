# UOperatorField

**继承自**: `UFieldNodeBase`

Compute an operation between 2 incoming fields

## 属性

### Magnitude
- **类型**: `float32`

### RightField
- **类型**: `const UFieldNodeBase`

### LeftField
- **类型**: `const UFieldNodeBase`

### Operation
- **类型**: `EFieldOperationType`

## 方法

### SetOperatorField
```angelscript
UOperatorField SetOperatorField(float32 Magnitude, const UFieldNodeBase LeftField, const UFieldNodeBase RightField, EFieldOperationType Operation)
```
Compute an operation between 2 incoming fields
@param    Magnitude Magnitude of the operator field
@param    LeftField Input field A to be processed
@param    RightField Input field B to be processed
@param    Operation Type of math operation you want to perform between the 2 fields

