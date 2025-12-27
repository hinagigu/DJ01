# FChaosBreakEvent

## 属性

### Component
- **类型**: `UPrimitiveComponent`
- **描述**: primitive component involved in the break event

### Location
- **类型**: `FVector`
- **描述**: World location of the break

### Velocity
- **类型**: `FVector`
- **描述**: Linear Velocity of the breaking particle

### AngularVelocity
- **类型**: `FVector`
- **描述**: Angular Velocity of the breaking particle

### Extents
- **类型**: `FVector`
- **描述**: Extents of the bounding box

### Mass
- **类型**: `float32`
- **描述**: Mass of the breaking particle

### Index
- **类型**: `int`
- **描述**: Index of the geometry collection bone if positive

### bFromCrumble
- **类型**: `bool`
- **描述**: Whether the break event originated from a crumble event

## 方法

### opAssign
```angelscript
FChaosBreakEvent& opAssign(FChaosBreakEvent Other)
```

