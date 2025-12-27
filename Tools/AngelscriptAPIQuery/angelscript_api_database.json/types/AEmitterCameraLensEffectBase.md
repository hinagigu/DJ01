# AEmitterCameraLensEffectBase

**继承自**: `AEmitter`

## 属性

### PS_CameraEffect
- **类型**: `UParticleSystem`
- **描述**: Particle System to use

### RelativeTransform
- **类型**: `FTransform`
- **描述**: Effect-to-camera transform to allow arbitrary placement of the particle system .
Note the X component of the location will be scaled with camera fov to keep the lens effect the same apparent size.

### BaseFOV
- **类型**: `float32`
- **描述**: This is the assumed FOV for which the effect was authored. The code will make automatic adjustments to make it look the same at different FOVs

### EmittersToTreatAsSame
- **类型**: `TArray<TSubclassOf<AActor>>`
- **描述**: If an emitter class in this array is currently playing, do not play this effect.
Useful for preventing multiple similar or expensive camera effects from playing simultaneously.

### bAllowMultipleInstances
- **类型**: `bool`

### bResetWhenRetriggered
- **类型**: `bool`

