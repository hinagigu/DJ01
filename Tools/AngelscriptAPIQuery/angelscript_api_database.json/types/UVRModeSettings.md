# UVRModeSettings

**继承自**: `UVISettings`

Implements the settings for VR Mode.

## 属性

### InteractorHand
- **类型**: `EInteractorHand`
- **描述**: Which hand should have the primary interactor laser on it

### UIBrightness
- **类型**: `float32`
- **描述**: Adjusts the brightness of the UI panels

### GizmoScale
- **类型**: `float32`
- **描述**: The size of the transform gizmo

### DoubleClickTime
- **类型**: `float32`
- **描述**: The maximum time in seconds between two clicks for a double-click to register

### TriggerPressedThreshold_Vive
- **类型**: `float32`
- **描述**: The amount (between 0-1) you have to depress the Vive controller trigger to register a press

### TriggerPressedThreshold_Rift
- **类型**: `float32`
- **描述**: The amount (between 0-1) you have to depress the Oculus Touch controller trigger to register a press

### ModeClass
- **类型**: `TSoftClassPtr<UVREditorModeBase>`
- **描述**: The mode extension to use when UnrealEd is in VR mode. Use VREditorMode to get default editor behavior or select a custom mode.

### bEnableAutoVREditMode
- **类型**: `bool`

### bAutokeySequences
- **类型**: `bool`

### bShowWorldMovementGrid
- **类型**: `bool`

### bShowWorldMovementPostProcess
- **类型**: `bool`

### bShowWorldScaleProgressBar
- **类型**: `bool`

