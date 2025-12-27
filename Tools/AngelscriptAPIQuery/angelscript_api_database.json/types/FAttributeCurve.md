# FAttributeCurve

## 属性

### Keys
- **类型**: `TArray<FAttributeKey>`
- **描述**: The keys, ordered by time

### ScriptStruct
- **类型**: `UScriptStruct`
- **描述**: Transient UScriptStruct instance representing the underlying value type for the curve

### bShouldInterpolate
- **类型**: `bool`
- **描述**: Whether or not to interpolate between keys of ScripStruct type

## 方法

### opAssign
```angelscript
FAttributeCurve& opAssign(FAttributeCurve Other)
```

