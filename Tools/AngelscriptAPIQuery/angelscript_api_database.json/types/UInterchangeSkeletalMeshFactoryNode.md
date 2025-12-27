# UInterchangeSkeletalMeshFactoryNode

**继承自**: `UInterchangeMeshFactoryNode`

## 方法

### GetCustomBoneInfluenceLimit
```angelscript
bool GetCustomBoneInfluenceLimit(int& AttributeValue)
```
Query the maximum number of bone influences to allow each vertex in this mesh to use.
If set higher than the limit determined by the project settings, it has no effect.
If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.

### GetCustomCreatePhysicsAsset
```angelscript
bool GetCustomCreatePhysicsAsset(bool& AttributeValue)
```
Query whether the skeletal mesh factory should create a physics asset. Return false if the attribute was not set.

### GetCustomImportContentType
```angelscript
bool GetCustomImportContentType(EInterchangeSkeletalMeshContentType& AttributeValue)
```
Query the skeletal mesh import content type. This content type determines whether the factory imports partial or full translated content. Return false if the attribute was not set.

### GetCustomImportMorphTarget
```angelscript
bool GetCustomImportMorphTarget(bool& AttributeValue)
```
Query whether the skeletal mesh factory should create morph targets. Return false if the attribute was not set.

### GetCustomImportVertexAttributes
```angelscript
bool GetCustomImportVertexAttributes(bool& AttributeValue)
```
Query whether the skeletal mesh factory should import vertex attributes. Return false if the attribute was not set.

### GetCustomMorphThresholdPosition
```angelscript
bool GetCustomMorphThresholdPosition(float32& AttributeValue)
```
Query the skeletal mesh threshold value that is used to compare vertex position equality when computing morph target deltas.

### GetCustomPhysicAssetSoftObjectPath
```angelscript
bool GetCustomPhysicAssetSoftObjectPath(FSoftObjectPath& AttributeValue)
```
Query a physics asset the skeletal mesh factory should use. Return false if the attribute was not set.

### GetCustomSkeletonSoftObjectPath
```angelscript
bool GetCustomSkeletonSoftObjectPath(FSoftObjectPath& AttributeValue)
```
Query the skeletal mesh factory skeleton UObject. Return false if the attribute was not set.

### GetCustomThresholdPosition
```angelscript
bool GetCustomThresholdPosition(float32& AttributeValue)
```
Query the skeletal mesh threshold value that is used to decide whether two vertex positions are equal.

### GetCustomThresholdTangentNormal
```angelscript
bool GetCustomThresholdTangentNormal(float32& AttributeValue)
```
Query the skeletal mesh threshold value that is used to decide whether two normals, tangents, or bi-normals are equal.

### GetCustomThresholdUV
```angelscript
bool GetCustomThresholdUV(float32& AttributeValue)
```
Query the skeletal mesh threshold value that is used to decide whether two UVs are equal.

### GetCustomUseHighPrecisionSkinWeights
```angelscript
bool GetCustomUseHighPrecisionSkinWeights(bool& AttributeValue)
```
Query the skeletal mesh UseHighPrecisionSkinWeights setting.

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node creates.

### InitializeSkeletalMeshNode
```angelscript
void InitializeSkeletalMeshNode(FString UniqueID, FString DisplayLabel, FString InAssetClass)
```
Initialize node data.
@param: UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.
@param InAssetClass - The class the SkeletalMesh factory will create for this node.

### SetCustomBoneInfluenceLimit
```angelscript
bool SetCustomBoneInfluenceLimit(int AttributeValue, bool bAddApplyDelegate)
```
Set the maximum number of bone influences to allow each vertex in this mesh to use.
If set higher than the limit determined by the project settings, it has no effect.
If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.

### SetCustomCreatePhysicsAsset
```angelscript
bool SetCustomCreatePhysicsAsset(bool AttributeValue)
```
Set whether the skeletal mesh factory should create a physics asset. Return false if the attribute could not be set.

### SetCustomImportContentType
```angelscript
bool SetCustomImportContentType(EInterchangeSkeletalMeshContentType AttributeValue)
```
Set the skeletal mesh import content type. This content type determines whether the factory imports partial or full translated content. Return false if the attribute could not be set.

### SetCustomImportMorphTarget
```angelscript
bool SetCustomImportMorphTarget(bool AttributeValue)
```
Set whether the skeletal mesh factory should create morph targets. Return false if the attribute could not be set.

### SetCustomImportVertexAttributes
```angelscript
bool SetCustomImportVertexAttributes(bool AttributeValue)
```
Set whether the skeletal mesh factory should import vertex attributes. Return false if the attribute could not be set.

### SetCustomMorphThresholdPosition
```angelscript
bool SetCustomMorphThresholdPosition(float32 AttributeValue, bool bAddApplyDelegate)
```
Set the skeletal mesh threshold value that is used to compare vertex position equality when computing morph target deltas.

### SetCustomPhysicAssetSoftObjectPath
```angelscript
bool SetCustomPhysicAssetSoftObjectPath(FSoftObjectPath AttributeValue)
```
Set a physics asset the skeletal mesh factory should use. Return false if the attribute could not be set.

### SetCustomSkeletonSoftObjectPath
```angelscript
bool SetCustomSkeletonSoftObjectPath(FSoftObjectPath AttributeValue)
```
Set the skeletal mesh factory skeleton UObject. Return false if the attribute could not be set.

### SetCustomThresholdPosition
```angelscript
bool SetCustomThresholdPosition(float32 AttributeValue, bool bAddApplyDelegate)
```
Set the skeletal mesh threshold value that is used to decide whether two vertex positions are equal.

### SetCustomThresholdTangentNormal
```angelscript
bool SetCustomThresholdTangentNormal(float32 AttributeValue, bool bAddApplyDelegate)
```
Set the skeletal mesh threshold value that is used to decide whether two normals, tangents, or bi-normals are equal.

### SetCustomThresholdUV
```angelscript
bool SetCustomThresholdUV(float32 AttributeValue, bool bAddApplyDelegate)
```
Set the skeletal mesh threshold value that is used to decide whether two UVs are equal.

### SetCustomUseHighPrecisionSkinWeights
```angelscript
bool SetCustomUseHighPrecisionSkinWeights(bool AttributeValue, bool bAddApplyDelegate)
```
Set the skeletal mesh UseHighPrecisionSkinWeights setting.

