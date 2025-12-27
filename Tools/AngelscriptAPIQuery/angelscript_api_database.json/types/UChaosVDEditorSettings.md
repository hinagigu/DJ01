# UChaosVDEditorSettings

**继承自**: `UObject`

## 属性

### bPlaybackAtRecordedFrameRate
- **类型**: `bool`
- **描述**: If true, playback will respect the recorded frame times

### TargetFrameRateOverride
- **类型**: `int`
- **描述**: If play at recorded frame rate is disabled, CVD will attempt to play the recording at the specified frame rate

### FarClippingOverride
- **类型**: `float32`
- **描述**: Sets the desired far clipping for CVD's viewport

### GlobalParticleDataVisualizationFlags
- **类型**: `uint`
- **描述**: Set of flags to enable/disable visualization of specific particle data as debug draw

### GlobalCollisionDataVisualizationFlags
- **类型**: `uint`
- **描述**: Set of flags to enable/disable visualization of specific collision data as debug draw

### GlobalSceneQueriesVisualizationFlags
- **类型**: `uint`
- **描述**: Set of flags to enable/disable visualization of specific scene queries data as debug draw

### GlobalJointsDataVisualizationFlags
- **类型**: `uint`
- **描述**: Set of flags to enable/disable visualization of specific scene queries data as debug draw

### bShowDebugText
- **类型**: `bool`
- **描述**: If true, text information (if available) will be drawn alongside any other debug draw shape

### ContactDebugDrawSettings
- **类型**: `FChaosVDContactDebugDrawSettings`

### ParticleDataDebugDrawSettings
- **类型**: `FChaosParticleDataDebugDrawSettings`

### JointsDataDebugDrawSettings
- **类型**: `FChaosVDJointsDebugDrawSettings`

### ParticleColorMode
- **类型**: `EChaosVDParticleDebugColorMode`

### ColorsByShapeType
- **类型**: `FChaosDebugDrawColorsByShapeType`

### ColorsByParticleState
- **类型**: `FChaosDebugDrawColorsByState`

### ColorsByClientServer
- **类型**: `FChaosDebugDrawColorsByClientServer`

### TrackingTarget
- **类型**: `EChaosVDActorTrackingTarget`
- **描述**: Sets what should be auto tracked by CVD's Camera

### ExpandViewTrackingBy
- **类型**: `float32`
- **描述**: By how much we should expand the bounding box used to track a target by bounding box. Used to see more of the screen while tracking in Bounding Box mode

### GeometryVisibilityFlags
- **类型**: `uint8`
- **描述**: Set of flags to enable/disable visibility of specific types of geometry/particles

