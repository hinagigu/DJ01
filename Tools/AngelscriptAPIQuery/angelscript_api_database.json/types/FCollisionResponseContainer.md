# FCollisionResponseContainer

Container for indicating a set of collision channels that this object will collide with.

## 属性

### WorldStatic
- **类型**: `ECollisionResponse`

### WorldDynamic
- **类型**: `ECollisionResponse`

### Pawn
- **类型**: `ECollisionResponse`

### Visibility
- **类型**: `ECollisionResponse`

### Camera
- **类型**: `ECollisionResponse`

### PhysicsBody
- **类型**: `ECollisionResponse`

### Vehicle
- **类型**: `ECollisionResponse`

### Destructible
- **类型**: `ECollisionResponse`

### EngineTraceChannel1
- **类型**: `ECollisionResponse`

### EngineTraceChannel2
- **类型**: `ECollisionResponse`

### EngineTraceChannel3
- **类型**: `ECollisionResponse`

### EngineTraceChannel4
- **类型**: `ECollisionResponse`

### EngineTraceChannel5
- **类型**: `ECollisionResponse`

### EngineTraceChannel6
- **类型**: `ECollisionResponse`

### GameTraceChannel1
- **类型**: `ECollisionResponse`

### GameTraceChannel2
- **类型**: `ECollisionResponse`

### GameTraceChannel3
- **类型**: `ECollisionResponse`

### GameTraceChannel4
- **类型**: `ECollisionResponse`

### GameTraceChannel5
- **类型**: `ECollisionResponse`

### GameTraceChannel6
- **类型**: `ECollisionResponse`

### GameTraceChannel7
- **类型**: `ECollisionResponse`

### GameTraceChannel8
- **类型**: `ECollisionResponse`

### GameTraceChannel9
- **类型**: `ECollisionResponse`

### GameTraceChannel10
- **类型**: `ECollisionResponse`

### GameTraceChannel11
- **类型**: `ECollisionResponse`

### GameTraceChannel12
- **类型**: `ECollisionResponse`

### GameTraceChannel13
- **类型**: `ECollisionResponse`

### GameTraceChannel14
- **类型**: `ECollisionResponse`

### GameTraceChannel15
- **类型**: `ECollisionResponse`

### GameTraceChannel16
- **类型**: `ECollisionResponse`

### GameTraceChannel17
- **类型**: `ECollisionResponse`

### GameTraceChannel18
- **类型**: `ECollisionResponse`

## 方法

### SetResponse
```angelscript
bool SetResponse(ECollisionChannel Channel, ECollisionResponse NewResponse)
```

### SetAllChannels
```angelscript
bool SetAllChannels(ECollisionResponse NewResponse)
```

### ReplaceChannels
```angelscript
bool ReplaceChannels(ECollisionResponse OldResponse, ECollisionResponse NewResponse)
```

### GetResponse
```angelscript
ECollisionResponse GetResponse(ECollisionChannel Channel)
```

### opEquals
```angelscript
bool opEquals(FCollisionResponseContainer Other)
```

### opAssign
```angelscript
FCollisionResponseContainer& opAssign(FCollisionResponseContainer Other)
```

