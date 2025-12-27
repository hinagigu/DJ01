# UInterchangeManager

**继承自**: `UObject`

## 方法

### ExportAsset
```angelscript
bool ExportAsset(const UObject Asset, bool bIsAutomated)
```
Call this to start an asset export process. The caller must specify a source data.

@Param Asset - The asset to export.
@Param bIsAutomated - If true, the exporter will not show any UI or dialogs.
@return true if the export succeeds, or false otherwise.

### ExportScene
```angelscript
bool ExportScene(const UObject World, bool bIsAutomated)
```
Call this to start a scene export process. The caller must specify a source data.
@Param World - The scene to export.
@Param bIsAutomated - If true, the import process will not show any UI or dialogs.
@return true if the export succeeds, or false otherwise.

### GetRegisteredFactoryClass
```angelscript
const UClass GetRegisteredFactoryClass(const UClass ClassToMake)
```
Script helper to get a registered factory for a specified class.
@Param FactoryClass: The class whose registered factory you want to find.
@return: The registered factory class if found, or NULL if no registered factory was found.

### ImportAsset
```angelscript
bool ImportAsset(FString ContentPath, const UInterchangeSourceData SourceData, FImportAssetParameters ImportAssetParameters)
```
Call this to start an asset import process. The caller must specify the source data.
This process can import many different assets into the game content.

@Param ContentPath - The path where the imported assets will be created.
@Param SourceData - The source data input to translate.
@param ImportAssetParameters - All parameters that need to be passed to the import asset function.
@return true if the import succeeds, or false otherwise.

### ImportScene
```angelscript
bool ImportScene(FString ContentPath, const UInterchangeSourceData SourceData, FImportAssetParameters ImportAssetParameters)
```
Call this to start a scene import process. The caller must specify the source data.
This process can import many different assets and their transforms (USceneComponent), store the result in a Blueprint, and add the Blueprint to the level.

@Param ContentPath - The path where the imported assets will be created.
@Param SourceData - The source data input to translate. This object will be duplicated to allow thread-safe operations.
@param ImportAssetParameters - All parameters that need to be passed to the import asset function.
@return true if the import succeeds, or false otherwise.

