# UVariableFrameStrippingSettings

**继承自**: `UObject`

* This is a wrapper for the Variable frame stripping Codec.
* It allows for the mass changing of settings on animation sequences in an editor accessible way.

## 属性

### UseVariableFrameStripping
- **类型**: `FPerPlatformBool`
- **描述**: Enables the change from standard 1/2 frame stripping to stripping a higher amount of frames per frame kept

### FrameStrippingRate
- **类型**: `FPerPlatformInt`
- **描述**: The number of Frames that are stripped down to one.
Allows for overrides of that multiplier.
FrameStrippingRate == 1 would strip no frames, Therefore this is clamped to 2.

