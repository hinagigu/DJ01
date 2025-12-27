# FRigUnit_FullbodyIK

Based on Jacobian solver at core, this can solve multi chains within a root using multi effectors

## 属性

### Root
- **类型**: `FRigElementKey`
- **描述**: The first bone in the chain to solve

### Effectors
- **类型**: `TArray<FFBIKEndEffector>`

### Constraints
- **类型**: `TArray<FFBIKConstraintOption>`

### SolverProperty
- **类型**: `FSolverInput`

### MotionProperty
- **类型**: `FMotionProcessInput`

### bPropagateToChildren
- **类型**: `bool`

### DebugOption
- **类型**: `FFBIKDebugOption`

### ExecuteContext
- **类型**: `FControlRigExecuteContext`

## 方法

### opAssign
```angelscript
FRigUnit_FullbodyIK& opAssign(FRigUnit_FullbodyIK Other)
```

