# UInterchangePhysicsAssetFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

## 方法

### GetCustomSkeletalMeshUid
```angelscript
bool GetCustomSkeletalMeshUid(FString& AttributeValue)
```
Get the Skeletal Mesh asset UID used to create the data in the post-pipeline step.

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node creates.

### InitializePhysicsAssetNode
```angelscript
void InitializePhysicsAssetNode(FString UniqueID, FString DisplayLabel, FString InAssetClass)
```
Initialize node data.
@param: UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.
@param InAssetClass - The class the Skeleton factory will create for this node.

### SetCustomSkeletalMeshUid
```angelscript
bool SetCustomSkeletalMeshUid(FString AttributeValue)
```
Set the Skeletal Mesh asset UID used to create the data in the post-pipeline step.

