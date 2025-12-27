# UGraphEditorSettings

**继承自**: `UObject`

Implements settings for the graph editor.

## 属性

### DataPinStyle
- **类型**: `EBlueprintPinStyleType`
- **描述**: The visual styling to use for graph editor pins (in Blueprints, materials, etc...)

### PanningMouseButton
- **类型**: `EGraphPanningMouseButton`
- **描述**: Switch between using the right and middle mouse button for panning (defaults to right)

### PaddingAbovePin
- **类型**: `float32`
- **描述**: The amount of padding above a pin (defaults to 4)

### PaddingBelowPin
- **类型**: `float32`
- **描述**: The amount of padding below a pin (defaults to 4)

### PaddingRightOfInput
- **类型**: `float32`
- **描述**: The amount of horizontal padding towards the center of a node on an input pin (defaults to 10)

### PaddingLeftOfOutput
- **类型**: `float32`
- **描述**: The amount of horizontal padding towards the center of a node on an output pin (defaults to 10)

### PaddingTowardsNodeEdge
- **类型**: `float32`
- **描述**: The amount of padding towards the node edge (defaults to 10, can be negative to make pins overlap or stick out of a node

### bTreatSplinesLikePins
- **类型**: `bool`
- **描述**: If enabled, allows splines to be Alt+Clicked to break them or Ctrl+Dragged to move them as if these actions were taking place on the associated pin.

### SplineHoverTolerance
- **类型**: `float32`
- **描述**: The distance threshold controlling how close the mouse has to be to the spline in order to trigger a hover response

### SplineCloseTolerance
- **类型**: `float32`
- **描述**: The additional distance around the spline to count as close, preventing other actions if the user just misses the spline when clicking

### ForwardSplineHorizontalDeltaRange
- **类型**: `float32`
- **描述**: The maximum value to clamp the absolute value of the horizontal distance between endpoints when calculating tangents (when the wire is moving forward)

### ForwardSplineVerticalDeltaRange
- **类型**: `float32`
- **描述**: The maximum value to clamp the absolute value of the vertical distance between endpoints when calculating tangents (when the wire is moving forward)

### ForwardSplineTangentFromHorizontalDelta
- **类型**: `FVector2D`
- **描述**: The amount that the horizontal delta affects the generated tangent handle of splines (when the wire is moving forward)

### ForwardSplineTangentFromVerticalDelta
- **类型**: `FVector2D`
- **描述**: The amount that the vertical delta affects the generated tangent handle of splines (when the wire is moving forward)

### BackwardSplineHorizontalDeltaRange
- **类型**: `float32`
- **描述**: The maximum value to clamp the absolute value of the horizontal distance between endpoints when calculating tangents (when the wire is moving backwards)

### BackwardSplineVerticalDeltaRange
- **类型**: `float32`
- **描述**: The maximum value to clamp the absolute value of the vertical distance between endpoints when calculating tangents (when the wire is moving backwards)

### BackwardSplineTangentFromHorizontalDelta
- **类型**: `FVector2D`
- **描述**: The amount that the horizontal delta affects the generated tangent handle of splines (when the wire is moving backwards)

### BackwardSplineTangentFromVerticalDelta
- **类型**: `FVector2D`
- **描述**: The amount that the vertical delta affects the generated tangent handle of splines (when the wire is moving backwards)

### DefaultPinTypeColor
- **类型**: `FLinearColor`
- **描述**: The default color is used only for types not specifically defined below.  Generally if it's seen, it means another type needs to be defined so that the wire in question can have an appropriate color.

### ExecutionPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Execution pin type color

### BooleanPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Boolean pin type color

### BytePinTypeColor
- **类型**: `FLinearColor`
- **描述**: Byte pin type color

### ClassPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Class pin type color

### IntPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Integer pin type color

### Int64PinTypeColor
- **类型**: `FLinearColor`
- **描述**: Integer64 pin type color

### FloatPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Floating-point pin type color

### DoublePinTypeColor
- **类型**: `FLinearColor`
- **描述**: Double pin type color

### RealPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Real pin type color

### NamePinTypeColor
- **类型**: `FLinearColor`
- **描述**: Name pin type color

### SoftObjectPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Asset pin type color

### SoftClassPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Asset Class pin type color

### DelegatePinTypeColor
- **类型**: `FLinearColor`
- **描述**: Delegate pin type color

### ObjectPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Object pin type color

### InterfacePinTypeColor
- **类型**: `FLinearColor`
- **描述**: Interface pin type color

### StringPinTypeColor
- **类型**: `FLinearColor`
- **描述**: String pin type color

### TextPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Text pin type color

### StructPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Struct pin type color

### WildcardPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Wildcard pin type color

### VectorPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Vector pin type color

### RotatorPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Rotator pin type color

### TransformPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Transform pin type color

### IndexPinTypeColor
- **类型**: `FLinearColor`
- **描述**: Index pin type color

### EventNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Event node title color

### FunctionCallNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: CallFunction node title color

### PureFunctionCallNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Pure function call node title color

### ParentFunctionCallNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Parent class function call node title color

### FunctionTerminatorNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Function Terminator node title color

### ExecBranchNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Exec Branch node title color

### ExecSequenceNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Exec Sequence node title color

### ResultNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Result node title color

### DefaultCommentNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Default Comment node title color

### PreviewNodeTitleColor
- **类型**: `FLinearColor`
- **描述**: Preview node title color

### DefaultDataWireThickness
- **类型**: `float32`
- **描述**: The thickness of a data wire

### DefaultExecutionWireThickness
- **类型**: `float32`
- **描述**: The thickness of an execution wire when not debugging

### TraceAttackColor
- **类型**: `FLinearColor`
- **描述**: The color to display execution wires that were just executed

### TraceAttackWireThickness
- **类型**: `float32`

### TraceSustainColor
- **类型**: `FLinearColor`

### TraceSustainWireThickness
- **类型**: `float32`

### TraceReleaseColor
- **类型**: `FLinearColor`
- **描述**: The color to fade to for execution wires on release

### TraceReleaseWireThickness
- **类型**: `float32`
- **描述**: The thickness to drop down to during release / for unexecuted wires when debugging

### PaddingAutoCollateIncrement
- **类型**: `float32`
- **描述**: The amount of padding to add in order to auto collate multiple created nodes when using tab context menu (defaults to 20)

### bOpenCreateMenuOnBlankGraphAreas
- **类型**: `bool`
- **描述**: If a key press (default Tab) should open the create node context menu when the mouse is on top of blank areas of the graph (defaults to true)

### DefaultCommentNodeMoveMode
- **类型**: `ECommentBoxMode`
- **描述**: Whether a comment node should move any fully enclosed nodes around when it is moved

### bShowCommentBubbleWhenZoomedOut
- **类型**: `bool`
- **描述**: Whether to show a zoom-invariant comment bubble when zoomed out (making the comment node's text readable at any distance)

