# UMovieSceneUserImportFBXSettings

**继承自**: `UObject`

## 属性

### bMatchByNameOnly
- **类型**: `bool`
- **描述**: Match fbx node names to sequencer node names

### bForceFrontXAxis
- **类型**: `bool`
- **描述**: Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y

### bConvertSceneUnit
- **类型**: `bool`
- **描述**: Convert the scene from FBX unit to UE unit(centimeter)

### ImportUniformScale
- **类型**: `float32`
- **描述**: Import Uniform Scale

### bCreateCameras
- **类型**: `bool`
- **描述**: Whether to create cameras if they don't already exist in the level.

### bReplaceTransformTrack
- **类型**: `bool`
- **描述**: Whether to replace the existing transform track or create a new track/section

### bReduceKeys
- **类型**: `bool`
- **描述**: Whether to remove keyframes within a tolerance from the imported tracks

### ReduceKeysTolerance
- **类型**: `float32`
- **描述**: The tolerance for reduce keys

