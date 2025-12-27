# UDrawSplineToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### bLoop
- **类型**: `bool`
- **描述**: Determines whether the created spline is a loop. This can be toggled using "Closed Loop" in
the detail panel after spline creation.

### OutputMode
- **类型**: `EDrawSplineOutputMode`
- **描述**: Determines how the resulting spline is emitted on tool accept.

### TargetActor
- **类型**: `TWeakObjectPtr<AActor>`
- **描述**: Actor to attach to when Output Mode is "Existing Actor"

### BlueprintToCreate
- **类型**: `TWeakObjectPtr<UBlueprint>`
- **描述**: Blueprint to create when Output Mode is "Create Blueprint"

### ExistingSplineIndexToReplace
- **类型**: `int`
- **描述**: When attaching to an existing actor or creating a blueprint, controls whether the drawn
spline replaces one of the target's existing components or gets added as a new one (if
the index is out of bounds).

### DrawMode
- **类型**: `EDrawSplineDrawMode`
- **描述**: How the spline is drawn in the tool.

### MinPointSpacing
- **类型**: `float`
- **描述**: Point spacing when Draw Mode is "Free Draw"

### ClickOffset
- **类型**: `float`
- **描述**: How far to offset spline points from the clicked surface, along the surface normal

### OffsetMethod
- **类型**: `ESplineOffsetMethod`
- **描述**: How to choose the direction to offset points from the clicked surface

### OffsetDirection
- **类型**: `FVector`
- **描述**: Manually-specified click offset direction. Note: Will be normalized. If it is a zero vector, a default Up vector will be used instead.

### FrameVisualizationWidth
- **类型**: `float`
- **描述**: When nonzero, allows a visualization of the rotation of the spline. Can be controlled
in the detail panel after creation via "Scale Visualization Width" property.

### UpVectorMode
- **类型**: `EDrawSplineUpVectorMode`
- **描述**: How the spline rotation is set. It is suggested to use a nonzero FrameVisualizationWidth to
see the effects.

### bPreviewUsingActorCopy
- **类型**: `bool`
- **描述**: When modifying existing actors, whether the result should be previewed using a copy
of that actor (rather than just drawing the spline by itself). Could be toggled off
if something about duplicating the given actor is problematic.

### bHitWorld
- **类型**: `bool`
- **描述**: Whether to place spline points on the surface of objects in the world

### bHitCustomPlane
- **类型**: `bool`
- **描述**: Whether to place spline points on a custom, user-adjustable plane

### bHitGroundPlanes
- **类型**: `bool`
- **描述**: Whether to place spline points on a plane through the origin aligned with the Z axis in perspective views, or facing the camera in othographic views

### bRerunConstructionScriptOnDrag
- **类型**: `bool`
- **描述**: If modifying a blueprint actor, whether to run the construction script while dragging
or only at the end of a drag. Can be toggled off for expensive construction scripts.

