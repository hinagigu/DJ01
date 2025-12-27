# FChaosCrumblingEvent

## 属性

### Component
- **类型**: `UPrimitiveComponent`
- **描述**: primitive component involved in the crumble event

### Location
- **类型**: `FVector`
- **描述**: World location of the crumbling cluster

### Orientation
- **类型**: `FQuat`
- **描述**: World orientation of the crumbling cluster

### LinearVelocity
- **类型**: `FVector`
- **描述**: Linear Velocity of the crumbling cluster

### AngularVelocity
- **类型**: `FVector`
- **描述**: Angular Velocity of the crumbling cluster

### Mass
- **类型**: `float32`
- **描述**: Mass of the crumbling cluster

### LocalBounds
- **类型**: `FBox`
- **描述**: Local bounding box of the crumbling cluster

### Children
- **类型**: `TArray<int>`
- **描述**: List of children indices released (optional : see geometry collection component bCrumblingEventIncludesChildren)

## 方法

### opAssign
```angelscript
FChaosCrumblingEvent& opAssign(FChaosCrumblingEvent Other)
```

