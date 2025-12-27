# FAnimNode_PoseBlendNode

Evaluates a point in an anim sequence, using a specific time input rather than advancing time internally.
Typically the playback position of the animation for this node will represent something other than time, like jump height.
This node will not trigger any notifies present in the associated sequence.

## 属性

### SourcePose
- **类型**: `FPoseLink`

### BlendOption
- **类型**: `EAlphaBlendOption`
- **描述**: Type of blending used (Linear, Cubic, etc.)

### CustomCurve
- **类型**: `UCurveFloat`
- **描述**: If you're using Custom BlendOption, you can specify curve

### PoseAsset
- **类型**: `UPoseAsset`

### BlendWeight
- **类型**: `float32`
- **描述**: Last encountered blendweight for this node

### InternalTimeAccumulator
- **类型**: `float32`
- **描述**: Accumulated time used to reference the asset in this node

## 方法

### opAssign
```angelscript
FAnimNode_PoseBlendNode& opAssign(FAnimNode_PoseBlendNode Other)
```

