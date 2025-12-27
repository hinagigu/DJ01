# FPreviewSceneProfile

Preview scene profile settings structure.

## 属性

### ProfileName
- **类型**: `FString`
- **描述**: Name to identify the profile

### bSharedProfile
- **类型**: `bool`
- **描述**: Whether or not this profile should be stored in the Project ini file

### bUseSkyLighting
- **类型**: `bool`
- **描述**: Whether or not image based lighting is enabled for the environment cube map

### DirectionalLightIntensity
- **类型**: `float32`
- **描述**: Manually set the directional light intensity (0.0 - 20.0)

### DirectionalLightColor
- **类型**: `FLinearColor`
- **描述**: Manually set the directional light colour

### SkyLightIntensity
- **类型**: `float32`
- **描述**: Manually set the sky light intensity (0.0 - 20.0)

### bRotateLightingRig
- **类型**: `bool`
- **描述**: Toggle rotating of the sky and directional lighting, press K and drag for manual rotating of Sky and L for Directional lighting

### bShowEnvironment
- **类型**: `bool`
- **描述**: Toggle visibility of the environment sphere

### bShowFloor
- **类型**: `bool`
- **描述**: Toggle visibility of the floor mesh

### EnvironmentColor
- **类型**: `FLinearColor`
- **描述**: The environment color, used if Show Environment is false.

### EnvironmentIntensity
- **类型**: `float32`
- **描述**: The environment intensity (0.0 - 20.0), used if Show Environment is false.

### EnvironmentCubeMap
- **类型**: `TSoftObjectPtr<UTextureCube>`
- **描述**: Sets environment cube map used for sky lighting and reflections

### bPostProcessingEnabled
- **类型**: `bool`
- **描述**: Whether or not the Post Processing should influence the scene

### PostProcessingSettings
- **类型**: `FPostProcessSettings`
- **描述**: Manual set post processing settings

### LightingRigRotation
- **类型**: `float32`
- **描述**: Current rotation value of the sky in degrees (0 - 360)

### RotationSpeed
- **类型**: `float32`
- **描述**: Speed at which the sky rotates when rotating is toggled

## 方法

### opAssign
```angelscript
FPreviewSceneProfile& opAssign(FPreviewSceneProfile Other)
```

