# FRandomPlayerSequenceEntry

The random player node holds a list of sequences and parameter ranges which will be played continuously
In a random order. If shuffle mode is enabled then each entry will be played once before repeating any

## 属性

### Sequence
- **类型**: `UAnimSequenceBase`

### ChanceToPlay
- **类型**: `float32`

### MinLoopCount
- **类型**: `int`

### MaxLoopCount
- **类型**: `int`

### MinPlayRate
- **类型**: `float32`

### MaxPlayRate
- **类型**: `float32`

### BlendIn
- **类型**: `FAlphaBlend`
- **描述**: Blending properties used when this entry is blending in ontop of another entry

## 方法

### opAssign
```angelscript
FRandomPlayerSequenceEntry& opAssign(FRandomPlayerSequenceEntry Other)
```

