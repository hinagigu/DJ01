# FPositionHistory

An easing type defining how to ease float values.
The FPositionHistory is a container to record position changes
over time. This is used to calculate velocity of a bone, for example.
The FPositionArray also tracks the last index used to allow for
reuse of entries (instead of appending to the array all the time).

## 属性

### Positions
- **类型**: `TArray<FVector>`
- **描述**: The recorded positions

### Range
- **类型**: `float32`
- **描述**: The range for this particular history

## 方法

### opAssign
```angelscript
FPositionHistory& opAssign(FPositionHistory Other)
```

