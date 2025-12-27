# UPatternTool_ScaleSettings

**继承自**: `UInteractiveToolPropertySet`

Settings for Per Element Scale in the Pattern Tool

## 属性

### bProportional
- **类型**: `bool`
- **描述**: If true, changes to Start Scale, End Scale, and Jitter are proportional along all the axes

### bInterpolate
- **类型**: `bool`
- **描述**: If true, Scale is linearly interpolated between StartScale and Scale values

### bJitter
- **类型**: `bool`
- **描述**: If true, Scale at each Pattern Element is offset by a uniformly chosen random value in the range of [-ScaleJitterRange, ScaleJitterRange]

### StartScale
- **类型**: `FVector`
- **描述**: Scale applied to all Pattern Elements, or to first Pattern Element for Interpolated scale

### EndScale
- **类型**: `FVector`
- **描述**: Scale applied to last Pattern Element for Interpolated scale

### Jitter
- **类型**: `FVector`
- **描述**: Upper bound of the range which is sampled to randomly scale each Pattern Element if Jitter is true

