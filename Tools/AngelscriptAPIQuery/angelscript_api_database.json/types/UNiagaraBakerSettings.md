# UNiagaraBakerSettings

**继承自**: `UObject`

## 属性

### StartSeconds
- **类型**: `float32`
- **描述**: This is the start time of the simulation where we begin the capture.
I.e. 2.0 would mean the simulation warms up by 2 seconds before we begin capturing.

### DurationSeconds
- **类型**: `float32`
- **描述**: Duration in seconds to take the capture over.

### FramesPerSecond
- **类型**: `int`
- **描述**: The frame rate to run the simulation at during capturing.
This is only used for the preview view and calculating the number of ticks to execute
as we capture the generated texture.

### FramesPerDimension
- **类型**: `FIntPoint`
- **描述**: Number of frames in each dimension.

### Outputs
- **类型**: `TArray<TObjectPtr<UNiagaraBakerOutput>>`
- **描述**: Array of outputs for the baker to generate.

### CurrentCameraIndex
- **类型**: `int`
- **描述**: Active camera that we were saved with

### BakeQualityLevel
- **类型**: `FName`
- **描述**: What quality level to use when baking the simulation, where None means use the current quality level.

### CameraViewportLocation
- **类型**: `FVector`

### CameraViewportRotation
- **类型**: `FRotator`

### bLockToSimulationFrameRate
- **类型**: `bool`

### bPreviewLooping
- **类型**: `bool`

### bRenderComponentOnly
- **类型**: `bool`

