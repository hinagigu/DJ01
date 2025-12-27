# UPatternTool_TranslationSettings

**继承自**: `UInteractiveToolPropertySet`

Settings for Per Element Translation in the Pattern Tool

## 属性

### bInterpolate
- **类型**: `bool`
- **描述**: If true, Translation is linearly interpolated between StartTranslation and Translation values

### bJitter
- **类型**: `bool`
- **描述**: If true, Translation at each Pattern Element is offset by a uniformly chosen random value in the range of [-TranslationJitterRange, TranslationJitterRange]

### StartTranslation
- **类型**: `FVector`
- **描述**: Translation applied to all Pattern Elements, or to first Pattern Element for Interpolated translation

### EndTranslation
- **类型**: `FVector`
- **描述**: Translation applied to last Pattern Element for Interpolated translation

### Jitter
- **类型**: `FVector`
- **描述**: Upper bound of the range which is sampled to randomly translate each Pattern Element if Jitter is true

