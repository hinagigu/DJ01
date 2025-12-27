# __EditorUtility

## 方法

### ConvertToEditorUtilityWidget
```angelscript
void ConvertToEditorUtilityWidget(UWidgetBlueprint WidgetBP)
```

### GetCurrentContentBrowserItemPath
```angelscript
FContentBrowserItemPath GetCurrentContentBrowserItemPath()
```
Gets the current content browser path if one is open, whether it is internal or virtual.

### GetCurrentContentBrowserPath
```angelscript
bool GetCurrentContentBrowserPath(FString& OutPath)
```
Attempts to get the path for the active content browser, returns false if there is no active content browser
or if it was a virtual path
@param       OutPath The returned path if successfully found
@return      Whether a path was successfully returned

### GetSelectedAssetData
```angelscript
TArray<FAssetData> GetSelectedAssetData()
```
Gets the set of currently selected asset data

### GetSelectedAssets
```angelscript
TArray<UObject> GetSelectedAssets()
```
Gets the set of currently selected assets

### GetSelectedAssetsOfClass
```angelscript
TArray<UObject> GetSelectedAssetsOfClass(UClass AssetClass)
```

### GetSelectedBlueprintClasses
```angelscript
TArray<UClass> GetSelectedBlueprintClasses()
```
Gets the set of currently selected classes

### GetSelectedFolderPaths
```angelscript
TArray<FString> GetSelectedFolderPaths()
```
Gets the path to the currently selected folder in the content browser

### GetSelectedPathViewFolderPaths
```angelscript
TArray<FString> GetSelectedPathViewFolderPaths()
```
Returns the folders that are selected in the path view for the content browser

### GetSelectionBounds
```angelscript
void GetSelectionBounds(FVector& Origin, FVector& BoxExtent, float32& SphereRadius)
```

### GetSelectionSet
```angelscript
TArray<AActor> GetSelectionSet()
```

### RenameAsset
```angelscript
void RenameAsset(UObject Asset, FString NewName)
```
Renames an asset (cannot move folders)

### SyncBrowserToFolders
```angelscript
void SyncBrowserToFolders(TArray<FString> FolderList)
```
Sync the Content Browser to the given folder(s)
@param       FolderList      The list of folders to sync to in the Content Browser

