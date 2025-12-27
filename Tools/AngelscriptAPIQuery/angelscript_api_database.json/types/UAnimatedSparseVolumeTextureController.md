# UAnimatedSparseVolumeTextureController

**继承自**: `UObject`

Utility (blueprint) class for controlling SparseVolumeTexture playback.

## 属性

### SparseVolumeTexture
- **类型**: `USparseVolumeTexture`

### Time
- **类型**: `float32`

### bIsPlaying
- **类型**: `bool`

### FrameRate
- **类型**: `float32`

### MipLevel
- **类型**: `int`

### bBlockingStreamingRequests
- **类型**: `bool`

## 方法

### GetCurrentFrame
```angelscript
USparseVolumeTextureFrame GetCurrentFrame()
```

### GetCurrentFramesForInterpolation
```angelscript
void GetCurrentFramesForInterpolation(USparseVolumeTextureFrame& Frame0, USparseVolumeTextureFrame& Frame1, float32& LerpAlpha)
```

### GetDuration
```angelscript
float32 GetDuration()
```

### GetFractionalFrameIndex
```angelscript
float32 GetFractionalFrameIndex()
```

### GetFrameByIndex
```angelscript
USparseVolumeTextureFrame GetFrameByIndex(int FrameIndex)
```

### Pause
```angelscript
void Pause()
```

### Play
```angelscript
void Play()
```

### Stop
```angelscript
void Stop()
```

### Update
```angelscript
void Update(float32 DeltaTime)
```

