# UMovieSceneCapture

**继承自**: `UObject`

Class responsible for capturing scene data

## 属性

### Settings
- **类型**: `FMovieSceneCaptureSettings`

### bUseSeparateProcess
- **类型**: `bool`

### bCloseEditorWhenCaptureStarts
- **类型**: `bool`

### AdditionalCommandLineArguments
- **类型**: `FString`

### InheritedCommandLineArguments
- **类型**: `FString`

### ImageCaptureProtocol
- **类型**: `UMovieSceneImageCaptureProtocolBase`

### AudioCaptureProtocol
- **类型**: `UMovieSceneAudioCaptureProtocolBase`

## 方法

### GetAudioCaptureProtocol
```angelscript
UMovieSceneCaptureProtocolBase GetAudioCaptureProtocol()
```

### GetImageCaptureProtocol
```angelscript
UMovieSceneCaptureProtocolBase GetImageCaptureProtocol()
```
Access the capture protocol we are using

### SetAudioCaptureProtocolType
```angelscript
void SetAudioCaptureProtocolType(TSubclassOf<UMovieSceneCaptureProtocolBase> ProtocolType)
```

### SetImageCaptureProtocolType
```angelscript
void SetImageCaptureProtocolType(TSubclassOf<UMovieSceneCaptureProtocolBase> ProtocolType)
```

