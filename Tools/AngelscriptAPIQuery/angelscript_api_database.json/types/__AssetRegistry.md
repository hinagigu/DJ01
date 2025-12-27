# __AssetRegistry

## 方法

### IsLoadingAssets
```angelscript
bool IsLoadingAssets()
```

### HasAssets
```angelscript
bool HasAssets(FName PackagePath, bool bRecursive)
```

### GetAssetsByPackageName
```angelscript
bool GetAssetsByPackageName(FName PackageName, TArray<FAssetData>& OutAssetData, bool bIncludeOnlyOnDiskAssets)
```

### GetAssetsByPath
```angelscript
bool GetAssetsByPath(FName PackagePath, TArray<FAssetData>& OutAssetData, bool bRecursive, bool bIncludeOnlyOnDiskAssets)
```

### GetAssetsByClass
```angelscript
bool GetAssetsByClass(FTopLevelAssetPath ClassPath, TArray<FAssetData>& OutAssetData, bool bSearchSubClasses)
```

### GetBlueprintCDOsByParentClass
```angelscript
void GetBlueprintCDOsByParentClass(UClass Class, TArray<UObject>& OutAssets)
```

### GetWidgetBlueprintCDOsByParentClass
```angelscript
void GetWidgetBlueprintCDOsByParentClass(UClass Class, TArray<UObject>& OutAssets)
```

### GetAssetsByTags
```angelscript
bool GetAssetsByTags(TArray<FName> AssetTags, TArray<FAssetData>& OutAssetData)
```

### GetAssetByObjectPath
```angelscript
FAssetData GetAssetByObjectPath(FSoftObjectPath ObjectPath, bool bIncludeOnlyOnDiskAssets)
```

### GetAllAssets
```angelscript
bool GetAllAssets(TArray<FAssetData>& OutAssetData, bool bIncludeOnlyOnDiskAssets)
```

### GetAssets
```angelscript
bool GetAssets(FARFilter Filter, TArray<FAssetData>& OutAssetData, bool bSkipARFilteredAssets)
```

### GetDependencies
```angelscript
bool GetDependencies(FName PackageName, FAssetRegistryDependencyOptions DependencyOptions, TArray<FName>& OutDependencies)
```

### GetReferencers
```angelscript
bool GetReferencers(FName PackageName, FAssetRegistryDependencyOptions ReferenceOptions, TArray<FName>& OutReferencers)
```

### GetDerivedClassNames
```angelscript
void GetDerivedClassNames(TArray<FTopLevelAssetPath> ClassNames, TSet<FTopLevelAssetPath> ExcludedClassNames, TSet<FTopLevelAssetPath>& OutDerivedClassNames)
```

### GetGeneratedClassName
```angelscript
bool GetGeneratedClassName(FAssetData AssetData, FTopLevelAssetPath& OutGeneratedClassName)
```

### AssetCreated
```angelscript
void AssetCreated(UObject NewAsset)
```

### LoadAllBlueprintsUnderPath
```angelscript
void LoadAllBlueprintsUnderPath(FName PathToLoadFrom, FString OptionalFileIncludeRegex)
```

