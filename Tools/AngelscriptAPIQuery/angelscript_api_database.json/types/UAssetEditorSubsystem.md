# UAssetEditorSubsystem

**继承自**: `UEditorSubsystem`

UAssetEditorSubsystem

## 方法

### CloseAllEditorsForAsset
```angelscript
int CloseAllEditorsForAsset(UObject Asset)
```
Close all active editors for the supplied asset and return the number of asset editors that were closed

### OpenEditorForAssets
```angelscript
bool OpenEditorForAssets(TArray<UObject> Assets, EAssetTypeActivationOpenedMethod OpenedMethod)
```
Tries to open an editor for all of the specified assets.
If any of the assets are already open, it will not create a new editor for them.
If all assets are of the same type, the supporting AssetTypeAction (if it exists) is responsible for the details of how to handle opening multiple assets at once.

