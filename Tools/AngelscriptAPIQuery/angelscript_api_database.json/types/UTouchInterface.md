# UTouchInterface

**继承自**: `UObject`

Defines an interface by which touch input can be controlled using any number of buttons and virtual joysticks

## 属性

### Controls
- **类型**: `TArray<FTouchInputControl>`

### ActiveOpacity
- **类型**: `float32`
- **描述**: Opacity (0.0 - 1.0) of all controls while any control is active

### InactiveOpacity
- **类型**: `float32`
- **描述**: Opacity (0.0 - 1.0) of all controls while no controls are active

### TimeUntilDeactive
- **类型**: `float32`
- **描述**: How long after user interaction will all controls fade out to Inactive Opacity

### TimeUntilReset
- **类型**: `float32`
- **描述**: How long after going inactive will controls reset/recenter themselves (0.0 will disable this feature)

### ActivationDelay
- **类型**: `float32`
- **描述**: How long after joystick enabled for touch (0.0 will disable this feature)

### bPreventRecenter
- **类型**: `bool`
- **描述**: Prevent joystick re-centering and moving from Center through user taps

### StartupDelay
- **类型**: `float32`
- **描述**: Delay at startup before virtual joystick is drawn

