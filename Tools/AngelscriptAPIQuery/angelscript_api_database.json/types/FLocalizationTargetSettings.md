# FLocalizationTargetSettings

## 属性

### Name
- **类型**: `FString`
- **描述**: Unique name for the target.

### ConflictStatus
- **类型**: `ELocalizationTargetConflictStatus`
- **描述**: Whether the target has outstanding conflicts that require resolution.

### TargetDependencies
- **类型**: `TArray<FGuid>`
- **描述**: Text present in these targets will not be duplicated in this target.

### AdditionalManifestDependencies
- **类型**: `TArray<FFilePath>`
- **描述**: Text present in these manifests will not be duplicated in this target.

### RequiredModuleNames
- **类型**: `TArray<FString>`
- **描述**: The names of modules which must be loaded when gathering text. Use to gather from packages or metadata sourced from a module that isn't the primary game module.

### GatherFromTextFiles
- **类型**: `FGatherTextFromTextFilesConfiguration`
- **描述**: Parameters for defining what text is gathered from text files and how.

### GatherFromPackages
- **类型**: `FGatherTextFromPackagesConfiguration`
- **描述**: Parameters for defining what text is gathered from packages and how.

### GatherFromMetaData
- **类型**: `FGatherTextFromMetaDataConfiguration`
- **描述**: Parameters for defining what text is gathered from metadata and how.

### ExportSettings
- **类型**: `FLocalizationExportingSettings`
- **描述**: Settings for exporting translations.

### CompileSettings
- **类型**: `FLocalizationCompilationSettings`
- **描述**: Settings for compiling translations.

### ImportDialogueSettings
- **类型**: `FLocalizationImportDialogueSettings`
- **描述**: Settings for importing dialogue from WAV files.

### NativeCultureIndex
- **类型**: `int`
- **描述**: The index of the native culture among the supported cultures.

### SupportedCulturesStatistics
- **类型**: `TArray<FCultureStatistics>`
- **描述**: Cultures for which the source text is being localized for.

## 方法

### opAssign
```angelscript
FLocalizationTargetSettings& opAssign(FLocalizationTargetSettings Other)
```

