# UCubeGridToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### GridFrameOrigin
- **类型**: `FVector`

### GridFrameOrientation
- **类型**: `FRotator`

### bShowGizmo
- **类型**: `bool`

### GridPower
- **类型**: `uint8`
- **描述**: Determines cube grid scale. Can also be adjusted with hotkeys. This changes Current
       Block Size to match the current Base Block Size and Grid Power (differently depending
       on the Power of Two setting).

### CurrentBlockSize
- **类型**: `float`
- **描述**: Sets the size of a block at the current grid power. This changes Base Block Size
such that the given value is achieved at the the current value of Grid Power.

### BlocksPerStep
- **类型**: `int`
- **描述**: How many blocks each push/pull invocation will do at a time.

### bPowerOfTwoBlockSizes
- **类型**: `bool`
- **描述**: When true, block sizes change by powers of two as Grid Power is changed. When false, block
sizes change by twos and fives, much like the default editor grid snapping options (for
instance, sizes might increase from 10 to 50 to 100 to 500).
Note that toggling this option will reset Grid Power and Current Block Size to default values.

### BlockBaseSize
- **类型**: `float`
- **描述**: Smallest block size to use in the grid, i.e. the block size at Grid Power 0. This
       changes Current Block Size according to current value of Grid Power.

### bCrosswiseDiagonal
- **类型**: `bool`
- **描述**: When pushing/pulling in a way where the diagonal matters, setting this to true
       makes the diagonal generally try to lie flat across the face rather than at
       an incline.

### bKeepSideGroups
- **类型**: `bool`
- **描述**: When performing multiple push/pulls with the same selection, attempt to keep the
       same group IDs on the sides of the new geometry (ie multiple E/Q presses will not
       result in different group topology around the sides compared to a single Ctrl+drag).

### bShowSelectionMeasurements
- **类型**: `bool`
- **描述**: When true, displays dimensions of the given selection in the viewport.

### bHitUnrelatedGeometry
- **类型**: `bool`
- **描述**: When raycasting to find a selected grid face, this determines whether geometry
       in the scene that is not part of the edited mesh is hit.

### bHitGridGroundPlaneIfCloser
- **类型**: `bool`
- **描述**: When the grid ground plane is above some geometry, whether we should hit that
       plane or pass through to the other geometry.

### FaceSelectionMode
- **类型**: `ECubeGridToolFaceSelectionMode`
- **描述**: How the selected face is determined.

