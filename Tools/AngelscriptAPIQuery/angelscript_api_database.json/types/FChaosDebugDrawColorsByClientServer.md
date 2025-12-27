# FChaosDebugDrawColorsByClientServer

Structure holding the settings using to debug draw Particles shape based on whether they are client or server objects (in PIE) Chaos Visual Debugger

## 属性

### ServerColor
- **类型**: `FColor`
- **描述**: Color used for server shapes that are not awake or sleeping dynamic

### ServerDynamicColor
- **类型**: `FColor`
- **描述**: Color used for server shapes that are awake dynamic

### ServerSleepingColor
- **类型**: `FColor`
- **描述**: Color used for server shapes that are sleeping dynamics

### ClientColor
- **类型**: `FColor`
- **描述**: Color used for client shapes that are not awake or sleeping dynamic

### ClientDynamicColor
- **类型**: `FColor`
- **描述**: Color used for server shapes that are awake dynamic

### ClientSleepingColor
- **类型**: `FColor`
- **描述**: Color used for client shapes that are sleeping dynamics

## 方法

### opAssign
```angelscript
FChaosDebugDrawColorsByClientServer& opAssign(FChaosDebugDrawColorsByClientServer Other)
```

