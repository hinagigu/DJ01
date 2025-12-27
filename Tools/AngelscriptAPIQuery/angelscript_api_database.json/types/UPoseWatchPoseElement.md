# UPoseWatchPoseElement

**继承自**: `UPoseWatchElement`

## 属性

### ViewportMask
- **类型**: `UBlendProfile`
- **描述**: Optionally select a Blend Mask to control which bones on the skeleton are rendered. Any non-zero entries are rendered.

### bInvertViewportMask
- **类型**: `bool`
- **描述**: Invert which bones are rendered when using a viewport mask

### BlendScaleThreshold
- **类型**: `float32`
- **描述**: The threshold which each bone's blend scale much surpass to be rendered using the viewport mask

### ViewportOffset
- **类型**: `FVector3d`
- **描述**: Offset the rendering of the bones in the viewport.

