# FBranchFloatDataflowNode

Branch between two float inputs based on boolean condition

## 属性

### A
- **类型**: `float32`
- **描述**: Float input

### B
- **类型**: `float32`
- **描述**: Float input

### bCondition
- **类型**: `bool`
- **描述**: If true, Output = A, otherwise Output = B

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FBranchFloatDataflowNode& opAssign(FBranchFloatDataflowNode Other)
```

