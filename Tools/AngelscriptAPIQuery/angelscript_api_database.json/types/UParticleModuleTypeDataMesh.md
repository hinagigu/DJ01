# UParticleModuleTypeDataMesh

**继承自**: `UParticleModuleTypeDataBase`

## 属性

### Mesh
- **类型**: `UStaticMesh`
- **描述**: The static mesh to render at the particle positions

### LODSizeScale
- **类型**: `float32`
- **描述**: use the static mesh's LOD setup and switch LODs based on largest particle's screen size

### MeshAlignment
- **类型**: `EMeshScreenAlignment`
- **描述**: The alignment to use on the meshes emitted.
The RequiredModule->ScreenAlignment MUST be set to PSA_TypeSpecific to use.
One of the following:
PSMA_MeshFaceCameraWithRoll
        Face the camera allowing for rotation around the mesh-to-camera FVector
        (amount provided by the standard particle sprite rotation).
PSMA_MeshFaceCameraWithSpin
        Face the camera allowing for the mesh to rotate about the tangential axis.
PSMA_MeshFaceCameraWithLockedAxis
        Face the camera while maintaining the up FVector as the locked direction.

### RollPitchYawRange
- **类型**: `FRawDistributionVector`
- **描述**: The 'pre' rotation pitch (in degrees) to apply to the static mesh used.

### AxisLockOption
- **类型**: `EParticleAxisLock`
- **描述**: The axis to lock the mesh on. This overrides TypeSpecific mesh alignment as well as the LockAxis module.
        EPAL_NONE                -      No locking to an axis.
        EPAL_X                   -      Lock the mesh X-axis facing towards +X.
        EPAL_Y                   -      Lock the mesh X-axis facing towards +Y.
        EPAL_Z                   -      Lock the mesh X-axis facing towards +Z.
        EPAL_NEGATIVE_X  -      Lock the mesh X-axis facing towards -X.
        EPAL_NEGATIVE_Y  -      Lock the mesh X-axis facing towards -Y.
        EPAL_NEGATIVE_Z  -      Lock the mesh X-axis facing towards -Z.
        EPAL_ROTATE_X    -      Ignored for mesh emitters. Treated as EPAL_NONE.
        EPAL_ROTATE_Y    -      Ignored for mesh emitters. Treated as EPAL_NONE.
        EPAL_ROTATE_Z    -      Ignored for mesh emitters. Treated as EPAL_NONE.

### CameraFacingOption
- **类型**: `EMeshCameraFacingOptions`
- **描述**: The camera facing option to use:
All camera facing options without locked axis assume X-axis will be facing the camera.
        XAxisFacing_NoUp                                - X-axis camera facing, no attempt to face an axis up or down.
        XAxisFacing_ZUp                                 - X-axis camera facing, Z-axis of the mesh should attempt to point up.
        XAxisFacing_NegativeZUp                 - X-axis camera facing, Z-axis of the mesh should attempt to point down.
        XAxisFacing_YUp                                 - X-axis camera facing, Y-axis of the mesh should attempt to point up.
        XAxisFacing_NegativeYUp                 - X-axis camera facing, Y-axis of the mesh should attempt to point down.
All axis-locked camera facing options assume the AxisLockOption is set. EPAL_NONE will be treated as EPAL_X.
        LockedAxis_ZAxisFacing                  - X-axis locked on AxisLockOption axis, rotate Z-axis of the mesh to face towards camera.
        LockedAxis_NegativeZAxisFacing  - X-axis locked on AxisLockOption axis, rotate Z-axis of the mesh to face away from camera.
        LockedAxis_YAxisFacing                  - X-axis locked on AxisLockOption axis, rotate Y-axis of the mesh to face towards camera.
        LockedAxis_NegativeYAxisFacing  - X-axis locked on AxisLockOption axis, rotate Y-axis of the mesh to face away from camera.
All velocity-aligned options do NOT require the ScreenAlignment be set to PSA_Velocity.
Doing so will result in additional work being performed... (it will orient the mesh twice).
        VelocityAligned_ZAxisFacing         - X-axis aligned to the velocity, rotate the Z-axis of the mesh to face towards camera.
        VelocityAligned_NegativeZAxisFacing - X-axis aligned to the velocity, rotate the Z-axis of the mesh to face away from camera.
        VelocityAligned_YAxisFacing         - X-axis aligned to the velocity, rotate the Y-axis of the mesh to face towards camera.
        VelocityAligned_NegativeYAxisFacing - X-axis aligned to the velocity, rotate the Y-axis of the mesh to face away from camera.

### bUseStaticMeshLODs
- **类型**: `bool`

### bOverrideMaterial
- **类型**: `bool`

### bOverrideDefaultMotionBlurSettings
- **类型**: `bool`

### bEnableMotionBlur
- **类型**: `bool`

### bCameraFacing
- **类型**: `bool`

### bApplyParticleRotationAsSpin
- **类型**: `bool`

### bFaceCameraDirectionRatherThanPosition
- **类型**: `bool`

### bCollisionsConsiderPartilceSize
- **类型**: `bool`

