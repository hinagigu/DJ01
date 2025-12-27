# UPrimaryAssetLabel

**继承自**: `UPrimaryDataAsset`

A seed file that is created to mark referenced assets as part of this primary asset

## 属性

### Rules
- **类型**: `FPrimaryAssetRules`
- **描述**: Management rules for this specific asset, if set it will override the type rules

### ExplicitAssets
- **类型**: `TArray<TSoftObjectPtr<UObject>>`
- **描述**: List of manually specified assets to label

### ExplicitBlueprints
- **类型**: `TArray<TSoftClassPtr<UObject>>`
- **描述**: List of manually specified blueprint assets to label

### AssetCollection
- **类型**: `FCollectionReference`
- **描述**: Collection to load asset references out of

### bLabelAssetsInMyDirectory
- **类型**: `bool`

### bIsRuntimeLabel
- **类型**: `bool`

### bIncludeRedirectors
- **类型**: `bool`

