# UGizmoScaledAndUnscaledTransformSources

**继承自**: `UGizmoBaseTransformSource`

A wrapper around two IGizmoTransformSource's that generally forwards transforms to/from its ScaledTransformSource,
but also forwards an unscaled version of the transform to UnscaledTransformSource on SetTransform calls.
This handles the common case of wanting to apply the entire transform to one IGizmoTransformSource, but only
the unscaled transform to a gizmo component (since we don't want to scale the gizmo component but do want to
rotate/translate it).

