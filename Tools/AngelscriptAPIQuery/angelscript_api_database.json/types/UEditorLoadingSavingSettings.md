# UEditorLoadingSavingSettings

**继承自**: `UObject`

Implements the Level Editor's loading and saving settings.

## 属性

### LoadLevelAtStartup
- **类型**: `ELoadLevelAtStartup`
- **描述**: Whether to load a default example map at startup

### RestoreOpenAssetTabsOnRestart
- **类型**: `ERestoreOpenAssetTabsMethod`
- **描述**: Whether to restore previously open assets at startup after a clean shutdown

### bMonitorContentDirectories
- **类型**: `bool`
- **描述**: When enabled, changes to made to source content files inside the content directories will automatically be reflected in the content browser.
Note that source content files must reside in one of the monitored directories to be eligible for auto-reimport.
Advanced setup options are available below.

### AutoReimportDirectorySettings
- **类型**: `TArray<FAutoReimportDirectoryConfig>`
- **描述**: Lists every directory to monitor for content changes. Can be virtual package paths (eg /Game/ or /MyPlugin/), or absolute paths on disk.
Paths should point to the locations of the source content files (e.g. *.fbx, *.png) you want to be eligible for auto-reimport.

### AutoReimportThreshold
- **类型**: `float32`
- **描述**: Specifies an amount of time to wait before a specific file change is considered for auto reimport

### bAutoCreateAssets
- **类型**: `bool`
- **描述**: When enabled, newly added source content files will be automatically imported into new assets.

### bAutoDeleteAssets
- **类型**: `bool`
- **描述**: When enabled, deleting a source content file will automatically prompt the deletion of any related assets.

### bDetectChangesOnStartup
- **类型**: `bool`
- **描述**: When enabled, changes to monitored directories since UE was closed will be detected on restart.
(Not recommended when working in collaboration with others using revision control).

### bPromptBeforeAutoImporting
- **类型**: `bool`
- **描述**: Whether to prompt the user to import detected changes.

### bDirtyMigratedBlueprints
- **类型**: `bool`
- **描述**: Whether to mark blueprints dirty if they are automatically migrated during loads

### AutoSaveMethod
- **类型**: `EAutoSaveMethod`
- **描述**: What method should be used when performing an autosave?

### AutoSaveTimeMinutes
- **类型**: `int`
- **描述**: The time interval after which to auto save

### AutoSaveInteractionDelayInSeconds
- **类型**: `int`
- **描述**: The minimum number of seconds to wait after the last user interactions (with the editor) before auto-save can trigger

### AutoSaveWarningInSeconds
- **类型**: `int`
- **描述**: The number of seconds warning before an autosave

### AutoSaveMaxBackups
- **类型**: `int`
- **描述**: How many auto save files to keep around

### TextDiffToolPath
- **类型**: `FFilePath`
- **描述**: Specifies the file path to the tool to be used for diffing text files

### bForceCompilationAtStartup
- **类型**: `bool`

### bAutoSaveEnable
- **类型**: `bool`

### bAutoSaveMaps
- **类型**: `bool`

### bAutoSaveContent
- **类型**: `bool`

### bAutomaticallyCheckoutOnAssetModification
- **类型**: `bool`

### bPromptForCheckoutOnAssetModification
- **类型**: `bool`

### bSCCAutoAddNewFiles
- **类型**: `bool`

### bSCCUseGlobalSettings
- **类型**: `bool`

