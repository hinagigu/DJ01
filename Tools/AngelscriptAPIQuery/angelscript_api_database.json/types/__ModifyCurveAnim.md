# __ModifyCurveAnim

## 方法

### ConvertToModifyCurveNode
```angelscript
FModifyCurveAnimNodeReference ConvertToModifyCurveNode(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a modify curve node context from an anim node context

### ConvertToModifyCurveNodePure
```angelscript
void ConvertToModifyCurveNodePure(FAnimNodeReference Node, FModifyCurveAnimNodeReference& ModifyCurveNode, bool& Result)
```
Get a modify curve context from an anim node context (pure)

### GetAlpha
```angelscript
float32 GetAlpha(FModifyCurveAnimNodeReference ModifyCurveNode)
```

### GetApplyMode
```angelscript
EModifyCurveApplyMode GetApplyMode(FModifyCurveAnimNodeReference ModifyCurveNode)
```

### SetAlpha
```angelscript
FModifyCurveAnimNodeReference SetAlpha(FModifyCurveAnimNodeReference ModifyCurveNode, float32 InAlpha)
```

### SetApplyMode
```angelscript
FModifyCurveAnimNodeReference SetApplyMode(FModifyCurveAnimNodeReference ModifyCurveNode, EModifyCurveApplyMode InMode)
```

### SetCurveMap
```angelscript
FModifyCurveAnimNodeReference SetCurveMap(FModifyCurveAnimNodeReference ModifyCurveNode, TMap<FName,float32> InCurveMap)
```

