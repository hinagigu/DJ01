# FPerlinNoiseParams

Component data for Perlin Noise channels

## 属性

### Frequency
- **类型**: `float32`
- **描述**: The frequency of the noise, i.e. how many times per second does the noise peak

### Amplitude
- **类型**: `float`
- **描述**: The amplitude of the noise, which will vary between [-Amplitude, +Amplitude]

### Offset
- **类型**: `float32`
- **描述**: Starting offset, in seconds, into the noise pattern

## 方法

### opAssign
```angelscript
FPerlinNoiseParams& opAssign(FPerlinNoiseParams Other)
```

