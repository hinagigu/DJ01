# UPawnSensingComponent

**继承自**: `UActorComponent`

SensingComponent encapsulates sensory (ie sight and hearing) settings and functionality for an Actor,
allowing the actor to see/hear Pawns in the world. It does nothing on network clients.

## 属性

### HearingThreshold
- **类型**: `float32`

### LOSHearingThreshold
- **类型**: `float32`

### SightRadius
- **类型**: `float32`

### HearingMaxSoundAge
- **类型**: `float32`

### OnSeePawn
- **类型**: `FSeePawnDelegate__PawnSensingComponent`

### OnHearNoise
- **类型**: `FHearNoiseDelegate__PawnSensingComponent`

### SensingInterval
- **类型**: `float32`

### bEnableSensingUpdates
- **类型**: `bool`

### bOnlySensePlayers
- **类型**: `bool`

### bSeePawns
- **类型**: `bool`

### bHearNoises
- **类型**: `bool`

## 方法

### GetPeripheralVisionAngle
```angelscript
float32 GetPeripheralVisionAngle()
```

### GetPeripheralVisionCosine
```angelscript
float32 GetPeripheralVisionCosine()
```

### SetPeripheralVisionAngle
```angelscript
void SetPeripheralVisionAngle(float32 NewPeripheralVisionAngle)
```
Sets PeripheralVisionAngle. Calculates PeripheralVisionCosine from PeripheralVisionAngle

### SetSensingInterval
```angelscript
void SetSensingInterval(float32 NewSensingInterval)
```
Changes the SensingInterval.
If we are currently waiting for an interval, this can either extend or shorten that interval.
A value <= 0 prevents any updates.

### SetSensingUpdatesEnabled
```angelscript
void SetSensingUpdatesEnabled(bool bEnabled)
```
Enables or disables sensing updates. The timer is reset in either case.

