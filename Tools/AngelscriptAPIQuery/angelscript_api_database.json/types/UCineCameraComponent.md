# UCineCameraComponent

**继承自**: `UCameraComponent`

A specialized version of a camera component, geared toward cinematic usage.

## 属性

### CurrentFocusDistance
- **类型**: `float32`
- **描述**: Read-only. Control this value via FocusSettings.

### Filmback
- **类型**: `FCameraFilmbackSettings`

### LensSettings
- **类型**: `FCameraLensSettings`

### FocusSettings
- **类型**: `FCameraFocusSettings`

### CropSettings
- **类型**: `FPlateCropSettings`

### CurrentFocalLength
- **类型**: `float32`

### CurrentAperture
- **类型**: `float32`

### bOverride_CustomNearClippingPlane
- **类型**: `bool`

### CustomNearClippingPlane
- **类型**: `float32`

## 方法

### GetCropPresetName
```angelscript
FString GetCropPresetName()
```
Returns the lens name of the camera with the current settings.

### GetDefaultFilmbackPresetName
```angelscript
FString GetDefaultFilmbackPresetName()
```

### GetFilmbackPresetName
```angelscript
FString GetFilmbackPresetName()
```
Returns the filmback name of the camera with the current settings.

### GetHorizontalFieldOfView
```angelscript
float32 GetHorizontalFieldOfView()
```
Returns the horizonal FOV of the camera with current settings.

### GetLensPresetName
```angelscript
FString GetLensPresetName()
```
Returns the lens name of the camera with the current settings.

### GetVerticalFieldOfView
```angelscript
float32 GetVerticalFieldOfView()
```
Returns the vertical FOV of the camera with current settings.

### SetCropPresetByName
```angelscript
void SetCropPresetByName(FString InPresetName)
```
Set the current lens settings by preset name.

### SetCropSettings
```angelscript
void SetCropSettings(FPlateCropSettings NewCropSettings)
```

### SetCurrentAperture
```angelscript
void SetCurrentAperture(float32 NewCurrentAperture)
```

### SetCurrentFocalLength
```angelscript
void SetCurrentFocalLength(float32 InFocalLength)
```

### SetCustomNearClippingPlane
```angelscript
void SetCustomNearClippingPlane(float32 NewCustomNearClippingPlane)
```
Sets near clipping plane of the cine camera.

### SetFilmback
```angelscript
void SetFilmback(FCameraFilmbackSettings NewFilmback)
```

### SetFilmbackPresetByName
```angelscript
void SetFilmbackPresetByName(FString InPresetName)
```
Set the current preset settings by preset name.

### SetFocusSettings
```angelscript
void SetFocusSettings(FCameraFocusSettings NewFocusSettings)
```

### SetLensPresetByName
```angelscript
void SetLensPresetByName(FString InPresetName)
```
Set the current lens settings by preset name.

### SetLensSettings
```angelscript
void SetLensSettings(FCameraLensSettings NewLensSettings)
```

