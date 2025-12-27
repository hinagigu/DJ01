# UControlRigNumericalValidationPass

**继承自**: `UControlRigValidationPass`

Used to perform a numerical comparison of the poses

## 属性

### bCheckControls
- **类型**: `bool`
- **描述**: If set to true the pass will validate the poses of all bones

### bCheckBones
- **类型**: `bool`
- **描述**: If set to true the pass will validate the poses of all bones

### bCheckCurves
- **类型**: `bool`
- **描述**: If set to true the pass will validate the values of all curves

### TranslationPrecision
- **类型**: `float32`
- **描述**: The threshold under which we'll ignore a precision issue in the pass

### RotationPrecision
- **类型**: `float32`
- **描述**: The threshold under which we'll ignore a precision issue in the pass (in degrees)

### ScalePrecision
- **类型**: `float32`
- **描述**: The threshold under which we'll ignore a precision issue in the pass

### CurvePrecision
- **类型**: `float32`
- **描述**: The threshold under which we'll ignore a precision issue in the pass

