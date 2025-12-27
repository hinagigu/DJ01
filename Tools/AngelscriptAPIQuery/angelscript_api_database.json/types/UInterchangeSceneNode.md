# UInterchangeSceneNode

**继承自**: `UInterchangeBaseNode`

The scene node represents a transform node in the scene.
Scene nodes can have user-defined attributes. Use UInterchangeUserDefinedAttributesAPI to get and set user-defined attribute data.

## 方法

### AddSpecializedType
```angelscript
bool AddSpecializedType(FString SpecializedType)
```

### GetCustomAnimationAssetUidToPlay
```angelscript
bool GetCustomAnimationAssetUidToPlay(FString& AttributeValue)
```
Get the Animation Asset To Play by this Scene Node.

### GetCustomAssetInstanceUid
```angelscript
bool GetCustomAssetInstanceUid(FString& AttributeValue)
```
Get which asset, if any, a scene node is instantiating. Return false if the Attribute was not set previously.

### GetCustomBindPoseGlobalTransform
```angelscript
bool GetCustomBindPoseGlobalTransform(const UInterchangeBaseNodeContainer BaseNodeContainer, FTransform GlobalOffsetTransform, FTransform& AttributeValue, bool bForceRecache)
```
Get the global transform of the bind pose scene node. This value is computed from the local transforms of all parent bind poses.

### GetCustomBindPoseLocalTransform
```angelscript
bool GetCustomBindPoseLocalTransform(FTransform& AttributeValue)
```
Get the local transform of the bind pose scene node.

### GetCustomGeometricTransform
```angelscript
bool GetCustomGeometricTransform(FTransform& AttributeValue)
```
Get the geometric offset. Any mesh attached to this scene node will be offset using this transform.

### GetCustomGlobalTransform
```angelscript
bool GetCustomGlobalTransform(const UInterchangeBaseNodeContainer BaseNodeContainer, FTransform GlobalOffsetTransform, FTransform& AttributeValue, bool bForceRecache)
```
Get the default scene node global transform. This value is computed from the local transforms of all parent scene nodes.

### GetCustomLocalTransform
```angelscript
bool GetCustomLocalTransform(FTransform& AttributeValue)
```
Get the default scene node local transform.
The default transform is the local transform of the node (no bind pose, no time evaluation).

### GetCustomTimeZeroGlobalTransform
```angelscript
bool GetCustomTimeZeroGlobalTransform(const UInterchangeBaseNodeContainer BaseNodeContainer, FTransform GlobalOffsetTransform, FTransform& AttributeValue, bool bForceRecache)
```
Get the global transform of the time-zero scene node. This value is computed from the local transforms of all parent time-zero scene nodes.

### GetCustomTimeZeroLocalTransform
```angelscript
bool GetCustomTimeZeroLocalTransform(FTransform& AttributeValue)
```
Get the local transform of the time-zero scene node.

### GetMorphTargetCurveWeights
```angelscript
void GetMorphTargetCurveWeights(TMap<FString,float32>& OutMorphTargetCurveWeights)
```
Get MorphTargets and their weights.

### GetSlotMaterialDependencies
```angelscript
void GetSlotMaterialDependencies(TMap<FString,FString>& OutMaterialDependencies)
```
Retrieve the correspondence table between slot names and assigned materials for this object.

### GetSlotMaterialDependencyUid
```angelscript
bool GetSlotMaterialDependencyUid(FString SlotName, FString& OutMaterialDependency)
```
Retrieve the Material dependency for a given slot of this object.

### GetSpecializedType
```angelscript
void GetSpecializedType(int Index, FString& OutSpecializedType)
```

### GetSpecializedTypeCount
```angelscript
int GetSpecializedTypeCount()
```
Get the specialized type this scene node represents (for example, Joint or LODGroup).

### GetSpecializedTypes
```angelscript
void GetSpecializedTypes(TArray<FString>& OutSpecializedTypes)
```

### IsSpecializedTypeContains
```angelscript
bool IsSpecializedTypeContains(FString SpecializedType)
```

### RemoveSlotMaterialDependencyUid
```angelscript
bool RemoveSlotMaterialDependencyUid(FString SlotName)
```
Remove the Material dependency associated with the given slot name from this object.

### RemoveSpecializedType
```angelscript
bool RemoveSpecializedType(FString SpecializedType)
```

### SetCustomAnimationAssetUidToPlay
```angelscript
bool SetCustomAnimationAssetUidToPlay(FString AttributeValue)
```
Set the Animation Asset To Play by this Scene Node. Only relevant for SkeletalMeshActors (that is, SceneNodes that are instantiating Skeletal Meshes).

### SetCustomAssetInstanceUid
```angelscript
bool SetCustomAssetInstanceUid(FString AttributeValue)
```
Add an asset for this scene node to instantiate.

### SetCustomBindPoseLocalTransform
```angelscript
bool SetCustomBindPoseLocalTransform(const UInterchangeBaseNodeContainer BaseNodeContainer, FTransform AttributeValue, bool bResetCache)
```
Set the local transform of the bind pose scene node.

### SetCustomGeometricTransform
```angelscript
bool SetCustomGeometricTransform(FTransform AttributeValue)
```
Set the geometric offset. Any mesh attached to this scene node will be offset using this transform.

### SetCustomLocalTransform
```angelscript
bool SetCustomLocalTransform(const UInterchangeBaseNodeContainer BaseNodeContainer, FTransform AttributeValue, bool bResetCache)
```
Set the default scene node local transform.
The default transform is the local transform of the node (no bind pose, no time evaluation).

### SetCustomTimeZeroLocalTransform
```angelscript
bool SetCustomTimeZeroLocalTransform(const UInterchangeBaseNodeContainer BaseNodeContainer, FTransform AttributeValue, bool bResetCache)
```
Set the local transform of the time-zero scene node.

### SetMorphTargetCurveWeight
```angelscript
bool SetMorphTargetCurveWeight(FString MorphTargetName, float32 Weight)
```
Set MorphTarget with given weight.

### SetSlotMaterialDependencyUid
```angelscript
bool SetSlotMaterialDependencyUid(FString SlotName, FString MaterialDependencyUid)
```
Add the specified Material dependency to a specific slot name of this object.

