# UInterchangeImportTestStepReimport

**继承自**: `UInterchangeImportTestStepBase`

## 属性

### SourceFileToReimport
- **类型**: `FFilePath`
- **描述**: The source file to import (path relative to the json script).

### AssetTypeToReimport
- **类型**: `TSubclassOf<UObject>`
- **描述**: The type of the asset to reimport. If only one such asset was imported, this is unambiguous.

### AssetNameToReimport
- **类型**: `FString`
- **描述**: If there were multiple assets of the above type imported, specify the concrete name here.

### bSaveThenReloadImportedAssets
- **类型**: `bool`
- **描述**: Determines whether imported assets should be saved and freshly reloaded after import.

