# UAssetManager

**继承自**: `UObject`

A singleton UObject that is responsible for loading and unloading PrimaryAssets, and maintaining game-specific asset references
Games should override this class and change the class reference

## 方法

### GetPrimaryAssetIdForPath
```angelscript
FPrimaryAssetId GetPrimaryAssetIdForPath(FSoftObjectPath ObjectPath)
```

### GetPrimaryAssetPath
```angelscript
FSoftObjectPath GetPrimaryAssetPath(FPrimaryAssetId PrimaryAssetId)
```

### GetPrimaryAssetIdForData
```angelscript
FPrimaryAssetId GetPrimaryAssetIdForData(FAssetData AssetData)
```

### UnloadPrimaryAsset
```angelscript
int UnloadPrimaryAsset(FPrimaryAssetId AssetToUnload)
```

### UnloadPrimaryAssets
```angelscript
int UnloadPrimaryAssets(TArray<FPrimaryAssetId> AssetsToUnload)
```

### LoadPrimaryAsset
```angelscript
void LoadPrimaryAsset(FPrimaryAssetId AssetToLoad, TArray<FName> LoadBundles, int Priority, UObject OptionalCallbackObject, FName OptionalFinishedCallbackFunctionName, FName OptionalCanceledCallbackName)
```

### LoadPrimaryAssets
```angelscript
void LoadPrimaryAssets(TArray<FPrimaryAssetId> AssetsToLoad, TArray<FName> LoadBundles, int Priority, UObject OptionalCallbackObject, FName OptionalFinishedCallbackFunctionName, FName OptionalCanceledCallbackName)
```

### CallOrRegister_OnCompletedInitialScan
```angelscript
void CallOrRegister_OnCompletedInitialScan(UObject Object, FName FunctionName)
```
Register a function to call when all types are scanned at startup, if this has already happened call immediately

### GetPrimaryAssetData
```angelscript
bool GetPrimaryAssetData(FPrimaryAssetId PrimaryAssetId, FAssetData& AssetData)
```
Gets the FAssetData for a primary asset with the specified type/name, will only work for once that have been scanned for already. Returns true if it found a valid data

### GetPrimaryAssetDataList
```angelscript
bool GetPrimaryAssetDataList(FPrimaryAssetType PrimaryAssetType, TArray<FAssetData>& AssetDataList)
```
Gets list of all FAssetData for a primary asset type, returns true if any were found

### GetPrimaryAssetIdForObject
```angelscript
FPrimaryAssetId GetPrimaryAssetIdForObject(UObject Object)
```
Sees if the passed in object is a registered primary asset, if so return it. Returns invalid Identifier if not found

### GetPrimaryAssetIdList
```angelscript
bool GetPrimaryAssetIdList(FPrimaryAssetType PrimaryAssetType, TArray<FPrimaryAssetId>& PrimaryAssetIdList)
```
Gets list of all FPrimaryAssetId for a primary asset type, returns true if any were found

### GetPrimaryAssetObject
```angelscript
UObject GetPrimaryAssetObject(FPrimaryAssetId PrimaryAssetId)
```
Gets the in-memory UObject for a primary asset id, returning nullptr if it's not in memory. Will return blueprint class for blueprint assets. This works even if the asset wasn't loaded explicitly

### GetPrimaryAssetRules
```angelscript
FPrimaryAssetRules GetPrimaryAssetRules(FPrimaryAssetId PrimaryAssetId)
```
Gets the management rules for a specific asset, this will merge the type and individual values

### GetPrimaryAssetTypeInfo
```angelscript
bool GetPrimaryAssetTypeInfo(FPrimaryAssetType PrimaryAssetType, FPrimaryAssetTypeInfo& AssetTypeInfo)
```
Gets metadata for a specific asset type, returns false if not found

### GetPrimaryAssetTypeInfoList
```angelscript
void GetPrimaryAssetTypeInfoList(TArray<FPrimaryAssetTypeInfo>& AssetTypeInfoList)
```
Gets list of all primary asset types infos

