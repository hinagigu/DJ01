# __UMovieSceneSequenceExtensions

## 方法

### AddMarkedFrameToSequence
```angelscript
int AddMarkedFrameToSequence(UMovieSceneSequence Sequence, FMovieSceneMarkedFrame InMarkedFrame, EMovieSceneTimeUnit TimeUnit)
```
* Add a given user marked frame.
* A unique label will be generated if the marked frame label is empty
*
* @InMarkedFrame The given user marked frame to add
* @return The index to the newly added marked frame

### AddPossessable
```angelscript
FMovieSceneBindingProxy AddPossessable(UMovieSceneSequence Sequence, UObject ObjectToPossess)
```
Add a new binding to this sequence that will possess the specified object

@param Sequence        The sequence to add a possessable to
@param ObjectToPossess The object that this sequence should possess when evaluating
@return A unique identifier for the new binding

### AddRootFolderToSequence
```angelscript
UMovieSceneFolder AddRootFolderToSequence(UMovieSceneSequence Sequence, FString NewFolderName)
```
Add a root folder to the given sequence

@param Sequence                      The sequence to add a folder to
@param NewFolderName         The name to give the added folder
@return The newly created folder

### AddSpawnableFromClass
```angelscript
FMovieSceneBindingProxy AddSpawnableFromClass(UMovieSceneSequence Sequence, UClass ClassToSpawn)
```
Add a new binding to this sequence that will spawn the specified object

@param Sequence        The sequence to add to
@param ClassToSpawn    A class or blueprint type to spawn for this binding
@return A unique identifier for the new binding

### AddSpawnableFromInstance
```angelscript
FMovieSceneBindingProxy AddSpawnableFromInstance(UMovieSceneSequence Sequence, UObject ObjectToSpawn)
```
Add a new binding to this sequence that will spawn the specified object

@param Sequence        The sequence to add to
@param ObjectToSpawn   An object instance to use as a template for spawning
@return A unique identifier for the new binding

### AddTrack
```angelscript
UMovieSceneTrack AddTrack(UMovieSceneSequence Sequence, TSubclassOf<UMovieSceneTrack> TrackType)
```
Add a new track of the specified type

@param Sequence        The sequence to use
@param TrackType     A UMovieSceneTrack class type to create
@return The newly created track, if successful

### AreMarkedFramesLocked
```angelscript
bool AreMarkedFramesLocked(UMovieSceneSequence Sequence)
```
* Are marked frames locked
*
* @return Whether the movie scene marked frames are locked

### DeleteMarkedFrame
```angelscript
void DeleteMarkedFrame(UMovieSceneSequence Sequence, int DeleteIndex)
```
* Delete the user marked frame by index.
*
* @DeleteIndex The index to the user marked frame to delete

### DeleteMarkedFrames
```angelscript
void DeleteMarkedFrames(UMovieSceneSequence Sequence)
```
* Delete all user marked frames

### FindBindingById
```angelscript
FMovieSceneBindingProxy FindBindingById(UMovieSceneSequence Sequence, FGuid BindingId)
```
Attempt to locate a binding in this sequence by its Id

@param Sequence        The sequence within which to find the binding
@param BindingId       The binding Id to look up
@return A unique identifier for the binding, or invalid

### FindBindingByName
```angelscript
FMovieSceneBindingProxy FindBindingByName(UMovieSceneSequence Sequence, FString Name)
```
Attempt to locate a binding in this sequence by its name

@param Sequence        The sequence within which to find the binding
@param Name            The display name of the binding to look up
@return A unique identifier for the binding, or invalid

### FindMarkedFrameByFrameNumberInSequence
```angelscript
int FindMarkedFrameByFrameNumberInSequence(UMovieSceneSequence Sequence, FFrameNumber InFrameNumber, EMovieSceneTimeUnit TimeUnit)
```
* Find the user marked frame by frame number
*
* @InFrameNumber The frame number of the user marked frame to find

### FindMarkedFrameByLabel
```angelscript
int FindMarkedFrameByLabel(UMovieSceneSequence Sequence, FString InLabel)
```
* Find the user marked frame by label
*
* @InLabel The label to the user marked frame to find

### FindNextMarkedFrameInSequence
```angelscript
int FindNextMarkedFrameInSequence(UMovieSceneSequence Sequence, FFrameNumber InFrameNumber, bool bForward, EMovieSceneTimeUnit TimeUnit)
```
* Find the next/previous user marked frame from the given frame number
*
* @InFrameNumber The frame number to find the next/previous user marked frame from
* @bForward Find forward from the given frame number.

### FindTracksByExactType
```angelscript
TArray<UMovieSceneTrack> FindTracksByExactType(UMovieSceneSequence Sequence, TSubclassOf<UMovieSceneTrack> TrackType)
```
Find all tracks of the specified type, not allowing sub-classed types

@param Sequence        The sequence to use
@param TrackType     A UMovieSceneTrack class type specifying the exact types of track to return
@return An array containing any tracks that are exactly the same as the type specified

### FindTracksByType
```angelscript
TArray<UMovieSceneTrack> FindTracksByType(UMovieSceneSequence Sequence, TSubclassOf<UMovieSceneTrack> TrackType)
```
Find all tracks of the specified type

@param Sequence        The sequence to use
@param TrackType     A UMovieSceneTrack class type specifying which types of track to return
@return An array containing any tracks that match the type specified

### GetBindingID
```angelscript
FMovieSceneObjectBindingID GetBindingID(UMovieSceneSequence Sequence, FMovieSceneBindingProxy InBinding)
```
Get the binding ID for a binding within a sequence.
@note: The resulting binding is only valid when applied to properties within the same sequence as this binding. Use GetPortableBindingID for bindings which live in different sub-sequences.

@param Binding The binding proxy to generate the binding id from
@return The binding's id

### GetBindings
```angelscript
TArray<FMovieSceneBindingProxy> GetBindings(UMovieSceneSequence Sequence)
```
Get all the bindings in this sequence

@param Sequence        The sequence to get bindings for
@return An array of unique identifiers for all the bindings in this sequence

### GetClockSource
```angelscript
EUpdateClockSource GetClockSource(UMovieSceneSequence InSequence)
```
Get the clock source for this sequence

@param Sequence The sequence within which to get the clock source
@return The clock source for this sequence

### GetDisplayRate
```angelscript
FFrameRate GetDisplayRate(UMovieSceneSequence Sequence)
```
Gets this sequence's display rate

@param Sequence        The sequence to use
@return The display rate that this sequence is displayed as

### GetEvaluationType
```angelscript
EMovieSceneEvaluationType GetEvaluationType(UMovieSceneSequence InSequence)
```
Get the evaluation type for this sequence

@param Sequence The sequence within which to get the evaluation type
@return The evaluation type for this sequence

### GetMarkedFramesFromSequence
```angelscript
TArray<FMovieSceneMarkedFrame> GetMarkedFramesFromSequence(UMovieSceneSequence Sequence, EMovieSceneTimeUnit TimeUnit)
```
* Get the marked frames for this sequence
*
* @return Return the user marked frames

### GetMovieScene
```angelscript
UMovieScene GetMovieScene(UMovieSceneSequence Sequence)
```
Get this sequence's movie scene data

@param Sequence        The sequence to use
@return This sequence's movie scene data object

### GetPlaybackEnd
```angelscript
int GetPlaybackEnd(UMovieSceneSequence Sequence)
```
Get playback end of this sequence in display rate resolution

@param Sequence        The sequence within which to get the playback end
@return Playback end of this sequence

### GetPlaybackEndSeconds
```angelscript
float32 GetPlaybackEndSeconds(UMovieSceneSequence Sequence)
```
Get playback end of this sequence in seconds

@param Sequence        The sequence within which to get the playback end
@return Playback end of this sequence

### GetPlaybackRange
```angelscript
FSequencerScriptingRange GetPlaybackRange(UMovieSceneSequence Sequence)
```
Get playback range of this sequence in display rate resolution

@param Sequence        The sequence within which to get the playback range
@return Playback range of this sequence

### GetPlaybackStart
```angelscript
int GetPlaybackStart(UMovieSceneSequence Sequence)
```
Get playback start of this sequence in display rate resolution

@param Sequence        The sequence within which to get the playback start
@return Playback start of this sequence

### GetPlaybackStartSeconds
```angelscript
float32 GetPlaybackStartSeconds(UMovieSceneSequence Sequence)
```
Get playback start of this sequence in seconds

@param Sequence        The sequence within which to get the playback start
@return Playback start of this sequence

### GetPortableBindingID
```angelscript
FMovieSceneObjectBindingID GetPortableBindingID(UMovieSceneSequence RootSequence, UMovieSceneSequence DestinationSequence, FMovieSceneBindingProxy InBinding)
```
Get a portable binding ID for a binding that resides in a different sequence to the one where this binding will be resolved.
@note: This function must be used over GetBindingID when the target binding resides in different shots or sub-sequences.
@note: Only unique instances of sequences within a root sequences are supported

@param RootSequence The root sequence that contains both the destination sequence (that will resolve the binding ID) and the target sequence that contains the actual binding
@param DestinationSequence The sequence that will own or resolve the resulting binding ID. For example, if the binding ID will be applied to a camera cut section pass the sequence that contains the camera cut track to this parameter.
@param Binding The target binding to create the ID from
@return The binding's id

### GetPossessables
```angelscript
TArray<FMovieSceneBindingProxy> GetPossessables(UMovieSceneSequence Sequence)
```
Get all the possessables in this sequence

@param Sequence        The sequence to get possessables for
@return Possessables in this sequence

### GetRootFoldersInSequence
```angelscript
TArray<UMovieSceneFolder> GetRootFoldersInSequence(UMovieSceneSequence Sequence)
```
Get the root folders in the provided sequence

@param Sequence      The sequence to retrieve folders from
@return The folders contained within the given sequence

### GetSpawnables
```angelscript
TArray<FMovieSceneBindingProxy> GetSpawnables(UMovieSceneSequence Sequence)
```
Get all the spawnables in this sequence

@param Sequence        The sequence to get spawnables for
@return Spawnables in this sequence

### GetTickResolution
```angelscript
FFrameRate GetTickResolution(UMovieSceneSequence Sequence)
```
Gets this sequence's tick resolution

@param Sequence        The sequence to use
@return The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

### GetTracks
```angelscript
TArray<UMovieSceneTrack> GetTracks(UMovieSceneSequence Sequence)
```
Get all tracks

@param Sequence        The sequence to use
@return An array containing all tracks in this sequence

### GetViewRangeEnd
```angelscript
float GetViewRangeEnd(UMovieSceneSequence InSequence)
```
Get the sequence view range end in seconds

@param Sequence The sequence within which to get the view range end
@return The view range end time in seconds for this sequence

### GetViewRangeStart
```angelscript
float GetViewRangeStart(UMovieSceneSequence InSequence)
```
Get the sequence view range start in seconds

@param Sequence The sequence within which to get the view range start
@return The view range start time in seconds for this sequence

### GetWorkRangeEnd
```angelscript
float GetWorkRangeEnd(UMovieSceneSequence InSequence)
```
Get the sequence work range end in seconds

@param Sequence The sequence within which to get the work range end
@return The work range end time in seconds for this sequence

### GetWorkRangeStart
```angelscript
float GetWorkRangeStart(UMovieSceneSequence InSequence)
```
Get the sequence work range start in seconds

@param Sequence The sequence within which to get the work range start
@return The work range start time in seconds for this sequence

### IsPlaybackRangeLocked
```angelscript
bool IsPlaybackRangeLocked(UMovieSceneSequence Sequence)
```
* Is playback ranged locked
*
* @return Whether the movie scene playback range is locked

### IsReadOnly
```angelscript
bool IsReadOnly(UMovieSceneSequence Sequence)
```
* Is read only
*
* @return Whether the movie scene is read only or not

### LocateBoundObjects
```angelscript
TArray<UObject> LocateBoundObjects(UMovieSceneSequence Sequence, FMovieSceneBindingProxy InBinding, UObject Context)
```
Locate all the objects that correspond to the specified object ID, using the specified context

@param Sequence   The sequence to locate bound objects for
@param InBinding  The object binding
@param Context    Optional context to use to find the required object
@return An array of all bound objects

### MakeRange
```angelscript
FSequencerScriptingRange MakeRange(UMovieSceneSequence Sequence, int StartFrame, int Duration)
```
Make a new range for this sequence in its display rate

@param Sequence        The sequence within which to find the binding
@param StartFrame      The frame at which to start the range
@param Duration        The length of the range
@return Specified sequencer range

### MakeRangeSeconds
```angelscript
FSequencerScriptingRange MakeRangeSeconds(UMovieSceneSequence Sequence, float32 StartTime, float32 Duration)
```
Make a new range for this sequence in seconds

@param Sequence        The sequence within which to find the binding
@param StartTime       The time in seconds at which to start the range
@param Duration        The length of the range in seconds
@return Specified sequencer range

### RemoveRootFolderFromSequence
```angelscript
void RemoveRootFolderFromSequence(UMovieSceneSequence Sequence, UMovieSceneFolder Folder)
```
Remove a root folder from the given sequence. Will throw an exception if the specified folder is not valid or not a root folder.

@param Sequence                      The sequence That the folder belongs to
@param Folder                        The folder to remove

### RemoveTrack
```angelscript
bool RemoveTrack(UMovieSceneSequence Sequence, UMovieSceneTrack Track)
```
Removes a track

@param Sequence        The sequence to use
@param Track           The track to remove
@return Whether the track was successfully removed

### ResolveBindingID
```angelscript
FMovieSceneBindingProxy ResolveBindingID(UMovieSceneSequence RootSequence, FMovieSceneObjectBindingID InObjectBindingID)
```
Make a binding for the given binding ID

@param RootSequence  The root sequence that contains the sequence
@param ObjectBindingID The object binding id that has the guid and the sequence id
@return The new binding proxy

### SetClockSource
```angelscript
void SetClockSource(UMovieSceneSequence InSequence, EUpdateClockSource InClockSource)
```
Set the clock source for this sequence

@param Sequence The sequence within which to set the clock source
@param InClockSource The clock source to set for this sequence

### SetDisplayRate
```angelscript
void SetDisplayRate(UMovieSceneSequence Sequence, FFrameRate DisplayRate)
```
Sets this sequence's display rate

@param Sequence        The sequence to use
@param DisplayRate The display rate that this sequence is displayed as

### SetEvaluationType
```angelscript
void SetEvaluationType(UMovieSceneSequence InSequence, EMovieSceneEvaluationType InEvaluationType)
```
Set the evaluation type for this sequence

@param Sequence The sequence within which to set the evaluation type
@param InEvaluationType The evaluation type to set for this sequence

### SetMarkedFrameInSequence
```angelscript
void SetMarkedFrameInSequence(UMovieSceneSequence Sequence, int InMarkIndex, FFrameNumber InFrameNumber, EMovieSceneTimeUnit TimeUnit)
```
* Sets the frame number for the given marked frame index. Does not maintain sort. Call SortMarkedFrames
*
* @InMarkIndex The given user marked frame index to edit
* @InFrameNumber The frame number to set

### SetMarkedFramesLocked
```angelscript
void SetMarkedFramesLocked(UMovieSceneSequence Sequence, bool bInLocked)
```
* Set marked frames locked
*
* @bInLocked Whether the movie scene marked frames should be locked

### SetPlaybackEnd
```angelscript
void SetPlaybackEnd(UMovieSceneSequence Sequence, int EndFrame)
```
Set playback end of this sequence

@param Sequence        The sequence within which to set the playback end
@param EndFrame        The desired end frame for this sequence

### SetPlaybackEndSeconds
```angelscript
void SetPlaybackEndSeconds(UMovieSceneSequence Sequence, float32 EndTime)
```
Set playback end of this sequence in seconds

@param Sequence        The sequence within which to set the playback end
@param EndTime         The desired end time in seconds for this sequence

### SetPlaybackRangeLocked
```angelscript
void SetPlaybackRangeLocked(UMovieSceneSequence Sequence, bool bInLocked)
```
* Set playback range locked
*
* @bInLocked Whether the movie scene playback range should be locked

### SetPlaybackStart
```angelscript
void SetPlaybackStart(UMovieSceneSequence Sequence, int StartFrame)
```
Set playback start of this sequence

@param Sequence        The sequence within which to set the playback start
@param StartFrame      The desired start frame for this sequence

### SetPlaybackStartSeconds
```angelscript
void SetPlaybackStartSeconds(UMovieSceneSequence Sequence, float32 StartTime)
```
Set playback start of this sequence in seconds

@param Sequence        The sequence within which to set the playback start
@param StartTime       The desired start time in seconds for this sequence

### SetReadOnly
```angelscript
void SetReadOnly(UMovieSceneSequence Sequence, bool bInReadOnly)
```
* Set read only
*
* @bInReadOnly Whether the movie scene should be read only or not

### SetTickResolution
```angelscript
void SetTickResolution(UMovieSceneSequence Sequence, FFrameRate TickResolution)
```
Sets this sequence's tick resolution and migrates frame times

@param Sequence        The sequence to use
@param TickResolution The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

### SetTickResolutionDirectly
```angelscript
void SetTickResolutionDirectly(UMovieSceneSequence Sequence, FFrameRate TickResolution)
```
Sets this sequence's tick resolution directly without migrating frame times

@param Sequence        The sequence to use
@param TickResolution The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

### SetViewRangeEnd
```angelscript
void SetViewRangeEnd(UMovieSceneSequence InSequence, float EndTimeInSeconds)
```
Set the sequence view range end in seconds

@param Sequence The sequence within which to set the view range end
@param StartTimeInSeconds The desired view range end time in seconds for this sequence

### SetViewRangeStart
```angelscript
void SetViewRangeStart(UMovieSceneSequence InSequence, float StartTimeInSeconds)
```
Set the sequence view range start in seconds

@param Sequence The sequence within which to set the view range start
@param StartTimeInSeconds The desired view range start time in seconds for this sequence

### SetWorkRangeEnd
```angelscript
void SetWorkRangeEnd(UMovieSceneSequence InSequence, float EndTimeInSeconds)
```
Set the sequence work range end in seconds

@param Sequence The sequence within which to set the work range end
@param StartTimeInSeconds The desired work range end time in seconds for this sequence

### SetWorkRangeStart
```angelscript
void SetWorkRangeStart(UMovieSceneSequence InSequence, float StartTimeInSeconds)
```
Set the sequence work range start in seconds

@param Sequence The sequence within which to set the work range start
@param StartTimeInSeconds The desired work range start time in seconds for this sequence

### SortMarkedFrames
```angelscript
void SortMarkedFrames(UMovieSceneSequence Sequence)
```
* Sort the marked frames in chronological order

### StaticClass
```angelscript
UClass StaticClass()
```

