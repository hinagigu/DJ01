# UMovieSceneSection

**继承自**: `UMovieSceneSignedObject`

Base class for movie scene sections

## 属性

### EvalOptions
- **类型**: `FMovieSceneSectionEvalOptions`

### TimecodeSource
- **类型**: `FMovieSceneTimecodeSource`
- **描述**: The timecode at which this movie scene section is based (ie. when it was recorded)

### bIsActive
- **类型**: `bool`

### bIsLocked
- **类型**: `bool`

## 方法

### GetBlendType
```angelscript
FOptionalMovieSceneBlendType GetBlendType()
```
Gets this section's blend type

### GetColorTint
```angelscript
FColor GetColorTint()
```
Get this section's color tint.

### GetCompletionMode
```angelscript
EMovieSceneCompletionMode GetCompletionMode()
```
Gets this section's completion mode

### GetOverlapPriority
```angelscript
int GetOverlapPriority()
```
Gets this section's priority over overlapping sections (higher wins)

### GetPostRollFrames
```angelscript
int GetPostRollFrames()
```

### GetPreRollFrames
```angelscript
int GetPreRollFrames()
```

### GetRowIndex
```angelscript
int GetRowIndex()
```
Gets the row index for this section

### IsActive
```angelscript
bool IsActive()
```

### IsLocked
```angelscript
bool IsLocked()
```

### SetBlendType
```angelscript
void SetBlendType(EMovieSceneBlendType InBlendType)
```
Sets this section's blend type

### SetColorTint
```angelscript
void SetColorTint(FColor InColorTint)
```
Set this section's color tint.

### SetCompletionMode
```angelscript
void SetCompletionMode(EMovieSceneCompletionMode InCompletionMode)
```
* Sets this section's completion mode

### SetIsActive
```angelscript
void SetIsActive(bool bInIsActive)
```
Whether or not this section is active.

### SetIsLocked
```angelscript
void SetIsLocked(bool bInIsLocked)
```
Whether or not this section is locked.

### SetOverlapPriority
```angelscript
void SetOverlapPriority(int NewPriority)
```
Sets this section's priority over overlapping sections (higher wins)

### SetPostRollFrames
```angelscript
void SetPostRollFrames(int InPostRollFrames)
```
Gets/sets the number of frames to continue 'postrolling' this section for after evaluation has ended.

### SetPreRollFrames
```angelscript
void SetPreRollFrames(int InPreRollFrames)
```
Gets the number of frames to prepare this section for evaluation before it actually starts.

### SetRowIndex
```angelscript
void SetRowIndex(int NewRowIndex)
```
Sets this section's new row index

