# UNiagaraDataInterfaceStaticMesh

**继承自**: `UNiagaraDataInterface`

Data Interface allowing sampling of static meshes.

## 属性

### SourceMode
- **类型**: `ENDIStaticMesh_SourceMode`
- **描述**: Controls how to retrieve the Static Mesh Component to attach to.

### PreviewMesh
- **类型**: `TSoftObjectPtr<UStaticMesh>`
- **描述**: Mesh used to sample from when not overridden by a source actor from the scene. Only available in editor for previewing. This is removed in cooked builds.

### DefaultMesh
- **类型**: `UStaticMesh`
- **描述**: Mesh used to sample from when not overridden by a source actor from the scene. This mesh is NOT removed from cooked builds.

### SoftSourceActor
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: The source actor from which to sample. Takes precedence over the direct mesh. Note that this can only be set when used as a user variable on a component in the world.

### SectionFilter
- **类型**: `FNDIStaticMeshSectionFilter`
- **描述**: Array of filters the can be used to limit sampling to certain sections of the mesh.

### bCaptureTransformsPerFrame
- **类型**: `bool`
- **描述**: If true we capture the transforms from the mesh component each frame.

### bUsePhysicsBodyVelocity
- **类型**: `bool`
- **描述**: If true then the mesh velocity is taken from the mesh component's physics data. Otherwise it will be calculated by diffing the component transforms between ticks, which is more reliable but won't work on the first frame.

### bAllowSamplingFromStreamingLODs
- **类型**: `bool`
- **描述**: When true, we allow this DI to sample from streaming LODs. Selectively overriding the CVar fx.Niagara.NDIStaticMesh.UseInlineLODsOnly.

### LODIndex
- **类型**: `int`
- **描述**: Static Mesh LOD to sample.
When the desired LOD is not available, the next available LOD is used.
When LOD Index is negative, Desired LOD = Num LODs - LOD Index.

### LODIndexUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Reference to a user parameter if we're reading one.

### MeshParameterBinding
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Mesh parameter binding can be either an Actor (in which case we find the component), static mesh component or a static mesh.

### InstanceIndex
- **类型**: `int`
- **描述**: When attached to an Instanced Static Mesh, which instance should be read from.

### FilteredSockets
- **类型**: `TArray<FName>`
- **描述**: List of filtered sockets to use.

