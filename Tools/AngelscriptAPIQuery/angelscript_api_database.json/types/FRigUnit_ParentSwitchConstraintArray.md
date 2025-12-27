# FRigUnit_ParentSwitchConstraintArray

The Parent Switch Constraint is used to have an item follow one of multiple parents,
and allowing to switch between the parent in question.

## 属性

### Subject
- **类型**: `FRigElementKey`

### ParentIndex
- **类型**: `int`

### Parents
- **类型**: `TArray<FRigElementKey>`

### InitialGlobalTransform
- **类型**: `FTransform`

### Weight
- **类型**: `float32`

### Transform
- **类型**: `FTransform`
- **描述**: The transform result (full without weighting)

### Switched
- **类型**: `bool`
- **描述**: Returns true if the parent has changed

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_ParentSwitchConstraintArray& opAssign(FRigUnit_ParentSwitchConstraintArray Other)
```

