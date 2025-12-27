# UMeshOpPreviewWithBackgroundCompute

**继承自**: `UObject`

UMeshOpPreviewWithBackgroundCompute is an infrastructure object that implements a common UI
pattern in interactive 3D tools, where we want to run an expensive computation on a mesh that
is based on user-specified parameters, and show a preview of the result. The expensive computation
(a MeshOperator) must run in a background thread so as to not block the UI. If the user
changes parameters while the Operator is running, it should be canceled and restarted.
When it completes, the Preview will be updated. When the user is happy, the current Mesh is
returned to the owner of this object.

The MeshOperators are provided by the owner via a IDynamicMeshOperatorFactory implementation.
The owner must also Tick() this object regularly to allow the Preview to update when the
background computations complete.

If an InProgress Material is set (via ConfigureMaterials) then when a background computation
is active, this material will be used to draw the previous Preview result, to give the
user a visual indication that work is happening.

