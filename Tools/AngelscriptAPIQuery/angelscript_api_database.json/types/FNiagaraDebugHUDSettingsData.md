# FNiagaraDebugHUDSettingsData

Settings for Niagara debug HUD. Contained in it's own struct so that we can pass it whole in a message to the debugger client.

## 属性

### bHudEnabled
- **类型**: `bool`
- **描述**: Primary control for all HUD features.

### bHudRenderingEnabled
- **类型**: `bool`
- **描述**: Primary control for HUD rendering.

### bValidateSystemSimulationDataBuffers
- **类型**: `bool`
- **描述**: When enabled all Niagara systems that pass the filter will have the simulation data buffers validation.
i.e. we will look for NaN or other invalidate data  inside it
Note: This will have an impact on performance.

### bValidateParticleDataBuffers
- **类型**: `bool`
- **描述**: When enabled all Niagara systems that pass the filter will have the particle data buffers validation.
i.e. we will look for NaN or other invalidate data  inside it
Note: This will have an impact on performance.

### bValidationLogErrors
- **类型**: `bool`
- **描述**: When enabled all validation errors will be sent to the log as warnings.
This can be useful to try and narrow down the exact source of an invalid value in the data buffers as often
they will cascade from the first frame where one is generated into other attributes in the subsequent frames.

### ValidationAttributeDisplayTruncate
- **类型**: `int`
- **描述**: When > 0 this is the maximum number of attributes we will display that contain a NaN,
there could be more but the display will be truncated to this amount.  This is to reduce generating long strings.

### bOverviewEnabled
- **类型**: `bool`
- **描述**: When enabled the overview display will be enabled.

### bIncludeCascade
- **类型**: `bool`
- **描述**: When enabled the overview display will include cascade FX.

### OverviewMode
- **类型**: `ENiagaraDebugHUDOverviewMode`

### OverviewSortMode
- **类型**: `ENiagaraDebugHUDDOverviewSort`

### OverviewFont
- **类型**: `ENiagaraDebugHudFont`
- **描述**: Overview display font to use.

### OverviewLocation
- **类型**: `FVector2D`
- **描述**: Overview display location.

### bShowRegisteredComponents
- **类型**: `bool`
- **描述**: Overview display font to use.

### bOverviewShowFilteredSystemOnly
- **类型**: `bool`
- **描述**: When enabled the overview will only show the filter system information.

### ActorFilter
- **类型**: `FString`
- **描述**: Wildcard filter which is compared against the Components Actor name to narrow down the detailed information.
For example, "*Water*" would match all actors that contain the string "water".

### bComponentFilterEnabled
- **类型**: `bool`

### ComponentFilter
- **类型**: `FString`
- **描述**: Wildcard filter for the components to show more detailed information about.
For example, "*MyComp*" would match all components that contain MyComp.

### bSystemFilterEnabled
- **类型**: `bool`

### SystemFilter
- **类型**: `FString`
- **描述**: Wildcard filter for the systems to show more detailed information about.
For example,. "NS_*" would match all systems starting with NS_.

### bEmitterFilterEnabled
- **类型**: `bool`

### EmitterFilter
- **类型**: `FString`
- **描述**: Wildcard filter used to match emitters when generating particle attribute view.
For example,. "Fluid*" would match all emtiters starting with Fluid and only particle attributes for those would be visible.

### bActorFilterEnabled
- **类型**: `bool`

### SystemDebugVerbosity
- **类型**: `ENiagaraDebugHudVerbosity`
- **描述**: When enabled system debug information will be displayed in world.

### SystemEmitterVerbosity
- **类型**: `ENiagaraDebugHudVerbosity`
- **描述**: When enabled we show information about emitter / particle counts.

### DataInterfaceVerbosity
- **类型**: `ENiagaraDebugHudVerbosity`
- **描述**: When enabled allows data interfaces to include additional debugging information.

### bSystemShowBounds
- **类型**: `bool`
- **描述**: When enabled will show the system bounds for all filtered systems.

### SystemBoundsSolidBoxAlpha
- **类型**: `float32`
- **描述**: When bounds display is enabled allows you to draw a solid box if alpha is > 0.

### bSystemShowActiveOnlyInWorld
- **类型**: `bool`
- **描述**: When disabled in world rendering will show systems deactivated by scalability.

### bShowSystemVariables
- **类型**: `bool`
- **描述**: Should we display the system attributes.

### SystemVariables
- **类型**: `TArray<FNiagaraDebugHUDVariable>`
- **描述**: List of attributes to show about the system, each entry uses wildcard matching.
For example, "System.*" would match all system attributes.

### SystemTextOptions
- **类型**: `FNiagaraDebugHudTextOptions`
- **描述**: Sets display text options for system information.

### bShowParticleVariables
- **类型**: `bool`
- **描述**: When enabled will show particle attributes from the list.

### bEnableGpuParticleReadback
- **类型**: `bool`
- **描述**: When enabled GPU particle data will be copied from the GPU to the CPU.
Warning: This has an impact on performance & memory since we copy the whole buffer.
The displayed data is latent since we are seeing what happened a few frames ago.

### bShowParticleIndex
- **类型**: `bool`
- **描述**: When enabled the particle index will be displayed along with any attributes.
Note: This is the index in the particle data buffer and not the persistent ID index.

### ParticlesVariables
- **类型**: `TArray<FNiagaraDebugHUDVariable>`
- **描述**: List of attributes to show per particle, each entry uses wildcard matching.
For example, "*Position" would match all attributes that end in Position.

### ParticleTextOptions
- **类型**: `FNiagaraDebugHudTextOptions`
- **描述**: Sets display text options for particle information.

### bShowParticlesVariablesWithSystem
- **类型**: `bool`
- **描述**: When enabled particle attributes will display with the system information
rather than in world at the particle location.

### bShowParticleVariablesVertical
- **类型**: `bool`

### bUseMaxParticlesToDisplay
- **类型**: `bool`

### bUseParticleDisplayClip
- **类型**: `bool`
- **描述**: When enabled we use the clip planes to narrow down which particles to display

### ParticleDisplayClip
- **类型**: `FVector2D`
- **描述**: Clipping planes used to display particle attributes.

### bUseParticleDisplayCenterRadius
- **类型**: `bool`
- **描述**: When enabled we use a radius from the display center to avoid showing too many particle attributes.

### ParticleDisplayCenterRadius
- **类型**: `float32`
- **描述**: Radius from screen center where 0 is center to 1.0 is edge to avoid display too many particle attributes.

### MaxParticlesToDisplay
- **类型**: `int`
- **描述**: When enabled, the maximum number of particles to show information about.
When disabled all particles will show attributes, this can result in poor performance & potential OOM on some platforms.

### PerfReportFrames
- **类型**: `int`
- **描述**: How many frames to capture in between updates to the max and average perf report values.

### PerfSampleMode
- **类型**: `ENiagaraDebugHUDPerfSampleMode`

### PerfUnits
- **类型**: `ENiagaraDebugHUDPerfUnits`

### PerfGraphMode
- **类型**: `ENiagaraDebugHUDPerfGraphMode`
- **描述**: Time range of the Y Axis of the perf graph

### PerfHistoryFrames
- **类型**: `int`
- **描述**: How many frames of history to display in the perf graphs.

### bUsePerfGraphTimeRange
- **类型**: `bool`
- **描述**: Use the specified user range when enabled, otherwise we will auto detect the range to use.

### PerfGraphTimeRange
- **类型**: `float32`
- **描述**: Time range of the Y Axis of the perf graph

### PerfGraphSize
- **类型**: `FVector2D`
- **描述**: Pixel size of the perf graph.

### PerfGraphAxisColor
- **类型**: `FLinearColor`

### bEnableSmoothing
- **类型**: `bool`
- **描述**: True if perf graphs should be smoothed.

### SmoothingWidth
- **类型**: `int`
- **描述**: Number of samples to use either size of a value when smoothing perf graphs.

### DefaultBackgroundColor
- **类型**: `FLinearColor`
- **描述**: Default background color used generally for panels

### OverviewHeadingColor
- **类型**: `FLinearColor`
- **描述**: Overview heading text color

### OverviewDetailColor
- **类型**: `FLinearColor`
- **描述**: Overview detail text color

### OverviewDetailHighlightColor
- **类型**: `FLinearColor`
- **描述**: Overview detail highlight text color

### InWorldErrorTextColor
- **类型**: `FLinearColor`
- **描述**: In world text if an error is detected

### InWorldTextColor
- **类型**: `FLinearColor`
- **描述**: In world text color

### MessageInfoTextColor
- **类型**: `FLinearColor`
- **描述**: Message display text color

### MessageWarningTextColor
- **类型**: `FLinearColor`
- **描述**: Message display warning text color

### MessageErrorTextColor
- **类型**: `FLinearColor`
- **描述**: Message display error text color

### SystemColorTableOpacity
- **类型**: `float32`
- **描述**: Opacity of the system color background tile in overview table rows.

### SystemColorSeed
- **类型**: `uint`
- **描述**: Additional seed value for random system colors. Useful if current colors of systems are too similar.

### SystemColorHSVMin
- **类型**: `FVector`
- **描述**: Minimum HSV values for the random colors generated for each System.

### SystemColorHSVMax
- **类型**: `FVector`
- **描述**: Maximum HSV values for the random colors generated for each System.

### bShowGlobalBudgetInfo
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraDebugHUDSettingsData& opAssign(FNiagaraDebugHUDSettingsData Other)
```

