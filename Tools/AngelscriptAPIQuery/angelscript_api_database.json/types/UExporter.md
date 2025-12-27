# UExporter

**继承自**: `UObject`

## 属性

### SupportedClass
- **类型**: `TSubclassOf<UObject>`
- **描述**: Supported class of this exporter

### FormatExtension
- **类型**: `TArray<FString>`
- **描述**: File extension to use for this exporter

### FormatDescription
- **类型**: `TArray<FString>`
- **描述**: Descriptiong of the export format

### ExportTask
- **类型**: `UAssetExportTask`

### bText
- **类型**: `bool`

## 方法

### ScriptRunAssetExportTask
```angelscript
bool ScriptRunAssetExportTask(UAssetExportTask Task)
```
Export the given object to file.  Overridden by script based exporters.

@param        Task            The task to export.

@return       true if overridden by script exporter.

