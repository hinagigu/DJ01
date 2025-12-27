# FRigUnit_BoneHarmonics

Performs point based simulation

## 属性

### Bones
- **类型**: `TArray<FRigUnit_BoneHarmonics_BoneTarget>`
- **描述**: The bones to drive.

### WaveSpeed
- **类型**: `FVector`

### WaveFrequency
- **类型**: `FVector`

### WaveAmplitude
- **类型**: `FVector`

### WaveOffset
- **类型**: `FVector`

### WaveNoise
- **类型**: `FVector`

### WaveEase
- **类型**: `ERigVMAnimEasingType`

### WaveMinimum
- **类型**: `float32`

### WaveMaximum
- **类型**: `float32`

### RotationOrder
- **类型**: `EEulerRotationOrder`

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
FRigUnit_BoneHarmonics& opAssign(FRigUnit_BoneHarmonics Other)
```

