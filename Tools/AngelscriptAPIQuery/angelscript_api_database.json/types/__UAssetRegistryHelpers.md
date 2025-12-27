# __UAssetRegistryHelpers

## 方法

### CreateAssetData
```angelscript
FAssetData CreateAssetData(const UObject InAsset, bool bAllowBlueprintClass)
```
Creates asset data from a UObject.

@param InAsset       The asset to create asset data for
@param bAllowBlueprintClass  By default trying to create asset data for a blueprint class will create one for the UBlueprint instead

### FindAssetNativeClass
```angelscript
UClass FindAssetNativeClass(FAssetData AssetData)
```
Returns the first native class of the asset type that can be found.  Normally this is just the FAssetData::GetClass(),
however if the class is a blueprint generated class it may not be loaded.  In which case GetAncestorClassNames will
be used to find the first native super class.  This can be slow if temporary caching mode is not on.

### GetAsset
```angelscript
UObject GetAsset(FAssetData InAssetData)
```
Returns the asset UObject if it is loaded or loads the asset if it is unloaded then returns the result

### GetBlueprintAssets
```angelscript
void GetBlueprintAssets(FARFilter InFilter, TArray<FAssetData>& OutAssetData)
```
Gets asset data for all blueprint assets that match the filter. ClassPaths in the filter specify the blueprint's parent class.

### GetClass
```angelscript
UClass GetClass(FAssetData InAssetData)
```

### GetExportTextName
```angelscript
FString GetExportTextName(FAssetData InAssetData)
```
Returns the name for the asset in the form: Class'ObjectPath'

### GetFullName
```angelscript
FString GetFullName(FAssetData InAssetData)
```
Returns the full name for the asset in the form: Class ObjectPath

### GetTagValue
```angelscript
bool GetTagValue(FAssetData InAssetData, FName InTagName, FString& OutTagValue)
```
Gets the value associated with the given tag as a string

### IsAssetLoaded
```angelscript
bool IsAssetLoaded(FAssetData InAssetData)
```
Returns true if the asset is loaded

### IsRedirector
```angelscript
bool IsRedirector(FAssetData InAssetData)
```
Returns true if the this asset is a redirector.

### IsUAsset
```angelscript
bool IsUAsset(FAssetData InAssetData)
```
Returns true if this is the primary asset in a package, true for maps and assets but false for secondary objects like class redirectors

### IsValid
```angelscript
bool IsValid(FAssetData InAssetData)
```
Checks to see if this AssetData refers to an asset or is NULL

### SetFilterTagsAndValues
```angelscript
FARFilter SetFilterTagsAndValues(FARFilter InFilter, TArray<FTagAndValue> InTagsAndValues)
```
Populates the FARFilters tags and values map with the passed in tags and values

### ToSoftObjectPath
```angelscript
FSoftObjectPath ToSoftObjectPath(FAssetData InAssetData)
```
Convert to a SoftObjectPath for loading

### StaticClass
```angelscript
UClass StaticClass()
```

