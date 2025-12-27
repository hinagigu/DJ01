# UNiagaraDataInterfaceSceneCapture2D

**继承自**: `UNiagaraDataInterface`

Data Interface which can control or read from a scene capture component.

## 属性

### SourceMode
- **类型**: `ENDISceneCapture2DSourceMode`
- **描述**: How should we find the scene capture component to use?

### SceneCaptureUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: When valid should point to either a Scene Capture 2D Component or a Scene Capture 2D Actor.

### bAutoMoveWithComponent
- **类型**: `bool`
- **描述**: When enabled the scene capture component will be automatically moved to the location of the NiagaraComponent with an optional offset.

### AutoMoveOffsetLocationMode
- **类型**: `ENDISceneCapture2DOffsetMode`
- **描述**: Should we apply the auto move offset in local or world space?

### AutoMoveOffsetLocation
- **类型**: `FVector`
- **描述**: Location offset when applying auto movement.

### AutoMoveOffsetRotationMode
- **类型**: `ENDISceneCapture2DOffsetMode`
- **描述**: How we should apply the rotation

### AutoMoveOffsetRotation
- **类型**: `FRotator`
- **描述**: Rotation offset when applying auto movement.

### ManagedCaptureSource
- **类型**: `ESceneCaptureSource`

### ManagedTextureSize
- **类型**: `FIntPoint`

### ManagedTextureFormat
- **类型**: `ETextureRenderTargetFormat`

### ManagedProjectionType
- **类型**: `ECameraProjectionMode`

### ManagedFOVAngle
- **类型**: `float32`

### ManagedOrthoWidth
- **类型**: `float32`

### bManagedCaptureEveryFrame
- **类型**: `bool`

### bManagedCaptureOnMovement
- **类型**: `bool`

### ManagedShowOnlyActors
- **类型**: `TArray<TObjectPtr<AActor>>`

