# FAnimationSharingScalability

## 属性

### UseBlendTransitions
- **类型**: `FPerPlatformBool`
- **描述**: Flag whether or not to use blend transitions between states

### BlendSignificanceValue
- **类型**: `FPerPlatformFloat`
- **描述**: Significance value tied to whether or not a transition should be blended

### MaximumNumberConcurrentBlends
- **类型**: `FPerPlatformInt`
- **描述**: Maximum number of blends which can be running concurrently

### TickSignificanceValue
- **类型**: `FPerPlatformFloat`
- **描述**: Significance value tied to whether or not the leader pose components should be ticking

## 方法

### opAssign
```angelscript
FAnimationSharingScalability& opAssign(FAnimationSharingScalability Other)
```

