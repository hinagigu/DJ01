# UMovieSceneSequence

**继承自**: `UMovieSceneSignedObject`

Abstract base class for movie scene animations (C++ version).

## 方法

### FindBindingByTag
```angelscript
FMovieSceneObjectBindingID FindBindingByTag(FName InBindingName)
```
Find the first object binding ID associated with the specified tag name (set up through RMB->Expose on Object bindings from within sequencer)

### FindBindingsByTag
```angelscript
TArray<FMovieSceneObjectBindingID> FindBindingsByTag(FName InBindingName)
```
Find all object binding IDs associated with the specified tag name (set up through RMB->Expose on Object bindings from within sequencer)

### GetEarliestTimecodeSource
```angelscript
FMovieSceneTimecodeSource GetEarliestTimecodeSource()
```
Get the earliest timecode source out of all of the movie scene sections contained within this sequence's movie scene.

