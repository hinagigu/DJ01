# UAutomatedAssetImportData

**继承自**: `UObject`

Contains data for a group of assets to import

## 属性

### GroupName
- **类型**: `FString`
- **描述**: Display name of the group. This is for logging purposes only.

### Filenames
- **类型**: `TArray<FString>`
- **描述**: Filenames to import

### DestinationPath
- **类型**: `FString`
- **描述**: Content path in the projects content directory where assets will be imported

### FactoryName
- **类型**: `FString`
- **描述**: Name of the factory to use when importing these assets. If not specified the factory type will be auto detected

### bReplaceExisting
- **类型**: `bool`
- **描述**: Whether or not to replace existing assets

### bSkipReadOnly
- **类型**: `bool`
- **描述**: Whether or not to skip importing over read only assets that could not be checked out

### Factory
- **类型**: `UFactory`
- **描述**: Pointer to the factory currently being used

### LevelToLoad
- **类型**: `FString`
- **描述**: Full path to level to load before importing this group (only matters if importing assets into a level)

