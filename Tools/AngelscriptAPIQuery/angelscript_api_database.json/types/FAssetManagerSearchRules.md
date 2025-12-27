# FAssetManagerSearchRules

Rules for how to scan the asset registry for assets matching path and type descriptions

## 属性

### AssetScanPaths
- **类型**: `TArray<FString>`

### IncludePatterns
- **类型**: `TArray<FString>`

### ExcludePatterns
- **类型**: `TArray<FString>`

### AssetBaseClass
- **类型**: `UClass`

### bHasBlueprintClasses
- **类型**: `bool`

### bForceSynchronousScan
- **类型**: `bool`

### bSkipVirtualPathExpansion
- **类型**: `bool`

### bSkipManagerIncludeCheck
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAssetManagerSearchRules& opAssign(FAssetManagerSearchRules Other)
```

