# FChaosClothWeightedValue

## 属性

### Low
- **类型**: `float32`
- **描述**: Parameter value corresponding to the lower bound of the Weight Map.
A Weight Map stores a series of Weight values assigned to each point, all between 0 and 1.
The weights are used to interpolate the individual values from Low to High assigned to each different point.
A Weight of 0 always corresponds to the Low parameter value, and a Weight of 1 to the High parameter value.
The value for Low can be set to be bigger than for High in order to reverse the effect of the Weight Map.

### High
- **类型**: `float32`
- **描述**: Parameter value corresponding to the upper bound of the Weight Map.
A Weight Map stores a series of Weight values assigned to each point, all between 0 and 1.
The weights are used to interpolate the individual values from Low to High assigned to each different point.
A Weight of 0 always corresponds to the Low parameter value, and a Weight of 1 to the High parameter value.
The value for Low can be set to be bigger than for High in order to reverse the effect of the Weight Map.

## 方法

### opAssign
```angelscript
FChaosClothWeightedValue& opAssign(FChaosClothWeightedValue Other)
```

