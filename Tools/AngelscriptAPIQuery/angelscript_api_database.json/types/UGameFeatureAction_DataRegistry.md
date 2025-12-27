# UGameFeatureAction_DataRegistry

**继承自**: `UGameFeatureAction`

Specifies a list of Data Registries to load and initialize with this feature

## 属性

### RegistriesToAdd
- **类型**: `TArray<TSoftObjectPtr<UDataRegistry>>`
- **描述**: List of registry assets to load and initialize

### bPreloadInEditor
- **类型**: `bool`
- **描述**: If true, this will preload the registries when the feature is registered in the editor to support the editor pickers

### bPreloadInCommandlets
- **类型**: `bool`
- **描述**: If true, this will preload the registries when the feature is registered whilst a commandlet is running

