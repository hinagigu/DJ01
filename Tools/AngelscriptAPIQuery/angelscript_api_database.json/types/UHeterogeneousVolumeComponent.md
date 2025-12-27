# UHeterogeneousVolumeComponent

**继承自**: `UMeshComponent`

A component that represents a heterogeneous volume.

## 属性

### FrameTransform
- **类型**: `FTransform`

### StepFactor
- **类型**: `float32`

### ShadowStepFactor
- **类型**: `float32`

### ShadowBiasFactor
- **类型**: `float32`

### LightingDownsampleFactor
- **类型**: `float32`

### VolumeResolution
- **类型**: `FIntVector`

### Frame
- **类型**: `float32`

### bPlaying
- **类型**: `bool`

### bLooping
- **类型**: `bool`

### bIssueBlockingRequests
- **类型**: `bool`

### bPivotAtCentroid
- **类型**: `bool`

## 方法

### Play
```angelscript
void Play()
```

### SetEndFrame
```angelscript
void SetEndFrame(float32 NewValue)
```

### SetFrame
```angelscript
void SetFrame(float32 NewValue)
```

### SetFrameRate
```angelscript
void SetFrameRate(float32 NewValue)
```

### SetLooping
```angelscript
void SetLooping(bool NewValue)
```

### SetPlaying
```angelscript
void SetPlaying(bool NewValue)
```

### SetStartFrame
```angelscript
void SetStartFrame(float32 NewValue)
```

### SetStreamingMipBias
```angelscript
void SetStreamingMipBias(int NewValue)
```

### SetVolumeResolution
```angelscript
void SetVolumeResolution(FIntVector NewValue)
```

