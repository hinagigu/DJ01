# UInterchangeVariantSetNode

**继承自**: `UInterchangeBaseNode`

Class to represent a set of variants.

## 方法

### AddCustomDependencyUid
```angelscript
bool AddCustomDependencyUid(FString DependencyUid)
```
Add the specified translated node's unique ID to this VariantSet.

### GetCustomDependencyUid
```angelscript
void GetCustomDependencyUid(int Index, FString& OutDependencyUid)
```
Retrieve the specified translated node's unique ID for this VariantSet.

### GetCustomDependencyUidCount
```angelscript
int GetCustomDependencyUidCount()
```
Retrieve the number of translated node's unique IDs for this VariantSet.

### GetCustomDependencyUids
```angelscript
void GetCustomDependencyUids(TArray<FString>& OutDependencyUids)
```
Retrieve all the translated node's unique IDs for this VariantSet.

### GetCustomDisplayText
```angelscript
bool GetCustomDisplayText(FString& AttributeValue)
```
Retrieve the text that is displayed in the UI for this VariantSet.

### GetCustomVariantsPayloadKey
```angelscript
bool GetCustomVariantsPayloadKey(FString& PayloadKey)
```
Get the payload key needed to retrieve the variants for this VariantSet.

### RemoveCustomDependencyUid
```angelscript
bool RemoveCustomDependencyUid(FString DependencyUid)
```
Remove the specified translated node's unique ID from this VariantSet.

### SetCustomDisplayText
```angelscript
bool SetCustomDisplayText(FString AttributeValue)
```
Set the text to be displayed in the UI for this VariantSet.

### SetCustomVariantsPayloadKey
```angelscript
bool SetCustomVariantsPayloadKey(FString PayloadKey)
```
Set the payload key needed to retrieve the variants for this VariantSet.

