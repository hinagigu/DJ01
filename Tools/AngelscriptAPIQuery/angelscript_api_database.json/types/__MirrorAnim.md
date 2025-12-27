# __MirrorAnim

## 方法

### ConvertToMirrorNode
```angelscript
FMirrorAnimNodeReference ConvertToMirrorNode(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a mirror node context from an anim node context

### ConvertToMirrorNodePure
```angelscript
void ConvertToMirrorNodePure(FAnimNodeReference Node, FMirrorAnimNodeReference& MirrorNode, bool& Result)
```
Get a mirror context from an anim node context (pure)

### GetMirror
```angelscript
bool GetMirror(FMirrorAnimNodeReference MirrorNode)
```
Get the mirror state

### GetMirrorDataTable
```angelscript
UMirrorDataTable GetMirrorDataTable(FMirrorAnimNodeReference MirrorNode)
```
Get MirrorDataTable used to perform mirroring

### GetMirrorTransitionBlendTime
```angelscript
float32 GetMirrorTransitionBlendTime(FMirrorAnimNodeReference MirrorNode)
```
Get how long to blend using inertialization when switching mirrored state

### SetMirror
```angelscript
FMirrorAnimNodeReference SetMirror(FMirrorAnimNodeReference MirrorNode, bool bInMirror)
```
Set the mirror state

### SetMirrorTransitionBlendTime
```angelscript
FMirrorAnimNodeReference SetMirrorTransitionBlendTime(FMirrorAnimNodeReference MirrorNode, float32 InBlendTime)
```
Set how long to blend using inertialization when switching mirrored state

