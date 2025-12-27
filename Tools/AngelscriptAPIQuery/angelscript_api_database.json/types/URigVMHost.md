# URigVMHost

**继承自**: `UObject`

set this to something larger than 0 to profile N runs

## 属性

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### AssetUserDataEditorOnly
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

## 方法

### CanExecute
```angelscript
bool CanExecute()
```
Is valid for execution

### Execute
```angelscript
bool Execute(FName InEventName)
```
Execute

### ExecuteEvent
```angelscript
bool ExecuteEvent(FName InEventName)
```
Execute a user defined event

### GetAbsoluteTime
```angelscript
float32 GetAbsoluteTime()
```
Gets the current absolute time

### GetCurrentFramesPerSecond
```angelscript
float32 GetCurrentFramesPerSecond()
```
Returns the current frames per second (this may change over time)

### GetDeltaTime
```angelscript
float32 GetDeltaTime()
```
Gets the current delta time

### GetScriptAccessibleVariables
```angelscript
TArray<FName> GetScriptAccessibleVariables()
```
Returns the names of variables accessible in scripting

### GetSupportedEvents
```angelscript
TArray<FName> GetSupportedEvents()
```

### GetVariableAsString
```angelscript
FString GetVariableAsString(FName InVariableName)
```
Returns the value of a given variable as a string

### GetVariableType
```angelscript
FName GetVariableType(FName InVariableName)
```
Returns the type of a given variable

### GetVM
```angelscript
URigVM GetVM()
```

### IsInitRequired
```angelscript
bool IsInitRequired()
```
Returns true if this host requires the VM memory to be initialized

### RemoveRunOnceEvent
```angelscript
bool RemoveRunOnceEvent(FName InEventName)
```
Removes an event running once

### RequestInit
```angelscript
void RequestInit()
```
Requests to perform an init during the next execution

### RequestRunOnceEvent
```angelscript
void RequestRunOnceEvent(FName InEventName, int InEventIndex)
```
Requests to run an event once

### SetAbsoluteAndDeltaTime
```angelscript
void SetAbsoluteAndDeltaTime(float32 InAbsoluteTime, float32 InDeltaTime)
```
Set the current absolute and delta times

### SetAbsoluteTime
```angelscript
void SetAbsoluteTime(float32 InAbsoluteTime, bool InSetDeltaTimeZero)
```
Set the current absolute time

### SetDeltaTime
```angelscript
void SetDeltaTime(float32 InDeltaTime)
```
Set the current delta time

### SetFramesPerSecond
```angelscript
void SetFramesPerSecond(float32 InFramesPerSecond)
```
Set the current fps

### SetVariableFromString
```angelscript
bool SetVariableFromString(FName InVariableName, FString InValue)
```
Returns the value of a given variable as a string

### SupportsEvent
```angelscript
bool SupportsEvent(FName InEventName)
```

