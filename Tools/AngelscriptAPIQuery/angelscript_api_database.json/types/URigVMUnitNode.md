# URigVMUnitNode

**继承自**: `URigVMTemplateNode`

The Struct Node represents a Function Invocation of a RIGVM_METHOD
declared on a USTRUCT. Struct Nodes have input / output pins for all
struct UPROPERTY members.

## 方法

### GetMethodName
```angelscript
FName GetMethodName()
```
Returns the name of the declared RIGVM_METHOD

### GetStructDefaultValue
```angelscript
FString GetStructDefaultValue()
```
Returns the default value for the struct as text

