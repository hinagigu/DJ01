# FAnimNode_Slot

An animation slot node normally acts as a passthru, but a montage or PlaySlotAnimation call from
game code can cause an animation to blend in and be played on the slot temporarily, overriding the
Source input.

## 属性

### Source
- **类型**: `FPoseLink`

### SlotName
- **类型**: `FName`

### bAlwaysUpdateSourcePose
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_Slot& opAssign(FAnimNode_Slot Other)
```

