# UParticleModuleTypeDataRibbon

**继承自**: `UParticleModuleTypeDataBase`

## 属性

### SheetsPerTrail
- **类型**: `int`
- **描述**: The number of sheets to render for the trail.

### MaxTrailCount
- **类型**: `int`
- **描述**: The number of live trails

### MaxParticleInTrailCount
- **类型**: `int`
- **描述**: Max particles per trail

### RenderAxis
- **类型**: `ETrailsRenderAxisOption`
- **描述**: The 'render' axis for the trail (what axis the trail is stretched out on)
        Trails_CameraUp - Traditional camera-facing trail.
        Trails_SourceUp - Use the up axis of the source for each spawned particle.
        Trails_WorldUp  - Use the world up axis.

### TangentSpawningScalar
- **类型**: `float32`
- **描述**: The tangent scalar for spawning.
Angles between tangent A and B are mapped to [0.0f .. 1.0f]
This is then multiplied by TangentTessellationScalar to give the number of particles to spawn

### TilingDistance
- **类型**: `float32`
- **描述**: The (estimated) covered distance to tile the 2nd UV set at.
If 0.0, a second UV set will not be passed in.

### DistanceTessellationStepSize
- **类型**: `float32`
- **描述**: The distance step size for tessellation.
# Tessellation Points = TruncToInt((Distance Between Spawned Particles) / DistanceTessellationStepSize))

### TangentTessellationScalar
- **类型**: `float32`
- **描述**: The tangent scalar for tessellation.
Angles between tangent A and B are mapped to [0.0f .. 1.0f]
This is then multiplied by TangentTessellationScalar to give the number of points to tessellate

### bDeadTrailsOnDeactivate
- **类型**: `bool`

### bDeadTrailsOnSourceLoss
- **类型**: `bool`

### bClipSourceSegement
- **类型**: `bool`

### bEnablePreviousTangentRecalculation
- **类型**: `bool`

### bTangentRecalculationEveryFrame
- **类型**: `bool`

### bSpawnInitialParticle
- **类型**: `bool`

### bRenderGeometry
- **类型**: `bool`

### bRenderSpawnPoints
- **类型**: `bool`

### bRenderTangents
- **类型**: `bool`

### bRenderTessellation
- **类型**: `bool`

### bEnableTangentDiffInterpScale
- **类型**: `bool`

