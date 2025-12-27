# FAnimationAttributeIdentifier

Script-friendly structure for identifying an attribute (curve).
Wrapping the attribute name, bone name and index, and underlying data type for use within the AnimDataController API.

## 属性

### Name
- **类型**: `FName`

### BoneName
- **类型**: `FName`

### BoneIndex
- **类型**: `int`

### ScriptStruct
- **类型**: `UScriptStruct`

### ScriptStructPath
- **类型**: `FSoftObjectPath`

## 方法

### opAssign
```angelscript
FAnimationAttributeIdentifier& opAssign(FAnimationAttributeIdentifier Other)
```

