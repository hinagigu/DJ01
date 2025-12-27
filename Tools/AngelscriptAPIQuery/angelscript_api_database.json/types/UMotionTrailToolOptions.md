# UMotionTrailToolOptions

**继承自**: `UObject`

TODO: option to make tick size proportional to distance from camera to get a sense of perspective and scale

## 属性

### bShowTrails
- **类型**: `bool`
- **描述**: Whether or not to show motion trails

### TrailColor
- **类型**: `FLinearColor`
- **描述**: The color of the motion trail

### bShowFullTrail
- **类型**: `bool`
- **描述**: Whether or not to show the full motion trail

### TrailThickness
- **类型**: `float32`
- **描述**: The thickness of the motion trail

### FramesBefore
- **类型**: `int`
- **描述**: The number of frames to draw before the start of the trail. Requires not showing the full trail

### FramesAfter
- **类型**: `int`
- **描述**: The number of frames to draw after the end of the trail. Requires not showing the full trail

### bShowKeys
- **类型**: `bool`
- **描述**: Whether or not to show keys on the motion trail

### bShowFrameNumber
- **类型**: `bool`
- **描述**: Whether or not to show frame numbers for the keys on the motion trail

### KeyColor
- **类型**: `FLinearColor`
- **描述**: The color of the keys

### KeySize
- **类型**: `float`
- **描述**: The size of the keys

### bShowMarks
- **类型**: `bool`
- **描述**: Whether or not to show marks along the motion trail

### MarkColor
- **类型**: `FLinearColor`
- **描述**: The color of the marks

### MarkSize
- **类型**: `float`
- **描述**: The size of the marks

### bLockMarksToFrames
- **类型**: `bool`
- **描述**: Whether or not to lock the marks to the frames

### SecondsPerMark
- **类型**: `float`
- **描述**: The seconds per mark

