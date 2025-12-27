# __USkeletalMeshEditorSubsystem

## 方法

### AssignPhysicsAsset
```angelscript
bool AssignPhysicsAsset(USkeletalMesh TargetMesh, UPhysicsAsset PhysicsAsset)
```
Assigns a PhysicsAsset to the given SkeletalMesh if it is compatible. Passing
nullptr / None as the physics asset will always succeed and will clear the
physics asset assignment for the target SkeletalMesh

@param TargetMesh The mesh to attempt to assign the PhysicsAsset to
@param PhysicsAsset The physics asset to assign to the provided mesh (or nullptr/None)

@return Whether the physics asset was successfully assigned to the mesh

### CreatePhysicsAsset
```angelscript
UPhysicsAsset CreatePhysicsAsset(USkeletalMesh SkeletalMesh)
```
This function creates a PhysicsAsset for the given SkeletalMesh with the same settings as if it were created through FBX import

@Param SkeletalMesh: The SkeletalMesh we want to create the PhysicsAsset for

### GetLodBuildSettings
```angelscript
void GetLodBuildSettings(const USkeletalMesh SkeletalMesh, int LodIndex, FSkeletalMeshBuildSettings& OutBuildOptions)
```
Copy the build options with the specified LOD build settings.
@param SkeletalMesh - Mesh to process.
@param LodIndex - The LOD we get the reduction settings.
@param OutBuildOptions - The build settings where we copy the build options.

### GetLODCount
```angelscript
int GetLODCount(USkeletalMesh SkeletalMesh)
```
Retrieve the number of LOD contain in the specified skeletal mesh.

@param SkeletalMesh: The static mesh we import or re-import a LOD.

@return The LOD number.

### ImportLOD
```angelscript
int ImportLOD(USkeletalMesh BaseMesh, int LODIndex, FString SourceFilename)
```
Import or re-import a LOD into the specified base mesh. If the LOD do not exist it will import it and add it to the base static mesh. If the LOD already exist it will re-import the specified LOD.

@param BaseSkeletalMesh: The static mesh we import or re-import a LOD.
@param LODIndex: The index of the LOD to import or re-import. Valid value should be between 0 and the base skeletal mesh LOD number. Invalid value will return INDEX_NONE
@param SourceFilename: The fbx source filename. If we are re-importing an existing LOD, it can be empty in this case it will use the last import file. Otherwise it must be an existing fbx file.

@return The index of the LOD that was imported or re-imported. Will return INDEX_NONE if anything goes bad.

### IsPhysicsAssetCompatible
```angelscript
bool IsPhysicsAssetCompatible(USkeletalMesh TargetMesh, UPhysicsAsset PhysicsAsset)
```
Checks whether a physics asset is compatible with the given SkeletalMesh

@param TargetMesh The mesh to test for compatibility
@param PhysicsAsset The PhysicsAsset to test for compatibility

@return Whether the physics asset is compatible with the target SkeletalMesh

### RegenerateLOD
```angelscript
bool RegenerateLOD(USkeletalMesh SkeletalMesh, int NewLODCount, bool bRegenerateEvenIfImported, bool bGenerateBaseLOD)
```
Regenerate LODs of the mesh

@param SkeletalMesh  The mesh that will regenerate LOD
@param NewLODCount   Set valid value (>0) if you want to change LOD count.
                                            Otherwise, it will use the current LOD and regenerate
@param bRegenerateEvenIfImported     If this is true, it only regenerate even if this LOD was imported before
                                                                    If false, it will regenerate for only previously auto generated ones
@param bGenerateBaseLOD If this is true and there is some reduction data, the base LOD will be reduce according to the settings
@return      true if succeed. If mesh reduction is not available this will return false.

### ReimportAllCustomLODs
```angelscript
bool ReimportAllCustomLODs(USkeletalMesh SkeletalMesh)
```
Re-import the specified skeletal mesh and all the custom LODs.

@param SkeletalMesh: is the skeletal mesh we import or re-import a LOD.

@return true if re-import works, false otherwise see log for explanation.

### RenameSocket
```angelscript
bool RenameSocket(USkeletalMesh SkeletalMesh, FName OldName, FName NewName)
```
Rename a socket within a skeleton
@param SkeletalMesh  The mesh inside which we are renaming a socket
@param OldName       The old name of the socket
@param NewName               The new name of the socket
@return true if the renaming succeeded.

### SetLodBuildSettings
```angelscript
void SetLodBuildSettings(USkeletalMesh SkeletalMesh, int LodIndex, FSkeletalMeshBuildSettings BuildOptions)
```
Set the LOD build options for the specified LOD index.
@param SkeletalMesh - Mesh to process.
@param LodIndex - The LOD we will apply the build settings.
@param BuildOptions - The build settings we want to apply to the LOD.

### StaticClass
```angelscript
UClass StaticClass()
```

### Get
```angelscript
USkeletalMeshEditorSubsystem Get()
```

