# FAnimationSetup

## 属性

### AnimSequence
- **类型**: `UAnimSequence`
- **描述**: Animation Sequence to play for this particular setup

### AnimBlueprint
- **类型**: `TSubclassOf<UAnimSharingStateInstance>`
- **描述**: Animation blueprint to use for playing back the Animation Sequence

### NumRandomizedInstances
- **类型**: `FPerPlatformInt`
- **描述**: The number of randomized instances created from this setup, it will create instance with different start time offsets (Length / Number of Instance) * InstanceIndex

### Enabled
- **类型**: `FPerPlatformBool`
- **描述**: Whether or not this setup is enabled for specific platforms

## 方法

### opAssign
```angelscript
FAnimationSetup& opAssign(FAnimationSetup Other)
```

