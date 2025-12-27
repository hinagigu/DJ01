# URigVMLink

**继承自**: `UObject`

The Link represents a connection between two Pins
within a Graph. The Link can be accessed on the
Graph itself - or through the URigVMPin::GetLinks()
method.

## 方法

### GetGraph
```angelscript
URigVMGraph GetGraph()
```
Returns the Link's owning Graph/

### GetGraphDepth
```angelscript
int GetGraphDepth()
```
Returns the graph nesting depth of this link

### GetLinkIndex
```angelscript
int GetLinkIndex()
```
Returns the current index of this Link within its owning Graph.

### GetOppositePin
```angelscript
URigVMPin GetOppositePin(const URigVMPin InPin)
```
Returns the opposite Pin of this Link given one of its edges (or nullptr)

### GetPinPathRepresentation
```angelscript
FString GetPinPathRepresentation()
```
Returns a string representation of the Link,
for example: "NodeA.Color.R -> NodeB.Translation.X"
note: can be split again using SplitPinPathRepresentation

### GetSourceNode
```angelscript
URigVMNode GetSourceNode()
```
Returns the source Node of this Link (or nullptr)

### GetSourcePin
```angelscript
URigVMPin GetSourcePin()
```
Returns the source Pin of this Link (or nullptr)

### GetTargetNode
```angelscript
URigVMNode GetTargetNode()
```
Returns the target Node of this Link (or nullptr)

### GetTargetPin
```angelscript
URigVMPin GetTargetPin()
```
Returns the target Pin of this Link (or nullptr)

