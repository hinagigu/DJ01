# UNiagaraMeshRendererProperties

**继承自**: `UNiagaraRendererProperties`

## 属性

### Meshes
- **类型**: `TArray<FNiagaraMeshRendererMeshProperties>`
- **描述**: The static mesh(es) to be instanced when rendering mesh particles.

NOTES:
- If "Override Material" is not specified, the mesh's material is used. Override materials must have the Niagara Mesh Particles flag checked.
- If "Enable Mesh Flipbook" is specified, this mesh is assumed to be the first frame of the flipbook.

### SourceMode
- **类型**: `ENiagaraRendererSourceDataMode`
- **描述**: Whether or not to draw a single element for the Emitter or to draw the particles.

### SortMode
- **类型**: `ENiagaraSortMode`
- **描述**: Determines how we sort the particles prior to rendering.

### SortPrecision
- **类型**: `ENiagaraRendererSortPrecision`
- **描述**: Sort precision to use when sorting is active.

### GpuTranslucentLatency
- **类型**: `ENiagaraRendererGpuTranslucentLatency`
- **描述**: Gpu simulations run at different points in the frame depending on what features are used, i.e. depth buffer, distance fields, etc.
Opaque materials will run latent when these features are used.
Translucent materials can choose if they want to use this frames or the previous frames data to match opaque draws.

### OverrideMaterials
- **类型**: `TArray<FNiagaraMeshMaterialOverride>`
- **描述**: The materials to be used instead of the StaticMesh's materials. Note that each material must have the Niagara Mesh Particles flag checked. If the ParticleMesh
      requires more materials than exist in this array or any entry in this array is set to None, we will use the ParticleMesh's existing Material instead.

### SubImageSize
- **类型**: `FVector2D`
- **描述**: When using SubImage lookups for particles, this variable contains the number of columns in X and the number of rows in Y.

### LockedAxis
- **类型**: `FVector`
- **描述**: Arbitrary axis by which to lock facing rotations

### MeshBoundsScale
- **类型**: `FVector`
- **描述**: Scale factor applied to all of the meshes bounds.
This impacts distance based and per instance frustum culling.  Per instance frustum culling is enabled by default
when GPU scene is enabled.  When using WPO with a material that may expand the mesh beyond the original bounds instances
can be frustum culled incorrectly, this allows you to grow the bounds to avoid this issue.

### FacingMode
- **类型**: `ENiagaraMeshFacingMode`
- **描述**: Determines how the mesh orients itself relative to the camera.

### LockedAxisSpace
- **类型**: `ENiagaraMeshLockedAxisSpace`
- **描述**: Specifies what space the locked axis is in

### MinCameraDistance
- **类型**: `float32`

### MaxCameraDistance
- **类型**: `float32`

### RendererVisibility
- **类型**: `uint`
- **描述**: If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.

### MaterialParameters
- **类型**: `FNiagaraRendererMaterialParameters`
- **描述**: If this array has entries, we will create a MaterialInstanceDynamic per Emitter instance from Material and set the Material parameters using the Niagara simulation variables listed.

### FirstFlipbookFrame
- **类型**: `UStaticMesh`
- **描述**: The static mesh to use for the first frame of the flipbook. Its name will also be used to find subsequent frames of a similar name.
NOTE: The subsequent frames are expected to exist in the same content directory as the first frame of the flipbook, otherwise they
will not be found or used.

### FlipbookSuffixFormat
- **类型**: `FString`
- **描述**: Provides the format of the suffix of the names of the static meshes when searching for flipbook frames. "{frame_number}" is used to mark
where the frame number should appear in the suffix. If "Particle Mesh" contains this suffix, the number in its name will be treated as
the starting frame index. Otherwise, it will assume "Particle Mesh" is frame number 0, and that subsequent frames follow this format,
starting with frame number 1.

### FlipbookSuffixNumDigits
- **类型**: `uint`
- **描述**: The number of digits to expect in the frame number of the flipbook page. A value of 1 will expect no leading zeros in the package names,
and can also be used for names with frame numbers that extend to 10 and beyond (Example: Frame_1, Frame_2, ..., Frame_10, Frame_11, etc.)

### NumFlipbookFrames
- **类型**: `uint`
- **描述**: The number of frames (static meshes) to be included in the flipbook.

### bOverrideMaterials
- **类型**: `bool`

### bUseHeterogeneousVolumes
- **类型**: `bool`

### bSortOnlyWhenTranslucent
- **类型**: `bool`

### bSubImageBlend
- **类型**: `bool`

### bEnableFrustumCulling
- **类型**: `bool`

### bEnableCameraDistanceCulling
- **类型**: `bool`

### bEnableMeshFlipbook
- **类型**: `bool`

### bLockedAxisEnable
- **类型**: `bool`

### bCastShadows
- **类型**: `bool`

