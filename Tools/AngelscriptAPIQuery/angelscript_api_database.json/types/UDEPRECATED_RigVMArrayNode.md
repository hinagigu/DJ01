# UDEPRECATED_RigVMArrayNode

**继承自**: `URigVMTemplateNode`

The Array Node represents one of a series available
array operations such as SetNum, GetAtIndex etc.

## 方法

### GetCPPType
```angelscript
FString GetCPPType()
```
Returns the C++ data type of the element

### GetCPPTypeObject
```angelscript
UObject GetCPPTypeObject()
```
Returns the C++ data type struct of the array (or nullptr)

### GetOpCode
```angelscript
ERigVMOpCode GetOpCode()
```
Returns the op code of this node

