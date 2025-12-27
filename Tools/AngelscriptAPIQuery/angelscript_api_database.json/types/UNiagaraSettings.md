# UNiagaraSettings

**继承自**: `UDeveloperSettings`

## 属性

### AdditionalParameterTypes
- **类型**: `TArray<FSoftObjectPath>`

### AdditionalPayloadTypes
- **类型**: `TArray<FSoftObjectPath>`

### AdditionalParameterEnums
- **类型**: `TArray<FSoftObjectPath>`

### bSystemViewportInOrbitMode
- **类型**: `bool`
- **描述**: Sets the default navigation behavior for the system preview viewport.

### bShowConvertibleInputsInStack
- **类型**: `bool`
- **描述**: If true then the "link input" menu will also show variables of different types, as long as there is a conversion script for them.

### QuickSimCacheCaptureFrameCount
- **类型**: `int`
- **描述**: The number of frames to capture when capturing a Sim Cache from the Niagara Component Details Panel. *

### bSystemsSupportLargeWorldCoordinates
- **类型**: `bool`
- **描述**: If true then active effects rebase the simulation positions to not lose precision. Can be turned off if not needed to skip unnecessary rebasing calculations.

### bEnforceStrictStackTypes
- **类型**: `bool`
- **描述**: If set to true, types like positions and vectors cannot be assigned to each other without an explicit conversion step.
If false, type checks are loosened and some types can be implicitly converted into each other.
It is recommended to not disable this when working with large world coordinates.

### bExperimentalVMEnabled
- **类型**: `bool`
- **描述**: True indicates that we will generate byte code for the new optimized VM.  Control over whether the new VM will
be used when executing NiagaraScripts will also take into account the overrides on the system (bDisableExperimentalVM) and
the cvars fx.NiagaraScript.StripByteCodeOnLoad and fx.ForceExecVMPath.

### bStatelessEmittersEnabled
- **类型**: `bool`
- **描述**: Enables Lightweight Emitters experimental feature.
Statless emitters are lightweight fixed function emitters, they are not fully programmable like regular emitters and do not run scripts on the CPU.
Particle data is extrapolated per frame for the current particle age.  This means we never store particle data, we only generate it on demand.
Systems that contain only lightweight emitters and no system script modules can take advantage of a much faster path to execute.
* There is no guarantee on backwards compatability for this feature currently.  Do not ship lightweight content. **

### bAccurateQuatInterpolation
- **类型**: `bool`
- **描述**: If set to true, quaternion attributes will be interpolated via slerp instead of lerp in interpolated spawn scripts.

### InvalidNamespaceWriteSeverity
- **类型**: `ENiagaraCompileErrorSeverity`
- **描述**: If the Niagara compiler sees that a script writes to a namespace that is read only (e.g. a particle script writing to a system attribute), what should it do.

### bLimitDeltaTime
- **类型**: `bool`

### MaxDeltaTimePerTick
- **类型**: `float32`

### DefaultEffectType
- **类型**: `FSoftObjectPath`
- **描述**: Default effect type to use for effects that don't define their own. Can be null.

### RequiredEffectType
- **类型**: `FSoftObjectPath`
- **描述**: Specifies a required effect type which must be used for effects in the project.

### bAllowCreateActorFromSystemWithNoEffectType
- **类型**: `bool`
- **描述**: Should we allow placing a Niagara System in the editor into a level which has no effect type assigned?

### PositionPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Position pin type color. The other pin colors are defined in the general editor settings.

### ByteCodeStripOption
- **类型**: `ENiagaraStripScriptByteCodeOption`
- **描述**: Controls how byte code will be stripped when loading assets that have multiple sets of bytecode (i.e. optimized).

### CompilationMode
- **类型**: `ENiagaraCompilationMode`

### QualityLevels
- **类型**: `TArray<FText>`
- **描述**: The quality levels Niagara uses.

### ComponentRendererWarningsPerClass
- **类型**: `TMap<FString,FText>`
- **描述**: Info texts that the component renderer shows the user depending on the selected component class.

### DefaultRenderTargetFormat
- **类型**: `ETextureRenderTargetFormat`
- **描述**: The default render target format used by all Niagara Render Target Data Interfaces unless overridden.

### DefaultGridFormat
- **类型**: `ENiagaraGpuBufferFormat`
- **描述**: The default buffer format used by all Niagara Grid Data Interfaces unless overridden.

### DefaultRendererMotionVectorSetting
- **类型**: `ENiagaraDefaultRendererMotionVectorSetting`
- **描述**: The default setting for motion vectors in Niagara renderers

### DefaultPixelCoverageMode
- **类型**: `ENiagaraDefaultRendererPixelCoverageMode`
- **描述**: The default setting for pixel coverage mode when automatic is set on the Niagara Renderer.

### DefaultSortPrecision
- **类型**: `ENiagaraDefaultSortPrecision`
- **描述**: The default setting for sorting precision when automatic is set on the Niagara Renderer.

### DefaultGpuTranslucentLatency
- **类型**: `ENiagaraDefaultGpuTranslucentLatency`
- **描述**: The default setting for Gpu simulation translucent draw latency.

### DefaultLightInverseExposureBlend
- **类型**: `float32`
- **描述**: The default InverseExposureBlend used for the light renderer.

### NDISkelMesh_SupportReadingDeformedGeometry
- **类型**: `bool`
- **描述**: When enabled we will read deformed geometry if available, i.e. data from the deformed graph / skin cache
When disable we will only read from the default vertex data which does not include morph targets, skin, etc.
Changing this setting requires restarting the editor.
Note: Enabling this does add additional branches to the skel mesh data reading.

### NDISkelMesh_Support16BitIndexWeight
- **类型**: `bool`
- **描述**: Enabled support for 16 bit bone index & bone weight, optional to reduce shader complexity.  Changing this setting requires restarting the editor.

### NDISkelMesh_GpuMaxInfluences
- **类型**: `ENDISkelMesh_GpuMaxInfluences`
- **描述**: Controls the maximum number of influences we allow the Skeletal Mesh Data Interface to use on the GPU.  Changing this setting requires restarting the editor.

### NDISkelMesh_GpuUniformSamplingFormat
- **类型**: `ENDISkelMesh_GpuUniformSamplingFormat`
- **描述**: Controls the format used for uniform sampling on the GPU.  Changing this setting requires restarting the editor.

### NDISkelMesh_AdjacencyTriangleIndexFormat
- **类型**: `ENDISkelMesh_AdjacencyTriangleIndexFormat`
- **描述**: Controls the format used for specifying triangle indexes in adjacency buffers.  Changing this setting requires restarting the editor.

### NDIStaticMesh_AllowDistanceFields
- **类型**: `bool`
- **描述**: When enabled the static mesh data interface is allowed to sample from the distance field data (if present) on the GPU.
Enabling this feature will move all systems that contain static mesh samples into PostRenderOpaque tick group regardless of the features used.
Changing this setting requires restarting the editor.

### NDICollisionQuery_AsyncGpuTraceProviderOrder
- **类型**: `TArray<ENDICollisionQuery_AsyncGpuTraceProvider>`
- **描述**: Defines how traces tagged as 'Project Default' will be interpreted when using the AsyncGpuTrace data interface.
The system will go through (starting at element 0) to find the first provider that is available.

### SimCacheAuxiliaryFileBasePath
- **类型**: `FString`
- **描述**: Base path for auxiliary files written out during the generation of a Niagara Sim Cache (ie: volume files).

### SimCacheMaxCPUMemoryVolumetrics
- **类型**: `int64`
- **描述**: Max memory in megabytes for total CPU memory for cached volumetric data

### PlatformSetRedirects
- **类型**: `TArray<FNiagaraPlatformSetRedirect>`

