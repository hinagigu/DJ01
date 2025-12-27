# UAnimNotifyState

**继承自**: `UObject`

## 属性

### NotifyColor
- **类型**: `FColor`

### bShouldFireInEditor
- **类型**: `bool`

## 方法

### GetDefaultTriggerWeightThreshold
```angelscript
float32 GetDefaultTriggerWeightThreshold()
```
TriggerWeightThreshold to use when creating notifies of this type

### GetNotifyName
```angelscript
FString GetNotifyName()
```
Implementable event to get a custom name for the notify

### NotifyBegin
```angelscript
bool NotifyBegin(USkeletalMeshComponent MeshComp, UAnimSequenceBase Animation, float TotalDuration, FAnimNotifyEventReference EventReference)
```

### NotifyEnd
```angelscript
bool NotifyEnd(USkeletalMeshComponent MeshComp, UAnimSequenceBase Animation, FAnimNotifyEventReference EventReference)
```

### NotifyTick
```angelscript
bool NotifyTick(USkeletalMeshComponent MeshComp, UAnimSequenceBase Animation, float FrameDeltaTime, FAnimNotifyEventReference EventReference)
```

