# URigVMNode

**继承自**: `UObject`

The Node represents a single statement within a Graph.
Nodes can represent values such as Variables / Parameters,
they can represent Function Invocations or Control Flow
logic statements (such as If conditions of For loops).
Additionally Nodes are used to represent Comment statements.
Nodes contain Pins to represent parameters for Function
Invocations or Value access on Variables / Parameters.

## 方法

### CanBeUpgraded
```angelscript
bool CanBeUpgraded()
```
returns true if the node can be upgraded

### CanOnlyExistOnce
```angelscript
bool CanOnlyExistOnce()
```
Returns true if this node can only exist once in a graph

### ExecutionIsHaltedAtThisNode
```angelscript
bool ExecutionIsHaltedAtThisNode()
```

### FindFunctionForNode
```angelscript
URigVMLibraryNode FindFunctionForNode()
```

### FindPin
```angelscript
URigVMPin FindPin(FString InPinPath)
```
Returns a Pin given it's partial pin path below
this node (for example: "Color.R")

### GetAggregateInputs
```angelscript
TArray<URigVMPin> GetAggregateInputs()
```

### GetAggregateOutputs
```angelscript
TArray<URigVMPin> GetAggregateOutputs()
```

### GetAllPinsRecursively
```angelscript
TArray<URigVMPin> GetAllPinsRecursively()
```
Returns all of the Pins of this Node (including SubPins).

### GetDecoratorPins
```angelscript
TArray<URigVMPin> GetDecoratorPins()
```

### GetEventName
```angelscript
FName GetEventName()
```
Returns the name of the event

### GetFirstAggregatePin
```angelscript
URigVMPin GetFirstAggregatePin()
```

### GetGraph
```angelscript
URigVMGraph GetGraph()
```
Returns the Graph of this Node

### GetGraphDepth
```angelscript
int GetGraphDepth()
```
Returns the graph nesting depth of this node

### GetInjectionInfo
```angelscript
URigVMInjectionInfo GetInjectionInfo()
```
Returns the injection info of this Node (or nullptr)

### GetLinkedSourceNodes
```angelscript
TArray<URigVMNode> GetLinkedSourceNodes()
```
Returns a list of Nodes connected as sources to
this Node as the target.

### GetLinkedTargetNodes
```angelscript
TArray<URigVMNode> GetLinkedTargetNodes()
```
Returns a list of Nodes connected as targets to
this Node as the source.

### GetLinks
```angelscript
TArray<URigVMLink> GetLinks()
```
Returns all links to any pin on this node

### GetNextAggregateName
```angelscript
FName GetNextAggregateName(FName InLastAggregatePinName)
```

### GetNodeColor
```angelscript
FLinearColor GetNodeColor()
```
Returns the color of this node - used for UI.

### GetNodeIndex
```angelscript
int GetNodeIndex()
```
Returns the current index of the Node within the Graph.

### GetNodePath
```angelscript
FString GetNodePath(bool bRecursive)
```
Returns the a . separated string containing all of the
names used to reach this Node within the Graph.
(for now this is the same as the Node's name)

### GetNodeTitle
```angelscript
FString GetNodeTitle()
```
Returns the title of this Node - used for UI.

### GetOppositeAggregatePin
```angelscript
URigVMPin GetOppositeAggregatePin()
```

### GetOrphanedPins
```angelscript
TArray<URigVMPin> GetOrphanedPins()
```
Returns all of the top-level orphaned Pins of this Node.

### GetPins
```angelscript
TArray<URigVMPin> GetPins()
```
Returns all of the top-level Pins of this Node.

### GetPosition
```angelscript
FVector2D GetPosition()
```
Returns the 2d position of this node - used for UI.

### GetPreviousFName
```angelscript
FName GetPreviousFName()
```
Returns the name of the node prior to the renaming

### GetRootGraph
```angelscript
URigVMGraph GetRootGraph()
```
Returns the top level / root Graph of this Node

### GetSecondAggregatePin
```angelscript
URigVMPin GetSecondAggregatePin()
```

### GetSize
```angelscript
FVector2D GetSize()
```
Returns the 2d size of this node - used for UI.

### GetSupportedWorkflows
```angelscript
TArray<FRigVMUserWorkflow> GetSupportedWorkflows(ERigVMUserWorkflowType InType, const UObject InSubject)
```
returns all supported workflows of the node

### GetToolTipText
```angelscript
FText GetToolTipText()
```
Returns the tooltip of this node

### HasBreakpoint
```angelscript
bool HasBreakpoint()
```

### HasInputPin
```angelscript
bool HasInputPin(bool bIncludeIO)
```
Returns true if the node has any input pins

### HasIOPin
```angelscript
bool HasIOPin()
```
Returns true if the node has any io pins

### HasLazyPin
```angelscript
bool HasLazyPin(bool bOnlyConsiderPinsWithLinks)
```
Returns true if the node has any lazily evaluating pins

### HasOrphanedPins
```angelscript
bool HasOrphanedPins()
```
Returns true if the node has orphaned pins - which leads to a compiler error

### HasOutputPin
```angelscript
bool HasOutputPin(bool bIncludeIO)
```
Returns true if the node has any output pins

### HasPinOfDirection
```angelscript
bool HasPinOfDirection(ERigVMPinDirection InDirection)
```
Returns true if the node has any pins of the provided direction

### IsAggregate
```angelscript
bool IsAggregate()
```

### IsControlFlowNode
```angelscript
bool IsControlFlowNode()
```
return true if this node is a control flow node

### IsDecoratorPin
```angelscript
bool IsDecoratorPin(FName InName)
```

### IsDefinedAsConstant
```angelscript
bool IsDefinedAsConstant()
```
Returns true if the node is defined as non-varying

### IsDefinedAsVarying
```angelscript
bool IsDefinedAsVarying()
```
Returns true if the node is defined as non-varying

### IsEvent
```angelscript
bool IsEvent()
```
Returns true if this Node is the beginning of a scope

### IsInjected
```angelscript
bool IsInjected()
```
Returns true if this is an injected node.
Injected nodes are managed by pins are are not visible to the user.

### IsInputAggregate
```angelscript
bool IsInputAggregate()
```

### IsLinkedTo
```angelscript
bool IsLinkedTo(URigVMNode InNode)
```
Returns true if this Node is linked to another
given node through any of the Nodes' Pins.

### IsLoopNode
```angelscript
bool IsLoopNode()
```
return true if this node is a loop node

### IsMutable
```angelscript
bool IsMutable()
```
Returns true if this Node has side effects or
internal state.

### IsPure
```angelscript
bool IsPure()
```
Returns true if this Node has no side-effects
and no internal state.

### IsSelected
```angelscript
bool IsSelected()
```
Returns true if this Node is currently selected.

### IsVisibleInUI
```angelscript
bool IsVisibleInUI()
```
Returns true if this should be visible in the UI

### SetExecutionIsHaltedAtThisNode
```angelscript
void SetExecutionIsHaltedAtThisNode(bool bValue)
```

### SetHasBreakpoint
```angelscript
void SetHasBreakpoint(bool bValue)
```

