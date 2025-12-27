# UGizmoUniformScaleParameterSource

**继承自**: `UGizmoBaseVec2ParameterSource`

UGizmoUniformScaleParameterSource is an IGizmoVec2ParameterSource implementation that
interprets the Vec2 parameter as the position in a 2D plane, and maps this parameter to a
change in a uniform scale value. This scale is applied to an IGizmoTransformSource.

The X/Y plane parameter deltas are converted to a uniform scale delta simply by adding them.
This assumpes that the 3D plane is oriented such that "positive" along the X and Y
tangent axes corresponds to something semantically meaningful. It's up to the client to do this.

This ParameterSource is intended to be used to create 3D Uniform Scale Gizmos.

