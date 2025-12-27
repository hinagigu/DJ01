# FRigVMFunction_NameTruncate

Returns the left or right most characters from the string chopping the given number of characters from the start or the end

## 属性

### Name
- **类型**: `FName`

### Count
- **类型**: `int`

### FromEnd
- **类型**: `bool`

### Remainder
- **类型**: `FName`
- **描述**: the part of the string without the chopped characters

### Chopped
- **类型**: `FName`
- **描述**: the part of the name that has been chopped off

## 方法

### opAssign
```angelscript
FRigVMFunction_NameTruncate& opAssign(FRigVMFunction_NameTruncate Other)
```

