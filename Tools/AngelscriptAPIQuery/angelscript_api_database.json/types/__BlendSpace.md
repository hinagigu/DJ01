# __BlendSpace

## 方法

### ConvertToBlendSpace
```angelscript
FBlendSpaceReference ConvertToBlendSpace(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a blend space context from an anim node context.

### ConvertToBlendSpacePure
```angelscript
void ConvertToBlendSpacePure(FAnimNodeReference Node, FBlendSpaceReference& BlendSpace, bool& Result)
```
Get a blend space context from an anim node context (pure).

### GetFilteredPosition
```angelscript
FVector GetFilteredPosition(FBlendSpaceReference BlendSpace)
```
Get the current sample coordinates after going through the filtering.

### GetPosition
```angelscript
FVector GetPosition(FBlendSpaceReference BlendSpace)
```
Get the current position of the blend space.

### SnapToPosition
```angelscript
void SnapToPosition(FBlendSpaceReference BlendSpace, FVector NewPosition)
```
Forces the Position to the specified value

