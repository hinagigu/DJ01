# FAnimationCurveData

Structure encapsulating animated curve data. Currently only contains Float and Transform curves.

## 属性

### FloatCurves
- **类型**: `TArray<FFloatCurve>`
- **描述**: Float-based animation curves

### TransformCurves
- **类型**: `TArray<FTransformCurve>`
- **描述**: FTransform-based animation curves, used for animation layer editing

## 方法

### opAssign
```angelscript
FAnimationCurveData& opAssign(FAnimationCurveData Other)
```

