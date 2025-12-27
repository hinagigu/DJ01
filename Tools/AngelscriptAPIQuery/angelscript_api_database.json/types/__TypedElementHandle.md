# __TypedElementHandle

## 方法

### Equal
```angelscript
bool Equal(FScriptTypedElementHandle LHS, FScriptTypedElementHandle RHS)
```
Are these two handles equal?

### IsSet
```angelscript
bool IsSet(FScriptTypedElementHandle ElementHandle)
```
Has this handle been initialized to a valid element?

### NotEqual
```angelscript
bool NotEqual(FScriptTypedElementHandle LHS, FScriptTypedElementHandle RHS)
```
Are these two handles not equal?

### Release
```angelscript
void Release(FScriptTypedElementHandle& ElementHandle)
```
Release this handle and set it back to an empty state.

