# FDistanceDatum

## 属性

### FadeInDistanceStart
- **类型**: `float32`
- **描述**: The FadeInDistance at which to start hearing this sound.
       * If you want to hear the sound up close then setting this to 0 might be a good option.

### FadeInDistanceEnd
- **类型**: `float32`
- **描述**: The distance at which this sound has faded in completely.

### FadeOutDistanceStart
- **类型**: `float32`
- **描述**: The distance at which this sound starts fading out.

### FadeOutDistanceEnd
- **类型**: `float32`
- **描述**: The distance at which this sound is no longer audible.

### Volume
- **类型**: `float32`
- **描述**: The volume for which this Input should be played.

## 方法

### opAssign
```angelscript
FDistanceDatum& opAssign(FDistanceDatum Other)
```

