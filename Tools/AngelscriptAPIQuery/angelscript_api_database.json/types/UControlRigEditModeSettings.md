# UControlRigEditModeSettings

**继承自**: `UObject`

Settings object used to show useful information in the details panel

## 属性

### bDisplayHierarchy
- **类型**: `bool`
- **描述**: Whether to show all bones in the hierarchy

### bDisplayNulls
- **类型**: `bool`
- **描述**: Whether to show all nulls in the hierarchy

### bDisplaySockets
- **类型**: `bool`
- **描述**: Should we show sockets in the viewport

### bHideControlShapes
- **类型**: `bool`
- **描述**: Should we always hide control shapes in viewport

### bShowAllProxyControls
- **类型**: `bool`
- **描述**: Should we always hide control shapes in viewport

### bShowControlsAsOverlay
- **类型**: `bool`
- **描述**: Determins if controls should be rendered on top of other controls

### DrivenControlColor
- **类型**: `FLinearColor`
- **描述**: Indicates a control being driven by a proxy control

### bDisplayAxesOnSelection
- **类型**: `bool`
- **描述**: Should we show axes for the selected elements

### AxisScale
- **类型**: `float32`
- **描述**: The scale for axes to draw on the selection

### bCoordSystemPerWidgetMode
- **类型**: `bool`
- **描述**: If true we restore the coordinate space when changing Widget Modes in the Viewport

### bOnlySelectRigControls
- **类型**: `bool`
- **描述**: If true we can only select Rig Controls in the scene not other Actors.

### bLocalTransformsInEachLocalSpace
- **类型**: `bool`
- **描述**: If true when we transform multiple selected objects in the viewport they each transforms along their own local transform space

### GizmoScale
- **类型**: `float32`
- **描述**: The scale for Gizmos

