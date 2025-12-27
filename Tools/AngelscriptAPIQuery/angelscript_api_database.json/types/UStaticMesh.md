# UStaticMesh

**继承自**: `UStreamableRenderAsset`

A StaticMesh is a piece of geometry that consists of a static set of polygons.
Static Meshes can be translated, rotated, and scaled, but they cannot have their vertices animated in any way. As such, they are more efficient
to render than other types of geometry such as USkeletalMesh, and they are often the basic building block of levels created in the engine.

@see https://docs.unrealengine.com/latest/INT/Engine/Content/Types/StaticMeshes/
@see AStaticMeshActor, UStaticMeshComponent

## 属性

### LODGroup
- **类型**: `FName`
- **描述**: The LOD group to which this mesh belongs.

### NaniteSettings
- **类型**: `FMeshNaniteSettings`
- **描述**: Settings related to building Nanite data.

### LightMapResolution
- **类型**: `int`
- **描述**: The light map resolution

### LightMapCoordinateIndex
- **类型**: `int`
- **描述**: The light map coordinate index

### DistanceFieldSelfShadowBias
- **类型**: `float32`
- **描述**: Useful for reducing self shadowing from distance field methods when using world position offset to animate the mesh's vertices.

### BodySetup
- **类型**: `UBodySetup`

### LODForCollision
- **类型**: `int`

### AssetImportData
- **类型**: `UAssetImportData`
- **描述**: Importing data and options used for this mesh

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

### bCustomizedCollision
- **类型**: `bool`
- **描述**: If the user has modified collision in any way or has custom collision imported. Used for determining if to auto generate collision on import

### PositiveBoundsExtension
- **类型**: `FVector`

### NegativeBoundsExtension
- **类型**: `FVector`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### ComplexCollisionMesh
- **类型**: `UStaticMesh`

### NavCollision
- **类型**: `UNavCollisionBase`

### bGenerateMeshDistanceField
- **类型**: `bool`

### bHasNavigationData
- **类型**: `bool`

### bSupportUniformlyDistributedSampling
- **类型**: `bool`

### bSupportPhysicalMaterialMasks
- **类型**: `bool`

### bUseLegacyTangentScaling
- **类型**: `bool`

### bSupportRayTracing
- **类型**: `bool`

### bAllowCPUAccess
- **类型**: `bool`

### bSupportGpuUniformlyDistributedSampling
- **类型**: `bool`

## 方法

### AddMaterial
```angelscript
FName AddMaterial(UMaterialInterface Material)
```
Adds a new material and return its slot name

### AddSocket
```angelscript
void AddSocket(UStaticMeshSocket Socket)
```
Add a socket object in this StaticMesh.

### BuildFromStaticMeshDescriptions
```angelscript
void BuildFromStaticMeshDescriptions(TArray<UStaticMeshDescription> StaticMeshDescriptions, bool bBuildSimpleCollision, bool bFastBuild)
```
Builds static mesh LODs from the array of StaticMeshDescriptions passed in

### FindSocket
```angelscript
UStaticMeshSocket FindSocket(FName InSocketName)
```
Find a socket object in this StaticMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.

### GetBoundingBox
```angelscript
FBox GetBoundingBox()
```
Returns the bounding box, in local space including bounds extension(s), of the StaticMesh asset

### GetBounds
```angelscript
FBoxSphereBounds GetBounds()
```
Returns the number of bounds of the mesh.

@return      The bounding box represented as box origin with extents and also a sphere that encapsulates that box

### GetMaterial
```angelscript
UMaterialInterface GetMaterial(int MaterialIndex)
```
Gets a Material given a Material Index and an LOD number

@return Requested material

### GetMaterialIndex
```angelscript
int GetMaterialIndex(FName MaterialSlotName)
```
Gets a Material index given a slot name

@return Requested material

### GetMinimumLODForPlatform
```angelscript
int GetMinimumLODForPlatform(FName PlatformName)
```

### GetMinimumLODForPlatforms
```angelscript
void GetMinimumLODForPlatforms(TMap<FName,int>& PlatformMinimumLODs)
```

### GetMinimumLODForQualityLevel
```angelscript
int GetMinimumLODForQualityLevel(FName QualityLevel)
```

### GetMinimumLODForQualityLevels
```angelscript
void GetMinimumLODForQualityLevels(TMap<FName,int>& QualityLevelMinimumLODs)
```

### GetMinLODForQualityLevels
```angelscript
void GetMinLODForQualityLevels(TMap<EPerQualityLevels,int>& QualityLevelMinimumLODs, int& Default)
```

### GetNumLods
```angelscript
int GetNumLods()
```
Returns the number of LODs used by the mesh.

### GetNumSections
```angelscript
int GetNumSections(int InLOD)
```
Returns number of Sections that this StaticMesh has, in the supplied LOD (LOD 0 is the highest)

### GetNumTriangles
```angelscript
int GetNumTriangles(int LODIndex)
```
Returns the number of triangles in the render data for the specified LOD.

### GetSocketsByTag
```angelscript
TArray<UStaticMeshSocket> GetSocketsByTag(FString InSocketTag)
```
Returns a list of sockets with the provided tag.

### GetStaticMaterials
```angelscript
TArray<FStaticMaterial> GetStaticMaterials()
```

### GetStaticMeshDescription
```angelscript
UStaticMeshDescription GetStaticMeshDescription(int LODIndex)
```
Return a new StaticMeshDescription referencing the MeshDescription of the given LOD

### IsLODScreenSizeAutoComputed
```angelscript
bool IsLODScreenSizeAutoComputed()
```

### RemoveSocket
```angelscript
void RemoveSocket(UStaticMeshSocket Socket)
```
Remove a socket object in this StaticMesh by providing it's pointer. Use FindSocket() if needed.

### SetMaterial
```angelscript
void SetMaterial(int MaterialIndex, UMaterialInterface NewMaterial)
```
Sets a Material given a Material Index

### SetMinimumLODForPlatform
```angelscript
void SetMinimumLODForPlatform(FName PlatformName, int InMinLOD)
```

### SetMinimumLODForPlatforms
```angelscript
void SetMinimumLODForPlatforms(TMap<FName,int> PlatformMinimumLODs)
```

### SetMinLODForQualityLevels
```angelscript
void SetMinLODForQualityLevels(TMap<EPerQualityLevels,int> QualityLevelMinimumLODs, int Default)
```
Allow to override min lod quality levels on a staticMesh and it Default value (-1 value for Default dont override its value).

### SetNumSourceModels
```angelscript
void SetNumSourceModels(int Num)
```

### SetStaticMaterials
```angelscript
void SetStaticMaterials(TArray<FStaticMaterial> InStaticMaterials)
```

