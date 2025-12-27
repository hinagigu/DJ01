# FAnimNode_DeadBlending

Dead Blending Node

Dead blending is an alternative method of inertialization that extrapolates the animation being transitioned from
forward in time and then performs a normal cross-fade blend between this extrapolated animation and the new animation
being transitioned to.

For more background see: https://theorangeduck.com/page/dead-blending

This node works by extrapolating forward the animation being transition from using the animation's velocities at
the point of transition, with an exponential decay which reduces those velocities over time to avoid the pose
becoming invalid.

The rate of this decay is set automatically based on how much the velocities of the animation being transitioned
from are moving toward the pose of the animation being transitioned to. If they are moving in the wrong direction or
too quickly they will have a larger decay rate, while if they are in the correct direction and moving slowly relative
to the difference they will have a smaller decay rate.

These decay rates can be controlled by the `ExtrapolationHalfLife`, `ExtrapolationHalfLifeMin` and
`ExtrapolationHalfLifeMax` parameters, which specify the approximate average, min, and max decay periods.
More specifically they specify the "half-life" - or how it takes for the velocities to be decayed by half.

## 属性

### Source
- **类型**: `FPoseLink`
- **描述**: Input Pose

### bAlwaysUseDefaultBlendSettings
- **类型**: `bool`
- **描述**: When enabled, the default blend settings will always be used rather than those coming from the inertialization request.

### DefaultBlendDuration
- **类型**: `float32`
- **描述**: The default blend duration to use when "Always Use Default Blend Settings" is set to true.

### DefaultBlendProfile
- **类型**: `UBlendProfile`
- **描述**: Default blend profile to use when no blend profile is supplied with the inertialization request.

### DefaultBlendMode
- **类型**: `EAlphaBlendOption`
- **描述**: Default blend mode to use when no blend mode is supplied with the inertialization request.

### DefaultCustomBlendCurve
- **类型**: `UCurveFloat`
- **描述**: Default custom blend curve to use along with the default blend mode.

### BlendTimeMultiplier
- **类型**: `float32`
- **描述**: Multiplier that can be used to scale the overall blend durations coming from inertialization requests.

### bLinearlyInterpolateScales
- **类型**: `bool`
- **描述**: When enabled, bone scales will be linearly interpolated and extrapolated. This is slightly more performant and
consistent with the rest of Unreal but visually gives the appearance of the rate of change of scale being affected
by the overall size of the bone. Note: this option must be enabled if you want this node to support negative scales.

### FilteredCurves
- **类型**: `TArray<FName>`
- **描述**: List of curves that should not use inertial blending. These curves will change instantly when the animation switches.

### ExtrapolationFilteredCurves
- **类型**: `TArray<FName>`
- **描述**: List of curves that will not be included in the extrapolation. Curves in this list will effectively act like they have had their value reset
to zero at the point of the transition, and will be blended in with the curve values in the animation that is being transitioned to.

### FilteredBones
- **类型**: `TArray<FBoneReference>`
- **描述**: List of bones that should not use inertial blending. These bones will change instantly when the animation switches.

### ExtrapolationHalfLife
- **类型**: `float32`
- **描述**: The average half-life of decay in seconds to use when extrapolating the animation. To get the final half-life of
decay, this value will be scaled by the amount to which the velocities of the animation being transitioned from
are moving toward the animation being transitioned to.

### ExtrapolationHalfLifeMin
- **类型**: `float32`
- **描述**: The minimum half-life of decay in seconds to use when extrapolating the animation. This will be used when the
velocities of the animation being transitioned from are very small or moving away from the animation being
transitioned to.

### ExtrapolationHalfLifeMax
- **类型**: `float32`
- **描述**: The maximum half-life of decay in seconds to use when extrapolating the animation. This will dictate the longest
decay duration possible when velocities of the animation being transitioned from are small and moving towards the
animation being transitioned to.

### MaximumTranslationVelocity
- **类型**: `float32`
- **描述**: The maximum velocity to allow for extrapolation of bone translations in centimeters per second. Smaller values
may help prevent the pose breaking during blending but too small values can make the blend less smooth.

### MaximumRotationVelocity
- **类型**: `float32`
- **描述**: The maximum velocity to allow for extrapolation of bone rotations in degrees per second. Smaller values
may help prevent the pose breaking during blending but too small values can make the blend less smooth.

### MaximumScaleVelocity
- **类型**: `float32`
- **描述**: The maximum velocity to allow for extrapolation of bone scales. Smaller values may help prevent the pose
breaking during blending but too small values can make the blend less smooth.

### MaximumCurveVelocity
- **类型**: `float32`
- **描述**: The maximum velocity to allow for extrapolation of curves. Smaller values may help prevent extreme curve values
during blending but too small values can make the blending of curves less smooth.

### bResetOnBecomingRelevant
- **类型**: `bool`
- **描述**: Clear any active blends if we just became relevant, to avoid carrying over undesired blends.

### bShowExtrapolations
- **类型**: `bool`
- **描述**: This setting can be used to show what the extrapolation of the animation looks like.

## 方法

### opAssign
```angelscript
FAnimNode_DeadBlending& opAssign(FAnimNode_DeadBlending Other)
```

