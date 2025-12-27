# FRigUnit_SpringInterpQuaternionV2

Uses a simple spring model to interpolate a quaternion from Current to Target.

## 属性

### Target
- **类型**: `FQuat`

### Strength
- **类型**: `float32`

### CriticalDamping
- **类型**: `float32`

### Torque
- **类型**: `FVector`

### bUseCurrentInput
- **类型**: `bool`
- **描述**: If true, then the Current input will be used to initialize the state, and is required to be a variable that
holds the current state. If false then the Target value will be used to initialize the state and the Current
input will be ignored/unnecessary as a state will be maintained by this node.

### Current
- **类型**: `FQuat`

### TargetVelocityAmount
- **类型**: `float32`

### bInitializeFromTarget
- **类型**: `bool`
- **描述**: If true, then the initial value will be taken from the target value, and not from the current value.

### Result
- **类型**: `FQuat`
- **描述**: New position of the spring after delta time.

### AngularVelocity
- **类型**: `FVector`
- **描述**: Angular velocity

## 方法

### opAssign
```angelscript
FRigUnit_SpringInterpQuaternionV2& opAssign(FRigUnit_SpringInterpQuaternionV2 Other)
```

