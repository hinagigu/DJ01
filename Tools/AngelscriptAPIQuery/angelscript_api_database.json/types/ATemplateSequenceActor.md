# ATemplateSequenceActor

**继承自**: `AActor`

Actor responsible for controlling a specific template sequence in the world.

## 属性

### PlaybackSettings
- **类型**: `FMovieSceneSequencePlaybackSettings`

### TemplateSequence
- **类型**: `FSoftObjectPath`

### BindingOverride
- **类型**: `FTemplateSequenceBindingOverrideData`
- **描述**: The override for the template sequence's root object binding. See SetBinding.

### SequencePlayer
- **类型**: `UTemplateSequencePlayer`

## 方法

### GetSequence
```angelscript
UTemplateSequence GetSequence()
```
Get the template sequence being played by this actor.

@return the template sequence, or nullptr if it is not assigned or cannot be loaded

### GetSequencePlayer
```angelscript
UTemplateSequencePlayer GetSequencePlayer()
```
Get the actor's sequence player, or nullptr if it not yet initialized.

### LoadSequence
```angelscript
UTemplateSequence LoadSequence()
```
Get the template sequence being played by this actor.

@return the template sequence, or nullptr if it is not assigned or cannot be loaded

### SetBinding
```angelscript
void SetBinding(AActor Actor, bool bOverridesDefault)
```
Set the actor to play the template sequence onto, by setting up an override for the template
sequence's root object binding.

### SetSequence
```angelscript
void SetSequence(UTemplateSequence InSequence)
```
Set the template sequence being played by this actor.

