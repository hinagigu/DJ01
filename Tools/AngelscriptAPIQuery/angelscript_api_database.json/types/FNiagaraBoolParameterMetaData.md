# FNiagaraBoolParameterMetaData

## 属性

### DisplayMode
- **类型**: `ENiagaraBoolDisplayMode`
- **描述**: The mode used determines the cases in which a bool parameter is displayed.
If set to DisplayAlways, both True and False cases will display.
If set to DisplayIfTrue, it will only display if the bool evaluates to True.

### OverrideNameTrue
- **类型**: `FName`
- **描述**: If specified, this name will be used for the given bool if it evaluates to True.

### OverrideNameFalse
- **类型**: `FName`
- **描述**: If specified, this name will be used for the given bool if it evaluates to False.

### IconOverrideTrue
- **类型**: `UTexture2D`
- **描述**: If specified, this icon will be used for the given bool if it evaluates to True. If OverrideName isn't empty, the icon takes priority.

### IconOverrideFalse
- **类型**: `UTexture2D`
- **描述**: If specified, this icon will be used for the given bool if it evaluates to False. If OverrideName isn't empty, the icon takes priority.

## 方法

### opAssign
```angelscript
FNiagaraBoolParameterMetaData& opAssign(FNiagaraBoolParameterMetaData Other)
```

