# ULevelSequenceDirector

**继承自**: `UObject`

## 属性

### Player
- **类型**: `ULevelSequencePlayer`
- **描述**: Pointer to the player that's playing back this director's sequence. Only valid in game or in PIE/Simulate.

## 方法

### GetBoundActor
```angelscript
AActor GetBoundActor(FMovieSceneObjectBindingID ObjectBinding)
```
Resolve the first valid Actor binding inside this sub-sequence that relates to the specified ID
@note: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

@param ObjectBinding The ID for the object binding inside this sub-sequence or one of its children to resolve

### GetBoundActors
```angelscript
TArray<AActor> GetBoundActors(FMovieSceneObjectBindingID ObjectBinding)
```
Resolve the actor bindings inside this sub-sequence that relate to the specified ID
@note: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

@param ObjectBinding The ID for the object binding inside this sub-sequence or one of its children to resolve

### GetBoundObject
```angelscript
UObject GetBoundObject(FMovieSceneObjectBindingID ObjectBinding)
```
Resolve the first valid binding inside this sub-sequence that relates to the specified ID
@note: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

@param ObjectBinding The ID for the object binding inside this sub-sequence or one of its children to resolve

### GetBoundObjects
```angelscript
TArray<UObject> GetBoundObjects(FMovieSceneObjectBindingID ObjectBinding)
```
Resolve the bindings inside this sub-sequence that relate to the specified ID
@note: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

@param ObjectBinding The ID for the object binding inside this sub-sequence or one of its children to resolve

### GetCurrentTime
```angelscript
FQualifiedFrameTime GetCurrentTime()
```
Get the current time for this director's sub-sequence (or the root sequence, if this is a root sequence director)
@return The current playback position of this director's sequence

### GetRootSequenceTime
```angelscript
FQualifiedFrameTime GetRootSequenceTime()
```
Get the current time for the outermost (root) sequence
@return The current playback position of the outermost (root) sequence

### GetSequence
```angelscript
UMovieSceneSequence GetSequence()
```
* Get the current sequence that this director is playing back within

### OnCreated
```angelscript
void OnCreated()
```
Called when this director is created

