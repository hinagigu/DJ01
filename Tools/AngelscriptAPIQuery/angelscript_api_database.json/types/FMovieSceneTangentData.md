# FMovieSceneTangentData

Tangents for curve channel control points.

## 属性

### ArriveTangent
- **类型**: `float32`
- **描述**: If RCIM_Cubic, the arriving tangent at this key

### LeaveTangent
- **类型**: `float32`
- **描述**: If RCIM_Cubic, the leaving tangent at this key

### ArriveTangentWeight
- **类型**: `float32`
- **描述**: If RCTWM_WeightedArrive or RCTWM_WeightedBoth, the weight of the left tangent

### LeaveTangentWeight
- **类型**: `float32`
- **描述**: If RCTWM_WeightedLeave or RCTWM_WeightedBoth, the weight of the right tangent

### TangentWeightMode
- **类型**: `ERichCurveTangentWeightMode`
- **描述**: If RCIM_Cubic, the tangent weight mode

## 方法

### opAssign
```angelscript
FMovieSceneTangentData& opAssign(FMovieSceneTangentData Other)
```

