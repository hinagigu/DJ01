# FDeviceButtonState

Current State of a physical device button (mouse, key, etc) at a point in time.
Each "click" of a button should involve at minimum two separate state
events, one where bPressed=true and one where bReleased=true.
Each of these states should occur only once.
In addition there may be additional frames where the button is
held down and bDown=true and bPressed=false.

## 属性

### Button
- **类型**: `FKey`
- **描述**: Button identifier

### bPressed
- **类型**: `bool`
- **描述**: Was the button pressed down this frame. This should happen once per "click"

### bDown
- **类型**: `bool`
- **描述**: Is the button currently pressed down. This should be true every frame the button is pressed.

### bReleased
- **类型**: `bool`
- **描述**: Was the button released this frame. This should happen once per "click"

## 方法

### opAssign
```angelscript
FDeviceButtonState& opAssign(FDeviceButtonState Other)
```

