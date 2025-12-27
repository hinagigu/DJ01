# UGameFeaturesSubsystemSettings

**继承自**: `UDeveloperSettings`

Settings for the Game Features framework

## 属性

### GameFeaturesManagerClassName
- **类型**: `FSoftClassPath`
- **描述**: Name of a singleton class to spawn as the game feature project policy. If empty, it will spawn the default one (UDefaultGameFeaturesProjectPolicies)

### EnabledPlugins
- **类型**: `TArray<FString>`
- **描述**: List of plugins that are forcibly enabled (e.g., via a hotfix)

### DisabledPlugins
- **类型**: `TArray<FString>`
- **描述**: List of plugins that are forcibly disabled (e.g., via a hotfix)

### AdditionalPluginMetadataKeys
- **类型**: `TArray<FString>`
- **描述**: List of metadata (additional keys) to try parsing from the .uplugin to provide to FGameFeaturePluginDetails

