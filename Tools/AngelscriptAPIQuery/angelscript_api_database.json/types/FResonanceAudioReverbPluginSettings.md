# FResonanceAudioReverbPluginSettings

## 属性

### bEnableRoomEffects
- **类型**: `bool`

### bGetTransformFromAudioVolume
- **类型**: `bool`
- **描述**: Whether the room transform should be taken from the Audio Volume this preset is attached to.
If not used with the Audio Volume, last saved values will be used.

### RoomPosition
- **类型**: `FVector`

### RoomRotation
- **类型**: `FQuat`

### RoomDimensions
- **类型**: `FVector`

### LeftWallMaterial
- **类型**: `ERaMaterialName`

### RightWallMaterial
- **类型**: `ERaMaterialName`

### FloorMaterial
- **类型**: `ERaMaterialName`

### CeilingMaterial
- **类型**: `ERaMaterialName`

### FrontWallMaterial
- **类型**: `ERaMaterialName`

### BackWallMaterial
- **类型**: `ERaMaterialName`

### ReflectionScalar
- **类型**: `float32`

### ReverbGain
- **类型**: `float32`

### ReverbTimeModifier
- **类型**: `float32`

### ReverbBrightness
- **类型**: `float32`

## 方法

### opAssign
```angelscript
FResonanceAudioReverbPluginSettings& opAssign(FResonanceAudioReverbPluginSettings Other)
```

