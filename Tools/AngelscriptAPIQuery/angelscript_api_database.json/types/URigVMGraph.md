# URigVMGraph

**继承自**: `UObject`

The Graph represents a Function definition
using Nodes as statements.
Graphs can be compiled into a URigVM using the
FRigVMCompiler.
Graphs provide access to its Nodes, Pins and
Links.

## 方法

### ContainsLink
```angelscript
bool ContainsLink(FString InPinPathRepresentation)
```
Returns true if the graph contains a link given its string representation

### FindLink
```angelscript
URigVMLink FindLink(FString InLinkPinPathRepresentation)
```
Returns a link given its string representation,
for example "NodeA.Color.R -> NodeB.Translation.X"

### FindNode
```angelscript
URigVMNode FindNode(FString InNodePath)
```
Returns a Node given its path (or nullptr).
(for now this is the same as finding a node by its name.)

### FindNodeByName
```angelscript
URigVMNode FindNodeByName(FName InNodeName)
```
Returns a Node given its name (or nullptr).

### FindPin
```angelscript
URigVMPin FindPin(FString InPinPath)
```
Returns a Pin given its path, for example "Node.Color.R".

### GetContainedGraphs
```angelscript
TArray<URigVMGraph> GetContainedGraphs(bool bRecursive)
```
Returns all of the contained graphs

### GetDefaultFunctionLibrary
```angelscript
URigVMFunctionLibrary GetDefaultFunctionLibrary()
```
Returns the locally available function library

### GetEntryNode
```angelscript
URigVMFunctionEntryNode GetEntryNode()
```
Returns the entry node of this graph

### GetEventNames
```angelscript
TArray<FName> GetEventNames()
```
Returns array of event names

### GetGraphDepth
```angelscript
int GetGraphDepth()
```
Returns the root / top level parent graph of this graph (or this if it is the root graph)

### GetGraphName
```angelscript
FString GetGraphName()
```
Returns the name of this graph (as defined by the node path)

### GetInputArguments
```angelscript
TArray<FRigVMGraphVariableDescription> GetInputArguments()
```
Returns the input arguments of this graph

### GetLinks
```angelscript
TArray<URigVMLink> GetLinks()
```
Returns all of the Links within this Graph.

### GetLocalVariables
```angelscript
TArray<FRigVMGraphVariableDescription> GetLocalVariables(bool bIncludeInputArguments)
```
Returns the local variables of this function

### GetNodePath
```angelscript
FString GetNodePath()
```
Returns the path of this graph as defined by its invoking nodes

### GetNodes
```angelscript
TArray<URigVMNode> GetNodes()
```
Returns all of the Nodes within this Graph.

### GetOutputArguments
```angelscript
TArray<FRigVMGraphVariableDescription> GetOutputArguments()
```
Returns the output arguments of this graph

### GetParentGraph
```angelscript
URigVMGraph GetParentGraph()
```
Returns the parent graph of this graph

### GetReturnNode
```angelscript
URigVMFunctionReturnNode GetReturnNode()
```
Returns the return node of this graph

### GetRootGraph
```angelscript
URigVMGraph GetRootGraph()
```
Returns the root / top level parent graph of this graph (or this if it is the root graph)

### GetSelectNodes
```angelscript
TArray<FName> GetSelectNodes()
```
Returns the names of all currently selected Nodes.

### GetVariableDescriptions
```angelscript
TArray<FRigVMGraphVariableDescription> GetVariableDescriptions()
```
Returns a list of unique Variable descriptions within this Graph.
Multiple Variable Nodes can share the same description.

### IsNodeSelected
```angelscript
bool IsNodeSelected(FName InNodeName)
```
Returns true if a Node with a given name is selected.

### IsRootGraph
```angelscript
bool IsRootGraph()
```
Returns true if this graph is a root / top level graph

### IsTopLevelGraph
```angelscript
bool IsTopLevelGraph()
```
Returns true if this graph is the top level graph

### SetDefaultFunctionLibrary
```angelscript
void SetDefaultFunctionLibrary(URigVMFunctionLibrary InFunctionLibrary)
```

