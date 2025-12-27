# __BlendSpacePlayer

## 方法

### ConvertToBlendSpacePlayer
```angelscript
FBlendSpacePlayerReference ConvertToBlendSpacePlayer(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a blend space player context from an anim node context.

### ConvertToBlendSpacePlayerPure
```angelscript
void ConvertToBlendSpacePlayerPure(FAnimNodeReference Node, FBlendSpacePlayerReference& BlendSpacePlayer, bool& Result)
```
Get a blend space player context from an anim node context (pure).

### GetBlendSpace
```angelscript
UBlendSpace GetBlendSpace(FBlendSpacePlayerReference BlendSpacePlayer)
```
Get the current BlendSpace of the blend space player.

### GetLoop
```angelscript
bool GetLoop(FBlendSpacePlayerReference BlendSpacePlayer)
```
Get the current loop of the blend space player.

### GetPlayRate
```angelscript
float32 GetPlayRate(FBlendSpacePlayerReference BlendSpacePlayer)
```
Get the current play rate of the blend space player.

### GetPosition
```angelscript
FVector GetPosition(FBlendSpacePlayerReference BlendSpacePlayer)
```
Get the current position of the blend space player.

### GetStartPosition
```angelscript
float32 GetStartPosition(FBlendSpacePlayerReference BlendSpacePlayer)
```
Get the current start position of the blend space player.

### SetBlendSpace
```angelscript
FBlendSpacePlayerReference SetBlendSpace(FBlendSpacePlayerReference BlendSpacePlayer, UBlendSpace BlendSpace)
```
Set the current BlendSpace of the blend space player.

### SetLoop
```angelscript
FBlendSpacePlayerReference SetLoop(FBlendSpacePlayerReference BlendSpacePlayer, bool bLoop)
```
Set the loop of the blend space player.

### SetPlayRate
```angelscript
FBlendSpacePlayerReference SetPlayRate(FBlendSpacePlayerReference BlendSpacePlayer, float32 PlayRate)
```
Set the play rate of the blend space player.

### SetResetPlayTimeWhenBlendSpaceChanges
```angelscript
FBlendSpacePlayerReference SetResetPlayTimeWhenBlendSpaceChanges(FBlendSpacePlayerReference BlendSpacePlayer, bool bReset)
```
Set whether the current play time should reset when BlendSpace changes of the blend space player.

### ShouldResetPlayTimeWhenBlendSpaceChanges
```angelscript
bool ShouldResetPlayTimeWhenBlendSpaceChanges(FBlendSpacePlayerReference BlendSpacePlayer)
```
Get the current value of whether the current play time should reset when BlendSpace changes of the blend space player.

### SnapToPosition
```angelscript
void SnapToPosition(FBlendSpacePlayerReference BlendSpacePlayer, FVector NewPosition)
```
Forces the Position to the specified value

