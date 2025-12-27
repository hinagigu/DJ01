# ULevelSequenceEditorSubsystem

**继承自**: `UEditorSubsystem`

ULevelSequenceEditorSubsystem
Subsystem for level sequence editor related utilities to scripts

## 方法

### AddActors
```angelscript
TArray<FMovieSceneBindingProxy> AddActors(TArray<AActor> Actors)
```
Add existing actors to Sequencer. Tracks will be automatically added based on default track settings.

### AddActorsToBinding
```angelscript
void AddActorsToBinding(TArray<AActor> Actors, FMovieSceneBindingProxy ObjectBinding)
```
Assigns the given actors to the binding

### BakeTransform
```angelscript
void BakeTransform(TArray<FMovieSceneBindingProxy> ObjectBindings, FFrameTime BakeInTime, FFrameTime BakeOutTime, FFrameTime BakeInterval, FMovieSceneScriptingParams Params)
```

### BakeTransformWithSettings
```angelscript
bool BakeTransformWithSettings(TArray<FMovieSceneBindingProxy> ObjectBindings, FBakingAnimationKeySettings InSettings, FMovieSceneScriptingParams Params)
```

### ConvertToPossessable
```angelscript
FMovieSceneBindingProxy ConvertToPossessable(FMovieSceneBindingProxy ObjectBinding)
```
Convert to possessable

### ConvertToSpawnable
```angelscript
TArray<FMovieSceneBindingProxy> ConvertToSpawnable(FMovieSceneBindingProxy ObjectBinding)
```
Convert to spawnable. If there are multiple objects assigned to the possessable, multiple spawnables will be created.

### CopyBindings
```angelscript
void CopyBindings(TArray<FMovieSceneBindingProxy> Bindings, FString& ExportedText)
```
Copy bindings
The copied bindings will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteBindings if, for example, pasting copy/pasting multiple
bindings without relying on a single clipboard.

### CopyFolders
```angelscript
void CopyFolders(TArray<UMovieSceneFolder> Folders, FString& ExportedText)
```
Copy folders
The copied folders will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteFolders if, for example, pasting copy/pasting multiple
folders without relying on a single clipboard.

### CopySections
```angelscript
void CopySections(TArray<UMovieSceneSection> Sections, FString& ExportedText)
```
Copy sections
The copied sections will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteSections if, for example, pasting copy/pasting multiple
sections without relying on a single clipboard.

### CopyTracks
```angelscript
void CopyTracks(TArray<UMovieSceneTrack> Tracks, FString& ExportedText)
```
Copy tracks
The copied tracks will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteTracks if, for example, pasting copy/pasting multiple
tracks without relying on a single clipboard.

### CreateCamera
```angelscript
FMovieSceneBindingProxy CreateCamera(bool bSpawnable, ACineCameraActor& OutActor)
```
Create a cine camera actor and add it to Sequencer

### FixActorReferences
```angelscript
void FixActorReferences()
```
Attempts to automatically fix up broken actor references in the current scene

### GetCurveEditor
```angelscript
USequencerCurveEditorObject GetCurveEditor()
```
Retrieve the curve editor

### GetScriptingLayer
```angelscript
USequencerModuleScriptingLayer GetScriptingLayer()
```
Retrieve the scripting layer

### PasteBindings
```angelscript
bool PasteBindings(FString TextToImport, FMovieScenePasteBindingsParams PasteBindingsParams, TArray<FMovieSceneBindingProxy>& OutObjectBindings)
```
Paste bindings
Paste bindings from the given TextToImport string (used in conjunction with CopyBindings).
If TextToImport is empty, the contents of the clipboard will be used.

### PasteFolders
```angelscript
bool PasteFolders(FString TextToImport, FMovieScenePasteFoldersParams PasteFoldersParams, TArray<UMovieSceneFolder>& OutFolders)
```
Paste folders
Paste folders from the given TextToImport string (used in conjunction with CopyFolders).
If TextToImport is empty, the contents of the clipboard will be used.

### PasteSections
```angelscript
bool PasteSections(FString TextToImport, FMovieScenePasteSectionsParams PasteSectionsParams, TArray<UMovieSceneSection>& OutSections)
```
Paste sections
Paste sections from the given TextToImport string (used in conjunction with CopySections).
If TextToImport is empty, the contents of the clipboard will be used.

### PasteTracks
```angelscript
bool PasteTracks(FString TextToImport, FMovieScenePasteTracksParams PasteTracksParams, TArray<UMovieSceneTrack>& OutTracks)
```
Paste tracks
Paste tracks from the given TextToImport string (used in conjunction with CopyTracks).
If TextToImport is empty, the contents of the clipboard will be used.

### RebindComponent
```angelscript
void RebindComponent(TArray<FMovieSceneBindingProxy> ComponentBindings, FName ComponentName)
```
Rebind the component binding to the requested component

### RemoveActorsFromBinding
```angelscript
void RemoveActorsFromBinding(TArray<AActor> Actors, FMovieSceneBindingProxy ObjectBinding)
```
Removes the given actors from the binding

### RemoveAllBindings
```angelscript
void RemoveAllBindings(FMovieSceneBindingProxy ObjectBinding)
```
Remove all bound actors from this track

### RemoveInvalidBindings
```angelscript
void RemoveInvalidBindings(FMovieSceneBindingProxy ObjectBinding)
```
Remove missing objects bound to this track

### ReplaceBindingWithActors
```angelscript
void ReplaceBindingWithActors(TArray<AActor> Actors, FMovieSceneBindingProxy ObjectBinding)
```
Replaces the binding with the given actors

### SnapSectionsToTimelineUsingSourceTimecode
```angelscript
void SnapSectionsToTimelineUsingSourceTimecode(TArray<UMovieSceneSection> Sections)
```
Snap sections to timeline using source timecode

### SyncSectionsUsingSourceTimecode
```angelscript
void SyncSectionsUsingSourceTimecode(TArray<UMovieSceneSection> Sections)
```
Sync section using source timecode

