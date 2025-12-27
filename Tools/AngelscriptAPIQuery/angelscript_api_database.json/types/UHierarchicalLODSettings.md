# UHierarchicalLODSettings

**继承自**: `UDeveloperSettings`

## 属性

### bForceSettingsInAllMaps
- **类型**: `bool`
- **描述**: If enabled will force the project set HLOD level settings to be used across all levels in the project when Building Clusters

### bSaveLODActorsToHLODPackages
- **类型**: `bool`
- **描述**: If enabled, will save LOD actors descriptions in the HLOD packages

### DefaultSetup
- **类型**: `TSoftClassPtr<UHierarchicalLODSetup>`
- **描述**: When set in combination with

### DirectoriesForHLODCommandlet
- **类型**: `TArray<FDirectoryPath>`

### MapsToBuild
- **类型**: `TArray<FFilePath>`

### BaseMaterial
- **类型**: `TSoftObjectPtr<UMaterialInterface>`
- **描述**: Base material used for creating a Constant Material Instance as the Proxy Material

