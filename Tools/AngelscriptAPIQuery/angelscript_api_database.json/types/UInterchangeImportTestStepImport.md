# UInterchangeImportTestStepImport

**继承自**: `UInterchangeImportTestStepBase`

## 属性

### SourceFile
- **类型**: `FFilePath`
- **描述**: The source file to import (path relative to the json script)

### PipelineStack
- **类型**: `TArray<TObjectPtr<UInterchangePipelineBase>>`
- **描述**: The pipeline stack to use when importing (an empty array will use the defaults)

### bEmptyDestinationFolderPriorToImport
- **类型**: `bool`
- **描述**: Whether the destination folder should be emptied prior to import

### bSaveThenReloadImportedAssets
- **类型**: `bool`
- **描述**: Whether imported assets should be saved and freshly reloaded after import

### bImportIntoLevel
- **类型**: `bool`
- **描述**: Whether we should use the import into level workflow

