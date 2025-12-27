# UTransformMeshesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties of the Transform Meshes operation

## 属性

### TransformMode
- **类型**: `ETransformMeshesTransformMode`
- **描述**: Transformation Mode controls the overall behavior of the Gizmos in the Tool

### bApplyToInstances
- **类型**: `bool`
- **描述**: When true, transformations are applied to the Instances of any Instanced Components (eg InstancedStaticMeshComponent) instead of to the Components

### bSetPivotMode
- **类型**: `bool`
- **描述**: When true, the Gizmo can be moved independently without affecting objects. This allows the Gizmo to be repositioned before transforming.

### bEnableSnapDragging
- **类型**: `bool`
- **描述**: When Snap-Dragging is enabled, you can Click-drag starting on the target objects to reposition them relative to the rest of the scene

### SnapDragSource
- **类型**: `ETransformMeshesSnapDragSource`
- **描述**: Which point on the object being Snap-Dragged to use as the "Source" point

### RotationMode
- **类型**: `ETransformMeshesSnapDragRotationMode`
- **描述**: How the object being Snap-Dragged should be rotated relative to the Source point location and Hit Surface normal

