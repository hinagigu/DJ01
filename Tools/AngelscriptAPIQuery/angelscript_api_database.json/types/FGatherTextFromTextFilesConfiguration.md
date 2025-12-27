# FGatherTextFromTextFilesConfiguration

## 属性

### IsEnabled
- **类型**: `bool`
- **描述**: If enabled, text from text files will be gathered according to this configuration.

### SearchDirectories
- **类型**: `TArray<FGatherTextSearchDirectory>`
- **描述**: The paths of directories to be searched recursively for text files, specified relative to the project's root, which may be parsed for text to gather.

### ExcludePathWildcards
- **类型**: `TArray<FGatherTextExcludePath>`
- **描述**: Text files whose paths match these wildcard patterns will be excluded from gathering.

### FileExtensions
- **类型**: `TArray<FGatherTextFileExtension>`
- **描述**: Text files whose names match these wildcard patterns may be parsed for text to gather.

### ShouldGatherFromEditorOnlyData
- **类型**: `bool`
- **描述**: If enabled, data that is specified as editor-only may be processed for gathering.

## 方法

### opAssign
```angelscript
FGatherTextFromTextFilesConfiguration& opAssign(FGatherTextFromTextFilesConfiguration Other)
```

