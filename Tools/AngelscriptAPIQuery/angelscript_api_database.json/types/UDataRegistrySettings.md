# UDataRegistrySettings

**继承自**: `UDeveloperSettings`

Settings for the Data Registry subsystem, these settings are used to scan for registry assets and set runtime access rules

## 属性

### DirectoriesToScan
- **类型**: `TArray<FDirectoryPath>`
- **描述**: List of directories to scan for data registry assets

### bInitializeAllLoadedRegistries
- **类型**: `bool`
- **描述**: If false, only registry assets inside DirectoriesToScan will be initialized. If true, it will also initialize any in-memory DataRegistry assets outside the scan paths

### bIgnoreMissingCookedAssetRegistryData
- **类型**: `bool`
- **描述**: If true, cooked builds will ignore errors with missing AssetRegistry data for specific registered assets like DataTables as it may have been stripped out

