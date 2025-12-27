# URigVMTemplateNode

**继承自**: `URigVMNode`

The Template Node represents an unresolved function.
Template nodes can morph into all functions implementing
the template's template.

## 方法

### GetNotation
```angelscript
FName GetNotation()
```
Returns the notation of the node

### GetScriptStruct
```angelscript
UScriptStruct GetScriptStruct()
```
Returns the UStruct for this unit node
(the struct declaring the RIGVM_METHOD)

### IsFullyUnresolved
```angelscript
bool IsFullyUnresolved()
```
returns true if the template is fully unresolved

### IsResolved
```angelscript
bool IsResolved()
```
returns true if the template node is resolved

### IsSingleton
```angelscript
bool IsSingleton()
```

