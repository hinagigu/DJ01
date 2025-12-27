# UNiagaraDataInterfaceChaosDestruction

**继承自**: `UNiagaraDataInterface`

Data Interface allowing sampling of Chaos Destruction data.

## 属性

### ChaosSolverActorSet
- **类型**: `TSet<TObjectPtr<AChaosSolverActor>>`
- **描述**: Chaos Solver

### DataSourceType
- **类型**: `EDataSourceTypeEnum`

### DataProcessFrequency
- **类型**: `int`
- **描述**: Number of times the RBD collision data gets processed every second

### MaxNumberOfDataEntriesToSpawn
- **类型**: `int`
- **描述**: Maximum number of collision/breaking/trailing entry used for spawning particles every time data from the physics solver gets processed

### DoSpawn
- **类型**: `bool`
- **描述**: Turn on/off particle spawning

### SpawnMultiplierMinMax
- **类型**: `FVector2D`
- **描述**: For every collision random number of particles will be spawned in the range of [SpawnMultiplierMin, SpawnMultiplierMax]

### SpawnChance
- **类型**: `float32`
- **描述**: For every collision random number of particles will be spawned in the range of [SpawnMultiplierMin, SpawnMultiplierMax]

### ImpulseToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max collision accumulated impulse to spawn particles

### SpeedToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max speed to spawn particles

### MassToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max mass to spawn particles

### ExtentMinToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max ExtentMin to spawn particles

### ExtentMaxToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max ExtentMax to spawn particles

### VolumeToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max volume to spawn particles

### SolverTimeToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max solver time mass to spawn particles

### SurfaceTypeToSpawn
- **类型**: `int`
- **描述**: SurfaceType to spawn particles

### LocationFilteringMode
- **类型**: `ELocationFilteringModeEnum`
- **描述**: Location Filtering Mode

### LocationXToSpawn
- **类型**: `ELocationXToSpawnEnum`
- **描述**: How to use LocationX to filter

### LocationXToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max LocationX to spawn particles

### LocationYToSpawn
- **类型**: `ELocationYToSpawnEnum`
- **描述**: How to use LocationY to filter

### LocationYToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max LocationY to spawn particles

### LocationZToSpawn
- **类型**: `ELocationZToSpawnEnum`
- **描述**: How to use LocationZ to filter

### LocationZToSpawnMinMax
- **类型**: `FVector2D`
- **描述**: Min/Max LocationX to spawn particles

### TrailMinSpeedToSpawn
- **类型**: `float32`
- **描述**: Min Linear Speed to generate trailing particles

### DataSortingType
- **类型**: `EDataSortTypeEnum`
- **描述**: Sorting method to sort the collision data

### DoSpatialHash
- **类型**: `bool`

### SpatialHashVolumeMin
- **类型**: `FVector`
- **描述**: SpatialHash volume min

### SpatialHashVolumeMax
- **类型**: `FVector`
- **描述**: SpatialHash volume max

### SpatialHashVolumeCellSize
- **类型**: `FVector`
- **描述**: SpatialHash volume resolution

### MaxDataPerCell
- **类型**: `int`

### bApplyMaterialsFilter
- **类型**: `bool`
- **描述**: Materials Filter

### ChaosBreakingMaterialSet
- **类型**: `TSet<TObjectPtr<UPhysicalMaterial>>`
- **描述**: TODO: Explanatory comment

### bGetExternalBreakingData
- **类型**: `bool`
- **描述**: TODO: Explanatory comment

### RandomPositionMagnitudeMinMax
- **类型**: `FVector2D`
- **描述**: Random displacement value for the particle spawn position

### InheritedVelocityMultiplier
- **类型**: `float32`
- **描述**: How much of the collision velocity gets inherited

### RandomVelocityGenerationType
- **类型**: `ERandomVelocityGenerationTypeEnum`
- **描述**: The method used to create the random velocities for the newly spawned particles

### RandomVelocityMagnitudeMinMax
- **类型**: `FVector2D`
- **描述**: Every particles will be spawned with random velocity with magnitude in the range of [RandomVelocityMagnitudeMin, RandomVelocityMagnitudeMax]

### SpreadAngleMax
- **类型**: `float32`

### VelocityOffsetMin
- **类型**: `FVector`
- **描述**: Min Offset value added to spawned particles velocity

### VelocityOffsetMax
- **类型**: `FVector`
- **描述**: Max Offset value added to spawned particles velocity

### FinalVelocityMagnitudeMinMax
- **类型**: `FVector2D`
- **描述**: Clamp particles velocity

### MaxLatency
- **类型**: `float32`

### DebugType
- **类型**: `EDebugTypeEnum`
- **描述**: Debug visualization method

