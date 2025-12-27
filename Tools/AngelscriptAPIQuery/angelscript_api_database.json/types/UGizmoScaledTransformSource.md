# UGizmoScaledTransformSource

**继承自**: `UGizmoBaseTransformSource`

@deprecated Use UGizmoScaledAndUnscaledTransformSources instead.

Old description:
UGizmoScaledTransformSource wraps another IGizmoTransformSource implementation and adds a
separate scaling vector to the Transform. The main use of this class is to support scaling
in a 3D gizmo without actually scaling the Gizmo itself. Generally our pattern is to apply
the gizmo's position/rotation transform to the target object via a TransformProxy, but
that does not work with Scaling. So this class stores the scaling vector separately, provided by
an external source via FSeparateScaleProvider, and in GetTransform/SetTransform rewrites the
Transform from the child IGizmoTransformSource with the new scale.

