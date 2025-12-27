# UContentBrowserAssetContextMenuContext

**继承自**: `UObject`

## 属性

### SelectedAssets
- **类型**: `TArray<FAssetData>`
- **描述**: The currently selected assets in the content browser.

### bContainsUnsupportedAssets
- **类型**: `bool`

## 方法

### LoadSelectedObjects
```angelscript
TArray<UObject> LoadSelectedObjects(TSet<FName> LoadTags)
```
Loads all the selected assets and returns an array of the objects.

### LoadSelectedObjectsIfNeeded
```angelscript
TArray<UObject> LoadSelectedObjectsIfNeeded()
```
Loads the selected assets (if needed) which is based on AssetViewUtils::LoadAssetsIfNeeded, this exists primarily
for backwards compatability.  Reliance on a black box to determine 'neededness' is not recommended, this function
will likely be deprecated a few versions after GetSelectedObjects.

