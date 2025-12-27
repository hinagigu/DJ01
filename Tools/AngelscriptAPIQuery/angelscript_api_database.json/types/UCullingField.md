# UCullingField

**继承自**: `UFieldNodeBase`

Evaluate the input field according to the result of the culling field

## 属性

### Culling
- **类型**: `const UFieldNodeBase`

### Field
- **类型**: `const UFieldNodeBase`

### Operation
- **类型**: `EFieldCullingOperationType`

## 方法

### SetCullingField
```angelscript
UCullingField SetCullingField(const UFieldNodeBase Culling, const UFieldNodeBase Field, EFieldCullingOperationType Operation)
```
Evaluate the input field according to the result of the culling field.

@param    Culling Culling field to be used.
@param    Field Input field that will be evaluated according to the culling field result.
@param    Operation Evaluate the input field if the result of the culling field is equal to 0 (Inside) or different from 0 (Outside).

