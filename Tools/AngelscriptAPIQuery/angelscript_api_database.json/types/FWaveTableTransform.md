# FWaveTableTransform

## 属性

### Curve
- **类型**: `EWaveTableCurve`

### Scalar
- **类型**: `float32`

### CurveShared
- **类型**: `UCurveFloat`

### Duration
- **类型**: `float32`
- **描述**: Duration of curve or file.  Only valid if parent SampleRate is set and SamplingMode is set to 'FixedSampleRate'
(If set to 'FixedResolution', duration is variable depending on the resolution (number of samples in the table data)
and device's sample rate.

### WaveTableSettings
- **类型**: `FWaveTableSettings`

## 方法

### opAssign
```angelscript
FWaveTableTransform& opAssign(FWaveTableTransform Other)
```

