# __EToolChangeTrackingMode

UInteractiveToolManager can emit change events for the active tool in various ways.
This allows different modes to control how tools activate/deactivate on undo/redo, which is necessary
because some modes (eg Modeling Mode) do not support redo "into" a Tool, while others require it (like Paint Mode)

## 属性

### NoChangeTracking
- **类型**: `EToolChangeTrackingMode`

### UndoToExit
- **类型**: `EToolChangeTrackingMode`

### FullUndoRedo
- **类型**: `EToolChangeTrackingMode`

### EToolChangeTrackingMode_MAX
- **类型**: `EToolChangeTrackingMode`

