# UEditorAssetSubsystem

**继承自**: `UEditorSubsystem`

UEditorAssetSubsystem
Subsystem for exposing asset related utilities to scripts.
Asset Paths can be represented in the following ways:
             (Reference/Text Path)   StaticMesh'/Game/MyFolder/MyAsset.MyAsset'
             (Full Name)                             StaticMesh /Game/MyFolder/MyAsset.MyAsset
             (Path Name)                             /Game/MyFolder/MyAsset.MyAsset
             (Package Name)                  /Game/MyFolder/MyAsset
Directory Paths can be represented in the following ways:
             /Game/MyNewFolder/
             /Game/MyNewFolder

## 方法

### AddOnExtractAssetFromFile
```angelscript
void AddOnExtractAssetFromFile(FOnExtractAssetFromFileDynamic__EditorAssetSubsystem Delegate)
```
Call this to add a callback to extract an asset from a file,
for example from a drag and drop operation.

### CheckoutAsset
```angelscript
bool CheckoutAsset(FString AssetToCheckout)
```
Checkout an asset.
@param       AssetToCheckout         Asset Path of the asset that we want to checkout.
@return      True if the operation succeeds.

### CheckoutDirectory
```angelscript
bool CheckoutDirectory(FString DirectoryPath, bool bRecursive)
```
Checkout all assets in a directory. It will load the assets if needed.
All objects that are in the directory will be checked out. Assets will be loaded before being checked out.
@param       DirectoryPath           Directory of the assets to be checked out.
@param       bRecursive                      If the AssetPath is a folder, the search will be recursive and will checkout the assets in the sub folders.
@return      True if the operation succeeds.

### CheckoutLoadedAsset
```angelscript
bool CheckoutLoadedAsset(UObject AssetToCheckout)
```
Checkout the asset corresponding to an object.
@param       AssetToCheckout         Asset to checkout.
@return      True if the operation succeeds.

### CheckoutLoadedAssets
```angelscript
bool CheckoutLoadedAssets(TArray<UObject> AssetsToCheckout)
```
Checkout the assets.
@param       AssetsToCheckout                Assets to checkout.
@return      True if the operation succeeds.

### ConsolidateAssets
```angelscript
bool ConsolidateAssets(UObject AssetToConsolidateTo, TArray<UObject> AssetsToConsolidate)
```
Consolidates assets by replacing all references/uses of the provided AssetsToConsolidate with references to AssetToConsolidateTo.
This is useful when you want all references of assets to be replaced by a single asset.
The function first attempts to directly replace all relevant references located within objects that are already loaded and in memory.
Next, it deletes the AssetsToConsolidate, leaving behind object redirectors to AssetToConsolidateTo.
@param       AssetToConsolidateTo    Asset to which all references of the AssetsToConsolidate will instead refer to after this operation completes.
@param       AssetsToConsolidate             All references to these assets will be modified to reference AssetToConsolidateTo instead.
@note        The AssetsToConsolidate are DELETED by this function.
@note        Modified objects will be saved if the operation succeeds.
@return      True if the operation succeeds.

### DeleteAsset
```angelscript
bool DeleteAsset(FString AssetPathToDelete)
```
Delete the package an asset is in. All objects in the package will be deleted.
This is a Force Delete. It does not check if the asset has references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted. The Asset will be loaded before being deleted.
@param       AssetPathToDelete               Asset Path of the asset to delete.
@return      True if the operation succeeds.

### DeleteDirectory
```angelscript
bool DeleteDirectory(FString DirectoryPath)
```
Delete the packages inside a directory. If the directory is then empty, delete the directory.
This is a Force Delete. It does not check if the assets have references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted. Assets will be loaded before being deleted.
The search is always recursive. It will try to delete the sub folders.
@param       DirectoryPath           Directory that will be marked for deletion and deleted.
@return      True if the operation succeeds.

### DeleteLoadedAsset
```angelscript
bool DeleteLoadedAsset(UObject AssetToDelete)
```
Delete an asset that is already loaded.
This is a Force Delete. It does not check if the asset has references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted.
@param       AssetToDelete                   Asset to delete.
@return      True if the operation succeeds.

### DeleteLoadedAssets
```angelscript
bool DeleteLoadedAssets(TArray<UObject> AssetsToDelete)
```
Delete assets that are already loaded.
This is a Force Delete. It does not check if the assets have references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the files as deleted.
@param       AssetsToDelete                  Loaded assets to delete.
@return      True if the operation succeeds.

### DoAssetsExist
```angelscript
bool DoAssetsExist(TArray<FString> AssetPaths)
```
Check if assets exist in the Asset Registry.
@param       AssetPaths              Asset Paths of the assets to check for existence.
@return      True if all assets exist and are valid.

### DoesAssetExist
```angelscript
bool DoesAssetExist(FString AssetPath)
```
Check if an asset exists in the Asset Registry.
@param       AssetPath               Asset Path to check for existence.
@return      True if the asset exists and is valid.

### DoesDirectoryContainAssets
```angelscript
bool DoesDirectoryContainAssets(FString DirectoryPath, bool bRecursive)
```
Check if a directory contains any assets.
@param       DirectoryPath           Long Path Name of the directory.
@return      True if there is any assets.

### DoesDirectoryExist
```angelscript
bool DoesDirectoryExist(FString DirectoryPath)
```
Check if a directory exists.
@param        DirectoryPath           Long Path Name of the directory.
@return       True if it does exist and it is valid.

### DuplicateAsset
```angelscript
UObject DuplicateAsset(FString SourceAssetPath, FString DestinationAssetPath)
```
Duplicate an asset. Will try to checkout the file. The Asset will be loaded before being duplicated.
@param       SourceAssetPath                 Asset Path of the asset that we want to copy from.
@param       DestinationAssetPath    Asset Path of the duplicated asset.
@return      The duplicated object if the operation succeeds.

### DuplicateDirectory
```angelscript
bool DuplicateDirectory(FString SourceDirectoryPath, FString DestinationDirectoryPath)
```
Duplicate a directory and the assets in it.
Will try to checkout the files. The Assets will be loaded before being duplicated.
@param       SourceDirectoryPath                     Directory of the assets that we want to duplicate from.
@param       DestinationDirectoryPath        Directory of the duplicated asset.
@return      The duplicated object if the operation succeeds.

### DuplicateLoadedAsset
```angelscript
UObject DuplicateLoadedAsset(UObject SourceAsset, FString DestinationAssetPath)
```
Duplicate an asset that is already loaded. Will try to checkout the file.
@param       SourceAsset                             Asset that we want to copy from.
@param       DestinationAssetPath    Asset Path of the duplicated asset.
@return      The duplicated object if the operation succeeds

### FindAssetData
```angelscript
FAssetData FindAssetData(FString AssetPath)
```
Return the AssetData for the Asset that can then be used with AssetRegistryHelpers.
@param       AssetPath       Asset Path to retrieve data from.
@return      The AssetData found.

### FindPackageReferencersForAsset
```angelscript
TArray<FString> FindPackageReferencersForAsset(FString AssetPath, bool bLoadAssetsToConfirm)
```
Find Package Referencers for an asset. Only Soft and Hard dependencies will be looked for.
Soft are dependencies which don't need to be loaded for the object to be used.
Hard are dependencies which are required for correct usage of the source asset and must be loaded at the same time.
Other references may exist. The asset may be currently used in memory by another asset, by the editor or by code.
Package dependencies are cached with the asset. False positives can happen until all the assets are loaded and re-saved.
@param       AssetPath                               Asset Path of the asset that we are looking for.
@param       bLoadAssetsToConfirm    Whether the asset and any potential referencers will be loaded to confirm the dependencies.
@return      The package paths of the referencers.

### GetMetadataTag
```angelscript
FString GetMetadataTag(UObject Object, FName Tag)
```
Get the value associated with the given tag of a loaded asset's metadata.
@param  Object          The object from which to retrieve the metadata.
@param  Tag                     The tag to find in the metadata.
@return The string value associated with the tag.

### GetMetadataTagValues
```angelscript
TMap<FName,FString> GetMetadataTagValues(UObject Object)
```
Get all tags/values of a loaded asset's metadata.
@param  Object          The object from which to retrieve the metadata.
@return The list of all Tags and Values.

### GetPathNameForLoadedAsset
```angelscript
FString GetPathNameForLoadedAsset(UObject LoadedAsset)
```
Return a valid AssetPath for a loaded asset.
Similar to GetPathName(). The format will be: /Game/MyFolder/MyAsset.MyAsset
@param       LoadedAsset             The loaded asset to get the path of.
@return      If valid, the asset Path of the loaded asset.

### GetTagValues
```angelscript
TMap<FName,FString> GetTagValues(FString AssetPath)
```
Gets all TagValues (from Asset Registry) associated with an (unloaded) asset as strings value.
@param       AssetPath               Asset Path we are trying to find.
@return      The list of all TagNames & TagValues.

### ListAssets
```angelscript
TArray<FString> ListAssets(FString DirectoryPath, bool bRecursive, bool bIncludeFolder)
```
Return the list of all the assets found in the DirectoryPath.
@param       DirectoryPath           Directory path of the asset we want the list from.
@param       bRecursive                      The search will be recursive and will look in sub folders.
@param       bIncludeFolder          The result will include folders name.
@return      The list of assets found.

### ListAssetsByTagValue
```angelscript
TArray<FString> ListAssetsByTagValue(FName TagName, FString TagValue)
```
Return the list of all the assets that have the pair of Tag/Value.
@param TagName       The tag associated with the assets requested.
@param TagValue      The value associated with the assets requested.
@return      The list of assets found.

### LoadAsset
```angelscript
UObject LoadAsset(FString AssetPath)
```
Load an asset. It will verify if the object is already loaded and only load it if it's necessary.
@param       AssetPath               Asset Path of the asset to load
@return      Found or loaded asset.

### LoadBlueprintClass
```angelscript
UClass LoadBlueprintClass(FString AssetPath)
```
Load a Blueprint asset and return its generated class. It will verify if the object is already loaded and only load it if it's necessary.
@param       AssetPath               Asset Path of the Blueprint asset.
@return      Found or loaded class.

### MakeDirectory
```angelscript
bool MakeDirectory(FString DirectoryPath)
```
Create a directory on disk.
@param       DirectoryPath           Long Path Name of the directory.
@return      True if the operation succeeds.

### RemoveMetadataTag
```angelscript
void RemoveMetadataTag(UObject Object, FName Tag)
```
Remove the given tag from a loaded asset's metadata.
@param  Object          The object from which to retrieve the metadata.
@param  Tag                     The tag to remove from the metadata.

### RemoveOnExtractAssetFromFile
```angelscript
void RemoveOnExtractAssetFromFile(FOnExtractAssetFromFileDynamic__EditorAssetSubsystem Delegate)
```
Call this to remove a callback added with AddOnExtractAssetFromFile.

### RenameAsset
```angelscript
bool RenameAsset(FString SourceAssetPath, FString DestinationAssetPath)
```
Rename an asset. Equivalent to a Move operation.
Will try to checkout the file. The Asset will be loaded before being renamed.
@param       SourceAssetPath                 Asset Path of the asset that we want to copy from.
@param       DestinationAssetPath    Asset Path of the renamed asset.
@return      True if the operation succeeds.

### RenameDirectory
```angelscript
bool RenameDirectory(FString SourceDirectoryPath, FString DestinationDirectoryPath)
```
Rename a directory. Equivalent to a Move operation moving all contained assets.
Will try to checkout the files. The Assets will be loaded before being renamed.
@param       SourceDirectoryPath                     Directory of the assets that we want to rename from.
@param       DestinationDirectoryPath        Directory of the renamed asset.
@return      True if the operation succeeds.

### RenameLoadedAsset
```angelscript
bool RenameLoadedAsset(UObject SourceAsset, FString DestinationAssetPath)
```
Rename an asset that is already loaded. Equivalent to a Move operation.
Will try to checkout the file.
@param       SourceAsset                             Asset that we want to copy from.
@param       DestinationAssetPath    Asset Path of the duplicated asset.
@return      True if the operation succeeds.

### SaveAsset
```angelscript
bool SaveAsset(FString AssetToSave, bool bOnlyIfIsDirty)
```
Save the packages the assets live in. All objects that live in the package will be saved.
Will try to checkout the file first. The Asset will be loaded before being saved.
@param       AssetToSave             Asset Path of the asset that we want to save.
@param       bOnlyIfIsDirty          Only checkout/save the asset if it's dirty.
@return      True if the operation succeeds.

### SaveDirectory
```angelscript
bool SaveDirectory(FString DirectoryPath, bool bOnlyIfIsDirty, bool bRecursive)
```
Save the packages the assets live in inside the directory. All objects that are in the directory will be saved.
Will try to checkout the file first. Assets will be loaded before being saved.
@param       DirectoryPath           Directory that will be checked out and saved.
@param       bOnlyIfIsDirty          Only checkout asset that are dirty.
@param       bRecursive                      The search will be recursive and it will save the asset in the sub folders.
@return      True if the operation succeeds.

### SaveLoadedAsset
```angelscript
bool SaveLoadedAsset(UObject AssetToSave, bool bOnlyIfIsDirty)
```
Save the package the asset lives in. All objects that live in the package will be saved. Will try to checkout the file.
@param       AssetToSave                     Asset that we want to save.
@param       bOnlyIfIsDirty          Only checkout asset that are dirty.
@return      True if the operation succeeds.

### SaveLoadedAssets
```angelscript
bool SaveLoadedAssets(TArray<UObject> AssetsToSave, bool bOnlyIfIsDirty)
```
Save the packages the assets live in. All objects that live in the packages will be saved. Will try to checkout the files.
@param       AssetsToSave            Assets that we want to save.
@param       bOnlyIfIsDirty          Only checkout asset that are dirty.
@return      True if the operation succeeds.

### SetMetadataTag
```angelscript
void SetMetadataTag(UObject Object, FName Tag, FString Value)
```
Set the value associated with a given tag of a loaded asset's metadata.
@param  Object          The object from which to retrieve the metadata.
@param  Tag                     The tag to set in the metadata.
@param  Value           The string value to associate with the tag.

