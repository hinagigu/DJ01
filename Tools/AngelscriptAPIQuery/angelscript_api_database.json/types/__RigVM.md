# __RigVM

## 方法

### GetAssetsWithFilter
```angelscript
TArray<FAssetData> GetAssetsWithFilter(TSubclassOf<URigVMBlueprint> InClass, FRigVMAssetDataFilterDynamic InAssetDataFilter)
```

### GetController
```angelscript
URigVMController GetController(URigVMBlueprint InBlueprint)
```

### GetModel
```angelscript
URigVMGraph GetModel(URigVMBlueprint InBlueprint)
```

### LoadAssets
```angelscript
TArray<URigVMBlueprint> LoadAssets()
```

### LoadAssetsByClass
```angelscript
TArray<URigVMBlueprint> LoadAssetsByClass(TSubclassOf<URigVMBlueprint> InClass)
```

### LoadAssetsWithAssetDataAndBlueprintFilters
```angelscript
TArray<URigVMBlueprint> LoadAssetsWithAssetDataAndBlueprintFilters(TSubclassOf<URigVMBlueprint> InClass, FRigVMAssetDataFilterDynamic InAssetDataFilter, FRigVMBlueprintFilterDynamic InBlueprintFilter)
```

### LoadAssetsWithAssetDataAndNodeFilters
```angelscript
TArray<URigVMBlueprint> LoadAssetsWithAssetDataAndNodeFilters(TSubclassOf<URigVMBlueprint> InClass, FRigVMAssetDataFilterDynamic InAssetDataFilter, FRigVMNodeFilterDynamic InNodeFilter)
```

### LoadAssetsWithAssetDataFilter
```angelscript
TArray<URigVMBlueprint> LoadAssetsWithAssetDataFilter(TSubclassOf<URigVMBlueprint> InClass, FRigVMAssetDataFilterDynamic InAssetDataFilter)
```

### LoadAssetsWithBlueprintFilter
```angelscript
TArray<URigVMBlueprint> LoadAssetsWithBlueprintFilter(TSubclassOf<URigVMBlueprint> InClass, FRigVMBlueprintFilterDynamic InBlueprintFilter)
```

### LoadAssetsWithNodeFilter
```angelscript
TArray<URigVMBlueprint> LoadAssetsWithNodeFilter(TSubclassOf<URigVMBlueprint> InClass, FRigVMNodeFilterDynamic InNodeFilter)
```

### RecompileVM
```angelscript
void RecompileVM(URigVMBlueprint InBlueprint)
```

### RecompileVMIfRequired
```angelscript
void RecompileVMIfRequired(URigVMBlueprint InBlueprint)
```

### RequestAutoVMRecompilation
```angelscript
void RequestAutoVMRecompilation(URigVMBlueprint InBlueprint)
```

