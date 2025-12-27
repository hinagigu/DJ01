# UNiagaraVersionMetaData

**继承自**: `UObject`

## 属性

### bIsExposedVersion
- **类型**: `bool`
- **描述**: If true then this version is exposed to the user and is used as the default version for new assets.

### ChangeDescription
- **类型**: `FText`
- **描述**: Changelist displayed to the user when upgrading to a new script version.

### bIsVisibleInVersionSelector
- **类型**: `bool`
- **描述**: If false then this version is not visible in the version selector dropdown menu of the stack. This is useful to hide work in progress versions without removing the module from the search menu.
The exposed version is always visible to users.

### bDeprecated
- **类型**: `bool`
- **描述**: True if this asset version is deprecated and should no longer be used.

### DeprecationMessage
- **类型**: `FText`
- **描述**: Message to display when the asset is used in an emitter.

### UpdateScriptExecution
- **类型**: `ENiagaraPythonUpdateScriptReference`
- **描述**: Reference to a python script that is executed when the user updates from a previous version to this version.

### PythonUpdateScript
- **类型**: `FString`
- **描述**: Python script to run when updating to this script version.

### ScriptAsset
- **类型**: `FFilePath`
- **描述**: Asset reference to a python script to run when updating to this script version.

