# UEditorInteractiveGizmoManager

**继承自**: `UInteractiveGizmoManager`

UEditorInteractiveGizmoManager allows users of the Tools framework to register and create selection-based Gizmo instances.
For each selection-based Gizmo, a builder derived from UInteractiveGizmoSelectionBuilder is registered with the GizmoManager.
When the section changes, the highest priority builders for which SatisfiesCondition() return true, will be used to
build gizmos.

