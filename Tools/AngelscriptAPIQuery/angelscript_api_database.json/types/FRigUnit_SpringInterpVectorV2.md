# FRigUnit_SpringInterpVectorV2

Uses a simple spring model to interpolate a vector from Current to Target.

## 属性

### Target
- **类型**: `FVector`

### Strength
- **类型**: `float32`

### CriticalDamping
- **类型**: `float32`

### Force
- **类型**: `FVector`

### bUseCurrentInput
- **类型**: `bool`
- **描述**: If true, then the Current input will be used to initialize the state, and is required to be a variable that
holds the current state. If false then the Target value will be used to initialize the state and the Current
input will be ignored/unnecessary as a state will be maintained by this node.

### Current
- **类型**: `FVector`

### TargetVelocityAmount
- **类型**: `float32`

### bInitializeFromTarget
- **类型**: `bool`
- **描述**: If true, then the initial value will be taken from the target value, and not from the current value.

### Result
- **类型**: `FVector`
- **描述**: New position of the spring after delta time.

### Velocity
- **类型**: `FVector`
- **描述**: Velocity

## 方法

### opAssign
```angelscript
FRigUnit_SpringInterpVectorV2& opAssign(FRigUnit_SpringInterpVectorV2 Other)
```

