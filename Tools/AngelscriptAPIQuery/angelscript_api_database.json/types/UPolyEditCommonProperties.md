# UPolyEditCommonProperties

**继承自**: `UInteractiveToolPropertySet`

These are properties that do not get enabled/disabled based on the action

## 属性

### bShowWireframe
- **类型**: `bool`

### bShowSelectableCorners
- **类型**: `bool`

### bGizmoVisible
- **类型**: `bool`
- **描述**: When true, allows the transform gizmo to be rendered

### LocalFrameMode
- **类型**: `ELocalFrameMode`
- **描述**: Determines whether, on selection changes, the gizmo's rotation is taken from the object transform, or from the geometry
       elements selected. Only relevant with a local coordinate system and when rotation is not locked.

### bLockRotation
- **类型**: `bool`
- **描述**: When true, keeps rotation of gizmo constant through selection changes and manipulations
       (but not middle-click repositions). Only active with a local coordinate system.

