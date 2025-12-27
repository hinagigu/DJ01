# UFractureTransformGizmoSettings

**继承自**: `UFractureToolSettings`

This helps create a 3D transform gizmo that can be used to adjust fracture placement
Note it is tailored to UFractureToolCutterBase, and expects Setup(), Shutdown()
and ResetGizmo() to be called on tool setup, shutdown, and selection change respectively

## 属性

### bUseGizmo
- **类型**: `bool`
- **描述**: Use a 3D rigid transform gizmo to place the fracture pattern.  Only supports grouped fracture.

### bCenterOnSelection
- **类型**: `bool`
- **描述**: Recenter the gizmo to the center of the selection when selection changes

