# UCineCameraSettings

**继承自**: `UDeveloperSettings`

## 属性

### DefaultLensPresetName
- **类型**: `FString`

### DefaultLensFocalLength
- **类型**: `float32`

### DefaultLensFStop
- **类型**: `float32`

### LensPresets
- **类型**: `TArray<FNamedLensPreset>`

### DefaultFilmbackPreset
- **类型**: `FString`

### FilmbackPresets
- **类型**: `TArray<FNamedFilmbackPreset>`

### DefaultCropPresetName
- **类型**: `FString`

### CropPresets
- **类型**: `TArray<FNamedPlateCropPreset>`

## 方法

### GetCropPresetByName
```angelscript
bool GetCropPresetByName(FString PresetName, FPlateCropSettings& CropSettings)
```
Gets the Crop settings associated with a given preset name
Returns true if a preset with the given name was found

### GetFilmbackPresetByName
```angelscript
bool GetFilmbackPresetByName(FString PresetName, FCameraFilmbackSettings& FilmbackSettings)
```
Gets the Filmback settings associated with a given preset name
Returns true if a preset with the given name was found

### GetLensPresetByName
```angelscript
bool GetLensPresetByName(FString PresetName, FCameraLensSettings& LensSettings)
```
Gets the Lens settings associated with a given preset name
Returns true if a preset with the given name was found

### SetCropPresets
```angelscript
void SetCropPresets(TArray<FNamedPlateCropPreset> InCropPresets)
```

### SetDefaultCropPresetName
```angelscript
void SetDefaultCropPresetName(FString InDefaultCropPresetName)
```

### SetDefaultFilmbackPreset
```angelscript
void SetDefaultFilmbackPreset(FString InDefaultFilmbackPreset)
```

### SetDefaultLensFocalLength
```angelscript
void SetDefaultLensFocalLength(float32 InDefaultLensFocalLength)
```

### SetDefaultLensFStop
```angelscript
void SetDefaultLensFStop(float32 InDefaultLensFStop)
```

### SetDefaultLensPresetName
```angelscript
void SetDefaultLensPresetName(FString InDefaultLensPresetName)
```
Internal Blueprint Setter functions that call SaveConfig after setting the variable to ensure settings persist

### SetFilmbackPresets
```angelscript
void SetFilmbackPresets(TArray<FNamedFilmbackPreset> InFilmbackPresets)
```

### SetLensPresets
```angelscript
void SetLensPresets(TArray<FNamedLensPreset> InLensPresets)
```

