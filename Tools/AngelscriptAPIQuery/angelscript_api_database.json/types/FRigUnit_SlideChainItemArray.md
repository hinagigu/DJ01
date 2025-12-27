# FRigUnit_SlideChainItemArray

Slides an existing chain along itself with control over extrapolation.

## 属性

### Items
- **类型**: `TArray<FRigElementKey>`

### SlideAmount
- **类型**: `float32`

### bPropagateToChildren
- **类型**: `bool`
- **描述**: If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_SlideChainItemArray& opAssign(FRigUnit_SlideChainItemArray Other)
```

