# __UUniversalObjectLocatorScriptingExtensions

## 方法

### IsEmpty
```angelscript
bool IsEmpty(FUniversalObjectLocator Locator)
```
Check whether the specified locator is empty; not equivalent to Resolve() != None.
An empty locator will never resolve to a valid object.

### MakeUniversalObjectLocator
```angelscript
FUniversalObjectLocator MakeUniversalObjectLocator(UObject Object, UObject Context)
```
Construct a new universal object locator

### SyncFind
```angelscript
UObject SyncFind(FUniversalObjectLocator Locator, UObject Context)
```
Attempt to resolve the object locator by finding the object. If it is not currently loaded or created,

@param Context    (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.
@return The resolve object pointer, or null if it was not found.

### SyncLoad
```angelscript
UObject SyncLoad(FUniversalObjectLocator Locator, UObject Context)
```
Attempt to resolve the object locator by finding or loading the object.

@param Context    (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.
@return The resolve object pointer, or null if it was not found.

### SyncUnload
```angelscript
void SyncUnload(FUniversalObjectLocator Locator, UObject Context)
```
Attempt to resolve the object locator by unloading the object if possible.

@param Context    (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.
@return The resolve object pointer, or null if it was not found.

### ToString
```angelscript
FString ToString(FUniversalObjectLocator Locator)
```
Convert the specified locator to its string representation

### UniversalObjectLocatorFromString
```angelscript
FUniversalObjectLocator UniversalObjectLocatorFromString(FString InString)
```
Construct a new universal object locator from a string

### StaticClass
```angelscript
UClass StaticClass()
```

