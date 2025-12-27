# FDJ01ComboBufferedInput

FDJ01ComboBufferedInput

缓冲的输入条目 - 用于连招系统

## 属性

### AbilityTag
- **类型**: `FGameplayTag`
- **描述**: 请求激活的技能Tag

### Priority
- **类型**: `int`
- **描述**: 技能优先级 (数值越小优先级越高)

### InputTime
- **类型**: `float32`
- **描述**: 输入时间戳

### BufferDuration
- **类型**: `float32`
- **描述**: 缓冲有效期 (秒)

### ComboIndex
- **类型**: `int`
- **描述**: 当前连段索引

### InputDirection
- **类型**: `FVector2D`
- **描述**: 输入方向 (用于方向技)

## 方法

### opAssign
```angelscript
FDJ01ComboBufferedInput& opAssign(FDJ01ComboBufferedInput Other)
```

