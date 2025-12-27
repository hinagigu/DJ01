# FChaosVDJointsDebugDrawSettings

## 属性

### DepthPriority
- **类型**: `ESceneDepthPriorityGroup`
- **描述**: The depth priority used for while drawing data. Can be World or Foreground (with this one the shapes will be drawn on top of the geometry and be always visible)

### LinearImpulseScale
- **类型**: `float32`
- **描述**: Scale to apply to the Linear Impulse vector before draw it.

### AngularImpulseScale
- **类型**: `float32`
- **描述**: Scale to apply to the Angular Impulse vector before draw it.

### GeneralScale
- **类型**: `float32`
- **描述**: Scale to apply to anything that does not have a dedicated scale setting before draw it.

### BaseLineThickness
- **类型**: `float32`
- **描述**: Line thickness to use as a base to calculate the different line thickness values used to debug draw the data.

### CenterOfMassSize
- **类型**: `float32`
- **描述**: Size of the debug drawn Center Of Mass.

### ConstraintAxisLength
- **类型**: `float32`
- **描述**: Size of the debug drawn if the Constraint Axis

## 方法

### opAssign
```angelscript
FChaosVDJointsDebugDrawSettings& opAssign(FChaosVDJointsDebugDrawSettings Other)
```

