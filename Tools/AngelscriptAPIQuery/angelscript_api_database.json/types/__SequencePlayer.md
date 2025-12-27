# __SequencePlayer

## 方法

### ComputePlayRateFromDuration
```angelscript
float32 ComputePlayRateFromDuration(FSequencePlayerReference SequencePlayer, float32 Duration)
```
Returns the Play Rate to provide when playing this animation if a specific animation duration is desired

### ConvertToSequencePlayer
```angelscript
FSequencePlayerReference ConvertToSequencePlayer(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a sequence player context from an anim node context

### ConvertToSequencePlayerPure
```angelscript
void ConvertToSequencePlayerPure(FAnimNodeReference Node, FSequencePlayerReference& SequencePlayer, bool& Result)
```
Get a sequence player context from an anim node context (pure)

### GetAccumulatedTime
```angelscript
float32 GetAccumulatedTime(FSequencePlayerReference SequencePlayer)
```
Gets the current accumulated time of the sequence player

### GetLoopAnimation
```angelscript
bool GetLoopAnimation(FSequencePlayerReference SequencePlayer)
```
Get the looping state of the sequence player

### GetPlayRate
```angelscript
float32 GetPlayRate(FSequencePlayerReference SequencePlayer)
```
Get the play rate of the sequence player

### GetSequencePure
```angelscript
UAnimSequenceBase GetSequencePure(FSequencePlayerReference SequencePlayer)
```
Get the current sequence of the sequence player

### GetStartPosition
```angelscript
float32 GetStartPosition(FSequencePlayerReference SequencePlayer)
```
Get the start position of the sequence player

### SetAccumulatedTime
```angelscript
FSequencePlayerReference SetAccumulatedTime(FSequencePlayerReference SequencePlayer, float32 Time)
```
Set the current accumulated time of the sequence player

### SetPlayRate
```angelscript
FSequencePlayerReference SetPlayRate(FSequencePlayerReference SequencePlayer, float32 PlayRate)
```
Set the play rate of the sequence player

### SetSequence
```angelscript
FSequencePlayerReference SetSequence(FSequencePlayerReference SequencePlayer, UAnimSequenceBase Sequence)
```
Set the current sequence of the sequence player

### SetStartPosition
```angelscript
FSequencePlayerReference SetStartPosition(FSequencePlayerReference SequencePlayer, float32 StartPosition)
```
Set the start position of the sequence player.
If this is called from On Become Relevant or On Initial Update then it should be accompanied by a call to
SetAccumulatedTime to achieve the desired effect of resetting the play time of a sequence player.

