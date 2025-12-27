# UCombinedTransformGizmo

**继承自**: `UInteractiveGizmo`

UCombinedTransformGizmo provides standard Transformation Gizmo interactions,
applied to a UTransformProxy target object. By default the Gizmo will be
a standard XYZ translate/rotate Gizmo (axis and plane translation).

The in-scene representation of the Gizmo is a ACombinedTransformGizmoActor (or subclass).
This Actor has FProperty members for the various sub-widgets, each as a separate Component.
Any particular sub-widget of the Gizmo can be disabled by setting the respective
Actor Component to null.

So, to create non-standard variants of the Transform Gizmo, set a new GizmoActorBuilder
in the UCombinedTransformGizmoBuilder registered with the GizmoManager. Return
a suitably-configured GizmoActor and everything else will be handled automatically.

