# FRigVMGraphParameterDescription

The parameter description is used to convey information
about unique parameters within a Graph. Multiple Parameter
Nodes can share the same parameter description.

## 属性

### Name
- **类型**: `FName`
- **描述**: The name of the parameter

### bIsInput
- **类型**: `bool`
- **描述**: True if the parameter is an input

### CPPType
- **类型**: `FString`
- **描述**: The C++ data type of the parameter

### CPPTypeObject
- **类型**: `UObject`
- **描述**: The Struct of the C++ data type of the parameter (or nullptr)

### DefaultValue
- **类型**: `FString`
- **描述**: The default value of the parameter

## 方法

### opAssign
```angelscript
FRigVMGraphParameterDescription& opAssign(FRigVMGraphParameterDescription Other)
```

