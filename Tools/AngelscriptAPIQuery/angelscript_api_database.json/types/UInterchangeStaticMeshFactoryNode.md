# UInterchangeStaticMeshFactoryNode

**继承自**: `UInterchangeMeshFactoryNode`

namespace UE

## 方法

### AddSocketUid
```angelscript
bool AddSocketUid(FString SocketUid)
```

### AddSocketUids
```angelscript
bool AddSocketUids(TArray<FString> InSocketUids)
```

### GetCustomBuildNanite
```angelscript
bool GetCustomBuildNanite(bool& AttributeValue)
```
Get whether the static mesh factory should set the Nanite build setting. Return false if the attribute was not set.

### GetCustomBuildReversedIndexBuffer
```angelscript
bool GetCustomBuildReversedIndexBuffer(bool& AttributeValue)
```
Get whether the static mesh should build a reversed index buffer.

### GetCustomBuildScale3D
```angelscript
bool GetCustomBuildScale3D(FVector& AttributeValue)
```
Get the local scale that is applied when building the static mesh.

### GetCustomDistanceFieldReplacementMesh
```angelscript
bool GetCustomDistanceFieldReplacementMesh(FSoftObjectPath& AttributeValue)
```
Get the static mesh asset whose distance field will be used as the distance field for the imported mesh.

### GetCustomDistanceFieldResolutionScale
```angelscript
bool GetCustomDistanceFieldResolutionScale(float32& AttributeValue)
```
Get the scale to apply to the mesh when allocating the distance field volume texture.
The default scale is 1, which assumes that the mesh will be placed unscaled in the world.

### GetCustomDstLightmapIndex
```angelscript
bool GetCustomDstLightmapIndex(int& AttributeValue)
```
Get the index of the UV that is used to store generated lightmaps for the static mesh.

### GetCustomGenerateDistanceFieldAsIfTwoSided
```angelscript
bool GetCustomGenerateDistanceFieldAsIfTwoSided(bool& AttributeValue)
```
Get whether to generate the distance field by treating every triangle hit as a front face.
This prevents the distance field from being discarded due to the mesh being open, but also lowers distance field ambient occlusion quality.

### GetCustomGenerateLightmapUVs
```angelscript
bool GetCustomGenerateLightmapUVs(bool& AttributeValue)
```
Get whether the static mesh should generate lightmap UVs.

### GetCustomMaxLumenMeshCards
```angelscript
bool GetCustomMaxLumenMeshCards(int& AttributeValue)
```
Get the maximum number of Lumen mesh cards to generate for this mesh.
More cards means that the surface will have better coverage, but will result in increased runtime overhead.
Set this to 0 to disable mesh card generation for this mesh.
The default is 12.

### GetCustomMinLightmapResolution
```angelscript
bool GetCustomMinLightmapResolution(int& AttributeValue)
```
Get the amount of padding used to pack UVs for the static mesh.

### GetCustomSrcLightmapIndex
```angelscript
bool GetCustomSrcLightmapIndex(int& AttributeValue)
```
Get the index of the UV that is used as the source for generating lightmaps for the static mesh.

### GetCustomSupportFaceRemap
```angelscript
bool GetCustomSupportFaceRemap(bool& AttributeValue)
```
Get whether the static mesh is set up for use with physical material masks.

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node creates.

### GetSocketUidCount
```angelscript
int GetSocketUidCount()
```
Return the number of socket UIDs this static mesh has.

### GetSocketUids
```angelscript
void GetSocketUids(TArray<FString>& OutSocketUids)
```

### InitializeStaticMeshNode
```angelscript
void InitializeStaticMeshNode(FString UniqueID, FString DisplayLabel, FString InAssetClass)
```
Initialize node data.
@param UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.
@param InAssetClass - The class the StaticMesh factory will create for this node.

### RemoveSocketUd
```angelscript
bool RemoveSocketUd(FString SocketUid)
```

### SetCustomBuildNanite
```angelscript
bool SetCustomBuildNanite(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether the static mesh factory should set the Nanite build setting. Return false if the attribute was not set.

### SetCustomBuildReversedIndexBuffer
```angelscript
bool SetCustomBuildReversedIndexBuffer(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether the static mesh should build a reversed index buffer.

### SetCustomBuildScale3D
```angelscript
bool SetCustomBuildScale3D(FVector AttributeValue, bool bAddApplyDelegate)
```
Set the local scale that is applied when building the static mesh.

### SetCustomDistanceFieldReplacementMesh
```angelscript
bool SetCustomDistanceFieldReplacementMesh(FSoftObjectPath AttributeValue, bool bAddApplyDelegate)
```
Set the static mesh asset whose distance field will be used as the distance field for the imported mesh.

### SetCustomDistanceFieldResolutionScale
```angelscript
bool SetCustomDistanceFieldResolutionScale(float32 AttributeValue, bool bAddApplyDelegate)
```
Set the scale to apply to the mesh when allocating the distance field volume texture.
The default scale is 1, which assumes that the mesh will be placed unscaled in the world.

### SetCustomDstLightmapIndex
```angelscript
bool SetCustomDstLightmapIndex(int AttributeValue, bool bAddApplyDelegate)
```
Set the index of the UV that is used to store generated lightmaps for the static mesh.

### SetCustomGenerateDistanceFieldAsIfTwoSided
```angelscript
bool SetCustomGenerateDistanceFieldAsIfTwoSided(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether to generate the distance field by treating every triangle hit as a front face.
This prevents the distance field from being discarded due to the mesh being open, but also lowers distance field ambient occlusion quality.

### SetCustomGenerateLightmapUVs
```angelscript
bool SetCustomGenerateLightmapUVs(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether the static mesh should generate lightmap UVs.

### SetCustomMaxLumenMeshCards
```angelscript
bool SetCustomMaxLumenMeshCards(int AttributeValue, bool bAddApplyDelegate)
```
Set the maximum number of Lumen mesh cards to generate for this mesh.
More cards means that the surface will have better coverage, but will result in increased runtime overhead.
Set this to 0 to disable mesh card generation for this mesh.
The default is 12.

### SetCustomMinLightmapResolution
```angelscript
bool SetCustomMinLightmapResolution(int AttributeValue, bool bAddApplyDelegate)
```
Set the amount of padding used to pack UVs for the static mesh.

### SetCustomSrcLightmapIndex
```angelscript
bool SetCustomSrcLightmapIndex(int AttributeValue, bool bAddApplyDelegate)
```
Set the index of the UV that is used as the source for generating lightmaps for the static mesh.

### SetCustomSupportFaceRemap
```angelscript
bool SetCustomSupportFaceRemap(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether the static mesh is set up for use with physical material masks.

