# URigVMFunctionLibrary

**继承自**: `URigVMGraph`

The Function Library is a graph used only to store
the sub graphs used for functions.

## 方法

### FindFunction
```angelscript
URigVMLibraryNode FindFunction(FName InFunctionName)
```
Finds a function by name

### FindFunctionForNode
```angelscript
URigVMLibraryNode FindFunctionForNode(URigVMNode InNode)
```
Finds a function by a node within a function (or a sub graph of that)

### GetFunctions
```angelscript
TArray<URigVMLibraryNode> GetFunctions()
```
Returns all of the stored functions

### GetReferencePathsForFunction
```angelscript
TArray<FString> GetReferencePathsForFunction(FName InFunctionName)
```
Returns all references for a given function name

### GetReferencesForFunction
```angelscript
TArray<TSoftObjectPtr<URigVMFunctionReferenceNode>> GetReferencesForFunction(FName InFunctionName)
```
Returns all references for a given function name

