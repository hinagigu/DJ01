# URigVMVariableNode

**继承自**: `URigVMNode`

The Variable Node represents a mutable value / local state within the
the Function / Graph. Variable Node's can be a getter or a setter.
Getters are pure nodes with just an output value pin, while setters
are mutable nodes with an execute and input value pin.

## 方法

### GetCPPType
```angelscript
FString GetCPPType()
```
Returns the C++ data type of the variable

### GetCPPTypeObject
```angelscript
UObject GetCPPTypeObject()
```
Returns the C++ data type struct of the variable (or nullptr)

### GetDefaultValue
```angelscript
FString GetDefaultValue()
```
Returns the default value of the variable as a string

### GetVariableDescription
```angelscript
FRigVMGraphVariableDescription GetVariableDescription()
```
Returns this variable node's variable description

### GetVariableName
```angelscript
FName GetVariableName()
```
Returns the name of the variable

### IsExternalVariable
```angelscript
bool IsExternalVariable()
```
Returns true if this variable is an external variable

### IsGetter
```angelscript
bool IsGetter()
```
Returns true if this node is a variable getter

### IsInputArgument
```angelscript
bool IsInputArgument()
```
Returns true if this variable is an input argument

### IsLocalVariable
```angelscript
bool IsLocalVariable()
```
Returns true if this variable is a local variable

