# FInterpolationParameter

## 属性

### InterpolationTime
- **类型**: `float32`
- **描述**: Smoothing Time used to move smoothly across the blendpsace from the current parameters to the target
parameters. The different Smoothing Types will treat this in different ways, but in general a value of
zero will disable all smoothing, and larger values will smooth more.

### DampingRatio
- **类型**: `float32`
- **描述**: Damping ratio - only used when the type is set to SpringDamper. A value of 1 will move quickly and
smoothly to the target, without overshooting. Values as low as 0 can be used to encourage some overshoot,
and values around 0.7 can make pose transitions look more natural.

### MaxSpeed
- **类型**: `float32`
- **描述**: Maximum speed, in real units. For example, if this axis is degrees then you could use a value of 90 to
limit the turn rate to 90 degrees per second. Only used when greater than zero and the type is
set to SpringDamper or Exponential.

### InterpolationType
- **类型**: `EFilterInterpolationType`
- **描述**: Type of smoothing used for filtering the input value to decide how to get to target.

## 方法

### opAssign
```angelscript
FInterpolationParameter& opAssign(FInterpolationParameter Other)
```

