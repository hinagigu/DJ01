# FAnimNode_Inertialization

## 属性

### Source
- **类型**: `FPoseLink`

### DefaultBlendProfile
- **类型**: `UBlendProfile`
- **描述**: Optional default blend profile to use when no blend profile is supplied with the inertialization request

### FilteredCurves
- **类型**: `TArray<FName>`
- **描述**: List of curves that should not use inertial blending. These curves will instantly change when inertialization begins.

### FilteredBones
- **类型**: `TArray<FBoneReference>`
- **描述**: List of bones that should not use inertial blending. These bones will change instantly when the animation switches.

### bResetOnBecomingRelevant
- **类型**: `bool`
- **描述**: Clear any active blends if we just became relevant, to avoid carrying over undesired blends.

### bForwardRequestsThroughSkippedCachedPoseNodes
- **类型**: `bool`
- **描述**: When enabled this option will forward inertialization requests through any downstream UseCachedPose nodes which
have had their update skipped (e.g. because they have already been updated in another location). This can be
useful in the case where the same cached pose is used in multiple places, and having an inertialization request
that goes with it caught in only one of those places would create popping.

## 方法

### opAssign
```angelscript
FAnimNode_Inertialization& opAssign(FAnimNode_Inertialization Other)
```

