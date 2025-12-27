# FNiagaraEnumParameterMetaData

Defines override data for enum parameters displayed in the UI.

## 属性

### OverrideName
- **类型**: `FName`
- **描述**: If specified, this name will be used for the given enum entry. Useful for shortening names.

### IconOverride
- **类型**: `UTexture2D`
- **描述**: If specified, this icon will be used for the given enum entry. If OverrideName isn't empty, the icon takes priority.

### bUseColorOverride
- **类型**: `bool`

### ColorOverride
- **类型**: `FLinearColor`

## 方法

### opAssign
```angelscript
FNiagaraEnumParameterMetaData& opAssign(FNiagaraEnumParameterMetaData Other)
```

