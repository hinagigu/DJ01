# FBPVariableDescription

Struct indicating a variable in the generated class

## 属性

### VarName
- **类型**: `FName`
- **描述**: Name of the variable

### VarType
- **类型**: `FEdGraphPinType`
- **描述**: Type of the variable

### FriendlyName
- **类型**: `FString`
- **描述**: Friendly name of the variable

### Category
- **类型**: `FText`
- **描述**: Category this variable should be in

### PropertyFlags
- **类型**: `uint64`
- **描述**: Property flags for this variable - Changed from int32 to uint64

### RepNotifyFunc
- **类型**: `FName`

### ReplicationCondition
- **类型**: `ELifetimeCondition`

### MetaDataArray
- **类型**: `TArray<FBPVariableMetaDataEntry>`
- **描述**: Metadata information for this variable

### DefaultValue
- **类型**: `FString`
- **描述**: Optional new default value stored as string

## 方法

### opAssign
```angelscript
FBPVariableDescription& opAssign(FBPVariableDescription Other)
```

