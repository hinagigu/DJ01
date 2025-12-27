# FRigVMFunction_MathTransformAccumulateArray

Treats the provided transforms as a chain with global / local transforms, and
projects each transform into the target space. Optionally you can provide
a custom parent indices array, with which you can represent more than just chains.

## 属性

### Transforms
- **类型**: `TArray<FTransform>`

### TargetSpace
- **类型**: `ERigVMTransformSpace`

### Root
- **类型**: `FTransform`

### ParentIndices
- **类型**: `TArray<int>`

### ExecuteContext
- **类型**: `FRigVMExecuteContext`

## 方法

### opAssign
```angelscript
FRigVMFunction_MathTransformAccumulateArray& opAssign(FRigVMFunction_MathTransformAccumulateArray Other)
```

