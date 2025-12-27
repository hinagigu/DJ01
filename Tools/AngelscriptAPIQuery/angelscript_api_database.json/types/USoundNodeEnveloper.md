# USoundNodeEnveloper

**继承自**: `USoundNode`

Allows manipulation of volume and pitch over a set time period

## 属性

### LoopStart
- **类型**: `float32`
- **描述**: The time in seconds where the envelope's loop begins.

### LoopEnd
- **类型**: `float32`
- **描述**: The time in seconds where the envelope's loop ends.

### DurationAfterLoop
- **类型**: `float32`
- **描述**: The time in seconds it takes the evelope to fade out after the last loop is completed.

### LoopCount
- **类型**: `int`
- **描述**: The number of times the envelope should loop if looping is enabled and the envelope is not set to loop indefinitely.

### VolumeCurve
- **类型**: `FRuntimeFloatCurve`
- **描述**: The distribution defining the volume envelope.

### PitchCurve
- **类型**: `FRuntimeFloatCurve`
- **描述**: The distribution defining the pitch envelope.

### PitchMin
- **类型**: `float32`
- **描述**: The lower bound of pitch (1.0 is no change)

### PitchMax
- **类型**: `float32`
- **描述**: The upper bound of pitch (1.0 is no change)

### VolumeMin
- **类型**: `float32`
- **描述**: The lower bound of volume (1.0 is no change)

### VolumeMax
- **类型**: `float32`
- **描述**: The upper bound of volume (1.0 is no change)

### bLoopIndefinitely
- **类型**: `bool`

### bLoop
- **类型**: `bool`

