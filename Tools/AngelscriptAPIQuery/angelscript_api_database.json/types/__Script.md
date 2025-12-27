# __Script

## 方法

### GetModuleNameOfGlobalVariableBeingInitialized
```angelscript
FString GetModuleNameOfGlobalVariableBeingInitialized()
```
If we are currently initializing a script global variable, return the name of the module it is in.
Returns an empty string if no global variable is currently being initialized.

### GetNameOfGlobalVariableBeingInitialized
```angelscript
FString GetNameOfGlobalVariableBeingInitialized()
```
If we are currently initializing a script global variable, return its name.
Returns an empty string if no global variable is currently being initialized.

### GetNamespaceOfGlobalVariableBeingInitialized
```angelscript
FString GetNamespaceOfGlobalVariableBeingInitialized()
```
If we are currently initializing a script global variable, return the namespace it is in.
Returns an empty string if no global variable is currently being initialized.

