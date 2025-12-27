# UPlanePositionGizmo

**继承自**: `UInteractiveGizmo`

UPlanePositionGizmo implements a gizmo interaction where 2D parameter value is manipulated
by dragging a point on a 3D plane in space. The 3D position is converted to 2D coordinates
based on the tangent axes of the plane.

As with other base gizmos, this class only implements the interaction. The visual aspect of the
gizmo, the plane, and the parameter storage are all provided externally.

The plane is provided by an IGizmoAxisSource. The origin and normal define the plane and then
the tangent axes of the source define the coordinate space.

The interaction target (ie the thing you have to click on to start the dragging interaction) is provided by an IGizmoClickTarget.

The new 2D parameter value is sent to an IGizmoVec2ParameterSource

Internally a UClickDragInputBehavior is used to handle mouse input, configured in ::Setup()

