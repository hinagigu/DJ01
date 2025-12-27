# USkeletalMesh

**继承自**: `USkinnedAsset`

SkeletalMesh is geometry bound to a hierarchical skeleton of bones which can be animated for the purpose of deforming the mesh.
Skeletal Meshes are built up of two parts; a set of polygons composed to make up the surface of the mesh, and a hierarchical skeleton which can be used to animate the polygons.
The 3D models, rigging, and animations are created in an external modeling and animation application (3DSMax, Maya, Softimage, etc).

@see https://docs.unrealengine.com/latest/INT/Engine/Content/Types/SkeletalMeshes/

## 属性

### PositiveBoundsExtension
- **类型**: `FVector`

### NegativeBoundsExtension
- **类型**: `FVector`

### SkelMirrorTable
- **类型**: `TArray<FBoneMirrorInfo>`

### LODInfo
- **类型**: `TArray<FSkeletalMeshLODInfo>`

### MinQualityLevelLOD
- **类型**: `FPerQualityLevelInt`

### MinLod
- **类型**: `FPerPlatformInt`

### DisableBelowMinLodStripping
- **类型**: `FPerPlatformBool`

### bOverrideLODStreamingSettings
- **类型**: `bool`

### bSupportLODStreaming
- **类型**: `FPerPlatformBool`

### MaxNumStreamedLODs
- **类型**: `FPerPlatformInt`

### MaxNumOptionalLODs
- **类型**: `FPerPlatformInt`

### SkelMirrorAxis
- **类型**: `EAxis`

### SkelMirrorFlipAxis
- **类型**: `EAxis`

### AssetImportData
- **类型**: `UAssetImportData`

### ThumbnailInfo
- **类型**: `UThumbnailInfo`

### RayTracingMinLOD
- **类型**: `int`

### ClothLODBiasMode
- **类型**: `EClothLODBiasMode`

### PostProcessAnimBlueprint
- **类型**: `TSubclassOf<UAnimInstance>`

### PostProcessAnimBPLODThreshold
- **类型**: `int`
- **描述**: * Max LOD level that post-process AnimBPs are evaluated.
* For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating the post-process AnimBP.
* Setting it to -1 will always evaluate it and disable LODing.

### SamplingInfo
- **类型**: `FSkeletalMeshSamplingInfo`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### AssetUserDataEditorOnly
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### SkinWeightProfiles
- **类型**: `TArray<FSkinWeightProfileInfo>`

### MorphTargets
- **类型**: `TArray<UMorphTarget>`

### bEnablePerPolyCollision
- **类型**: `bool`

### PhysicsAsset
- **类型**: `UPhysicsAsset`

### ShadowPhysicsAsset
- **类型**: `UPhysicsAsset`

### NodeMappingData
- **类型**: `TArray<TObjectPtr<UNodeMappingContainer>>`

### bSupportRayTracing
- **类型**: `bool`

### DefaultMeshDeformer
- **类型**: `UMeshDeformer`

## 方法

### AddSocket
```angelscript
void AddSocket(USkeletalMeshSocket InSocket, bool bAddToSkeleton)
```
Add a skeletal socket object to this SkeletalMesh, and optionally promotes it to USkeleton socket.

### FindSocketAndIndex
```angelscript
USkeletalMeshSocket FindSocketAndIndex(FName InSocketName, int& OutIndex)
```
Find a socket object in this SkeletalMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.
Also returns the index for the socket allowing for future fast access via GetSocketByIndex()

### GetBounds
```angelscript
FBoxSphereBounds GetBounds()
```
Get the extended bounds of this mesh (imported bounds plus bounds extension). USkinnedAsset interface.

### GetDefaultAnimatingRig
```angelscript
TSoftObjectPtr<UObject> GetDefaultAnimatingRig()
```

### GetDefaultMeshDeformer
```angelscript
UMeshDeformer GetDefaultMeshDeformer()
```
Get the default mesh deformer used by this mesh. A mesh deformer is used to deform the skeletal mesh at runtime

### GetImportedBounds
```angelscript
FBoxSphereBounds GetImportedBounds()
```
Get the original imported bounds of the skel mesh

### GetLODSettings
```angelscript
const USkeletalMeshLODSettings GetLODSettings()
```

### GetMaterials
```angelscript
TArray<FSkeletalMaterial> GetMaterials()
```
USkinnedAsset interface.

### GetMeshClothingAssets
```angelscript
TArray<UClothingAssetBase> GetMeshClothingAssets()
```

### GetMinLODForQualityLevels
```angelscript
void GetMinLODForQualityLevels(TMap<EPerQualityLevels,int>& QualityLevelMinimumLODs, int& Default)
```

### GetMorphTargetsPtrConv
```angelscript
TArray<UMorphTarget> GetMorphTargetsPtrConv()
```
NOTE: BP compiler doesn't support TObjectPtr as an argument type for UFUNCTION so this converting call is
required. For many morphs, this can be expensive, since it needs to resolve _all_ TObjectPtrs and construct a new
array for it.

### GetNodeMappingContainer
```angelscript
UNodeMappingContainer GetNodeMappingContainer(UBlueprint SourceAsset)
```

### GetNodeMappingData
```angelscript
TArray<UNodeMappingContainer> GetNodeMappingData()
```

### GetOverlayMaterial
```angelscript
UMaterialInterface GetOverlayMaterial()
```
Get the default overlay material used by this mesh

### GetOverlayMaterialMaxDrawDistance
```angelscript
float32 GetOverlayMaterialMaxDrawDistance()
```
Get the default overlay material max draw distance used by this mesh

### GetPhysicsAsset
```angelscript
UPhysicsAsset GetPhysicsAsset()
```
USkinnedAsset interface.

### GetShadowPhysicsAsset
```angelscript
UPhysicsAsset GetShadowPhysicsAsset()
```
USkinnedAsset interface.

### GetSkeleton
```angelscript
const USkeleton GetSkeleton()
```
USkinnedAsset interface.

### GetSocketByIndex
```angelscript
USkeletalMeshSocket GetSocketByIndex(int Index)
```
Returns a socket by index. Max index is NumSockets(). The meshes sockets are accessed first, then the skeletons.

### IsSectionUsingCloth
```angelscript
bool IsSectionUsingCloth(int InSectionIndex, bool bCheckCorrespondingSections)
```
Checks whether the provided section is using APEX cloth. if bCheckCorrespondingSections is true
disabled sections will defer to correspond sections to see if they use cloth (non-cloth sections
are disabled and another section added when cloth is enabled, using this flag allows for a check
on the original section to succeed)
@param InSectionIndex Index to check
@param bCheckCorrespondingSections Whether to check corresponding sections for disabled sections

### GetAllMorphTargetNames
```angelscript
TArray<FString> GetAllMorphTargetNames()
```
Returns the list of all morph targets of this skeletal mesh
@return     The list of morph targets

### NumSockets
```angelscript
int NumSockets()
```
Returns the number of sockets available. Both on this mesh and it's skeleton.

### SetDefaultAnimatingRig
```angelscript
void SetDefaultAnimatingRig(TSoftObjectPtr<UObject> InAnimatingRig)
```

### SetLODSettings
```angelscript
void SetLODSettings(USkeletalMeshLODSettings InLODSettings)
```

### SetMaterials
```angelscript
void SetMaterials(TArray<FSkeletalMaterial> InMaterials)
```

### SetMeshClothingAssets
```angelscript
void SetMeshClothingAssets(TArray<UClothingAssetBase> InMeshClothingAssets)
```

### SetMinLODForQualityLevels
```angelscript
void SetMinLODForQualityLevels(TMap<EPerQualityLevels,int> QualityLevelMinimumLODs, int Default)
```
Allow to override min lod quality levels on a skeletalMesh and it Default value (-1 value for Default dont override its value).

### SetMorphTargets
```angelscript
void SetMorphTargets(TArray<UMorphTarget> InMorphTargets)
```

### SetOverlayMaterial
```angelscript
void SetOverlayMaterial(UMaterialInterface NewOverlayMaterial)
```
Change the default overlay material used by this mesh

### SetOverlayMaterialMaxDrawDistance
```angelscript
void SetOverlayMaterialMaxDrawDistance(float32 InMaxDrawDistance)
```
Change the default overlay material max draw distance used by this mesh

### SetSkeleton
```angelscript
void SetSkeleton(USkeleton InSkeleton)
```

