# UPaperFlipbookComponent

**继承自**: `UMeshComponent`

## 属性

### SourceFlipbook
- **类型**: `UPaperFlipbook`
- **描述**: Flipbook currently being played

### OnFinishedPlaying
- **类型**: `FFlipbookFinishedPlaySignature`

## 方法

### GetFlipbook
```angelscript
UPaperFlipbook GetFlipbook()
```
Gets the flipbook used by this instance.

### GetFlipbookFramerate
```angelscript
float32 GetFlipbookFramerate()
```
Get the nominal framerate that the flipbook will be played back at (ignoring PlayRate), in frames per second

### GetFlipbookLength
```angelscript
float32 GetFlipbookLength()
```
Get length of the flipbook (in seconds)

### GetFlipbookLengthInFrames
```angelscript
int GetFlipbookLengthInFrames()
```
Get length of the flipbook (in frames)

### GetPlaybackPosition
```angelscript
float32 GetPlaybackPosition()
```
Get the current playback position (in seconds) of the flipbook

### GetPlaybackPositionInFrames
```angelscript
int GetPlaybackPositionInFrames()
```
Get the current playback position (in frames) of the flipbook

### GetPlayRate
```angelscript
float32 GetPlayRate()
```
Get the current play rate for this flipbook

### GetSpriteColor
```angelscript
FLinearColor GetSpriteColor()
```
Returns the current color of the sprite

### IsLooping
```angelscript
bool IsLooping()
```
Get whether we are looping or not

### IsPlaying
```angelscript
bool IsPlaying()
```
Get whether this flipbook is playing or not.

### IsReversing
```angelscript
bool IsReversing()
```
Get whether we are reversing or not

### Play
```angelscript
void Play()
```
Start playback of flipbook

### PlayFromStart
```angelscript
void PlayFromStart()
```
Start playback of flipbook from the start

### Reverse
```angelscript
void Reverse()
```
Start playback of flipbook in reverse

### ReverseFromEnd
```angelscript
void ReverseFromEnd()
```
Start playback of flipbook in reverse from the end

### SetFlipbook
```angelscript
bool SetFlipbook(UPaperFlipbook NewFlipbook)
```
Change the flipbook used by this instance (will reset the play time to 0 if it is a new flipbook).

### SetLooping
```angelscript
void SetLooping(bool bNewLooping)
```
true means we should loop, false means we should not.

### SetNewTime
```angelscript
void SetNewTime(float32 NewTime)
```
Set the new playback position time to use

### SetPlaybackPosition
```angelscript
void SetPlaybackPosition(float32 NewPosition, bool bFireEvents)
```
Jump to a position in the flipbook (expressed in seconds). If bFireEvents is true, event functions will fire, otherwise they will not.

### SetPlaybackPositionInFrames
```angelscript
void SetPlaybackPositionInFrames(int NewFramePosition, bool bFireEvents)
```
Jump to a position in the flipbook (expressed in frames). If bFireEvents is true, event functions will fire, otherwise they will not.

### SetPlayRate
```angelscript
void SetPlayRate(float32 NewRate)
```
Sets the new play rate for this flipbook

### SetSpriteColor
```angelscript
void SetSpriteColor(FLinearColor NewColor)
```
Set color of the sprite

### Stop
```angelscript
void Stop()
```
Stop playback of flipbook

