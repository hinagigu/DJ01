# FAnimGraphBlendOptions

Blending options for animation graphs in Linked Animation Blueprints.

## 属性

### BlendInTime
- **类型**: `float32`
- **描述**: Time to blend this graph in using Inertialization. Specify -1.0 to defer to the BlendOutTime of the previous graph.
To blend this graph in you must place an Inertialization node after the Linked Anim Graph node or Linked Anim Layer node that uses this graph.

### BlendInProfile
- **类型**: `UBlendProfile`
- **描述**: Optional blend profile to use when blending this graph in (if BlendInTime > 0)

### BlendOutTime
- **类型**: `float32`
- **描述**: Time to blend this graph out using Inertialization. Specify -1.0 to defer to the BlendInTime of the next graph.
To blend this graph out you must place an Inertialization node after the Linked Anim Graph node or Linked Anim Layer node that uses this graph.

### BlendOutProfile
- **类型**: `UBlendProfile`
- **描述**: Optional blend profile to use when blending this graph out (if BlendOutTime > 0)

## 方法

### opAssign
```angelscript
FAnimGraphBlendOptions& opAssign(FAnimGraphBlendOptions Other)
```

