# UInterchangeSkeletonFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

## 方法

### GetCustomRootJointUid
```angelscript
bool GetCustomRootJointUid(FString& AttributeValue)
```
Return false if the attribute was not set previously.

### GetCustomSkeletalMeshFactoryNodeUid
```angelscript
bool GetCustomSkeletalMeshFactoryNodeUid(FString& AttributeValue)
```

### GetCustomUseTimeZeroForBindPose
```angelscript
bool GetCustomUseTimeZeroForBindPose(bool& AttributeValue)
```
Query whether this skeleton should replace joint transforms with time-zero evaluation instead of bind pose.

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node creates.

### InitializeSkeletonNode
```angelscript
void InitializeSkeletonNode(FString UniqueID, FString DisplayLabel, FString InAssetClass)
```
Initialize node data.
@param: UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.
@param InAssetClass - The class the Skeleton factory will create for this node.

### SetCustomRootJointUid
```angelscript
bool SetCustomRootJointUid(FString AttributeValue)
```

### SetCustomSkeletalMeshFactoryNodeUid
```angelscript
bool SetCustomSkeletalMeshFactoryNodeUid(FString AttributeValue)
```

### SetCustomUseTimeZeroForBindPose
```angelscript
bool SetCustomUseTimeZeroForBindPose(bool AttributeValue)
```
If AttributeValue is true, force this skeleton to use time-zero evaluation instead of its bind pose.

