# UMetaSoundSettings

**继承自**: `UDeveloperSettings`

## 属性

### bAutoUpdateEnabled
- **类型**: `bool`
- **描述**: If true, AutoUpdate is enabled, increasing load times.  If false, skips AutoUpdate on load, but can result in MetaSounds failing to load,
register, and execute if interface differences are present.

### AutoUpdateDenylist
- **类型**: `TArray<FMetasoundFrontendClassName>`
- **描述**: List of native MetaSound classes whose node references should not be AutoUpdated.

### AutoUpdateAssetDenylist
- **类型**: `TArray<FDefaultMetaSoundAssetAutoUpdateSettings>`
- **描述**: List of MetaSound assets whose node references should not be AutoUpdated.

### bAutoUpdateLogWarningOnDroppedConnection
- **类型**: `bool`
- **描述**: If true, warnings will be logged if updating a node results in existing connections being discarded.

### DirectoriesToRegister
- **类型**: `TArray<FDirectoryPath>`
- **描述**: Directories to scan & automatically register MetaSound post initial asset scan on engine start-up.
May speed up subsequent calls to playback MetaSounds post asset scan but increases application load time.
See 'MetaSoundAssetSubsystem::RegisterAssetClassesInDirectories' to dynamically register or
'MetaSoundAssetSubsystem::UnregisterAssetClassesInDirectories' to unregister asset classes.

### QualitySettings
- **类型**: `TArray<FMetaSoundQualitySettings>`
- **描述**: Array of possible quality settings for Metasounds to chose from // NOTE: Ideally this would be wrapped with WITH_EDITORONLY_DATA, but standalone "-game" requires
// it to exist. Access is limited to the accessor above, which enforces it correctly.

