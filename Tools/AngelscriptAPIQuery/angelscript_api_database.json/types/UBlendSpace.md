# UBlendSpace

**继承自**: `UAnimationAsset`

Allows multiple animations to be blended between based on input parameters

## 属性

### InterpolationParam
- **类型**: `FInterpolationParameter`
- **描述**: Input Smoothing parameters for each input axis

### AnalysisProperties
- **类型**: `UAnalysisProperties`
- **描述**: Analysis properties for each axis. Note that these can be null. They will be created/set from
FBlendSpaceDetails::HandleAnalysisFunctionChanged

### TargetWeightInterpolationSpeedPerSec
- **类型**: `float32`
- **描述**: If greater than zero, this is the speed at which the sample weights are allowed to change.

A speed of 1 means a sample weight can change from zero to one (or one to zero) in one second.
A speed of 2 means that this would take half a second.

This allows the Blend Space to switch to new parameters without going through intermediate states,
effectively blending between where it was and where the new target is. For example, imagine we have
a blend space for locomotion, moving left, forward and right. Now if you interpolate the inputs of
the blend space itself, from one extreme to the other, you will go from left, to forward, to right.
As an alternative, by setting this Sample Weight Speed to a value higher than zero, it will go
directly from left to right, without going through moving forward first.

Smaller values mean slower adjustments of the sample weights, and thus more smoothing. However, a
value of zero disables this smoothing entirely.

### bTargetWeightInterpolationEaseInOut
- **类型**: `bool`
- **描述**: If set then this eases in/out the sample weight adjustments, using the speed to determine how much smoothing to apply.

### bAllowMeshSpaceBlending
- **类型**: `bool`
- **描述**: If set then blending is performed in mesh space if there are per-bone sample smoothing overrides.

Note that mesh space blending is significantly more expensive (slower) than normal blending when the
samples are regular animations (i.e. not additive animations that are already set to apply in mesh
space), and is typically only useful if you want some parts of the skeleton to achieve a pose
in mesh space faster or slower than others - for example to make the head move faster than the
body/arms when aiming, so the character looks at the target slightly before aiming at it.

Note also that blend space assets with additive/mesh space samples will always blend in mesh space, and
also that enabling this option with blend space graphs producing additive/mesh space samples may cause
undesired results.

### bLoop
- **类型**: `bool`
- **描述**: The default looping behavior of this blend space.
Asset players can override this

### PreviewBasePose
- **类型**: `UAnimSequence`
- **描述**: Preview Base pose for additive BlendSpace *

### NotifyTriggerMode
- **类型**: `ENotifyTriggerMode`
- **描述**: The current mode used by the BlendSpace to decide which animation notifies to fire. Valid options are:
      - AllAnimations: All notify events will fire
      - HighestWeightedAnimation: Notify events will only fire from the highest weighted animation
      - None: No notify events will fire from any animations

### bInterpolateUsingGrid
- **类型**: `bool`
- **描述**: If true then interpolation is done via a grid at runtime. If false the interpolation uses the triangulation.

### PreferredTriangulationDirection
- **类型**: `EPreferredTriangulationDirection`
- **描述**: Preferred edge direction when the triangulation has to make an arbitrary choice

### PerBoneBlendMode
- **类型**: `EBlendSpacePerBoneBlendMode`
- **描述**: There are two ways to use per pone sample smoothing: Blend profiles and manually maintaining the per bone overrides.

### ManualPerBoneOverrides
- **类型**: `TArray<FPerBoneInterpolation>`
- **描述**: Per bone sample smoothing settings, which affect the specified bone and all its descendants in the skeleton.
These act as overrides to the global sample smoothing speed, which means the global sample smoothing speed does
not affect these bones. Note that they also override each other - so a per-bone setting on the chest will not
affect the hand if there is a per-bone setting on the arm.

### PerBoneBlendProfile
- **类型**: `FBlendSpaceBlendProfile`
- **描述**: Reference to a blend profile of the corresponding skeleton to be used for per bone smoothing in case the per bone blend mode is set to use a blend profile.

### SampleData
- **类型**: `TArray<FBlendSample>`
- **描述**: Sample animation data

### BlendParameters
- **类型**: `FBlendParameter`
- **描述**: Blend Parameters for each axis. *

### AxisToScaleAnimation
- **类型**: `EBlendSpaceAxis`
- **描述**: If you have input smoothing, this specifies the axis on which to scale the animation playback speed. E.g. for
locomotion animation, the speed axis will scale the animation speed in order to make up the difference
between the target and the result of blending the samples.

