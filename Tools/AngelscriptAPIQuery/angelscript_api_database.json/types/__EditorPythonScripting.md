# __EditorPythonScripting

## 方法

### GetKeepPythonScriptAlive
```angelscript
bool GetKeepPythonScriptAlive()
```
Returns the value of the bKeepPythonScriptAlive flag.

If this is false (default), it will close the editor during the next tick (when executing a Python script in the editor-environment using the UnrealEditor-Cmd commandline tool).
If this is true, it will not close the editor by itself, and you will have to close it manually, either by setting this value to false again, or by calling a function like unreal.SystemLibrary.quit_editor().

@return The current value of the bKeepPythonScriptAlive flag.

### SetKeepPythonScriptAlive
```angelscript
void SetKeepPythonScriptAlive(bool bNewKeepAlive)
```
Sets the bKeepPythonScriptAlive flag.

If this is false (default), it will close the editor during the next tick (when executing a Python script in the editor-environment using the UnrealEditor-Cmd commandline tool).
If this is true, it will not close the editor by itself, and you will have to close it manually, either by setting this value to false again, or by calling a function like unreal.SystemLibrary.quit_editor().

@param bNewKeepAlive The new value of the bKeepPythonScriptAlive flag.
@return The result of the users decision, true=Ok, false=Cancel, or false if running in unattended mode.

