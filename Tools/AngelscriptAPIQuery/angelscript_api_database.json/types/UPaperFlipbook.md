# UPaperFlipbook

**继承自**: `UObject`

Contains an animation sequence of sprite frames

## 属性

### FramesPerSecond
- **类型**: `float32`

### KeyFrames
- **类型**: `TArray<FPaperFlipbookKeyFrame>`
- **描述**: The set of key frames for this flipbook animation (each one has a duration and a sprite to display)

### DefaultMaterial
- **类型**: `UMaterialInterface`

### CollisionSource
- **类型**: `EFlipbookCollisionMode`

## 方法

### GetKeyFrameIndexAtTime
```angelscript
int GetKeyFrameIndexAtTime(float32 Time, bool bClampToEnds)
```
Returns the keyframe index that covers the specified time (in seconds), or INDEX_NONE if none exists.
When bClampToEnds is true, it will choose the first or last keyframe if the time is out of range.

### GetNumFrames
```angelscript
int GetNumFrames()
```
Returns the total number of frames

### GetNumKeyFrames
```angelscript
int GetNumKeyFrames()
```
Returns the number of key frames

### GetSpriteAtFrame
```angelscript
UPaperSprite GetSpriteAtFrame(int FrameIndex)
```
Returns the sprite at the specified keyframe index, or nullptr if none exists

### GetSpriteAtTime
```angelscript
UPaperSprite GetSpriteAtTime(float32 Time, bool bClampToEnds)
```
Returns the sprite at the specified time (in seconds), or nullptr if none exists.
When bClampToEnds is true, it will choose the first or last sprite if the time is out of range.

### GetTotalDuration
```angelscript
float32 GetTotalDuration()
```
Returns the total duration in seconds

### IsValidKeyFrameIndex
```angelscript
bool IsValidKeyFrameIndex(int Index)
```
Is the specified Index within the valid range of key frames?

