# UGizmoAxisScaleParameterSource

**继承自**: `UGizmoBaseFloatParameterSource`

UGizmoAxisScaleParameterSource is an IGizmoFloatParameterSource implementation that
interprets the float value as the parameter of a line equation, and maps this parameter to a scale factor
along a line with origin/direction given by an IGizmoAxisSource. This scale is applied to an IGizmoTransformSource.

This ParameterSource is intended to be used to create 3D Axis Scale Gizmos.

