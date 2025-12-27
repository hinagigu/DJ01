# FPerSkeletonAnimationSharingSetup

## 属性

### Skeleton
- **类型**: `USkeleton`
- **描述**: Skeleton compatible with the animation sharing setup

### SkeletalMesh
- **类型**: `USkeletalMesh`
- **描述**: Skeletal mesh used to setup skeletal mesh components

### BlendAnimBlueprint
- **类型**: `TSubclassOf<UAnimSharingTransitionInstance>`
- **描述**: Animation blueprint used to perform the blending between states

### AdditiveAnimBlueprint
- **类型**: `TSubclassOf<UAnimSharingAdditiveInstance>`
- **描述**: Animation blueprint used to apply additive animation on top of other states

### StateProcessorClass
- **类型**: `TSubclassOf<UAnimationSharingStateProcessor>`
- **描述**: Interface class used when determining which state an actor is in

### AnimationStates
- **类型**: `TArray<FAnimationStateEntry>`
- **描述**: Definition of different animation states

## 方法

### opAssign
```angelscript
FPerSkeletonAnimationSharingSetup& opAssign(FPerSkeletonAnimationSharingSetup Other)
```

