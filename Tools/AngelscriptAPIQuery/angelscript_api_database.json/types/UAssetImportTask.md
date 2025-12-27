# UAssetImportTask

**继承自**: `UObject`

Contains data for a group of assets to import

## 属性

### Filename
- **类型**: `FString`
- **描述**: Filename to import

### DestinationPath
- **类型**: `FString`
- **描述**: Path where asset will be imported to

### DestinationName
- **类型**: `FString`
- **描述**: Optional custom name to import as (if you are using interchange the name must be set in a pipeline and this field will be ignored)

### bReplaceExisting
- **类型**: `bool`
- **描述**: Overwrite existing assets

### bReplaceExistingSettings
- **类型**: `bool`
- **描述**: Replace existing settings when overwriting existing assets

### bAutomated
- **类型**: `bool`
- **描述**: Avoid dialogs

### bSave
- **类型**: `bool`
- **描述**: Save after importing

### bAsync
- **类型**: `bool`
- **描述**: Perform the import asynchronously for file formats where async import is available

### Factory
- **类型**: `UFactory`
- **描述**: Optional factory to use

### Options
- **类型**: `UObject`
- **描述**: Import options specific to the type of asset

### ImportedObjectPaths
- **类型**: `TArray<FString>`
- **描述**: Paths to objects created or updated after import

## 方法

### GetObjects
```angelscript
TArray<UObject> GetObjects()
```
Get the list of imported objects.
Note that if the import was asynchronous, this will block until the results are ready.
To test whether asynchronous results are ready or not, use IsAsyncImportComplete().

### IsAsyncImportComplete
```angelscript
bool IsAsyncImportComplete()
```
Query whether this asynchronous import task is complete, and the results are ready to read.
This will always return true in the case of a blocking import.

