# FRigUnit_CollectionLoop

Given a collection of items, execute iteratively across all items in a given collection

## 属性

### Collection
- **类型**: `FRigElementKeyCollection`

### Item
- **类型**: `FRigElementKey`

### Index
- **类型**: `int`

### Count
- **类型**: `int`

### Ratio
- **类型**: `float32`
- **描述**: Ranging from 0.0 (first item) and 1.0 (last item)
This is useful to drive a consecutive node with a
curve or an ease to distribute a value.

### Completed
- **类型**: `FControlRigExecuteContext`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_CollectionLoop& opAssign(FRigUnit_CollectionLoop Other)
```

