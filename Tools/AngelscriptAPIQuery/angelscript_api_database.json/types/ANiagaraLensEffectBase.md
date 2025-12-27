# ANiagaraLensEffectBase

**继承自**: `ANiagaraActor`

Niagara equivalent of AEmitterCameraLensEffectBase.
This class is supported by APlayerCameraManager (via ICameraLensEffectInterface) as a camera lens effect.

## 属性

### DesiredRelativeTransform
- **类型**: `FTransform`
- **描述**: Relative offset from the camera (where X is out from the camera)
Might be changed slightly when the FOV is different than expected.

### BaseAuthoredFOV
- **类型**: `float32`
- **描述**: FOVs that differ from this may cause adjustments in positioning.
This is the FOV which the effect was tested with.

### EmittersToTreatAsSame
- **类型**: `TArray<TSubclassOf<AActor>>`
- **描述**: If an effect class in this array is currently playing, do not play this effect.
Useful for preventing multiple similar or expensive camera effects from playing simultaneously.

### bAllowMultipleInstances
- **类型**: `bool`

### bResetWhenRetriggered
- **类型**: `bool`

