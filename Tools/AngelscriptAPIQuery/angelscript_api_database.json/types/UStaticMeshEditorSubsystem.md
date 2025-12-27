# UStaticMeshEditorSubsystem

**继承自**: `UEditorSubsystem`

UStaticMeshEditorSubsystem
Subsystem for exposing static mesh functionality to scripts

## 方法

### AddSimpleCollisions
```angelscript
int AddSimpleCollisions(UStaticMesh StaticMesh, EScriptCollisionShapeType ShapeType)
```
Same as AddSimpleCollisionsWithNotification but changes are automatically applied.

### AddSimpleCollisionsWithNotification
```angelscript
int AddSimpleCollisionsWithNotification(UStaticMesh StaticMesh, EScriptCollisionShapeType ShapeType, bool bApplyChanges)
```
Add simple collisions to a static mesh.
This method replicates what is done when invoking menu entries "Collision > Add [...] Simplified Collision" in the Mesh Editor.
@param       StaticMesh                      Mesh to generate simple collision for.
@param       ShapeType                       Options on which simple collision to add to the mesh.
@param       bApplyChanges           Indicates if changes must be apply or not.
@return An integer indicating the index of the collision newly created.
A negative value indicates the addition failed.

### AddUVChannel
```angelscript
bool AddUVChannel(UStaticMesh StaticMesh, int LODIndex)
```
Adds an empty UV channel at the end of the existing channels on the given LOD of a StaticMesh.
@param       StaticMesh                      Static mesh on which to add a UV channel.
@param       LODIndex                        Index of the StaticMesh LOD.
@return true if a UV channel was added.

### BulkSetConvexDecompositionCollisions
```angelscript
bool BulkSetConvexDecompositionCollisions(TArray<UStaticMesh> StaticMeshes, int HullCount, int MaxHullVerts, int HullPrecision)
```
Same as SetConvexDecompositionCollisionsWithNotification but changes are automatically applied.

### BulkSetConvexDecompositionCollisionsWithNotification
```angelscript
bool BulkSetConvexDecompositionCollisionsWithNotification(TArray<UStaticMesh> StaticMeshes, int HullCount, int MaxHullVerts, int HullPrecision, bool bApplyChanges)
```
Compute convex collisions for a set of static meshes.
Any existing collisions will be removed from the static meshes.
This method replicates what is done when invoking menu entry "Collision > Auto Convex Collision" in the Mesh Editor.
@param       StaticMeshes                    Set of Static mesh to add convex collision on.
@param       HullCount                               Maximum number of convex pieces that will be created. Must be positive.
@param       MaxHullVerts                    Maximum number of vertices allowed for any generated convex hull.
@param       HullPrecision                   Number of voxels to use when generating collision. Must be positive.
@param       bApplyChanges                   Indicates if changes must be apply or not.
@return A boolean indicating if the addition was successful or not.

### CreateProxyMeshActor
```angelscript
bool CreateProxyMeshActor(TArray<AStaticMeshActor> ActorsToMerge, FCreateProxyMeshActorOptions MergeOptions, AStaticMeshActor& OutMergedActor)
```
Build a proxy mesh actor that can replace a set of mesh actors.
@param   ActorsToMerge  List of actors to build a proxy for.
@param   MergeOptions
@param   OutMergedActor generated actor if requested
@return  Success of the proxy creation

### EnableSectionCastShadow
```angelscript
void EnableSectionCastShadow(UStaticMesh StaticMesh, bool bCastShadow, int LODIndex, int SectionIndex)
```
Enables/disables mesh section shadow casting for a specific LOD.
@param       StaticMesh                      Static mesh to Enables/disables shadow casting from.
@param       bCastShadow                     If the section should cast shadow.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       SectionIndex            Index of the StaticMesh Section.

### EnableSectionCollision
```angelscript
void EnableSectionCollision(UStaticMesh StaticMesh, bool bCollisionEnabled, int LODIndex, int SectionIndex)
```
Enables/disables mesh section collision for a specific LOD.
@param       StaticMesh                      Static mesh to Enables/disables collisions from.
@param       bCollisionEnabled       If the collision is enabled or not.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       SectionIndex            Index of the StaticMesh Section.

### GenerateBoxUVChannel
```angelscript
bool GenerateBoxUVChannel(UStaticMesh StaticMesh, int LODIndex, int UVChannelIndex, FVector Position, FRotator Orientation, FVector Size)
```
Generates box UV mapping in the specified UV channel on the given LOD of a StaticMesh.
@param       StaticMesh                      Static mesh on which to generate the UV mapping.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       UVChannelIndex          Channel where to save the UV mapping.
@param       Position                        Position of the center of the projection gizmo.
@param       Orientation                     Rotation to apply to the projection gizmo.
@param       Size                            The size of the box projection gizmo.
@return true if the UV mapping was generated.

### GenerateCylindricalUVChannel
```angelscript
bool GenerateCylindricalUVChannel(UStaticMesh StaticMesh, int LODIndex, int UVChannelIndex, FVector Position, FRotator Orientation, FVector2D Tiling)
```
Generates cylindrical UV mapping in the specified UV channel on the given LOD of a StaticMesh.
@param       StaticMesh                      Static mesh on which to generate the UV mapping.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       UVChannelIndex          Channel where to save the UV mapping.
@param       Position                        Position of the center of the projection gizmo.
@param       Orientation                     Rotation to apply to the projection gizmo.
@param       Tiling                          The UV tiling to use to generate the UV mapping.
@return true if the UV mapping was generated.

### GeneratePlanarUVChannel
```angelscript
bool GeneratePlanarUVChannel(UStaticMesh StaticMesh, int LODIndex, int UVChannelIndex, FVector Position, FRotator Orientation, FVector2D Tiling)
```
Generates planar UV mapping in the specified UV channel on the given LOD of a StaticMesh.
@param       StaticMesh                      Static mesh on which to generate the UV mapping.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       UVChannelIndex          Channel where to save the UV mapping.
@param       Position                        Position of the center of the projection gizmo.
@param       Orientation                     Rotation to apply to the projection gizmo.
@param       Tiling                          The UV tiling to use to generate the UV mapping.
@return true if the UV mapping was generated.

### GetCollisionComplexity
```angelscript
ECollisionTraceFlag GetCollisionComplexity(UStaticMesh StaticMesh)
```
Get the Collision Trace behavior of a static mesh
@param       StaticMesh                              Mesh to query on.
@return the Collision Trace behavior.

### GetConvexCollisionCount
```angelscript
int GetConvexCollisionCount(UStaticMesh StaticMesh)
```
Get number of convex collisions present on a static mesh.
@param       StaticMesh                              Mesh to query on.
@return An integer representing the number of convex collisions on the input static mesh.
An negative value indicates that the command could not be executed. See log for explanation.

### GetLodBuildSettings
```angelscript
void GetLodBuildSettings(const UStaticMesh StaticMesh, int LodIndex, FMeshBuildSettings& OutBuildOptions)
```
Copy the build options with the specified LOD build settings.
@param StaticMesh - Mesh to process.
@param LodIndex - The LOD we get the reduction settings.
@param OutBuildOptions - The build settings where we copy the build options.

### GetLodCount
```angelscript
int GetLodCount(UStaticMesh StaticMesh)
```
Get number of LODs present on a static mesh.
@param       StaticMesh                              Mesh to process.
@return the number of LODs present on the input mesh.
An negative value indicates that the command could not be executed. See log for explanation.

### GetLODGroup
```angelscript
FName GetLODGroup(UStaticMesh StaticMesh)
```
Get the LODGroup for the specified static mesh
@param StaticMesh
@return LODGroup

### GetLODMaterialSlot
```angelscript
int GetLODMaterialSlot(UStaticMesh StaticMesh, int LODIndex, int SectionIndex)
```
Gets the material slot used for a specific LOD section.
@param       StaticMesh                      Static mesh to get the material index from.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       SectionIndex            Index of the StaticMesh Section.
@return  MaterialSlotIndex   Index of the material slot used by the section or INDEX_NONE in case of error.

### GetLodReductionSettings
```angelscript
void GetLodReductionSettings(const UStaticMesh StaticMesh, int LodIndex, FMeshReductionSettings& OutReductionOptions)
```
Copy the reduction options with the specified LOD reduction settings.
@param StaticMesh - Mesh to process.
@param LodIndex - The LOD we get the reduction settings.
@param OutReductionOptions - The reduction settings where we copy the reduction options.

### GetLodScreenSizes
```angelscript
TArray<float32> GetLodScreenSizes(UStaticMesh StaticMesh)
```
Get an array of LOD screen sizes for evaluation.
@param       StaticMesh                      Mesh to process.
@return array of LOD screen sizes.

### GetNaniteSettings
```angelscript
FMeshNaniteSettings GetNaniteSettings(UStaticMesh StaticMesh)
```
Get the Nanite Settings for the mesh
@param StaticMesh        Mesh to access
@return FMeshNaniteSettings struct for the given static mesh

### GetNumberMaterials
```angelscript
int GetNumberMaterials(UStaticMesh StaticMesh)
```
Get number of Materials for a StaticMesh

### GetNumberVerts
```angelscript
int GetNumberVerts(UStaticMesh StaticMesh, int LODIndex)
```
Get number of StaticMesh verts for an LOD

### GetNumUVChannels
```angelscript
int GetNumUVChannels(UStaticMesh StaticMesh, int LODIndex)
```
Returns the number of UV channels for the given LOD of a StaticMesh.
@param       StaticMesh                      Static mesh to query.
@param       LODIndex                        Index of the StaticMesh LOD.
@return the number of UV channels.

### GetSimpleCollisionCount
```angelscript
int GetSimpleCollisionCount(UStaticMesh StaticMesh)
```
Get number of simple collisions present on a static mesh.
@param       StaticMesh                              Mesh to query on.
@return An integer representing the number of simple collisions on the input static mesh.
An negative value indicates that the command could not be executed. See log for explanation.

### HasInstanceVertexColors
```angelscript
bool HasInstanceVertexColors(UStaticMeshComponent StaticMeshComponent)
```
Check whether a static mesh component has vertex colors

### HasVertexColors
```angelscript
bool HasVertexColors(UStaticMesh StaticMesh)
```
Check whether a static mesh has vertex colors

### ImportLOD
```angelscript
int ImportLOD(UStaticMesh BaseStaticMesh, int LODIndex, FString SourceFilename)
```
Import or re-import a LOD into the specified base mesh. If the LOD do not exist it will import it and add it to the base static mesh. If the LOD already exist it will re-import the specified LOD.

@param BaseStaticMesh: The static mesh we import or re-import a LOD.
@param LODIndex: The index of the LOD to import or re-import. Valid value should be between 0 and the base static mesh LOD number. Invalid value will return INDEX_NONE
@param SourceFilename: The fbx source filename. If we are re-importing an existing LOD, it can be empty in this case it will use the last import file. Otherwise it must be an existing fbx file.

@return the index of the LOD that was imported or re-imported. Will return INDEX_NONE if anything goes bad.

### InsertUVChannel
```angelscript
bool InsertUVChannel(UStaticMesh StaticMesh, int LODIndex, int UVChannelIndex)
```
Inserts an empty UV channel at the specified channel index on the given LOD of a StaticMesh.
@param       StaticMesh                      Static mesh on which to insert a UV channel.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       UVChannelIndex          Index where to insert the UV channel.
@return true if a UV channel was added.

### IsSectionCollisionEnabled
```angelscript
bool IsSectionCollisionEnabled(UStaticMesh StaticMesh, int LODIndex, int SectionIndex)
```
Checks if a specific LOD mesh section has collision.
@param       StaticMesh                      Static mesh to remove collisions from.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       SectionIndex            Index of the StaticMesh Section.
@return True if the collision is enabled for the specified LOD of the StaticMesh section.

### JoinStaticMeshActors
```angelscript
AActor JoinStaticMeshActors(TArray<AStaticMeshActor> ActorsToJoin, FJoinStaticMeshActorsOptions JoinOptions)
```
Create a new Actor in the level that contains a duplicate of all the Actors Static Meshes Component.
The ActorsToJoin need to be in the same Level.
This will have a low impact on performance but may help the edition by grouping the meshes under a single Actor.
@param       ActorsToJoin                    List of Actors to join.
@param       JoinOptions                             Options on how to join the actors.
@return The new created actor.

### MergeStaticMeshActors
```angelscript
bool MergeStaticMeshActors(TArray<AStaticMeshActor> ActorsToMerge, FMergeStaticMeshActorsOptions MergeOptions, AStaticMeshActor& OutMergedActor)
```
Merge the meshes into a unique mesh with the provided StaticMeshActors. There are multiple options on how to merge the meshes and their materials.
The ActorsToMerge need to be in the same Level.
This may have a high impact on performance depending of the MeshMergingSettings options.
@param       ActorsToMerge                   List of Actors to merge.
@param       MergeOptions                    Options on how to merge the actors.
@param       OutMergedActor                  The new created actor, if requested.
@return      if the operation is successful.

### ReimportAllCustomLODs
```angelscript
bool ReimportAllCustomLODs(UStaticMesh StaticMesh)
```
Re-import all the custom LODs present in the specified static mesh.

@param StaticMesh: is the static mesh we import or re-import all LODs.

@return true if re-import all LODs works, false otherwise see log for explanation.

### RemoveCollisions
```angelscript
bool RemoveCollisions(UStaticMesh StaticMesh)
```
Same as RemoveCollisionsWithNotification but changes are applied.

### RemoveCollisionsWithNotification
```angelscript
bool RemoveCollisionsWithNotification(UStaticMesh StaticMesh, bool bApplyChanges)
```
Remove collisions from a static mesh.
This method replicates what is done when invoking menu entries "Collision > Remove Collision" in the Mesh Editor.
@param       StaticMesh                      Static mesh to remove collisions from.
@param       bApplyChanges           Indicates if changes must be apply or not.
@return A boolean indicating if the removal was successful or not.

### RemoveLods
```angelscript
bool RemoveLods(UStaticMesh StaticMesh)
```
Remove LODs on a static mesh except LOD 0.
@param       StaticMesh                      Mesh to remove LOD from.
@return A boolean indicating if the removal was successful, true, or not.

### RemoveUVChannel
```angelscript
bool RemoveUVChannel(UStaticMesh StaticMesh, int LODIndex, int UVChannelIndex)
```
Removes the UV channel at the specified channel index on the given LOD of a StaticMesh.
@param       StaticMesh                      Static mesh on which to remove the UV channel.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       UVChannelIndex          Index where to remove the UV channel.
@return true if the UV channel was removed.

### ReplaceMeshComponentsMaterials
```angelscript
void ReplaceMeshComponentsMaterials(TArray<UMeshComponent> MeshComponents, UMaterialInterface MaterialToBeReplaced, UMaterialInterface NewMaterial)
```
Find the references of the material MaterialToReplaced on all the MeshComponents provided and replace it by NewMaterial.
@param       MeshComponents                  List of MeshComponent to search from.
@param       MaterialToBeReplaced    Material we want to replace.
@param       NewMaterial                             Material to replace MaterialToBeReplaced by.

### ReplaceMeshComponentsMaterialsOnActors
```angelscript
void ReplaceMeshComponentsMaterialsOnActors(TArray<AActor> Actors, UMaterialInterface MaterialToBeReplaced, UMaterialInterface NewMaterial)
```
Find the references of the material MaterialToReplaced on all the MeshComponents of all the Actors provided and replace it by NewMaterial.
@param       Actors                                  List of Actors to search from.
@param       MaterialToBeReplaced    Material we want to replace.
@param       NewMaterial                             Material to replace MaterialToBeReplaced by.

### ReplaceMeshComponentsMeshes
```angelscript
void ReplaceMeshComponentsMeshes(TArray<UStaticMeshComponent> MeshComponents, UStaticMesh MeshToBeReplaced, UStaticMesh NewMesh)
```
Find the references of the mesh MeshToBeReplaced on all the MeshComponents provided and replace it by NewMesh.
The editor should not be in play in editor mode.
@param       MeshComponents                  List of MeshComponent to search from.
@param       MeshToBeReplaced                Mesh we want to replace.
@param       NewMesh                                 Mesh to replace MeshToBeReplaced by.

### ReplaceMeshComponentsMeshesOnActors
```angelscript
void ReplaceMeshComponentsMeshesOnActors(TArray<AActor> Actors, UStaticMesh MeshToBeReplaced, UStaticMesh NewMesh)
```
Find the references of the mesh MeshToBeReplaced on all the MeshComponents of all the Actors provided and replace it by NewMesh.
@param       Actors                                  List of Actors to search from.
@param       MeshToBeReplaced                Mesh we want to replace.
@param       NewMesh                                 Mesh to replace MeshToBeReplaced by.

### SetAllowCPUAccess
```angelscript
void SetAllowCPUAccess(UStaticMesh StaticMesh, bool bAllowCPUAccess)
```
Sets StaticMeshFlag bAllowCPUAccess

### SetConvexDecompositionCollisions
```angelscript
bool SetConvexDecompositionCollisions(UStaticMesh StaticMesh, int HullCount, int MaxHullVerts, int HullPrecision)
```
Same as SetConvexDecompositionCollisionsWithNotification but changes are automatically applied.

### SetConvexDecompositionCollisionsWithNotification
```angelscript
bool SetConvexDecompositionCollisionsWithNotification(UStaticMesh StaticMesh, int HullCount, int MaxHullVerts, int HullPrecision, bool bApplyChanges)
```
Add a convex collision to a static mesh.
Any existing collisions will be removed from the static mesh.
This method replicates what is done when invoking menu entry "Collision > Auto Convex Collision" in the Mesh Editor.
@param       StaticMesh                              Static mesh to add convex collision on.
@param       HullCount                               Maximum number of convex pieces that will be created. Must be positive.
@param       MaxHullVerts                    Maximum number of vertices allowed for any generated convex hull.
@param       HullPrecision                   Number of voxels to use when generating collision. Must be positive.
@param       bApplyChanges                   Indicates if changes must be apply or not.
@return A boolean indicating if the addition was successful or not.

### SetGenerateLightmapUv
```angelscript
bool SetGenerateLightmapUv(UStaticMesh StaticMesh, bool bGenerateLightmapUVs)
```
Set Generate Lightmap UVs for StaticMesh

### SetLodBuildSettings
```angelscript
void SetLodBuildSettings(UStaticMesh StaticMesh, int LodIndex, FMeshBuildSettings BuildOptions)
```
Set the LOD build options for the specified LOD index.
@param StaticMesh - Mesh to process.
@param LodIndex - The LOD we will apply the build settings.
@param BuildOptions - The build settings we want to apply to the LOD.

### SetLodFromStaticMesh
```angelscript
int SetLodFromStaticMesh(UStaticMesh DestinationStaticMesh, int DestinationLodIndex, UStaticMesh SourceStaticMesh, int SourceLodIndex, bool bReuseExistingMaterialSlots)
```
Adds or create a LOD at DestinationLodIndex using the geometry from SourceStaticMesh SourceLodIndex
@param       DestinationStaticMesh           The static mesh to set the LOD in.
@param       DestinationLodIndex                     The index of the LOD to set.
@param       SourceStaticMesh                        The static mesh to get the LOD from.
@param       SourceLodIndex                          The index of the LOD to get.
@param       bReuseExistingMaterialSlots     If true, sections from SourceStaticMesh will be remapped to match the material slots of DestinationStaticMesh
                                                                                       when they have the same material assigned. If false, all material slots of SourceStaticMesh will be appended in DestinationStaticMesh.
@return      The index of the LOD that was set. It can be different than DestinationLodIndex if it wasn't a valid index.
                     A negative value indicates that the LOD was not set. See log for explanation.

### SetLODGroup
```angelscript
bool SetLODGroup(UStaticMesh StaticMesh, FName LODGroup, bool bRebuildImmediately)
```
Set the LODGroup for the specified static mesh
@param StaticMesh - Mesh to process.
@param LODGroup - Name of the LODGroup to apply
@param bRebuildImmediately - If true, rebuild the static mesh immediately
@return Success

### SetLODMaterialSlot
```angelscript
void SetLODMaterialSlot(UStaticMesh StaticMesh, int MaterialSlotIndex, int LODIndex, int SectionIndex)
```
Sets the material slot for a specific LOD.
@param        StaticMesh                      Static mesh to Enables/disables shadow casting from.
@param        MaterialSlotIndex       Index of the material slot to use.
@param        LODIndex                        Index of the StaticMesh LOD.
@param        SectionIndex            Index of the StaticMesh Section.

### SetLodReductionSettings
```angelscript
void SetLodReductionSettings(UStaticMesh StaticMesh, int LodIndex, FMeshReductionSettings ReductionOptions)
```
Set the LOD reduction for the specified LOD index.
@param StaticMesh - Mesh to process.
@param LodIndex - The LOD we will apply the reduction settings.
@param ReductionOptions - The reduction settings we want to apply to the LOD.

### SetLods
```angelscript
int SetLods(UStaticMesh StaticMesh, FStaticMeshReductionOptions ReductionOptions)
```
Same as SetLodsWithNotification but changes are applied.

### SetLodScreenSizes
```angelscript
bool SetLodScreenSizes(UStaticMesh StaticMesh, TArray<float32> ScreenSizes)
```
Set LOD screen sizes.
@param       StaticMesh                      Mesh to process.
@param       ScreenSizes                     Array of LOD screen sizes to set.
@return A boolean indicating if setting the screen sizes was successful.

### SetLodsWithNotification
```angelscript
int SetLodsWithNotification(UStaticMesh StaticMesh, FStaticMeshReductionOptions ReductionOptions, bool bApplyChanges)
```
Remove then add LODs on a static mesh.
The static mesh must have at least LOD 0.
The LOD 0 of the static mesh is kept after removal.
The build settings of LOD 0 will be applied to all subsequent LODs.
@param       StaticMesh                              Mesh to process.
@param       ReductionOptions                Options on how to generate LODs on the mesh.
@param       bApplyChanges                           Indicates if change must be notified.
@return the number of LODs generated on the input mesh.
An negative value indicates that the reduction could not be performed. See log for explanation.
No action will be performed if ReductionOptions.ReductionSettings is empty

### SetNaniteSettings
```angelscript
void SetNaniteSettings(UStaticMesh StaticMesh, FMeshNaniteSettings NaniteSettings, bool bApplyChanges)
```
Get the Nanite Settings for the mesh
@param StaticMesh        Mesh to update nanite settings for
@param NaniteSettings    Settings with which to update the mesh
@param bApplyChanges     Indicates if changes must be applied or not.

