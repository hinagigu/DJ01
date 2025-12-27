# UFactory

**继承自**: `UObject`

Base class for all factories
An object responsible for creating and importing new objects.

## 属性

### SupportedClass
- **类型**: `TSubclassOf<UObject>`
- **描述**: The class manufactured by this factory.

### ContextClass
- **类型**: `TSubclassOf<UObject>`
- **描述**: Class of the context object used to help create the object.

### Formats
- **类型**: `TArray<FString>`
- **描述**: List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.

### AutomatedImportData
- **类型**: `const UAutomatedAssetImportData`
- **描述**: Data for how to import files via the automated command line importing interface

### AssetImportTask
- **类型**: `UAssetImportTask`
- **描述**: Task for importing file via script interfaces

### bCreateNew
- **类型**: `bool`

### bEditAfterNew
- **类型**: `bool`

### bEditorImport
- **类型**: `bool`

### bText
- **类型**: `bool`

## 方法

### ScriptFactoryCanImport
```angelscript
bool ScriptFactoryCanImport(FString Filename)
```
Whether the specified file can be imported by this factory. (Implemented in script)

@return true if the file is supported, false otherwise.

### ScriptFactoryCreateFile
```angelscript
bool ScriptFactoryCreateFile(UAssetImportTask InTask)
```
Import object(s) using a task via script

@param InTask
@return True if script implements

