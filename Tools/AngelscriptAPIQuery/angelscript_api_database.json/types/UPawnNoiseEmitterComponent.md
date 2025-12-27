# UPawnNoiseEmitterComponent

**继承自**: `UActorComponent`

PawnNoiseEmitterComponent tracks noise event data used by SensingComponents to hear a Pawn.
This component is intended to exist on either a Pawn or its Controller. It does nothing on network clients.

## 属性

### NoiseLifetime
- **类型**: `float32`

### bAIPerceptionSystemCompatibilityMode
- **类型**: `bool`

## 方法

### MakeNoise
```angelscript
void MakeNoise(AActor NoiseMaker, float32 Loudness, FVector NoiseLocation)
```
Cache noises instigated by the owning pawn for AI sensing
@param NoiseMaker - is the actual actor which made the noise
@param Loudness - is the relative loudness of the noise (0.0 to 1.0)
@param NoiseLocation - is the position of the noise

