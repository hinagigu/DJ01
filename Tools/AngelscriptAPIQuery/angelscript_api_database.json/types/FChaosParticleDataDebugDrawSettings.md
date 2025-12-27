# FChaosParticleDataDebugDrawSettings

## 属性

### DepthPriority
- **类型**: `ESceneDepthPriorityGroup`
- **描述**: The depth priority used for while drawing contact data. Can be World or Foreground (with this one the shapes will be drawn on top of the geometry and be always visible)

### VelocityScale
- **类型**: `float32`
- **描述**: Scale to apply to the Velocity vector before draw it. Unit is cm/s

### AngularVelocityScale
- **类型**: `float32`
- **描述**: Scale to apply to the Angular Velocity vector before draw it. Unit is rad/s

### AccelerationScale
- **类型**: `float32`
- **描述**: Scale to apply to the Acceleration vector before draw it. Unit is cm/s2

### AngularAccelerationScale
- **类型**: `float32`
- **描述**: Scale to apply to the Angular Acceleration vector before draw it. Unit is rad/s2

### LinearImpulseScale
- **类型**: `float32`
- **描述**: Scale to apply to the Linear Impulse vector before draw it. Unit is g.m/s

### AngularImpulseScale
- **类型**: `float32`
- **描述**: Scale to apply to the Angular Impulse vector before draw it. Unit is g.m2/s

### CenterOfMassRadius
- **类型**: `float32`
- **描述**: Radius to use when creating the sphere that will represent the center of mass location

### ColorSettings
- **类型**: `FChaosParticleDataDebugDrawColors`

## 方法

### opAssign
```angelscript
FChaosParticleDataDebugDrawSettings& opAssign(FChaosParticleDataDebugDrawSettings Other)
```

