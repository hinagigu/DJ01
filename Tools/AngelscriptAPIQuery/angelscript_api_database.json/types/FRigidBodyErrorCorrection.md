# FRigidBodyErrorCorrection

Rigid body error correction data

## 属性

### PingExtrapolation
- **类型**: `float32`
- **描述**: Value between 0 and 1 which indicates how much velocity
              and ping based correction to use

### PingLimit
- **类型**: `float32`
- **描述**: For the purpose of extrapolation, ping will be clamped to this value

### ErrorPerLinearDifference
- **类型**: `float32`
- **描述**: Error per centimeter

### ErrorPerAngularDifference
- **类型**: `float32`
- **描述**: Error per degree

### MaxRestoredStateError
- **类型**: `float32`
- **描述**: Maximum allowable error for a state to be considered "resolved"

### MaxLinearHardSnapDistance
- **类型**: `float32`

### PositionLerp
- **类型**: `float32`
- **描述**: How much to directly lerp to the correct position. Generally
              this should be very low, if not zero. A higher value will
              increase precision along with jerkiness.

### AngleLerp
- **类型**: `float32`
- **描述**: How much to directly lerp to the correct angle.

### LinearVelocityCoefficient
- **类型**: `float32`
- **描述**: This is the coefficient `k` in the differential equation:
              dx/dt = k ( x_target(t) - x(t) ), which is used to update
              the velocity in a replication step.

### AngularVelocityCoefficient
- **类型**: `float32`
- **描述**: This is the angular analog to LinearVelocityCoefficient.

### ErrorAccumulationSeconds
- **类型**: `float32`
- **描述**: Number of seconds to remain in a heuristically
              unresolveable state before hard snapping.

### ErrorAccumulationDistanceSq
- **类型**: `float32`
- **描述**: If the body has moved less than the square root of
              this amount towards a resolved state in the previous
              frame, then error may accumulate towards a hard snap.

### ErrorAccumulationSimilarity
- **类型**: `float32`
- **描述**: If the previous error projected onto the current error
              is greater than this value (indicating "similarity"
              between states), then error may accumulate towards a
              hard snap.

## 方法

### opAssign
```angelscript
FRigidBodyErrorCorrection& opAssign(FRigidBodyErrorCorrection Other)
```

