# __DEPRECATED_EditorSkeletalMesh

## 方法

### CreatePhysicsAsset
```angelscript
UPhysicsAsset CreatePhysicsAsset(USkeletalMesh SkeletalMesh)
```
This function creates a PhysicsAsset for the given SkeletalMesh with the same settings as if it were created through FBX import

@Param SkeletalMesh: The SkeletalMesh we want to create the PhysicsAsset for

### RemoveLODs
```angelscript
bool RemoveLODs(USkeletalMesh SkeletalMesh, TArray<int> ToRemoveLODs)
```
Remove all the specified LODs. This function will remove all the valid LODs in the list.
Valid LOD is any LOD greater then 0 that exist in the skeletalmesh. We cannot remove the base LOD 0.

@param SkeletalMesh  The mesh inside which we are renaming a socket
@param ToRemoveLODs  The LODs we need to remove
@return true if the successfully remove all the LODs. False otherwise, but evedn if it return false it
will have removed all valid LODs.

### StripLODGeometry
```angelscript
bool StripLODGeometry(USkeletalMesh SkeletalMesh, int LODIndex, UTexture2D TextureMask, float32 Threshold)
```
This function will strip all triangle in the specified LOD that don't have any UV area pointing on a black pixel in the TextureMask.
We use the UVChannel 0 to find the pixels in the texture.

@Param SkeletalMesh: The skeletalmesh we want to optimize
@Param LODIndex: The LOD we want to optimize
@Param TextureMask: The texture containing the stripping mask. non black pixel strip triangle, black pixel keep them.
@Param Threshold: The threshold we want when comparing the texture value with zero.

