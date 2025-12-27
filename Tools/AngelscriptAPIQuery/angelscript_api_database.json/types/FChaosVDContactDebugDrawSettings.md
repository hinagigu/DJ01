# FChaosVDContactDebugDrawSettings

Structure holding the settings using to debug draw contact data on the Chaos Visual Debugger

## 属性

### DepthPriority
- **类型**: `ESceneDepthPriorityGroup`
- **描述**: The depth priority used for while drawing contact data. Can be World or Foreground (with this one the shapes will be drawn on top of the geometry and be always visible)

### ContactCircleRadius
- **类型**: `float32`
- **描述**: The radius of the debug draw circle used to represent a contact point

### ContactNormalScale
- **类型**: `float32`
- **描述**: The scale value to be applied to the normal vector of a contact used to change its size to make it easier to see

## 方法

### opAssign
```angelscript
FChaosVDContactDebugDrawSettings& opAssign(FChaosVDContactDebugDrawSettings Other)
```

