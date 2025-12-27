# UCurveControlPointsMechanic

**继承自**: `UInteractionMechanic`

A mechanic for displaying a sequence of control points and moving them about. Has an interactive initialization mode for
first setting the points.

When editing, hold shift to select multiple points. Hold Ctrl to add an extra point along an edge. To add points to either end of
the sequence, first select either the first or last point and then hold Ctrl.
Backspace deletes currently selected points. In edit mode, holding Shift generally toggles the snapping behavior (makes it opposite
of the current SnappingEnabled setting), though this is not yet implemented while the gizmo is being dragged.

TODO:
- Make it possible to open/close loop in edit mode
- Improve display of occluded control points (checkerboard the material)
- Allow deselection of vertices by clicking away?
- Lump the point/line set components into PreviewGeometryActor.

