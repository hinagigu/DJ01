# UCookerSettings

**继承自**: `UDeveloperSettings`

Various cooker settings.

## 属性

### bEnableCookOnTheSide
- **类型**: `bool`

### bEnableBuildDDCInBackground
- **类型**: `bool`

### bIterativeCookingForLaunchOn
- **类型**: `bool`
- **描述**: Enable -iterate for launch on

### bIterativeCookingForFileCookContent
- **类型**: `bool`
- **描述**: Enable -iterate when triggering from File dropdown menu

### bCookOnTheFlyForLaunchOn
- **类型**: `bool`
- **描述**: Enable -cookonthefly for launch on

### CookProgressDisplayMode
- **类型**: `ECookProgressDisplayMode`
- **描述**: Controls log output of the cooker

### bIgnoreIniSettingsOutOfDateForIteration
- **类型**: `bool`
- **描述**: Ignore ini changes when doing iterative cooking, either in editor or out of editor

### bIgnoreScriptPackagesOutOfDateForIteration
- **类型**: `bool`
- **描述**: Ignore native header file changes when doing iterative cooking, either in editor or out of editor

### bCompileBlueprintsInDevelopmentMode
- **类型**: `bool`
- **描述**: Whether or not to compile Blueprints in development mode when cooking.

### BlueprintComponentDataCookingMethod
- **类型**: `EBlueprintComponentDataCookingMethod`
- **描述**: Generate optimized component data to speed up Blueprint construction at runtime. This option can increase the overall Blueprint memory usage in a cooked build. Requires Event-Driven Loading (EDL), which is enabled by default.

### BlueprintPropertyGuidsCookingMethod
- **类型**: `EBlueprintPropertyGuidsCookingMethod`
- **描述**: Should we include the property GUIDs for a Blueprint class in a cooked build, so that SaveGame archives can redirect property names via the GUIDs?
@note This option can increase the overall Blueprint memory usage in a cooked build, but can avoid needing to add CoreRedirect data for Blueprint classes stored within SaveGame archives.

### ClassesExcludedOnDedicatedServer
- **类型**: `TArray<FString>`
- **描述**: List of class names to exclude when cooking for dedicated server

### ModulesExcludedOnDedicatedServer
- **类型**: `TArray<FString>`
- **描述**: List of module names to exclude when cooking for dedicated server

### ClassesExcludedOnDedicatedClient
- **类型**: `TArray<FString>`
- **描述**: List of class names to exclude when cooking for dedicated client

### ModulesExcludedOnDedicatedClient
- **类型**: `TArray<FString>`
- **描述**: List of module names to exclude when cooking for dedicated client

### VersionedIntRValues
- **类型**: `TArray<FString>`
- **描述**: List of r values that need to be versioned

### DefaultASTCQualityBySpeed
- **类型**: `int`
- **描述**: Quality of 0 means fastest, 3 means best quality

### DefaultASTCQualityBySize
- **类型**: `int`
- **描述**: Quality of 0 means smallest (12x12 block size), 4 means best (4x4 block size)

### DefaultASTCCompressor
- **类型**: `ETextureFormatASTCCompressor`
- **描述**: which compressor to use for ASTC textures

### bAllowASTCHDRProfile
- **类型**: `bool`

### bAllowCookedDataInEditorBuilds
- **类型**: `bool`

