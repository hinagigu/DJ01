# __LayeredBoneBlend

## 方法

### ConvertToLayeredBlendPerBonePure
```angelscript
void ConvertToLayeredBlendPerBonePure(FAnimNodeReference Node, FLayeredBoneBlendReference& LayeredBoneBlend, bool& Result)
```
Get a layered bone blend context from an anim node context (pure).

### ConvertToLayeredBoneBlend
```angelscript
FLayeredBoneBlendReference ConvertToLayeredBoneBlend(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a layered bone blend context from an anim node context.

### GetNumPoses
```angelscript
int GetNumPoses(FLayeredBoneBlendReference LayeredBoneBlend)
```
Get the number of poses that a layered bone blend node has (this does not include the base pose)

