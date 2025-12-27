# __AssetTools

## 方法

### CreateAsset
```angelscript
UObject CreateAsset(FString AssetName, FString PackagePath, UClass AssetClass, UFactory Factory, FName CallingContext)
```
Creates an asset with the specified name, path, and optional factory

@param AssetName the name of the new asset
@param PackagePath the package that will contain the new asset
@param AssetClass the class of the new asset
@param Factory optional factory that will build the new asset
@param CallingContext optional name of the module or method calling CreateAsset() - this is passed to the factory
@return the new asset or nullptr if it fails

### FixupReferencers
```angelscript
void FixupReferencers(TArray<UObject> Objects, bool bCheckoutDialogPrompt, ERedirectFixupMode FixupMode)
```
Fix up references to the specified redirectors.

@param bCheckoutDialogPrompt indicates whether to prompt the user with files checkout dialog or silently attempt to checkout all necessary files.

### ImportAssetTasks
```angelscript
void ImportAssetTasks(TArray<UAssetImportTask> ImportTasks)
```
Imports assets using tasks specified.

@param ImportTasks Tasks that specify how to import each file

