# UInterchangeSceneVariantSetsNode

**继承自**: `UInterchangeBaseNode`

Class to represent a set of VariantSet nodes

## 方法

### AddCustomVariantSetUid
```angelscript
bool AddCustomVariantSetUid(FString VariantUid)
```
Add the specified VariantSet's unique id to this object.

### GetCustomVariantSetUid
```angelscript
void GetCustomVariantSetUid(int Index, FString& OutVariantUid)
```
Retrieve the specified VariantSet's unique id for this object.

### GetCustomVariantSetUidCount
```angelscript
int GetCustomVariantSetUidCount()
```
Retrieve the number of VariantSets for this object.

### GetCustomVariantSetUids
```angelscript
void GetCustomVariantSetUids(TArray<FString>& OutVariantUids)
```
Retrieve all the VariantSets' unique ids for this object.

### RemoveCustomVariantSetUid
```angelscript
bool RemoveCustomVariantSetUid(FString VariantUid)
```
Remove the specified VariantSet's unique id from this object.

