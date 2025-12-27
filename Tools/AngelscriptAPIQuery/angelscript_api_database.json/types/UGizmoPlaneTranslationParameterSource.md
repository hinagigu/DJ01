# UGizmoPlaneTranslationParameterSource

**继承自**: `UGizmoBaseVec2ParameterSource`

UGizmoAxisRotationParameterSource is an IGizmoVec2ParameterSource implementation that
interprets the FVector2D parameter as a position in a 2D plane, and maps this position to a 3D translation in
a plane with origin/normal given by an IGizmoAxisSource. This translation is applied to an IGizmoTransformSource.

This ParameterSource is intended to be used to create 3D Plane Translation Gizmos.

