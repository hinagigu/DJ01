# FAnimationGroupReference

## 属性

### Method
- **类型**: `EAnimSyncMethod`
- **描述**: How this animation will synchronize with other animations.

### GroupName
- **类型**: `FName`
- **描述**: The group name that we synchronize with (NAME_None if it is not part of any group).

### GroupRole
- **类型**: `EAnimGroupRole`
- **描述**: The role this animation can assume within the group (ignored if GroupName is not set)

## 方法

### opAssign
```angelscript
FAnimationGroupReference& opAssign(FAnimationGroupReference Other)
```

