# UInterchangeMeshFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

namespace Interchange

## 方法

### AddLodDataUniqueId
```angelscript
bool AddLodDataUniqueId(FString LodDataUniqueId)
```

### GetCustomComputeWeightedNormals
```angelscript
bool GetCustomComputeWeightedNormals(bool& AttributeValue)
```
Query whether normals are recomputed by weighting the surface area and the corner angle of the triangle as a ratio.

### GetCustomKeepSectionsSeparate
```angelscript
bool GetCustomKeepSectionsSeparate(bool& AttributeValue)
```
Query whether sections with matching materials are kept separate and will not get combined.

### GetCustomLODGroup
```angelscript
bool GetCustomLODGroup(FName& AttributeValue)
```
Query whether a custom LOD group is set for the mesh.

### GetCustomRecomputeNormals
```angelscript
bool GetCustomRecomputeNormals(bool& AttributeValue)
```
Query whether normals in the imported mesh are ignored and recomputed. When normals are recomputed, the tangents are also recomputed.

### GetCustomRecomputeTangents
```angelscript
bool GetCustomRecomputeTangents(bool& AttributeValue)
```
Query whether tangents in the imported mesh are ignored and recomputed.

### GetCustomRemoveDegenerates
```angelscript
bool GetCustomRemoveDegenerates(bool& AttributeValue)
```
Query whether degenerate triangles are removed.

### GetCustomUseBackwardsCompatibleF16TruncUVs
```angelscript
bool GetCustomUseBackwardsCompatibleF16TruncUVs(bool& AttributeValue)
```
Query whether UVs are converted to 16-bit by a legacy truncation process instead of the default rounding process. This may avoid differences when reimporting older content.

### GetCustomUseFullPrecisionUVs
```angelscript
bool GetCustomUseFullPrecisionUVs(bool& AttributeValue)
```
Query whether UVs are stored at full floating point precision.

### GetCustomUseHighPrecisionTangentBasis
```angelscript
bool GetCustomUseHighPrecisionTangentBasis(bool& AttributeValue)
```
Query whether tangents are stored at 16-bit precision instead of the default 8-bit precision.

### GetCustomUseMikkTSpace
```angelscript
bool GetCustomUseMikkTSpace(bool& AttributeValue)
```
Query whether tangents are recomputed using MikkTSpace when they need to be recomputed.

### GetCustomVertexColorIgnore
```angelscript
bool GetCustomVertexColorIgnore(bool& AttributeValue)
```
Query whether the static mesh factory should ignore the vertex color. Return false if the attribute was not set.

### GetCustomVertexColorOverride
```angelscript
bool GetCustomVertexColorOverride(FColor& AttributeValue)
```
Query whether the static mesh factory should override the vertex color. Return false if the attribute was not set.

### GetCustomVertexColorReplace
```angelscript
bool GetCustomVertexColorReplace(bool& AttributeValue)
```
Query whether the static mesh factory should replace the vertex color. Return false if the attribute was not set.

### GetLodDataCount
```angelscript
int GetLodDataCount()
```
Return the number of LODs this static mesh has.

### GetLodDataUniqueIds
```angelscript
void GetLodDataUniqueIds(TArray<FString>& OutLodDataUniqueIds)
```

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

### RemoveLodDataUniqueId
```angelscript
bool RemoveLodDataUniqueId(FString LodDataUniqueId)
```

### RemoveSlotMaterialDependencyUid
```angelscript
bool RemoveSlotMaterialDependencyUid(FString SlotName)
```
Remove the Material dependency associated with the specfied slot name of this object.

### ResetSlotMaterialDependencies
```angelscript
bool ResetSlotMaterialDependencies()
```
Reset all the material dependencies.

### SetCustomComputeWeightedNormals
```angelscript
bool SetCustomComputeWeightedNormals(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether normals are recomputed by weighting the surface area and the corner angle of the triangle as a ratio.

### SetCustomKeepSectionsSeparate
```angelscript
bool SetCustomKeepSectionsSeparate(bool AttributeValue)
```
Set whether sections with matching materials are kept separate and will not get combined.

### SetCustomLODGroup
```angelscript
bool SetCustomLODGroup(FName AttributeValue, bool bAddApplyDelegate)
```
Set a custom LOD group for the mesh.

### SetCustomRecomputeNormals
```angelscript
bool SetCustomRecomputeNormals(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether normals in the imported mesh are ignored and recomputed. When normals are recomputed, the tangents are also recomputed.

### SetCustomRecomputeTangents
```angelscript
bool SetCustomRecomputeTangents(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether tangents in the imported mesh are ignored and recomputed.

### SetCustomRemoveDegenerates
```angelscript
bool SetCustomRemoveDegenerates(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether degenerate triangles are removed.

### SetCustomUseBackwardsCompatibleF16TruncUVs
```angelscript
bool SetCustomUseBackwardsCompatibleF16TruncUVs(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether UVs are converted to 16-bit by a legacy truncation process instead of the default rounding process. This may avoid differences when reimporting older content.

### SetCustomUseFullPrecisionUVs
```angelscript
bool SetCustomUseFullPrecisionUVs(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether UVs are stored at full floating point precision.

### SetCustomUseHighPrecisionTangentBasis
```angelscript
bool SetCustomUseHighPrecisionTangentBasis(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether tangents are stored at 16-bit precision instead of the default 8-bit precision.

### SetCustomUseMikkTSpace
```angelscript
bool SetCustomUseMikkTSpace(bool AttributeValue, bool bAddApplyDelegate)
```
Set whether tangents are recomputed using MikkTSpace when they need to be recomputed.

### SetCustomVertexColorIgnore
```angelscript
bool SetCustomVertexColorIgnore(bool AttributeValue)
```
Set whether the static mesh factory should ignore the vertex color. Return false if the attribute could not be set.

### SetCustomVertexColorOverride
```angelscript
bool SetCustomVertexColorOverride(FColor AttributeValue)
```
Set whether the static mesh factory should override the vertex color. Return false if the attribute could not be set.

### SetCustomVertexColorReplace
```angelscript
bool SetCustomVertexColorReplace(bool AttributeValue)
```
Set whether the static mesh factory should replace the vertex color. Return false if the attribute could not be set.

### SetSlotMaterialDependencyUid
```angelscript
bool SetSlotMaterialDependencyUid(FString SlotName, FString MaterialDependencyUid)
```
Add a Material dependency to the specified slot of this object.

