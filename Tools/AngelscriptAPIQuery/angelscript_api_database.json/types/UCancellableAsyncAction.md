# UCancellableAsyncAction

**继承自**: `UBlueprintAsyncActionBase`

base class for asynchronous actions that can be spawned from UK2Node_AsyncAction or C++ code.
These actions register themselves with the game instance and need to be explicitly canceled or ended normally to go away.
The ExposedAsyncProxy metadata specifies the blueprint node will return this object for later canceling.

## 方法

### Cancel
```angelscript
void Cancel()
```
Cancel an asynchronous action, this attempts to cancel any lower level processes and also prevents delegates from being fired

### IsActive
```angelscript
bool IsActive()
```
Returns true if this action is still active and has not completed or been cancelled

