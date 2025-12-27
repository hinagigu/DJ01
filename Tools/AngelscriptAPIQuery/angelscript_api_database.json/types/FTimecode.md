# FTimecode

A timecode that stores time in HH:MM:SS format with the remainder of time represented by an integer frame count.
@note The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\TimeCode.h

## 属性

### Hours
- **类型**: `int`

### Minutes
- **类型**: `int`

### Seconds
- **类型**: `int`

### Frames
- **类型**: `int`

### bDropFrameFormat
- **类型**: `bool`
- **描述**: If true, this Timecode represents a Drop Frame timecode used to account for fractional frame rates in NTSC play rates.

## 方法

### opAssign
```angelscript
FTimecode& opAssign(FTimecode Other)
```

