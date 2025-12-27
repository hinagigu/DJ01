# UNiagaraDataInterfaceSkeletalMesh

**继承自**: `UNiagaraDataInterface`

Data Interface allowing sampling of skeletal meshes.

## 属性

### SourceMode
- **类型**: `ENDISkeletalMesh_SourceMode`
- **描述**: Controls how to retrieve the Skeletal Mesh Component to attach to.

### PreviewMesh
- **类型**: `TSoftObjectPtr<USkeletalMesh>`
- **描述**: Mesh used to sample from when not overridden by a source actor from the scene. Only available in editor for previewing. This is removed in cooked builds.

### DefaultMesh
- **类型**: `USkeletalMesh`
- **描述**: Mesh used to sample from when not overridden by a source actor from the scene. This mesh is NOT removed from cooked builds.

### SoftSourceActor
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: The source actor from which to sample. Takes precedence over the direct mesh. Note that this can only be set when used as a user variable on a component in the world.

### ComponentTags
- **类型**: `TArray<FName>`
- **描述**: If defined, the supplied tags will be used to identify a valid component

### MeshUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Reference to a user parameter if we're reading one.

### SkinningMode
- **类型**: `ENDISkeletalMesh_SkinningMode`
- **描述**: Selects which skinning mode to use, for most cases Skin On The Fly will cover your requirements, see individual tooltips for more information.

### SamplingRegions
- **类型**: `TArray<FName>`
- **描述**: Sampling regions on the mesh from which to sample. Leave this empty to sample from the whole mesh.

### WholeMeshLOD
- **类型**: `int`
- **描述**: If no regions are specified, we'll sample the whole mesh at this LODIndex.
-1 will use the lowest quality LOD available, i.e. Number of LODs - 1.

### FilteredBones
- **类型**: `TArray<FName>`
- **描述**: Set of filtered bones that can be used for sampling. Select from these with GetFilteredBoneAt and RandomFilteredBone.

### FilteredSockets
- **类型**: `TArray<FName>`
- **描述**: Set of filtered sockets that can be used for sampling. Select from these with GetFilteredSocketAt and RandomFilteredSocket.

### ExcludeBoneName
- **类型**: `FName`
- **描述**: Optionally remove a single bone from Random / Random Unfiltered access.
You can still include this bone in filtered list and access using the direct index functionality.

### UvSetIndex
- **类型**: `int`

### bRequireCurrentFrameData
- **类型**: `bool`
- **描述**: When this option is disabled, we use the previous frame's data for the skeletal mesh and can often issue the simulation early. This greatly
      reduces overhead and allows the game thread to run faster, but comes at a tradeoff if the dependencies might leave gaps or other visual artifacts.

### bReadDeformedGeometry
- **类型**: `bool`
- **描述**: Overrides the project setting and allows you to opt out of reading from deformed geometry.
These is not performance gain from doing this, the branches will still exist in the generated code.

### bExcludeBone
- **类型**: `bool`

