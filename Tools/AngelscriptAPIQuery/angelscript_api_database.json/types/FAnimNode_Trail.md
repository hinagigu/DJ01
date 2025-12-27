# FAnimNode_Trail

Trail Controller

## 属性

### TrailBone
- **类型**: `FBoneReference`
- **描述**: Reference to the active bone in the hierarchy to modify.

### ChainLength
- **类型**: `int`
- **描述**: Number of bones above the active one in the hierarchy to modify. ChainLength should be at least 2.

### ChainBoneAxis
- **类型**: `EAxis`
- **描述**: Axis of the bones to point along trail.

### DebugLifeTime
- **类型**: `float32`
- **描述**: Debug Life Time

### MaxDeltaTime
- **类型**: `float32`
- **描述**: To avoid hitches causing stretch of trail, you can use MaxDeltaTime to clamp the long delta time. If you want 30 fps to set it to 0.03333f ( = 1/30 ).

### RelaxationSpeedScale
- **类型**: `float32`

### TrailRelaxationSpeed
- **类型**: `FRuntimeFloatCurve`
- **描述**: How quickly we 'relax' the bones to their animated positions. Time 0 will map to top root joint, time 1 will map to the bottom joint.

### RelaxationSpeedScaleInputProcessor
- **类型**: `FInputScaleBiasClamp`

### RotationLimits
- **类型**: `TArray<FRotationLimit>`

### RotationOffsets
- **类型**: `TArray<FVector>`

### PlanarLimits
- **类型**: `TArray<FAnimPhysPlanarLimit>`
- **描述**: List of available planar limits for this node

### StretchLimit
- **类型**: `float32`
- **描述**: If bLimitStretch is true, this indicates how long a bone can stretch beyond its length in the ref-pose.

### FakeVelocity
- **类型**: `FVector`
- **描述**: 'Fake' velocity applied to bones.

### BaseJoint
- **类型**: `FBoneReference`
- **描述**: Base Joint to calculate velocity from. If none, it will use Component's World Transform. .

### LastBoneRotationAnimAlphaBlend
- **类型**: `float32`
- **描述**: How to set last bone rotation. It copies from previous joint if alpha is 0.f, or 1.f will use animated pose
       * This alpha dictates the blend between parent joint and animated pose, and how much you'd like to use animated pose for

### ComponentPose
- **类型**: `FComponentSpacePoseLink`

### LODThreshold
- **类型**: `int`

### AlphaInputType
- **类型**: `EAnimAlphaInputType`

### bAlphaBoolEnabled
- **类型**: `bool`

### Alpha
- **类型**: `float32`

### AlphaScaleBias
- **类型**: `FInputScaleBias`

### AlphaBoolBlend
- **类型**: `FInputAlphaBoolBlend`

### AlphaCurveName
- **类型**: `FName`

### AlphaScaleBiasClamp
- **类型**: `FInputScaleBiasClamp`

### bInvertChainBoneAxis
- **类型**: `bool`

### bLimitStretch
- **类型**: `bool`

### bLimitRotation
- **类型**: `bool`

### bUsePlanarLimit
- **类型**: `bool`

### bActorSpaceFakeVel
- **类型**: `bool`

### bReorientParentToChild
- **类型**: `bool`

### bEnableDebug
- **类型**: `bool`

### bShowBaseMotion
- **类型**: `bool`

### bShowTrailLocation
- **类型**: `bool`

### bShowLimit
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_Trail& opAssign(FAnimNode_Trail Other)
```

