# FNiagaraTypeDefinition

## 属性

### ClassStructOrEnum
- **类型**: `UObject`
- **描述**: Underlying type for this variable, use FUnderlyingType to determine type without casting
This can be a UClass, UStruct or UEnum.  Pointing to something like the struct for an FVector, etc.
In occasional situations this may be a UClass when we're dealing with DataInterface etc.

### UnderlyingType
- **类型**: `uint16`
- **描述**: See enumeration FUnderlyingType for possible values

### Flags
- **类型**: `uint8`

## 方法

### opAssign
```angelscript
FNiagaraTypeDefinition& opAssign(FNiagaraTypeDefinition Other)
```

