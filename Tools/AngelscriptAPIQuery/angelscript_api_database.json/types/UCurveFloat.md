# UCurveFloat

**继承自**: `UCurveBase`

## 方法

### GetFloatValue
```angelscript
float32 GetFloatValue(float32 InTime)
```
Evaluate this float curve at the specified time

### AddAutoCurveKey
```angelscript
FCurveKeyHandle AddAutoCurveKey(float32 InTime, float32 InValue)
```

### AddConstantCurveKey
```angelscript
FCurveKeyHandle AddConstantCurveKey(float32 InTime, float32 InValue)
```

### AddCurveKey
```angelscript
FCurveKeyHandle AddCurveKey(float32 InTime, float32 InValue)
```

### AddCurveKeyBrokenTangent
```angelscript
FCurveKeyHandle AddCurveKeyBrokenTangent(float32 InTime, float32 InValue, float32 ArriveTangent, float32 LeaveTangent)
```

### AddCurveKeyTangent
```angelscript
FCurveKeyHandle AddCurveKeyTangent(float32 InTime, float32 InValue, float32 Tangent)
```

### AddCurveKeyWeightedArriveTangent
```angelscript
FCurveKeyHandle AddCurveKeyWeightedArriveTangent(float32 InTime, float32 InValue, bool bBrokenTangent, float32 ArriveTangent, float32 LeaveTangent, float32 ArriveTangentWeight, float32 LeaveTangentWeight)
```

### AddCurveKeyWeightedBothTangent
```angelscript
FCurveKeyHandle AddCurveKeyWeightedBothTangent(float32 InTime, float32 InValue, bool bBrokenTangent, float32 ArriveTangent, float32 LeaveTangent, float32 ArriveTangentWeight, float32 LeaveTangentWeight)
```

### AddCurveKeyWeightedLeaveTangent
```angelscript
FCurveKeyHandle AddCurveKeyWeightedLeaveTangent(float32 InTime, float32 InValue, bool bBrokenTangent, float32 ArriveTangent, float32 LeaveTangent, float32 ArriveTangentWeight, float32 LeaveTangentWeight)
```

### AddLinearCurveKey
```angelscript
FCurveKeyHandle AddLinearCurveKey(float32 InTime, float32 InValue)
```

### AddSmartAutoCurveKey
```angelscript
FCurveKeyHandle AddSmartAutoCurveKey(float32 InTime, float32 InValue)
```

### AutoSetTangents
```angelscript
void AutoSetTangents()
```

### SetDefaultValue
```angelscript
void SetDefaultValue(float32 DefaultValue)
```

### SetKeyInterpMode
```angelscript
void SetKeyInterpMode(FCurveKeyHandle KeyHandle, ERichCurveInterpMode NewInterpMode, bool bAutoSetTangents)
```

### SetKeyTangentMode
```angelscript
void SetKeyTangentMode(FCurveKeyHandle KeyHandle, ERichCurveTangentMode NewTangentMode, bool bAutoSetTangents)
```

### SetKeyTangentWeightMode
```angelscript
void SetKeyTangentWeightMode(FCurveKeyHandle KeyHandle, ERichCurveTangentWeightMode NewTangentWeightMode, bool bAutoSetTangents)
```

### SetKeyUserTangents
```angelscript
void SetKeyUserTangents(FCurveKeyHandle KeyHandle, float32 ArriveTangent, float32 LeaveTangent)
```

### SetKeyUserTangentWeights
```angelscript
void SetKeyUserTangentWeights(FCurveKeyHandle KeyHandle, float32 ArriveTangentWeight, float32 LeaveTangentWeight)
```

### SetPostInfinityExtrap
```angelscript
void SetPostInfinityExtrap(ERichCurveExtrapolation Extrapolation)
```

### SetPreInfinityExtrap
```angelscript
void SetPreInfinityExtrap(ERichCurveExtrapolation Extrapolation)
```

