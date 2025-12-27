# UAssetManagerSettings

**继承自**: `UDeveloperSettings`

Settings for the Asset Management framework, which can be used to discover, load, and audit game-specific asset types

## 属性

### PrimaryAssetTypesToScan
- **类型**: `TArray<FPrimaryAssetTypeInfo>`
- **描述**: List of asset types to scan at startup

### DirectoriesToExclude
- **类型**: `TArray<FDirectoryPath>`
- **描述**: List of directories to exclude from scanning for Primary Assets, useful to exclude test assets

### PrimaryAssetRules
- **类型**: `TArray<FPrimaryAssetRulesOverride>`
- **描述**: List of specific asset rule overrides

### CustomPrimaryAssetRules
- **类型**: `TArray<FPrimaryAssetRulesCustomOverride>`
- **描述**: List of game-specific asset rule overrides for types, this will not do anything by default

### bOnlyCookProductionAssets
- **类型**: `bool`
- **描述**: If true, DevelopmentCook assets will error when they are cooked, you should enable this on production branches

### bShouldManagerDetermineTypeAndName
- **类型**: `bool`
- **描述**: If true, the asset manager will determine the type and name for Primary Assets that do not implement GetPrimaryAssetId, by calling DeterminePrimaryAssetIdForObject and using the ini settings.
This works in both cooked and uncooked builds but is slower than directly implementing GetPrimaryAssetId on the native asset

### bShouldGuessTypeAndNameInEditor
- **类型**: `bool`
- **描述**: If true, PrimaryAsset Type/Name will be implied for assets in the editor even if bShouldManagerDetermineTypeAndName is false.
This guesses the correct id for content that hasn't been resaved after GetPrimaryAssetId was implemented

### bShouldAcquireMissingChunksOnLoad
- **类型**: `bool`
- **描述**: If true, this will query the platform chunk install interface to request missing chunks for any requested primary asset loads

### bShouldWarnAboutInvalidAssets
- **类型**: `bool`
- **描述**: If true, the asset manager will warn when it is told to load or do something with assets it does not know about

### PrimaryAssetIdRedirects
- **类型**: `TArray<FAssetManagerRedirect>`
- **描述**: Redirect from Type:Name to Type:NameNew

### PrimaryAssetTypeRedirects
- **类型**: `TArray<FAssetManagerRedirect>`
- **描述**: Redirect from Type to TypeNew

### AssetPathRedirects
- **类型**: `TArray<FAssetManagerRedirect>`
- **描述**: Redirect from /game/assetpath to /game/assetpathnew

### MetaDataTagsForAssetRegistry
- **类型**: `TSet<FName>`
- **描述**: The metadata tags to be transferred to the Asset Registry.

