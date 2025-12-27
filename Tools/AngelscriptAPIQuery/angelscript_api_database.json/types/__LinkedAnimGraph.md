# __LinkedAnimGraph

## 方法

### ConvertToLinkedAnimGraph
```angelscript
FLinkedAnimGraphReference ConvertToLinkedAnimGraph(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a linked anim graph reference from an anim node reference

### ConvertToLinkedAnimGraphPure
```angelscript
void ConvertToLinkedAnimGraphPure(FAnimNodeReference Node, FLinkedAnimGraphReference& LinkedAnimGraph, bool& Result)
```
Get a linked anim graph reference from an anim node reference (pure)

### GetLinkedAnimInstance
```angelscript
UAnimInstance GetLinkedAnimInstance(FLinkedAnimGraphReference Node)
```
Get the linked instance is hosted by this node. If the node does not host an instance then HasLinkedAnimInstance will return false

### HasLinkedAnimInstance
```angelscript
bool HasLinkedAnimInstance(FLinkedAnimGraphReference Node)
```
Returns whether the node hosts an instance (e.g. linked anim graph or layer)

