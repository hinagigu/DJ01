# ALevelSequenceActor

**继承自**: `AActor`

Actor responsible for controlling a specific level sequence in the world.

## 属性

### PlaybackSettings
- **类型**: `FMovieSceneSequencePlaybackSettings`

### LevelSequenceAsset
- **类型**: `ULevelSequence`

### CameraSettings
- **类型**: `FLevelSequenceCameraSettings`

### BurnInOptions
- **类型**: `ULevelSequenceBurnInOptions`

### BindingOverrides
- **类型**: `UMovieSceneBindingOverrides`
- **描述**: Mapping of actors to override the sequence bindings with

### DefaultInstanceData
- **类型**: `UObject`
- **描述**: Instance data that can be used to dynamically control sequence evaluation at runtime

### bReplicatePlayback
- **类型**: `bool`

### SequencePlayer
- **类型**: `ULevelSequencePlayer`

### bOverrideInstanceData
- **类型**: `bool`

## 方法

### AddBinding
```angelscript
void AddBinding(FMovieSceneObjectBindingID Binding, AActor Actor, bool bAllowBindingsFromAsset)
```
Adds the specified actor to the overridden bindings for the specified binding ID, optionally still allowing the bindings defined in the Level Sequence asset

@param Binding Binding to modify
@param Actor Actor to bind
@param bAllowBindingsFromAsset If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by
                                                               Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set
                                                               set in Sequencer UI. This function will not modify the original asset.

### AddBindingByTag
```angelscript
void AddBindingByTag(FName BindingTag, AActor Actor, bool bAllowBindingsFromAsset)
```
Binds an actor to all the bindings tagged with the specified name in this sequence. Does not remove any exising bindings that have been set up through this API. Object Bindings can be tagged within the sequence UI by RMB -> Tags... on the object binding in the tree.

@param BindingTag   The unique tag name to lookup bindings with
@param Actor        The actor to assign to all the tagged bindings
@param bAllowBindingsFromAsset If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by
                                                               Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set
                                                               set in Sequencer UI. This function will not modify the original asset.

### FindNamedBinding
```angelscript
FMovieSceneObjectBindingID FindNamedBinding(FName Tag)
```
Retrieve the first object binding that has been tagged with the specified name

### FindNamedBindings
```angelscript
TArray<FMovieSceneObjectBindingID> FindNamedBindings(FName Tag)
```
Retrieve all the bindings that have been tagged with the specified name

@param Tag  The unique tag name to lookup bindings with. Object Bindings can be tagged within the sequence UI by RMB -> Tags... on the object binding in the tree.
@return An array containing all the bindings that are tagged with this name, potentially empty.

### GetSequence
```angelscript
ULevelSequence GetSequence()
```
Get the level sequence being played by this actor.

@return Level sequence, or nullptr if not assigned or if it cannot be loaded.
@see SetSequence

### GetSequencePlayer
```angelscript
ULevelSequencePlayer GetSequencePlayer()
```
Access this actor's sequence player, or None if it is not yet initialized

### HideBurnin
```angelscript
void HideBurnin()
```
Hide burnin

### RemoveBinding
```angelscript
void RemoveBinding(FMovieSceneObjectBindingID Binding, AActor Actor)
```
Removes the specified actor from the specified binding's actor array

### RemoveBindingByTag
```angelscript
void RemoveBindingByTag(FName Tag, AActor Actor)
```
Removes the specified actor from the specified binding's actor array

### ResetBinding
```angelscript
void ResetBinding(FMovieSceneObjectBindingID Binding)
```
Resets the specified binding back to the defaults defined by the Level Sequence asset

### ResetBindings
```angelscript
void ResetBindings()
```
Resets all overridden bindings back to the defaults defined by the Level Sequence asset

### SetBinding
```angelscript
void SetBinding(FMovieSceneObjectBindingID Binding, TArray<AActor> Actors, bool bAllowBindingsFromAsset)
```
Overrides the specified binding with the specified actors, optionally still allowing the bindings defined in the Level Sequence asset

@param Binding Binding to modify
@param Actors Actors to bind
@param bAllowBindingsFromAsset If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by
                                                               Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set
                                                               set in Sequencer UI. This function will not modify the original asset.

### SetBindingByTag
```angelscript
void SetBindingByTag(FName BindingTag, TArray<AActor> Actors, bool bAllowBindingsFromAsset)
```
Assigns an set of actors to all the bindings tagged with the specified name in this sequence. Object Bindings can be tagged within the sequence UI by RMB -> Tags... on the object binding in the tree.

@param BindingTag   The unique tag name to lookup bindings with
@param Actors       The actors to assign to all the tagged bindings
@param bAllowBindingsFromAsset If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by
                                                               Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set
                                                               set in Sequencer UI. This function will not modify the original asset.

### SetReplicatePlayback
```angelscript
void SetReplicatePlayback(bool ReplicatePlayback)
```
Set whether or not to replicate playback for this actor

### SetSequence
```angelscript
void SetSequence(ULevelSequence InSequence)
```
Set the level sequence being played by this actor.

@param InSequence The sequence object to set.
@see GetSequence

### ShowBurnin
```angelscript
void ShowBurnin()
```
Show burnin

