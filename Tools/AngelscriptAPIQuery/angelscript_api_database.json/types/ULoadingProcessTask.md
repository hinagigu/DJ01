# ULoadingProcessTask

**继承自**: `UObject`

ULoadingProcessTask

A simple UObject that implements ILoadingProcessInterface, useful for Blueprint-driven loading scenarios.
Create an instance of this, and it will keep the loading screen visible until you call Unregister().

## 方法

### SetShowLoadingScreenReason
```angelscript
void SetShowLoadingScreenReason(FString InReason)
```
Updates the reason string (useful for debugging)

### Unregister
```angelscript
void Unregister()
```
Call this when you're done with the loading task to allow the loading screen to be dismissed

