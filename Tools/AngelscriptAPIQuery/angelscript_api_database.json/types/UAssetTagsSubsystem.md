# UAssetTagsSubsystem

**继承自**: `UEngineSubsystem`

## 方法

### AddAssetDatasToCollection
```angelscript
bool AddAssetDatasToCollection(FName Name, TArray<FAssetData> AssetDatas)
```
Add the given assets to the given collection.

@param Name Name of the collection to modify.
@param AssetDatas Assets to add.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### AddAssetDataToCollection
```angelscript
bool AddAssetDataToCollection(FName Name, FAssetData AssetData)
```
Add the given asset to the given collection.

@param Name Name of the collection to modify.
@param AssetData Asset to add.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### AddAssetPtrsToCollection
```angelscript
bool AddAssetPtrsToCollection(FName Name, TArray<UObject> AssetPtrs)
```
Add the given assets to the given collection.

@param Name Name of the collection to modify.
@param AssetPtrs Assets to add.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### AddAssetPtrToCollection
```angelscript
bool AddAssetPtrToCollection(FName Name, const UObject AssetPtr)
```
Add the given asset to the given collection.

@param Name Name of the collection to modify.
@param AssetPtr Asset to add.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### AddAssetsToCollection
```angelscript
bool AddAssetsToCollection(FName Name, TArray<FName> AssetPathNames)
```

### AddAssetToCollection
```angelscript
bool AddAssetToCollection(FName Name, FName AssetPathName)
```

### CollectionExists
```angelscript
bool CollectionExists(FName Name)
```
Check whether the given collection exists.

@param Name Name of the collection to test.

@return True if the collection exists, false otherwise.

### CreateCollection
```angelscript
bool CreateCollection(FName Name, ECollectionScriptingShareType ShareType)
```
Create a new collection with the given name and share type.

@param Name Name to give to the collection.
@param ShareType Whether the collection should be local, private, or shared?

@return True if the collection was created, false otherwise (see the output log for details on error).

### DestroyCollection
```angelscript
bool DestroyCollection(FName Name)
```
Destroy the given collection.

@param Name Name of the collection to destroy.

@return True if the collection was destroyed, false otherwise (see the output log for details on error).

### EmptyCollection
```angelscript
bool EmptyCollection(FName Name)
```
Remove all assets from the given collection.

@param Name Name of the collection to modify.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### GetAssetsInCollection
```angelscript
TArray<FAssetData> GetAssetsInCollection(FName Name)
```
Get the assets in the given collection.

@param Name Name of the collection to test.

@return Assets in the given collection.

### GetCollections
```angelscript
TArray<FName> GetCollections()
```
Get the names of all available collections.

@return Names of all available collections.

### GetCollectionsContainingAsset
```angelscript
TArray<FName> GetCollectionsContainingAsset(FName AssetPathName)
```

### GetCollectionsContainingAssetData
```angelscript
TArray<FName> GetCollectionsContainingAssetData(FAssetData AssetData)
```
Get the names of the collections that contain the given asset.

@param AssetData Asset to test.

@return Names of the collections that contain the asset.

### GetCollectionsContainingAssetPtr
```angelscript
TArray<FName> GetCollectionsContainingAssetPtr(const UObject AssetPtr)
```
Get the names of the collections that contain the given asset.

@param AssetPtr Asset to test.

@return Names of the collections that contain the asset.

### K2_AddAssetsToCollection
```angelscript
bool K2_AddAssetsToCollection(FName Name, TArray<FSoftObjectPath> AssetPaths)
```
Add the given assets to the given collection.

@param Name Name of the collection to modify.
@param AssetPathNames Assets to add (their path names, eg) /Game/MyFolder/MyAsset.MyAsset).

@return True if the collection was modified, false otherwise (see the output log for details on error).

### K2_AddAssetToCollection
```angelscript
bool K2_AddAssetToCollection(FName Name, FSoftObjectPath AssetPath)
```
Add the given asset to the given collection.

@param Name Name of the collection to modify.
@param AssetPathName Asset to add (its path name, eg) /Game/MyFolder/MyAsset.MyAsset).

@return True if the collection was modified, false otherwise (see the output log for details on error).

### K2_GetCollectionsContainingAsset
```angelscript
TArray<FName> K2_GetCollectionsContainingAsset(FSoftObjectPath AssetPath)
```
Get the names of the collections that contain the given asset.

@param AssetPathName Asset to test (its path name, eg) /Game/MyFolder/MyAsset.MyAsset).

@return Names of the collections that contain the asset.

### K2_RemoveAssetFromCollection
```angelscript
bool K2_RemoveAssetFromCollection(FName Name, FSoftObjectPath AssetPath)
```
Remove the given asset from the given collection.

@param Name Name of the collection to modify.
@param AssetPath Asset to remove (its path, eg) /Game/MyFolder/MyAsset.MyAsset).

@return True if the collection was modified, false otherwise (see the output log for details on error).

### K2_RemoveAssetsFromCollection
```angelscript
bool K2_RemoveAssetsFromCollection(FName Name, TArray<FSoftObjectPath> AssetPaths)
```
Remove the given assets from the given collection.

@param Name Name of the collection to modify.
@param AssetPathNames Assets to remove (their path names, eg) /Game/MyFolder/MyAsset.MyAsset).

@return True if the collection was modified, false otherwise (see the output log for details on error).

### RemoveAssetDataFromCollection
```angelscript
bool RemoveAssetDataFromCollection(FName Name, FAssetData AssetData)
```
Remove the given asset from the given collection.

@param Name Name of the collection to modify.
@param AssetData Asset to remove.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### RemoveAssetDatasFromCollection
```angelscript
bool RemoveAssetDatasFromCollection(FName Name, TArray<FAssetData> AssetDatas)
```
Remove the given assets from the given collection.

@param Name Name of the collection to modify.
@param AssetDatas Assets to remove.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### RemoveAssetFromCollection
```angelscript
bool RemoveAssetFromCollection(FName Name, FName AssetPathName)
```

### RemoveAssetPtrFromCollection
```angelscript
bool RemoveAssetPtrFromCollection(FName Name, const UObject AssetPtr)
```
Remove the given asset from the given collection.

@param Name Name of the collection to modify.
@param AssetPtr Asset to remove.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### RemoveAssetPtrsFromCollection
```angelscript
bool RemoveAssetPtrsFromCollection(FName Name, TArray<UObject> AssetPtrs)
```
Remove the given assets from the given collection.

@param Name Name of the collection to modify.
@param AssetPtrs Assets to remove.

@return True if the collection was modified, false otherwise (see the output log for details on error).

### RemoveAssetsFromCollection
```angelscript
bool RemoveAssetsFromCollection(FName Name, TArray<FName> AssetPathNames)
```

### RenameCollection
```angelscript
bool RenameCollection(FName Name, FName NewName)
```
Rename the given collection.

@param Name Name of the collection to rename.
@param NewName Name to give to the collection.

@return True if the collection was renamed, false otherwise (see the output log for details on error).

### ReparentCollection
```angelscript
bool ReparentCollection(FName Name, FName NewParentName)
```
Re-parent the given collection.

@param Name Name of the collection to re-parent.
@param NewParentName Name of the new parent collection, or None to have the collection become a root collection.

@return True if the collection was renamed, false otherwise (see the output log for details on error).

