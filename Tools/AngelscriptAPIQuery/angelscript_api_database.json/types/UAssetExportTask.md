# UAssetExportTask

**继承自**: `UObject`

Contains data for a group of assets to export

## 属性

### Object
- **类型**: `UObject`
- **描述**: Asset to export

### Exporter
- **类型**: `UExporter`
- **描述**: Optional exporter, otherwise it will be determined automatically

### Filename
- **类型**: `FString`
- **描述**: File to export as

### bSelected
- **类型**: `bool`
- **描述**: Export selected only

### bReplaceIdentical
- **类型**: `bool`
- **描述**: Replace identical files

### bPrompt
- **类型**: `bool`
- **描述**: Allow dialog prompts

### bAutomated
- **类型**: `bool`
- **描述**: Unattended export

### bUseFileArchive
- **类型**: `bool`
- **描述**: Save to a file archive

### bWriteEmptyFiles
- **类型**: `bool`
- **描述**: Write even if file empty

### IgnoreObjectList
- **类型**: `TArray<TObjectPtr<UObject>>`
- **描述**: Array of objects to ignore exporting

### Options
- **类型**: `UObject`
- **描述**: Exporter specific options

### Errors
- **类型**: `TArray<FString>`
- **描述**: Array of error messages encountered during exporter

