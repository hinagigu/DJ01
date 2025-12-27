# FEditorImportExportTestDefinition

Holds settings for the asset import / export automation test

## 属性

### ImportFilePath
- **类型**: `FFilePath`
- **描述**: The file to import

### ExportFileExtension
- **类型**: `FString`
- **描述**: The file extension to use when exporting this asset.  Used to find a supporting exporter

### bSkipExport
- **类型**: `bool`
- **描述**: If true, the export step will be skipped

### FactorySettings
- **类型**: `TArray<FImportFactorySettingValues>`
- **描述**: Settings for the import factory

## 方法

### opAssign
```angelscript
FEditorImportExportTestDefinition& opAssign(FEditorImportExportTestDefinition Other)
```

