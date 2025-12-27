# FTimecodeCustomAttributeNameSettings

Settings that identify the names of custom attributes that represent the individual components of a timecode and a subframe along with a take name.

## 属性

### HourAttributeName
- **类型**: `FName`
- **描述**: Name of the custom attribute representing the hour component of a timecode.

### MinuteAttributeName
- **类型**: `FName`
- **描述**: Name of the custom attribute representing the minute component of a timecode.

### SecondAttributeName
- **类型**: `FName`
- **描述**: Name of the custom attribute representing the second component of a timecode.

### FrameAttributeName
- **类型**: `FName`
- **描述**: Name of the custom attribute representing the frame component of a timecode.

### SubframeAttributeName
- **类型**: `FName`
- **描述**: Name of the custom attribute representing a subframe value. Though not strictly a component
              of a timecode, this attribute can be authored to identify samples in between timecodes.

### RateAttributeName
- **类型**: `FName`
- **描述**: Name of the custom attribute representing the timecode rate. This may be different from
          the animation or capture frame rate, for example when capturing "high" frame rate data
              at 120 frames per second but recording SMPTE timecode at 30 frames per second.

### TakenameAttributeName
- **类型**: `FName`
- **描述**: Name of the custom attribute representing the name of a take.

## 方法

### opAssign
```angelscript
FTimecodeCustomAttributeNameSettings& opAssign(FTimecodeCustomAttributeNameSettings Other)
```

