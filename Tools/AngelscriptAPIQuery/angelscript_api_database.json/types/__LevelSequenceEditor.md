# __LevelSequenceEditor

## 方法

### CloseLevelSequence
```angelscript
void CloseLevelSequence()
```
* Close

### EmptySelection
```angelscript
void EmptySelection()
```
Empties the current selection.

### FocusLevelSequence
```angelscript
void FocusLevelSequence(UMovieSceneSubSection SubSection)
```
* Focus/view the sequence associated to the given sub sequence section.

### FocusParentSequence
```angelscript
void FocusParentSequence()
```
* Focus/view the parent sequence, popping out of the current sub sequence section.

### GetBoundObjects
```angelscript
TArray<UObject> GetBoundObjects(FMovieSceneObjectBindingID ObjectBinding)
```
Get the object bound to the given binding ID with the current level sequence editor

### GetChannelsWithSelectedKeys
```angelscript
TArray<FSequencerChannelProxy> GetChannelsWithSelectedKeys()
```
Gets the channel with selected keys.

### GetCurrentLevelSequence
```angelscript
ULevelSequence GetCurrentLevelSequence()
```
* Get the currently opened root level sequence asset

### GetFocusedLevelSequence
```angelscript
ULevelSequence GetFocusedLevelSequence()
```
* Get the currently focused/viewed level sequence asset if there is a hierarchy of sequences.

### GetGlobalPosition
```angelscript
FMovieSceneSequencePlaybackParams GetGlobalPosition(EMovieSceneTimeUnit TimeUnit)
```
Get the current global playhead position

### GetLocalPosition
```angelscript
FMovieSceneSequencePlaybackParams GetLocalPosition(EMovieSceneTimeUnit TimeUnit)
```
Get the current local playhead position

### GetLoopMode
```angelscript
ESequencerLoopMode GetLoopMode()
```
Get loop mode (note this is a per user preference)

### GetPlaybackSpeed
```angelscript
float32 GetPlaybackSpeed()
```
Get playback speed of the current level sequence

### GetSelectedBindings
```angelscript
TArray<FMovieSceneBindingProxy> GetSelectedBindings()
```
Gets the currently selected object bindings

### GetSelectedChannels
```angelscript
TArray<FSequencerChannelProxy> GetSelectedChannels()
```
Gets the currently selected channels.

### GetSelectedFolders
```angelscript
TArray<UMovieSceneFolder> GetSelectedFolders()
```
Gets the currently selected folders.

### GetSelectedKeys
```angelscript
TArray<int> GetSelectedKeys(FSequencerChannelProxy ChannelProxy)
```
Gets the selected key indices with this channel

### GetSelectedSections
```angelscript
TArray<UMovieSceneSection> GetSelectedSections()
```
Gets the currently selected sections.

### GetSelectedTracks
```angelscript
TArray<UMovieSceneTrack> GetSelectedTracks()
```
Gets the currently selected tracks.

### GetSelectionRangeEnd
```angelscript
int GetSelectionRangeEnd()
```
Get the selection range end frame.

### GetSelectionRangeStart
```angelscript
int GetSelectionRangeStart()
```
Get the selection range start frame.

### GetSubSequenceHierarchy
```angelscript
TArray<UMovieSceneSubSection> GetSubSequenceHierarchy()
```
* Get the current sub section hierarchy from the current sequence to the section associated with the focused sequence.

### GetTrackFilterNames
```angelscript
TArray<FText> GetTrackFilterNames()
```
Gets all the available track filter names

### IsCameraCutLockedToViewport
```angelscript
bool IsCameraCutLockedToViewport()
```
Check whether the lock for the viewport to the camera cuts is enabled.

### IsLevelSequenceLocked
```angelscript
bool IsLevelSequenceLocked()
```
Check whether the current level sequence and its descendants are locked for editing.

### IsPlaying
```angelscript
bool IsPlaying()
```
Check whether the sequence is actively playing.

### IsTrackFilterEnabled
```angelscript
bool IsTrackFilterEnabled(FText TrackFilterName)
```
Gets whether the specified track filter is on/off

### OpenLevelSequence
```angelscript
bool OpenLevelSequence(ULevelSequence LevelSequence)
```
* Open a level sequence asset

### Pause
```angelscript
void Pause()
```
Pause the current level sequence

### Play
```angelscript
void Play()
```
Play the current level sequence

### PlayTo
```angelscript
void PlayTo(FMovieSceneSequencePlaybackParams PlaybackParams, EMovieSceneTimeUnit TimeUnit)
```
Play from the current time to the requested time in frames

### RefreshCurrentLevelSequence
```angelscript
void RefreshCurrentLevelSequence()
```
Refresh Sequencer UI.

### SelectBindings
```angelscript
void SelectBindings(TArray<FMovieSceneBindingProxy> ObjectBindings)
```
Select bindings

### SelectChannels
```angelscript
void SelectChannels(TArray<FSequencerChannelProxy> Channels)
```
Select channels

### SelectFolders
```angelscript
void SelectFolders(TArray<UMovieSceneFolder> Folders)
```
Select folders

### SelectKeys
```angelscript
void SelectKeys(FSequencerChannelProxy Channel, TArray<int> Indices)
```
Select keys from indices

### SelectSections
```angelscript
void SelectSections(TArray<UMovieSceneSection> Sections)
```
Select sections

### SelectTracks
```angelscript
void SelectTracks(TArray<UMovieSceneTrack> Tracks)
```
Select tracks

### SetGlobalPosition
```angelscript
void SetGlobalPosition(FMovieSceneSequencePlaybackParams PlaybackParams, EMovieSceneTimeUnit TimeUnit)
```
Set global playhead position for the current level sequence. If the requested time is the same as the current time, an evaluation will be forced.

### SetLocalPosition
```angelscript
void SetLocalPosition(FMovieSceneSequencePlaybackParams PlaybackParams, EMovieSceneTimeUnit TimeUnit)
```
Set local playhead position for the current level sequence. If the requested time is the same as the current time, an evaluation will be forced.

### SetLockCameraCutToViewport
```angelscript
void SetLockCameraCutToViewport(bool bLock)
```
Sets the lock for the viewport to the camera cuts.

### SetLockLevelSequence
```angelscript
void SetLockLevelSequence(bool bLock)
```
Sets the lock for the current level sequence and its descendants for editing.

### SetLoopMode
```angelscript
void SetLoopMode(ESequencerLoopMode NewLoopMode)
```
Set loop mode (note this is a per user preference)

### SetPlaybackSpeed
```angelscript
void SetPlaybackSpeed(float32 NewPlaybackSpeed)
```
Set playback speed of the current level sequence

### SetSelectionRangeEnd
```angelscript
void SetSelectionRangeEnd(int NewFrame)
```
Set the selection range end frame.

### SetSelectionRangeStart
```angelscript
void SetSelectionRangeStart(int NewFrame)
```
Set the selection range start frame.

### SetTrackFilterEnabled
```angelscript
void SetTrackFilterEnabled(FText TrackFilterName, bool bEnabled)
```
Sets the specified track filter to be on or off

