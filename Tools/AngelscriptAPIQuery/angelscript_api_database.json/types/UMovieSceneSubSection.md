# UMovieSceneSubSection

**继承自**: `UMovieSceneSection`

Implements a section in sub-sequence tracks.

## 属性

### Parameters
- **类型**: `FMovieSceneSectionParameters`

### NetworkMask
- **类型**: `uint8`

### SubSequence
- **类型**: `UMovieSceneSequence`
- **描述**: Movie scene being played by this section

## 方法

### GetSequence
```angelscript
UMovieSceneSequence GetSequence()
```
Get the sequence that is assigned to this section.

@return The sequence.
@see SetSequence

### SetSequence
```angelscript
void SetSequence(UMovieSceneSequence Sequence)
```
Sets the sequence played by this section.

@param Sequence The sequence to play.
@see GetSequence

