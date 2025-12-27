# FTouchInputControl

## 属性

### bTreatAsButton
- **类型**: `bool`
- **描述**: Set this to true to treat the joystick as a simple button

### Image1
- **类型**: `UTexture2D`
- **描述**: For sticks, this is the Thumb

### Image2
- **类型**: `UTexture2D`
- **描述**: For sticks, this is the Background

### Center
- **类型**: `FVector2D`
- **描述**: The initial center point of the control. If Time Until Reset is < 0, control resets back to here.
Use negative numbers to invert positioning from top to bottom, left to right. (if <= 1.0, it's relative to screen, > 1.0 is absolute)

### VisualSize
- **类型**: `FVector2D`
- **描述**: The size of the control (if <= 1.0, it's relative to screen, > 1.0 is absolute)

### ThumbSize
- **类型**: `FVector2D`
- **描述**: For sticks, the size of the thumb (if <= 1.0, it's relative to screen, > 1.0 is absolute)

### InteractionSize
- **类型**: `FVector2D`
- **描述**: The interactive size of the control. Measured outward from Center. (if <= 1.0, it's relative to screen, > 1.0 is absolute)

### InputScale
- **类型**: `FVector2D`
- **描述**: The scale for control input

### MainInputKey
- **类型**: `FKey`
- **描述**: The main input to send from this control (for sticks, this is the horizontal axis)

### AltInputKey
- **类型**: `FKey`
- **描述**: The alternate input to send from this control (for sticks, this is the vertical axis)

## 方法

### opAssign
```angelscript
FTouchInputControl& opAssign(FTouchInputControl Other)
```

