# FMovieSceneCaptureSettings

Common movie-scene capture settings

## 属性

### OutputDirectory
- **类型**: `FDirectoryPath`

### GameModeOverride
- **类型**: `TSubclassOf<AGameModeBase>`

### OutputFormat
- **类型**: `FString`

### bOverwriteExisting
- **类型**: `bool`

### bUseRelativeFrameNumbers
- **类型**: `bool`

### HandleFrames
- **类型**: `int`

### MovieExtension
- **类型**: `FString`

### ZeroPadFrameNumbers
- **类型**: `uint8`

### FrameRate
- **类型**: `FFrameRate`
- **描述**: The sequence's frame rate at which to capture if "Use Custom Frame Rate" is not enabled

### bUseCustomFrameRate
- **类型**: `bool`

### CustomFrameRate
- **类型**: `FFrameRate`

### Resolution
- **类型**: `FCaptureResolution`

### bEnableTextureStreaming
- **类型**: `bool`

### bCinematicEngineScalability
- **类型**: `bool`

### bCinematicMode
- **类型**: `bool`

### bAllowMovement
- **类型**: `bool`

### bAllowTurning
- **类型**: `bool`

### bShowPlayer
- **类型**: `bool`

### bShowHUD
- **类型**: `bool`

### bUsePathTracer
- **类型**: `bool`

### PathTracerSamplePerPixel
- **类型**: `int`

## 方法

### opAssign
```angelscript
FMovieSceneCaptureSettings& opAssign(FMovieSceneCaptureSettings Other)
```

