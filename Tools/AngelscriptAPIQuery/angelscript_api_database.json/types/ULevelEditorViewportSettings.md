# ULevelEditorViewportSettings

**继承自**: `UObject`

Implements the Level Editor's view port settings.

## 属性

### FlightCameraControlType
- **类型**: `EWASDType`
- **描述**: Enable the use of flight camera controls under various circumstances.

### FlightCameraControlExperimentalNavigation
- **类型**: `bool`
- **描述**: Enable the use of the experimental navigation in the flight camera controls.

### LandscapeEditorControlType
- **类型**: `ELandscapeFoliageEditorControlType`
- **描述**: Choose the control scheme for landscape tools (ignored for pen input)

### FoliageEditorControlType
- **类型**: `ELandscapeFoliageEditorControlType`
- **描述**: Choose the control scheme for foliage tools

### MinimumOrthographicZoom
- **类型**: `float32`
- **描述**: The closest possible distance allowed when viewing through an orthographic camera

### MouseScrollCameraSpeed
- **类型**: `int`
- **描述**: How fast the perspective camera moves through the world when using mouse scroll.

### MouseSensitivty
- **类型**: `float32`
- **描述**: The sensitivity of mouse movement when rotating the camera.

### bInvertMouseLookYAxis
- **类型**: `bool`
- **描述**: Whether or not to invert mouse on the y axis in free look mode

### bInvertOrbitYAxis
- **类型**: `bool`
- **描述**: Whether or not to invert mouse on y axis in orbit mode

### bInvertMiddleMousePan
- **类型**: `bool`
- **描述**: Whether or not to invert the direction of middle mouse panning in viewports

### bInvertRightMouseDollyYAxis
- **类型**: `bool`
- **描述**: Whether or not to invert the direction of right mouse dolly on the Y axis in orbit mode

### bLevelStreamingVolumePrevis
- **类型**: `bool`
- **描述**: If enabled, the viewport will stream in levels automatically when the camera is moved.

### bUseUE3OrbitControls
- **类型**: `bool`
- **描述**: When checked, orbit the camera by using the L or U keys when unchecked, Alt and Left Mouse Drag will orbit around the look at point

### ScrollGestureDirectionFor3DViewports
- **类型**: `EScrollGestureDirection`
- **描述**: Direction of the scroll gesture for 3D viewports

### ScrollGestureDirectionForOrthoViewports
- **类型**: `EScrollGestureDirection`
- **描述**: Direction of the scroll gesture for orthographic viewports

### bLevelEditorJoystickControls
- **类型**: `bool`
- **描述**: Enables joystick-based camera movement in 3D level editing viewports

### bUseDistanceScaledCameraSpeed
- **类型**: `bool`
- **描述**: If enabled, scale the perspective camera speed based on the distance between the camera and its look-at position

### bOrbitCameraAroundSelection
- **类型**: `bool`
- **描述**: If enabled, the camera will orbit around the current selection in the viewport

### bUsePowerOf2SnapSize
- **类型**: `bool`
- **描述**: If enabled will use power of 2 grid settings (e.g, 1,2,4,8,16,...,1024) instead of decimal grid sizes

### DecimalGridSizes
- **类型**: `TArray<float32>`
- **描述**: Decimal grid sizes (for translation snapping and grid rendering)

### DecimalGridIntervals
- **类型**: `TArray<float32>`
- **描述**: The number of lines between each major line interval for decimal grids

### Pow2GridSizes
- **类型**: `TArray<float32>`
- **描述**: Power of 2 grid sizes (for translation snapping and grid rendering)

### Pow2GridIntervals
- **类型**: `TArray<float32>`
- **描述**: The number of lines between each major line interval for pow2 grids

### CommonRotGridSizes
- **类型**: `TArray<float32>`
- **描述**: User defined grid intervals for rotations

### DivisionsOf360RotGridSizes
- **类型**: `TArray<float32>`
- **描述**: Preset grid intervals for rotations

### ScalingGridSizes
- **类型**: `TArray<float32>`
- **描述**: Grid sizes for scaling

### AspectRatioAxisConstraint
- **类型**: `EAspectRatioAxisConstraint`
- **描述**: How to constrain perspective view port FOV

### SelectionHighlightIntensity
- **类型**: `float32`
- **描述**: Sets the intensity of the overlay displayed when an object is selected

### BSPSelectionHighlightIntensity
- **类型**: `float32`
- **描述**: Sets the intensity of the overlay displayed when an object is selected

### CameraPreviewSize
- **类型**: `float32`
- **描述**: Affects the size of 'picture in picture' previews if they are enabled

### BackgroundDropDistance
- **类型**: `float32`
- **描述**: Distance from the camera to place actors which are dropped on nothing in the view port.

### PreviewMeshes
- **类型**: `TArray<FSoftObjectPath>`
- **描述**: A list of meshes that can be used as preview mesh in the editor view port by holding down the backslash key

### BillboardScale
- **类型**: `float32`

### TransformWidgetSizeAdjustment
- **类型**: `int`
- **描述**: The size adjustment to apply to the translate/rotate/scale widgets (in Unreal units).

### MeasuringToolUnits
- **类型**: `EMeasuringToolUnits`
- **描述**: Specify the units used by the measuring tool

### SelectedSplinePointSizeAdjustment
- **类型**: `float32`
- **描述**: The size adjustment to apply to selected spline points (in screen space units).

### SplineLineThicknessAdjustment
- **类型**: `float32`
- **描述**: The size adjustment to apply to spline line thickness which increases the spline's hit tolerance.

### SplineTangentHandleSizeAdjustment
- **类型**: `float32`
- **描述**: The size adjustment to apply to spline tangent handle (in screen space units).

### SplineTangentScale
- **类型**: `float32`
- **描述**: The scale to apply to spline tangent lengths

### MaterialForDroppedTextures
- **类型**: `TSoftObjectPtr<UMaterialInterface>`
- **描述**: When dropping a texture in the viewport, create an instance of this material instead of creating a new material. Populate MaterialParamsForDroppedTextures to specify the parameter names.

### MaterialParamsForDroppedTextures
- **类型**: `TMap<EMaterialKind,FName>`
- **描述**: When dropping a texture in the viewport, determines which material parameter to assign for each found texture type. Only relevant if MaterialForDroppedTextures is assigned.

### bPanMovesCanvas
- **类型**: `bool`

### bCenterZoomAroundCursor
- **类型**: `bool`

### bAllowTranslateRotateZWidget
- **类型**: `bool`

### bAllowArcballRotate
- **类型**: `bool`

### bAllowScreenRotate
- **类型**: `bool`

### bClickBSPSelectsBrush
- **类型**: `bool`

### bShowActorEditorContext
- **类型**: `bool`

### bAllowEditWidgetAxisDisplay
- **类型**: `bool`

### bUseLegacyCameraMovementNotifications
- **类型**: `bool`

### bUseAbsoluteTranslation
- **类型**: `bool`

### GridEnabled
- **类型**: `bool`

### RotGridEnabled
- **类型**: `bool`

### SnapScaleEnabled
- **类型**: `bool`

### bUsePercentageBasedScaling
- **类型**: `bool`

### bEnableLayerSnap
- **类型**: `bool`

### bEnableViewportHoverFeedback
- **类型**: `bool`

### bHighlightWithBrackets
- **类型**: `bool`

### bUseLinkedOrthographicViewports
- **类型**: `bool`

### bUseSelectionOutline
- **类型**: `bool`

### bEnableViewportCameraToUpdateFromPIV
- **类型**: `bool`

### bPreviewSelectedCameras
- **类型**: `bool`

### bSaveEngineStats
- **类型**: `bool`

