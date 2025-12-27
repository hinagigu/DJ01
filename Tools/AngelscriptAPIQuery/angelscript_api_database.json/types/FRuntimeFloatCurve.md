# FRuntimeFloatCurve

## 属性

### ExternalCurve
- **类型**: `UCurveFloat`

## 方法

### AddDefaultKey
```angelscript
void AddDefaultKey(float32 InTime, float32 InValue)
```

### Equals
```angelscript
bool Equals(FRuntimeFloatCurve Other)
```

### GetFloatValue
```angelscript
float32 GetFloatValue(float32 InTime, float32 DefaultValue)
```
Evaluate this float curve at the specified time

### GetNumKeys
```angelscript
int GetNumKeys()
```

### GetTimeRange
```angelscript
void GetTimeRange(float32& MinTime, float32& MaxTime)
```

### GetTimeRange
```angelscript
void GetTimeRange(float& MinTime, float& MaxTime)
```

### GetValueRange
```angelscript
void GetValueRange(float32& MinValue, float32& MaxValue)
```

### GetValueRange
```angelscript
void GetValueRange(float& MinValue, float& MaxValue)
```

### opAssign
```angelscript
FRuntimeFloatCurve& opAssign(FRuntimeFloatCurve Other)
```

