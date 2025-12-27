# UInterchangeMeshActorFactoryNode

**继承自**: `UInterchangeActorFactoryNode`

## 方法

### GetCustomAnimationAssetUidToPlay
```angelscript
bool GetCustomAnimationAssetUidToPlay(FString& AttributeValue)
```
Get the animation asset set for this scene node to play.

### GetCustomGeometricTransform
```angelscript
bool GetCustomGeometricTransform(FTransform& AttributeValue)
```
Get the geometric offset. Any mesh attached to this scene node will be offset using this transform.

### GetSlotMaterialDependencies
```angelscript
void GetSlotMaterialDependencies(TMap<FString,FString>& OutMaterialDependencies)
```
Retrieve the correspondence table between slot names and assigned materials for this object.

### GetSlotMaterialDependencyUid
```angelscript
bool GetSlotMaterialDependencyUid(FString SlotName, FString& OutMaterialDependency)
```
Retrieve the Material dependency for the specified slot of this object.

### RemoveSlotMaterialDependencyUid
```angelscript
bool RemoveSlotMaterialDependencyUid(FString SlotName)
```
Remove the Material dependency associated with the specified slot name from this object.

### SetCustomAnimationAssetUidToPlay
```angelscript
bool SetCustomAnimationAssetUidToPlay(FString AttributeValue)
```
Set the animation asset for this scene node to play. (This is only relevant for SkeletalMeshActors: scene nodes that are instantiating skeletal meshes.)

### SetCustomGeometricTransform
```angelscript
bool SetCustomGeometricTransform(FTransform AttributeValue)
```
Set the geometric offset. Any mesh attached to this scene node will be offset using this transform.

### SetSlotMaterialDependencyUid
```angelscript
bool SetSlotMaterialDependencyUid(FString SlotName, FString MaterialDependencyUid)
```
Add a Material dependency to the specified slot of this object.

