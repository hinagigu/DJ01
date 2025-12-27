# UCameraShakeSourceComponent

**继承自**: `USceneComponent`

## 属性

### Attenuation
- **类型**: `ECameraShakeAttenuation`

### InnerAttenuationRadius
- **类型**: `float32`

### OuterAttenuationRadius
- **类型**: `float32`

### CameraShake
- **类型**: `TSubclassOf<UCameraShakeBase>`

### bAutoStart
- **类型**: `bool`

## 方法

### GetAttenuationFactor
```angelscript
float32 GetAttenuationFactor(FVector Location)
```
Computes an attenuation factor from this source

### Start
```angelscript
void Start()
```

### StartCameraShake
```angelscript
void StartCameraShake(TSubclassOf<UCameraShakeBase> InCameraShake, float32 Scale, ECameraShakePlaySpace PlaySpace, FRotator UserPlaySpaceRot)
```
Starts a new camera shake originating from this source, and apply it on all player controllers

### StopAllCameraShakes
```angelscript
void StopAllCameraShakes(bool bImmediately)
```
Stops all currently active camera shakes that are originating from this source from all player controllers

### StopAllCameraShakesOfType
```angelscript
void StopAllCameraShakesOfType(TSubclassOf<UCameraShakeBase> InCameraShake, bool bImmediately)
```
Stops a camera shake originating from this source

