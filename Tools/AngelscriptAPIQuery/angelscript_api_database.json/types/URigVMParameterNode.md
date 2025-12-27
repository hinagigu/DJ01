# URigVMParameterNode

**继承自**: `URigVMNode`

The Parameter Node represents an input or output argument / parameter
of the Function / Graph. Parameter Node have only a single value pin.

## 方法

### GetCPPType
```angelscript
FString GetCPPType()
```
Returns the C++ data type of the parameter

### GetCPPTypeObject
```angelscript
UObject GetCPPTypeObject()
```
Returns the C++ data type struct of the parameter (or nullptr)

### GetDefaultValue
```angelscript
FString GetDefaultValue()
```
Returns the default value of the parameter as a string

### GetParameterDescription
```angelscript
FRigVMGraphParameterDescription GetParameterDescription()
```
Returns this parameter node's parameter description

### GetParameterName
```angelscript
FName GetParameterName()
```
Returns the name of the parameter

### IsInput
```angelscript
bool IsInput()
```
Returns true if this node is an input

