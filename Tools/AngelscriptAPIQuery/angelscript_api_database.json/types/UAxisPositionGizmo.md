# UAxisPositionGizmo

**继承自**: `UInteractiveGizmo`

UAxisPositionGizmo implements a gizmo interaction where 1D parameter value is manipulated
by dragging a point on a 3D line/axis in space. The 3D point is converted to the axis parameter at
the nearest point, giving us the 1D parameter value.

As with other base gizmos, this class only implements the interaction. The visual aspect of the
gizmo, the axis, and the parameter storage are all provided externally.

The axis direction+origin is provided by an IGizmoAxisSource.

The interaction target (ie the thing you have to click on to start the dragging interaction) is provided by an IGizmoClickTarget.

The new 1D parameter value is sent to an IGizmoFloatParameterSource

Internally a UClickDragInputBehavior is used to handle mouse input, configured in ::Setup()

