# FAnimNotifyEvent

Triggers an animation notify.  Each AnimNotifyEvent contains an AnimNotify object
which has its Notify method called and passed to the animation.

## 属性

### TriggerWeightThreshold
- **类型**: `float32`

### NotifyName
- **类型**: `FName`

### Notify
- **类型**: `UAnimNotify`

### NotifyStateClass
- **类型**: `UAnimNotifyState`

### MontageTickType
- **类型**: `EMontageNotifyTickType`

### NotifyTriggerChance
- **类型**: `float32`

### NotifyFilterType
- **类型**: `ENotifyFilterType`

### NotifyFilterLOD
- **类型**: `int`

### bCanBeFilteredViaRequest
- **类型**: `bool`

### bTriggerOnDedicatedServer
- **类型**: `bool`

### bTriggerOnFollower
- **类型**: `bool`

### SlotIndex
- **类型**: `int`
- **描述**: The slot index we are currently using within LinkedMontage

### LinkMethod
- **类型**: `EAnimLinkMethod`
- **描述**: The method we are using to calculate our times

## 方法

### opAssign
```angelscript
FAnimNotifyEvent& opAssign(FAnimNotifyEvent Other)
```

