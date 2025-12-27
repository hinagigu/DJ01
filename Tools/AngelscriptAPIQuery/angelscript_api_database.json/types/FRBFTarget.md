# FRBFTarget

Data about a particular target in the RBF, including scaling factor

## 属性

### ScaleFactor
- **类型**: `float32`
- **描述**: How large the influence of this target.

### bApplyCustomCurve
- **类型**: `bool`
- **描述**: Whether we want to apply an additional custom curve when activating this target.
          Ignored if the solver type is Interpolative.

### CustomCurve
- **类型**: `FRichCurve`
- **描述**: Custom curve to apply to activation of this target, if bApplyCustomCurve is true.
              Ignored if the solver type is Interpolative.

### DistanceMethod
- **类型**: `ERBFDistanceMethod`
- **描述**: Override the distance method used to calculate the distance from this target to
              the input. Ignored if the solver type is Interpolative.

### FunctionType
- **类型**: `ERBFFunctionType`
- **描述**: Override the falloff function used to smooth the distance from this target to
              the input. Ignored if the solver type is Interpolative.

### Values
- **类型**: `TArray<float32>`
- **描述**: Set of values for this target, size must be TargetDimensions

## 方法

### opAssign
```angelscript
FRBFTarget& opAssign(FRBFTarget Other)
```

