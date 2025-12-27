# URigVMController

**继承自**: `UObject`

The Controller is the sole authority to perform changes
on the Graph. The Controller itself is stateless.
The Controller offers a Modified event to subscribe to
for user interface views - so they can be informed about
any change that's happening within the Graph.
The Controller routes all changes through the Graph itself,
so you can have N Controllers performing edits on 1 Graph,
and N Views subscribing to 1 Controller.
In Python you can also subscribe to this event to be
able to react to topological changes of the Graph there.

## 属性

### ModifiedEvent
- **类型**: `FRigVMGraphModifiedDynamicEvent`

## 方法

### AddAggregatePin
```angelscript
FString AddAggregatePin(FString InNodeName, FString InPinName, FString InDefaultValue, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### AddArrayNode
```angelscript
URigVMNode AddArrayNode(ERigVMOpCode InOpCode, FString InCPPType, UObject InCPPTypeObject, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand, bool bIsPatching)
```
Adds a Array Node to the edited Graph.
This causes a NodeAdded modified event.

### AddArrayNodeFromObjectPath
```angelscript
URigVMNode AddArrayNodeFromObjectPath(ERigVMOpCode InOpCode, FString InCPPType, FString InCPPTypeObjectPath, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand, bool bIsPatching)
```
Adds a Array Node to the edited Graph given a struct object path name.
This causes a NodeAdded modified event.

### AddArrayPin
```angelscript
FString AddArrayPin(FString InArrayPinPath, FString InDefaultValue, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds an array element pin to the end of an array pin.
This causes a PinArraySizeChanged modified event.

### AddBranchNode
```angelscript
URigVMNode AddBranchNode(FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a branch node to the graph.
Branch nodes can be used to split the execution of into multiple branches,
allowing to drive behavior by logic.

### AddCommentNode
```angelscript
URigVMCommentNode AddCommentNode(FString InCommentText, FVector2D InPosition, FVector2D InSize, FLinearColor InColor, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Comment Node to the edited Graph.
Comments can be used to annotate the Graph.
This causes a NodeAdded modified event.

### AddDecorator
```angelscript
FName AddDecorator(FName InNodeName, FName InDecoratorTypeObjectPath, FName InDecoratorName, FString InDefaultValue, int InPinIndex, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a decorator to a node

### AddEnumNode
```angelscript
URigVMEnumNode AddEnumNode(FName InCPPTypeObjectPath, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds an enum node to the graph
Enum nodes can be used to represent constant enum values within the graph

### AddExposedPin
```angelscript
FName AddExposedPin(FName InPinName, ERigVMPinDirection InDirection, FString InCPPType, FName InCPPTypeObjectPath, FString InDefaultValue, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds an exposed pin to the graph controlled by this

### AddExternalFunctionReferenceNode
```angelscript
URigVMFunctionReferenceNode AddExternalFunctionReferenceNode(FString InHostPath, FName InFunctionName, FVector2D InNodePosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### AddFreeRerouteNode
```angelscript
URigVMRerouteNode AddFreeRerouteNode(FString InCPPType, FName InCPPTypeObjectPath, bool bIsConstant, FName InCustomWidgetName, FString InDefaultValue, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo)
```
Adds a free Reroute Node

### AddFunctionReferenceNode
```angelscript
URigVMFunctionReferenceNode AddFunctionReferenceNode(URigVMLibraryNode InFunctionDefinition, FVector2D InNodePosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### AddFunctionReferenceNodeFromDescription
```angelscript
URigVMFunctionReferenceNode AddFunctionReferenceNodeFromDescription(FRigVMGraphFunctionHeader InFunctionDefinition, FVector2D InNodePosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a function reference / invocation to the graph

### AddFunctionToLibrary
```angelscript
URigVMLibraryNode AddFunctionToLibrary(FName InFunctionName, bool bMutable, FVector2D InNodePosition, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a function definition to a function library graph

### AddIfNode
```angelscript
URigVMNode AddIfNode(FString InCPPType, FName InCPPTypeObjectPath, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds an if node to the graph.
If nodes can be used to pick between two values based on a condition.

### AddIfNodeFromStruct
```angelscript
URigVMNode AddIfNodeFromStruct(UScriptStruct InScriptStruct, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo)
```

### AddInjectedNode
```angelscript
URigVMInjectionInfo AddInjectedNode(FString InPinPath, bool bAsInput, UScriptStruct InScriptStruct, FName InMethodName, FName InInputPinName, FName InOutputPinName, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Function / Struct Node to the edited Graph as an injected node
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

### AddInjectedNodeFromStructPath
```angelscript
URigVMInjectionInfo AddInjectedNodeFromStructPath(FString InPinPath, bool bAsInput, FString InScriptStructPath, FName InMethodName, FName InInputPinName, FName InOutputPinName, FString InNodeName, bool bSetupUndoRedo)
```
Adds a Function / Struct Node to the edited Graph as an injected node
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

### AddInvokeEntryNode
```angelscript
URigVMInvokeEntryNode AddInvokeEntryNode(FName InEntryName, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds an entry invocation node
This causes a NodeAdded modified event.

### AddLink
```angelscript
bool AddLink(FString InOutputPinPath, FString InInputPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand, ERigVMPinDirection InUserDirection, bool bCreateCastNode)
```
Adds a link to the graph.
This causes a LinkAdded modified event.

### AddLocalVariable
```angelscript
FRigVMGraphVariableDescription AddLocalVariable(FName InVariableName, FString InCPPType, UObject InCPPTypeObject, FString InDefaultValue, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Add a local variable to the graph

### AddLocalVariableFromObjectPath
```angelscript
FRigVMGraphVariableDescription AddLocalVariableFromObjectPath(FName InVariableName, FString InCPPType, FString InCPPTypeObjectPath, FString InDefaultValue, bool bSetupUndoRedo)
```
Add a local variable to the graph given a struct object path name.

### AddRerouteNodeOnLink
```angelscript
URigVMRerouteNode AddRerouteNodeOnLink(URigVMLink InLink, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Reroute Node on an existing Link to the edited Graph.
Reroute Nodes can be used to visually improve the data flow,
they don't require any additional memory though and are purely
cosmetic. This causes a NodeAdded modified event.

### AddRerouteNodeOnLinkPath
```angelscript
URigVMRerouteNode AddRerouteNodeOnLinkPath(FString InLinkPinPathRepresentation, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Reroute Node on an existing Link to the edited Graph given the Link's string representation.
Reroute Nodes can be used to visually improve the data flow,
they don't require any additional memory though and are purely
cosmetic. This causes a NodeAdded modified event.

### AddRerouteNodeOnPin
```angelscript
URigVMRerouteNode AddRerouteNodeOnPin(FString InPinPath, bool bAsInput, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Reroute Node on an existing Pin to the editor Graph.
Reroute Nodes can be used to visually improve the data flow,
they don't require any additional memory though and are purely
cosmetic. This causes a NodeAdded modified event.

### AddSelectNode
```angelscript
URigVMNode AddSelectNode(FString InCPPType, FName InCPPTypeObjectPath, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a select node to the graph.
Select nodes can be used to pick between multiple values based on an index.

### AddSelectNodeFromStruct
```angelscript
URigVMNode AddSelectNodeFromStruct(UScriptStruct InScriptStruct, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo)
```

### AddTemplateNode
```angelscript
URigVMTemplateNode AddTemplateNode(FName InNotation, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a template node to the graph.

### AddUnitNode
```angelscript
URigVMUnitNode AddUnitNode(UScriptStruct InScriptStruct, FName InMethodName, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Function / Struct Node to the edited Graph.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

### AddUnitNodeFromStructPath
```angelscript
URigVMUnitNode AddUnitNodeFromStructPath(FString InScriptStructPath, FName InMethodName, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Function / Struct Node to the edited Graph given its struct object path name.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

### AddUnitNodeWithDefaults
```angelscript
URigVMUnitNode AddUnitNodeWithDefaults(UScriptStruct InScriptStruct, FString InDefaults, FName InMethodName, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Function / Struct Node to the edited Graph.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

### AddVariableNode
```angelscript
URigVMVariableNode AddVariableNode(FName InVariableName, FString InCPPType, UObject InCPPTypeObject, bool bIsGetter, FString InDefaultValue, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Variable Node to the edited Graph.
Variables represent local work state for the function and
can be read from and written to.
This causes a NodeAdded modified event.

### AddVariableNodeFromObjectPath
```angelscript
URigVMVariableNode AddVariableNodeFromObjectPath(FName InVariableName, FString InCPPType, FString InCPPTypeObjectPath, bool bIsGetter, FString InDefaultValue, FVector2D InPosition, FString InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Variable Node to the edited Graph given a struct object path name.
Variables represent local work state for the function and
can be read from (bIsGetter == true) or written to (bIsGetter == false).
This causes a NodeAdded modified event.

### BindPinToVariable
```angelscript
bool BindPinToVariable(FString InPinPath, FString InNewBoundVariablePath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Binds a pin to a variable (or removes the binding given NAME_None)
This causes a PinBoundVariableChanged modified event.

### BreakAllLinks
```angelscript
bool BreakAllLinks(FString InPinPath, bool bAsInput, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes all links on a given pin from the graph.
This might cause multiple LinkRemoved modified event.

### BreakLink
```angelscript
bool BreakLink(FString InOutputPinPath, FString InInputPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes a link from the graph.
This causes a LinkRemoved modified event.

### CancelUndoBracket
```angelscript
bool CancelUndoBracket()
```
Cancels an undo bracket / scoped transaction.
This is primarily useful for Python.
This causes a UndoBracketCanceled modified event.

### CanImportNodesFromText
```angelscript
bool CanImportNodesFromText(FString InText)
```
Exports the given nodes as text

### ChangeExposedPinType
```angelscript
bool ChangeExposedPinType(FName InPinName, FString InCPPType, FName InCPPTypeObjectPath, bool& bSetupUndoRedo, bool bSetupOrphanPins, bool bPrintPythonCommand)
```
Changes the type of an exposed pin in the graph controlled by this

### ClearArrayPin
```angelscript
bool ClearArrayPin(FString InArrayPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes all (but one) array element pin from an array pin.
This causes a PinArraySizeChanged modified event.

### ClearNodeSelection
```angelscript
bool ClearNodeSelection(bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Deselects all currently selected nodes in the graph.
This might cause several NodeDeselected modified event.

### CloseUndoBracket
```angelscript
bool CloseUndoBracket()
```
Closes an undo bracket / scoped transaction.
This is primarily useful for Python.
This causes a UndoBracketClosed modified event.

### CollapseNodes
```angelscript
URigVMCollapseNode CollapseNodes(TArray<FName> InNodeNames, FString InCollapseNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand, bool bIsAggregate)
```
Turns a series of nodes into a Collapse node

### DuplicateArrayPin
```angelscript
FString DuplicateArrayPin(FString InArrayElementPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Duplicates an array element pin.
This causes a PinArraySizeChanged modified event.

### EjectNodeFromPin
```angelscript
URigVMNode EjectNodeFromPin(FString InPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Ejects the last injected node on a pin

### EnableReporting
```angelscript
void EnableReporting(bool bEnabled)
```
Enables or disables the error reporting of this Controller.

### ExpandLibraryNode
```angelscript
TArray<URigVMNode> ExpandLibraryNode(FName InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Turns a library node into its contained nodes

### ExportNodesToText
```angelscript
FString ExportNodesToText(TArray<FName> InNodeNames, bool bIncludeExteriorLinks)
```
Exports the given nodes as text

### ExportSelectedNodesToText
```angelscript
FString ExportSelectedNodesToText(bool bIncludeExteriorLinks)
```
Exports the selected nodes as text

### GeneratePythonCommands
```angelscript
TArray<FString> GeneratePythonCommands()
```

### GetControllerForGraph
```angelscript
URigVMController GetControllerForGraph(const URigVMGraph InGraph)
```
Returns another controller for a given graph

### GetGraph
```angelscript
URigVMGraph GetGraph()
```
Returns the currently edited Graph of this controller.

### GetPinDefaultValue
```angelscript
FString GetPinDefaultValue(FString InPinPath)
```
Returns the default value of a pin given its pinpath.

### GetSchema
```angelscript
URigVMSchema GetSchema()
```
Returns the schema used by this controller

### GetTopLevelGraph
```angelscript
URigVMGraph GetTopLevelGraph()
```
Returns the top level graph

### ImportNodesFromText
```angelscript
TArray<FName> ImportNodesFromText(FString InText, bool bSetupUndoRedo, bool bPrintPythonCommands)
```
Exports the given nodes as text

### InsertArrayPin
```angelscript
FString InsertArrayPin(FString InArrayPinPath, int InIndex, FString InDefaultValue, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Inserts an array element pin into an array pin.
This causes a PinArraySizeChanged modified event.

### IsFunctionPublic
```angelscript
bool IsFunctionPublic(FName InFunctionName)
```
Returns true if a function is marked as public in the function library

### IsReportingEnabled
```angelscript
bool IsReportingEnabled()
```
Returns true if reporting is enabled

### IsTransacting
```angelscript
bool IsTransacting()
```
Returns true if the controller is currently transacting

### LocalizeFunction
```angelscript
URigVMLibraryNode LocalizeFunction(FRigVMGraphFunctionIdentifier InFunctionDefinition, bool bLocalizeDependentPrivateFunctions, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### LocalizeFunctionFromPath
```angelscript
URigVMLibraryNode LocalizeFunctionFromPath(FString InHostPath, FName InFunctionName, bool bLocalizeDependentPrivateFunctions, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Copies a function declaration into this graph's local function library

### LocalizeFunctions
```angelscript
TMap<FRigVMGraphFunctionIdentifier,URigVMLibraryNode> LocalizeFunctions(TArray<FRigVMGraphFunctionIdentifier> InFunctionDefinitions, bool bLocalizeDependentPrivateFunctions, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Copies a series of function declaratioms into this graph's local function library

### MakeBindingsFromVariableNode
```angelscript
bool MakeBindingsFromVariableNode(FName InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Turns a variable node into one or more bindings

### MakeOptionsForWorkflow
```angelscript
URigVMUserWorkflowOptions MakeOptionsForWorkflow(UObject InSubject, FRigVMUserWorkflow InWorkflow)
```
creates the options struct for a given workflow

### MakeVariableNodeFromBinding
```angelscript
bool MakeVariableNodeFromBinding(FString InPinPath, FVector2D InNodePosition, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Turns a binding to a variable node

### MarkFunctionAsPublic
```angelscript
bool MarkFunctionAsPublic(FName InFunctionName, bool bInIsPublic, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Mark a function as public/private in the function library

### OpenUndoBracket
```angelscript
bool OpenUndoBracket(FString InTitle)
```
Opens an undo bracket / scoped transaction for
a series of actions to be performed as one step on the
Undo stack. This is primarily useful for Python.
This causes a UndoBracketOpened modified event.

### PerformUserWorkflow
```angelscript
bool PerformUserWorkflow(FRigVMUserWorkflow InWorkflow, const URigVMUserWorkflowOptions InOptions, bool bSetupUndoRedo)
```
performs all actions representing the workflow

### PromoteCollapseNodeToFunctionReferenceNode
```angelscript
FName PromoteCollapseNodeToFunctionReferenceNode(FName InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand, FString InExistingFunctionDefinitionPath)
```
Turns a collapse node into a function node

### PromoteFunctionReferenceNodeToCollapseNode
```angelscript
FName PromoteFunctionReferenceNodeToCollapseNode(FName InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand, bool bRemoveFunctionDefinition)
```
Turns a collapse node into a function node

### PromotePinToVariable
```angelscript
bool PromotePinToVariable(FString InPinPath, bool bCreateVariableNode, FVector2D InNodePosition, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Promotes a pin to a variable

### Redo
```angelscript
bool Redo()
```
Re-does the last action on the stack.
Note: This should really only be used for unit tests,
use the GEditor's main Undo method instead.

### RefreshVariableNode
```angelscript
void RefreshVariableNode(FName InNodeName, FName InVariableName, FString InCPPType, UObject InCPPTypeObject, bool bSetupUndoRedo, bool bSetupOrphanPins)
```
Refreshes the variable node with the new data

### RemoveAggregatePin
```angelscript
bool RemoveAggregatePin(FString InPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### RemoveArrayPin
```angelscript
bool RemoveArrayPin(FString InArrayElementPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes an array element pin from an array pin.
This causes a PinArraySizeChanged modified event.

### RemoveDecorator
```angelscript
bool RemoveDecorator(FName InNodeName, FName InDecoratorName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes a decorator from a node

### RemoveExposedPin
```angelscript
bool RemoveExposedPin(FName InPinName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes an exposed pin from the graph controlled by this

### RemoveFunctionFromLibrary
```angelscript
bool RemoveFunctionFromLibrary(FName InFunctionName, bool bSetupUndoRedo)
```
Removes a function from a function library graph

### RemoveInjectedNode
```angelscript
bool RemoveInjectedNode(FString InPinPath, bool bAsInput, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes an injected node
This causes a NodeRemoved modified event.

### RemoveLocalVariable
```angelscript
bool RemoveLocalVariable(FName InVariableName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Remove a local variable from the graph

### RemoveNode
```angelscript
bool RemoveNode(URigVMNode InNode, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes a node from the graph
This causes a NodeRemoved modified event.

### RemoveNodeByName
```angelscript
bool RemoveNodeByName(FName InNodeName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes a node from the graph given the node's name.
This causes a NodeRemoved modified event.

### RemoveNodes
```angelscript
bool RemoveNodes(TArray<URigVMNode> InNodes, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes a list of nodes from the graph
This causes a NodeRemoved modified event.

### RemoveNodesByName
```angelscript
bool RemoveNodesByName(TArray<FName> InNodeNames, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes a list of nodes from the graph given the names
This causes a NodeRemoved modified event.

### RenameExposedPin
```angelscript
bool RenameExposedPin(FName InOldPinName, FName InNewPinName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Renames an exposed pin in the graph controlled by this

### RenameFunction
```angelscript
bool RenameFunction(FName InOldFunctionName, FName InNewFunctionName, bool bSetupUndoRedo)
```
Renames a function in the function library

### RenameLocalVariable
```angelscript
bool RenameLocalVariable(FName InVariableName, FName InNewVariableName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Rename a local variable from the graph

### RenameNode
```angelscript
bool RenameNode(URigVMNode InNode, FName InNewName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Renames a node in the graph
This causes a NodeRenamed modified event.

### ReplaceParameterNodeWithVariable
```angelscript
URigVMVariableNode ReplaceParameterNodeWithVariable(FName InNodeName, FName InVariableName, FString InCPPType, UObject InCPPTypeObject, bool bSetupUndoRedo)
```
Refreshes the variable node with the new data

### ResetPinDefaultValue
```angelscript
bool ResetPinDefaultValue(FString InPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Resets the default value of a pin given its pinpath.
This causes a PinDefaultValueChanged modified event.

### ResolveWildCardPin
```angelscript
bool ResolveWildCardPin(FString InPinPath, FString InCPPType, FName InCPPTypeObjectPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Resolves a wildcard pin on any node

### SelectNode
```angelscript
bool SelectNode(URigVMNode InNode, bool bSelect, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Selects a single node in the graph.
This causes a NodeSelected / NodeDeselected modified event.

### SelectNodeByName
```angelscript
bool SelectNodeByName(FName InNodeName, bool bSelect, bool bSetupUndoRedo)
```
Selects a single node in the graph by name.
This causes a NodeSelected / NodeDeselected modified event.

### SetArrayPinSize
```angelscript
bool SetArrayPinSize(FString InArrayPinPath, int InSize, FString InDefaultValue, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Sets the size of the array pin
This causes a PinArraySizeChanged modified event.

### SetCommentText
```angelscript
bool SetCommentText(URigVMNode InNode, FString InCommentText, int InCommentFontSize, bool bInCommentBubbleVisible, bool bInCommentColorBubble, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Sets the comment text and properties of a comment node in the graph.
This causes a CommentTextChanged modified event.

### SetCommentTextByName
```angelscript
bool SetCommentTextByName(FName InNodeName, FString InCommentText, int InCommentFontSize, bool bInCommentBubbleVisible, bool bInCommentColorBubble, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Sets the comment text and properties of a comment node in the graph by name.
This causes a CommentTextChanged modified event.

### SetExposedPinIndex
```angelscript
bool SetExposedPinIndex(FName InPinName, int InNewIndex, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Sets the index for an exposed pin. This can be used to move the pin up and down on the node.

### SetIsRunningUnitTest
```angelscript
void SetIsRunningUnitTest(bool bIsRunning)
```
Helper function to disable a series of checks that can be ignored during a unit test

### SetLocalVariableDefaultValue
```angelscript
bool SetLocalVariableDefaultValue(FName InVariableName, FString InDefaultValue, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### SetLocalVariableType
```angelscript
bool SetLocalVariableType(FName InVariableName, FString InCPPType, UObject InCPPTypeObject, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Sets the type of the local variable

### SetLocalVariableTypeFromObjectPath
```angelscript
bool SetLocalVariableTypeFromObjectPath(FName InVariableName, FString InCPPType, FString InCPPTypeObjectPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### SetNodeCategory
```angelscript
bool SetNodeCategory(URigVMCollapseNode InNode, FString InCategory, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the category of a node in the graph.
This causes a NodeCategoryChanged modified event.

### SetNodeCategoryByName
```angelscript
bool SetNodeCategoryByName(FName InNodeName, FString InCategory, bool bSetupUndoRedo, bool bMergeUndoAction)
```
Sets the category of a node in the graph.
This causes a NodeCategoryChanged modified event.

### SetNodeColor
```angelscript
bool SetNodeColor(URigVMNode InNode, FLinearColor InColor, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the color of a node in the graph.
This causes a NodeColorChanged modified event.

### SetNodeColorByName
```angelscript
bool SetNodeColorByName(FName InNodeName, FLinearColor InColor, bool bSetupUndoRedo, bool bMergeUndoAction)
```
Sets the color of a node in the graph by name.
This causes a NodeColorChanged modified event.

### SetNodeDescription
```angelscript
bool SetNodeDescription(URigVMCollapseNode InNode, FString InDescription, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the function description of a node in the graph.
This causes a NodeDescriptionChanged modified event.

### SetNodeDescriptionByName
```angelscript
bool SetNodeDescriptionByName(FName InNodeName, FString InDescription, bool bSetupUndoRedo, bool bMergeUndoAction)
```
Sets the keywords of a node in the graph.
This causes a NodeDescriptionChanged modified event.

### SetNodeKeywords
```angelscript
bool SetNodeKeywords(URigVMCollapseNode InNode, FString InKeywords, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the keywords of a node in the graph.
This causes a NodeKeywordsChanged modified event.

### SetNodeKeywordsByName
```angelscript
bool SetNodeKeywordsByName(FName InNodeName, FString InKeywords, bool bSetupUndoRedo, bool bMergeUndoAction)
```
Sets the keywords of a node in the graph.
This causes a NodeKeywordsChanged modified event.

### SetNodePosition
```angelscript
bool SetNodePosition(URigVMNode InNode, FVector2D InPosition, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the position of a node in the graph.
This causes a NodePositionChanged modified event.

### SetNodePositionByName
```angelscript
bool SetNodePositionByName(FName InNodeName, FVector2D InPosition, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the position of a node in the graph by name.
This causes a NodePositionChanged modified event.

### SetNodeSelection
```angelscript
bool SetNodeSelection(TArray<FName> InNodeNames, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Selects the nodes given the selection
This might cause several NodeDeselected modified event.

### SetNodeSize
```angelscript
bool SetNodeSize(URigVMNode InNode, FVector2D InSize, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the size of a node in the graph.
This causes a NodeSizeChanged modified event.

### SetNodeSizeByName
```angelscript
bool SetNodeSizeByName(FName InNodeName, FVector2D InSize, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand)
```
Sets the size of a node in the graph by name.
This causes a NodeSizeChanged modified event.

### SetPinDefaultValue
```angelscript
bool SetPinDefaultValue(FString InPinPath, FString InDefaultValue, bool bResizeArrays, bool bSetupUndoRedo, bool bMergeUndoAction, bool bPrintPythonCommand, bool bSetValueOnLinkedPins)
```
Sets the default value of a pin given its pinpath.
This causes a PinDefaultValueChanged modified event.

### SetPinExpansion
```angelscript
bool SetPinExpansion(FString InPinPath, bool bIsExpanded, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Sets the pin to be expanded or not
This causes a PinExpansionChanged modified event.

### SetPinIsWatched
```angelscript
bool SetPinIsWatched(FString InPinPath, bool bIsWatched, bool bSetupUndoRedo)
```
Sets the pin to be watched (or not)
This causes a PinWatchedChanged modified event.

### SetRemappedVariable
```angelscript
bool SetRemappedVariable(URigVMFunctionReferenceNode InFunctionRefNode, FName InInnerVariableName, FName InOuterVariableName, bool bSetupUndoRedo)
```
Sets the remapped variable on a function reference node

### SetSchema
```angelscript
void SetSchema(URigVMSchema InSchema)
```
Sets the schema on the controller

### SetUnitNodeDefaults
```angelscript
bool SetUnitNodeDefaults(URigVMUnitNode InNode, FString InDefaults, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Adds a Function / Struct Node to the edited Graph.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

### UnbindPinFromVariable
```angelscript
bool UnbindPinFromVariable(FString InPinPath, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Removes the binging of a pin to a variable
This causes a PinBoundVariableChanged modified event.

### Undo
```angelscript
bool Undo()
```
Un-does the last action on the stack.
Note: This should really only be used for unit tests,
use the GEditor's main Undo method instead.

### UnresolveTemplateNodes
```angelscript
bool UnresolveTemplateNodes(TArray<FName> InNodeNames, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Turns a resolved templated node(s) back into its template.

### UpgradeNodes
```angelscript
TArray<URigVMNode> UpgradeNodes(TArray<FName> InNodeNames, bool bRecursive, bool bSetupUndoRedo, bool bPrintPythonCommand)
```
Upgrades a set of nodes with each corresponding next known version

