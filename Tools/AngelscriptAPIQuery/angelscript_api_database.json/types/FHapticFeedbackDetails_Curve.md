# FHapticFeedbackDetails_Curve

## 属性

### Frequency
- **类型**: `FRuntimeFloatCurve`
- **描述**: The frequency to vibrate the haptic device at.  Frequency ranges vary by device!

### Amplitude
- **类型**: `FRuntimeFloatCurve`
- **描述**: The amplitude to vibrate the haptic device at.  Amplitudes are normalized over the range [0.0, 1.0], with 1.0 being the max setting of the device

## 方法

### opAssign
```angelscript
FHapticFeedbackDetails_Curve& opAssign(FHapticFeedbackDetails_Curve Other)
```

