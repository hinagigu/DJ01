# UInterchangeSceneVariantSetsFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

## 方法

### AddCustomVariantSetUid
```angelscript
bool AddCustomVariantSetUid(FString VariantUid)
```
Add a unique id of a translated VariantSet for this object.

### GetCustomVariantSetUid
```angelscript
void GetCustomVariantSetUid(int Index, FString& OutVariantUid)
```
Retrieve the UID of the VariantSet with the specified index.

### GetCustomVariantSetUidCount
```angelscript
int GetCustomVariantSetUidCount()
```
Retrieve the number of unique IDs of all translated VariantSets for this object.

### GetCustomVariantSetUids
```angelscript
void GetCustomVariantSetUids(TArray<FString>& OutVariantUids)
```
Retrieve the unique IDs of all translated VariantSets for this object.

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node creates.

### RemoveCustomVariantSetUid
```angelscript
bool RemoveCustomVariantSetUid(FString VariantUid)
```
Remove the specified unique ID of a translated VariantSet from this object.

