# UInterchangeBaseNode

**继承自**: `UObject`

This struct is used to store and retrieve key-value attributes. The attributes are stored in a generic FAttributeStorage that serializes the values in a TArray64<uint8>.
See UE::Interchange::EAttributeTypes to know the supported template types.
This is an abstract class. This is the base class of the interchange node graph format; all classes in this format should derive from this class.

## 方法

### AddBooleanAttribute
```angelscript
bool AddBooleanAttribute(FString NodeAttributeKey, bool Value)
```
Add a Boolean attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### AddDoubleAttribute
```angelscript
bool AddDoubleAttribute(FString NodeAttributeKey, float Value)
```
Add a double attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### AddFloatAttribute
```angelscript
bool AddFloatAttribute(FString NodeAttributeKey, float32 Value)
```
Add a float attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### AddGuidAttribute
```angelscript
bool AddGuidAttribute(FString NodeAttributeKey, FGuid Value)
```
Add a GUID attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### AddInt32Attribute
```angelscript
bool AddInt32Attribute(FString NodeAttributeKey, int Value)
```
Add a int32 attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### AddLinearColorAttribute
```angelscript
bool AddLinearColorAttribute(FString NodeAttributeKey, FLinearColor Value)
```
Add an FLinearColor attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### AddStringAttribute
```angelscript
bool AddStringAttribute(FString NodeAttributeKey, FString Value)
```
Add a string attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### AddTargetNodeUid
```angelscript
bool AddTargetNodeUid(FString AssetUid)
```
Add an asset node UID relating to this object.

### AddVector2Attribute
```angelscript
bool AddVector2Attribute(FString NodeAttributeKey, FVector2f Value)
```
Add a Vector2 attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

### GetAssetName
```angelscript
FString GetAssetName()
```
Optional. Any node that can import or export an asset should set the desired name for the asset.
If the attribute was never set, returns GetDisplayLabel().

### GetBooleanAttribute
```angelscript
bool GetBooleanAttribute(FString NodeAttributeKey, bool& OutValue)
```
Get a Boolean attribute from this node. Returns false if the attribute does not exist.

### GetDisplayLabel
```angelscript
FString GetDisplayLabel()
```
Return the display label.

### GetDoubleAttribute
```angelscript
bool GetDoubleAttribute(FString NodeAttributeKey, float& OutValue)
```
Get a double attribute from this node. Returns false if the attribute does not exist.

### GetFloatAttribute
```angelscript
bool GetFloatAttribute(FString NodeAttributeKey, float32& OutValue)
```
Get a float attribute from this node. Returns false if the attribute does not exist.

### GetGuidAttribute
```angelscript
bool GetGuidAttribute(FString NodeAttributeKey, FGuid& OutValue)
```
Get a GUID attribute from this node. Returns false if the attribute does not exist.

### GetInt32Attribute
```angelscript
bool GetInt32Attribute(FString NodeAttributeKey, int& OutValue)
```
Get a int32 attribute from this node. Returns false if the attribute does not exist.

### GetLinearColorAttribute
```angelscript
bool GetLinearColorAttribute(FString NodeAttributeKey, FLinearColor& OutValue)
```
Get an FLinearColor attribute from this node. Returns false if the attribute does not exist.

### GetNodeContainerType
```angelscript
EInterchangeNodeContainerType GetNodeContainerType()
```
Return the node container type that defines the purpose of the node (factory node, translated scene node, or translated asset node).

### GetParentUid
```angelscript
FString GetParentUid()
```
Return the parent unique ID. If the attribute does not exist, returns InvalidNodeUid().

### GetStringAttribute
```angelscript
bool GetStringAttribute(FString NodeAttributeKey, FString& OutValue)
```
Get a string attribute from this node. Returns false if the attribute does not exist.

### GetTargetNodeCount
```angelscript
int GetTargetNodeCount()
```
Get the number of target assets relating to this object.

### GetTargetNodeUids
```angelscript
void GetTargetNodeUids(TArray<FString>& OutTargetAssets)
```
Get the target assets relating to this object.

### GetUniqueID
```angelscript
FString GetUniqueID()
```
Return the unique ID passed in the constructor.

### GetVector2Attribute
```angelscript
bool GetVector2Attribute(FString NodeAttributeKey, FVector2f& OutValue)
```
Get a Vector2 attribute from this node. Returns false if the attribute does not exist.

### InitializeNode
```angelscript
void InitializeNode(FString UniqueID, FString DisplayLabel, EInterchangeNodeContainerType NodeContainerType)
```
Initialize the base data of the node.
@param UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.

### IsEnabled
```angelscript
bool IsEnabled()
```
If true, the node is imported or exported. If false, it is discarded.
Returns false if the node was disabled. Returns true if the attribute is not there or if it was enabled.

### RemoveAttribute
```angelscript
bool RemoveAttribute(FString NodeAttributeKey)
```
Remove the specified attribute from this node. Returns false if it could not be removed. If the attribute does not exist, returns true.

### RemoveTargetNodeUid
```angelscript
bool RemoveTargetNodeUid(FString AssetUid)
```
Remove an asset node UID relating to this object.

### SetAssetName
```angelscript
bool SetAssetName(FString AssetName)
```
Set the name for the imported asset this node represents. The asset factory will call GetAssetName().

### SetDisplayLabel
```angelscript
bool SetDisplayLabel(FString DisplayName)
```
Change the display label.

### SetEnabled
```angelscript
bool SetEnabled(bool bIsEnabled)
```
Determine whether this node should be part of the import or export process.
@param bIsEnabled - If true, this node is imported or exported. If false, it is discarded.
@return true if the attribute was set, or false otherwise.

### SetParentUid
```angelscript
bool SetParentUid(FString ParentUid)
```

