# UPatternTool_RotationSettings

**继承自**: `UInteractiveToolPropertySet`

Settings for Per Element Rotation in the Pattern Tool

## 属性

### bInterpolate
- **类型**: `bool`
- **描述**: If true, Rotation is linearly interpolated between StartRotation and Rotation values

### bJitter
- **类型**: `bool`
- **描述**: If true, Rotation at each Pattern Element is offset by a uniformly chosen random value in the range of [-RotationJitterRange, RotationJitterRange]

### StartRotation
- **类型**: `FRotator`
- **描述**: Rotation applied to all Pattern Elements, or to first Pattern Element for Interpolated rotation

### EndRotation
- **类型**: `FRotator`
- **描述**: Rotation applied to last Pattern Elements for Interpolated rotation

### Jitter
- **类型**: `FRotator`
- **描述**: Upper bound of the range which is sampled to randomly rotate each Pattern Element if Jitter is true

