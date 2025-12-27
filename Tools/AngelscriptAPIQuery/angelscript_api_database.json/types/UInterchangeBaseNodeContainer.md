# UInterchangeBaseNodeContainer

**继承自**: `UObject`

The Interchange UInterchangeBaseNode graph is a format used to feed factories and writers when they import, reimport, and
export an asset or scene.

This container holds a flat list of all nodes that have been translated from the source data.
Translators fill this container, and the import/export managers read it to execute the import/export process.

## 方法

### AddNode
```angelscript
FString AddNode(UInterchangeBaseNode Node)
```
Add a node to the container. The node is added into a TMap.

@param Node - a pointer on the node you want to add
@return: return the node unique ID of the added item. If the node already exist it will return the existing ID. Return InvalidNodeUid if the node cannot be added.

### ComputeChildrenCache
```angelscript
void ComputeChildrenCache()
```
Fill the cache of children UIDs to optimize the GetNodeChildrenUids call.

### GetFactoryNode
```angelscript
UInterchangeFactoryBaseNode GetFactoryNode(FString NodeUniqueID)
```
Get a factory node pointer.

### GetNode
```angelscript
const UInterchangeBaseNode GetNode(FString NodeUniqueID)
```
Get a node pointer. Once added to the container, nodes are considered const.

### GetNodeChildren
```angelscript
UInterchangeBaseNode GetNodeChildren(FString NodeUniqueID, int ChildIndex)
```
Get the nth const child of the node

### GetNodeChildrenCount
```angelscript
int GetNodeChildrenCount(FString NodeUniqueID)
```
Get the number of children the node has.

### GetNodeChildrenUids
```angelscript
TArray<FString> GetNodeChildrenUids(FString NodeUniqueID)
```
Get the UIDs of all the node's children.

### GetNodes
```angelscript
void GetNodes(const UClass ClassNode, TArray<FString>& OutNodes)
```
Return all nodes that are of the ClassNode type.

### GetRoots
```angelscript
void GetRoots(TArray<FString>& RootNodes)
```
Return all nodes that do not have any parent.

### IsNodeUidValid
```angelscript
bool IsNodeUidValid(FString NodeUniqueID)
```
Return true if the node unique ID exists in the container.

### LoadFromFile
```angelscript
void LoadFromFile(FString Filename)
```
Serialize the node container from the specified file.

### ReplaceNode
```angelscript
void ReplaceNode(FString NodeUniqueID, UInterchangeFactoryBaseNode NewNode)
```

### Reset
```angelscript
void Reset()
```
Empty the container.

### ResetChildrenCache
```angelscript
void ResetChildrenCache()
```
Reset the cache of children UIDs.

### SaveToFile
```angelscript
void SaveToFile(FString Filename)
```
Serialize the node container into the specified file.

### SetNodeParentUid
```angelscript
bool SetNodeParentUid(FString NodeUniqueID, FString NewParentNodeUid)
```
Set the ParentUid of the node.

