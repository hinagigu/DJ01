# FRandomUnitVectorInConeDataflowNode

Returns a random vector with length of 1, within the specified cone, with uniform random distribution

## 属性

### bDeterministic
- **类型**: `bool`

### RandomSeed
- **类型**: `float32`

### ConeDirection
- **类型**: `FVector`
- **描述**: The base "center" direction of the cone

### ConeHalfAngle
- **类型**: `float32`
- **描述**: The half-angle of the cone (from ConeDir to edge), in degrees

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FRandomUnitVectorInConeDataflowNode& opAssign(FRandomUnitVectorInConeDataflowNode Other)
```

