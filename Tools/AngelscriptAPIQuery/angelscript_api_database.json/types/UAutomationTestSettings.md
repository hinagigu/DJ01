# UAutomationTestSettings

**继承自**: `UObject`

Implements the Editor's user settings.

## 属性

### EngineTestModules
- **类型**: `TArray<FString>`
- **描述**: Modules to load that have engine tests

### EditorTestModules
- **类型**: `TArray<FString>`
- **描述**: Modules to load that have editor tests

### AutomationTestmap
- **类型**: `FSoftObjectPath`
- **描述**: The automation test map to be used for several of the automation tests.

### EditorPerformanceTestMaps
- **类型**: `TArray<FEditorMapPerformanceTestDefinition>`
- **描述**: The map to be used for the editor performance capture tool.

### AssetsToOpen
- **类型**: `TArray<FString>`
- **描述**: Asset to test for open in automation process

### MapsToPIETest
- **类型**: `TArray<FString>`
- **描述**: Maps to PIE during the PIE test

### bUseAllProjectMapsToPlayInPIE
- **类型**: `bool`
- **描述**: Use all Maps from project for PlayMapInPIE test

### BuildPromotionTest
- **类型**: `FBuildPromotionTestSettings`
- **描述**: Editor build promotion test settings

### MaterialEditorPromotionTest
- **类型**: `FMaterialEditorPromotionSettings`
- **描述**: Material editor promotion test settings

### ParticleEditorPromotionTest
- **类型**: `FParticleEditorPromotionSettings`
- **描述**: Particle editor promotion test settings

### BlueprintEditorPromotionTest
- **类型**: `FBlueprintEditorPromotionSettings`
- **描述**: Blueprint editor promotion test settings

### TestLevelFolders
- **类型**: `TArray<FString>`
- **描述**: Folders containing levels to exclude from automated tests

### ExternalTools
- **类型**: `TArray<FExternalToolDefinition>`
- **描述**: External executables and scripts to run as part of automation.

### ImportExportTestDefinitions
- **类型**: `TArray<FEditorImportExportTestDefinition>`
- **描述**: Asset import / Export test settings

### LaunchOnSettings
- **类型**: `TArray<FLaunchOnTestSettings>`
- **描述**: The map and device type to be used for the editor Launch On With Map Iterations test.

### DefaultScreenshotResolution
- **类型**: `FIntPoint`
- **描述**: The default resolution to take all automation screenshots at.

### PIETestDuration
- **类型**: `float32`
- **描述**: PIE test duration in seconds. Only applied if you do PIETest

### DefaultInteractiveFramerate
- **类型**: `float32`
- **描述**: Default value used for FWaitForInteractiveFrameRate. This is a framerate determine to be suitably "interactive", but may be
less than the target framerate of the game as this is used for evaluating time to PIE, load the editor etc

### DefaultInteractiveFramerateWaitTime
- **类型**: `float32`
- **描述**: Default wait time in seconds for FWaitForInteractiveFrameRate. After this time a test will fail.

### DefaultInteractiveFramerateDuration
- **类型**: `float32`
- **描述**: Default time in seconds that DefaultInteractiveFramerate must remain true in FWaitForInteractiveFrameRate

