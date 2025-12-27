# FAnimationStateEntry

## 属性

### State
- **类型**: `uint8`
- **描述**: Enum value linked to this state

### AnimationSetups
- **类型**: `TArray<FAnimationSetup>`
- **描述**: Per state animation setup

### bOnDemand
- **类型**: `bool`
- **描述**: Flag whether or not this state is an on-demand state, this means that we kick off a unique animation when needed

### bAdditive
- **类型**: `bool`
- **描述**: Whether or not this state is an additive state

### BlendTime
- **类型**: `float32`
- **描述**: Duration of blending when blending to this state

### bReturnToPreviousState
- **类型**: `bool`
- **描述**: Flag whether or not we should return to the previous state, only used when this state is an on-demand one

### bSetNextState
- **类型**: `bool`

### NextState
- **类型**: `uint8`
- **描述**: State value to which the actors part of an on demand state should be set to when its animation has finished

### MaximumNumberOfConcurrentInstances
- **类型**: `FPerPlatformInt`
- **描述**: Number of instances that will be created for this state (platform-specific)

### WiggleTimePercentage
- **类型**: `float32`
- **描述**: Percentage of 'wiggle' frames, this is used when we run out of available entries in Components, if one of the on-demand animations has started SequenceLength * WiggleFramePercentage ago or earlier,
      it is used instead of a brand new one

### bRequiresCurves
- **类型**: `bool`
- **描述**: Whether or not this animation requires curves or morphtargets to function correctly for follower components

## 方法

### opAssign
```angelscript
FAnimationStateEntry& opAssign(FAnimationStateEntry Other)
```

