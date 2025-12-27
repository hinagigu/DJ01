# FIKFootPelvisPullDownSolver

## 属性

### PelvisAdjustmentInterp
- **类型**: `FVectorRK4SpringInterpolator`
- **描述**: Specifies the spring interpolation parameters applied during pelvis adjustment

### PelvisAdjustmentInterpAlpha
- **类型**: `float`
- **描述**: Specifies an alpha between the original and final adjusted pelvis locations
This is used to retain some degree of the original pelvis motion

### PelvisAdjustmentMaxDistance
- **类型**: `float`
- **描述**: Specifies the maximum displacement the pelvis can be adjusted relative to its original location

### PelvisAdjustmentErrorTolerance
- **类型**: `float`
- **描述**: Specifies the pelvis adjustment distance error that is tolerated for each iteration of the solver

When it is detected that the pelvis adjustment distance is incrementing at a value lower or equal
to this value for each iteration, the solve will halt. Lower values will marginally increase visual
quality at the cost of performance, but may require a higher PelvisAdjustmentMaxIter to be specified

The default value of 0.01 specifies 1 centimeter of error

### PelvisAdjustmentMaxIter
- **类型**: `int`
- **描述**: Specifies the maximum number of iterations to run for the pelvis adjustment solver
Higher iterations will guarantee closer PelvisAdjustmentErrorTolerance convergence at the cost of performance

## 方法

### opAssign
```angelscript
FIKFootPelvisPullDownSolver& opAssign(FIKFootPelvisPullDownSolver Other)
```

