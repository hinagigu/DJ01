# FCRSimLinearSpring

## 属性

### SubjectA
- **类型**: `int`
- **描述**: The first point affected by this spring

### SubjectB
- **类型**: `int`
- **描述**: The second point affected by this spring

### Coefficient
- **类型**: `float32`
- **描述**: The power of this spring

### Equilibrium
- **类型**: `float32`
- **描述**: The rest length of this spring.
A value of lower than zero indicates that the equilibrium
should be based on the current distance of the two subjects.

## 方法

### opAssign
```angelscript
FCRSimLinearSpring& opAssign(FCRSimLinearSpring Other)
```

