# FCRSimPointForce

## 属性

### ForceType
- **类型**: `ECRSimPointForceType`
- **描述**: The type of force.

### Vector
- **类型**: `FVector`
- **描述**: The point / direction to use for the force.
This is a direction for direction based forces,
while this is a position for attractor / repel based forces.

### Coefficient
- **类型**: `float32`
- **描述**: The strength of the force (a multiplier for direction based forces)

### bNormalize
- **类型**: `bool`
- **描述**: If set to true the input vector will be normalized.

## 方法

### opAssign
```angelscript
FCRSimPointForce& opAssign(FCRSimPointForce Other)
```

