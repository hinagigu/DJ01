# UTypedElementRegistry

**继承自**: `UObject`

Registry of element types and their associated interfaces, along with the elements that represent their instances.

## 方法

### GetElementInterface
```angelscript
UObject GetElementInterface(FScriptTypedElementHandle InElementHandle, TSubclassOf<UInterface> InBaseInterfaceType)
```
Get the element interface supported by the given handle, or null if there is no support for this interface or if the handle is invalid.

