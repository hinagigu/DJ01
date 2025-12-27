# __UMovieSceneSectionExtensions

## 方法

### GetAllChannels
```angelscript
TArray<UMovieSceneScriptingChannel> GetAllChannels(UMovieSceneSection Section)
```
Find all channels that belong to the specified UMovieSceneSection. Some sections have many channels (such as
Transforms containing 9 double channels to represent Translation/Rotation/Scale), and a section may have mixed
channel types.

@param Section       The section to use.
@return An array containing any key channels that match the type specified

### GetAutoSizeEndFrame
```angelscript
int GetAutoSizeEndFrame(UMovieSceneSection Section)
```
Get end frame of the AutoSize. Will throw an exception if section has no end frame, use GetAutoSizeHasEndFrame to check first.

@param Section        The section being queried
@return The end frame of the AutoSize data.

### GetAutoSizeEndFrameSeconds
```angelscript
float32 GetAutoSizeEndFrameSeconds(UMovieSceneSection Section)
```
Get end time of the AutoSize seconds. Will throw an exception if section has no end frame, use GetAutoSizeHasEndFrame to check first.

@param Section        The section being queried
@return The end frame of the AutoSize data in seconds.

### GetAutoSizeHasEndFrame
```angelscript
bool GetAutoSizeHasEndFrame(UMovieSceneSection Section)
```
Checks to see if this section has an AutoSize implementation, and if so, if that implementation has a end frame.

@param Section        The section being queried
@return Whether this section has a valid autosize range, and a valid end frame

### GetAutoSizeHasStartFrame
```angelscript
bool GetAutoSizeHasStartFrame(UMovieSceneSection Section)
```
Checks to see if this section has an AutoSize implementation, and if so, if that implementation has a start frame.

@param Section        The section being queried
@return Whether this section has a valid autosize range, and a valid start frame

### GetAutoSizeStartFrame
```angelscript
int GetAutoSizeStartFrame(UMovieSceneSection Section)
```
Get start frame of the AutoSize. Will throw an exception if section has no start frame, use GetAutoSizeHasStartFrame to check first.

@param Section        The section being queried
@return The start frame of the AutoSize data.

### GetAutoSizeStartFrameSeconds
```angelscript
float32 GetAutoSizeStartFrameSeconds(UMovieSceneSection Section)
```
Get start time of the AutoSize in seconds. Will throw an exception if section has no start frame, use GetAutoSizeHasStartFrame to check first.

@param Section        The section being queried
@return The start frame of the AutoSize data in seconds.

### GetChannel
```angelscript
UMovieSceneScriptingChannel GetChannel(UMovieSceneSection Section, FName ChannelName)
```
Get channel from specified section and channel name

@param Section        The section to use.
@param ChannelName    The name of the channel.
@return The channel if it exists

### GetChannelsByType
```angelscript
TArray<UMovieSceneScriptingChannel> GetChannelsByType(UMovieSceneSection Section, TSubclassOf<UMovieSceneScriptingChannel> ChannelType)
```
Find all channels that belong to the specified UMovieSceneSection that match the specific type. This will filter out any children who do not inherit
from the specified type for you.

@param Section        The section to use.
@param ChannelType    The class type to look for.
@return An array containing any key channels that match the type specified

### GetEndFrame
```angelscript
int GetEndFrame(UMovieSceneSection Section)
```
Get end frame. Will throw an exception if section has no end frame, use HasEndFrame to check first.

@param Section        The section within which to get the end frame
@return End frame of this section

### GetEndFrameSeconds
```angelscript
float32 GetEndFrameSeconds(UMovieSceneSection Section)
```
Get end time in seconds. Will throw an exception if section has no end frame, use HasEndFrame to check first.

@param Section        The section within which to get the end time
@return End time of this section

### GetParentSequenceFrame
```angelscript
int GetParentSequenceFrame(UMovieSceneSubSection Section, int InFrame, UMovieSceneSequence ParentSequence)
```
Get the frame in the space of its parent sequence

@param Section        The section that the InFrame is local to
@param InFrame The desired local frame
@param ParentSequence The parent sequence to traverse from
@return The frame at the parent sequence

### GetStartFrame
```angelscript
int GetStartFrame(UMovieSceneSection Section)
```
Get start frame. Will throw an exception if section has no start frame, use HasStartFrame to check first.

@param Section        The section within which to get the start frame
@return Start frame of this section

### GetStartFrameSeconds
```angelscript
float32 GetStartFrameSeconds(UMovieSceneSection Section)
```
Get start time in seconds. Will throw an exception if section has no start frame, use HasStartFrame to check first.

@param Section        The section within which to get the start time
@return Start time of this section

### HasEndFrame
```angelscript
bool HasEndFrame(UMovieSceneSection Section)
```
Has end frame

@param Section        The section being queried
@return Whether this section has a valid end frame (else infinite)

### HasStartFrame
```angelscript
bool HasStartFrame(UMovieSceneSection Section)
```
Has start frame

@param Section        The section being queried
@return Whether this section has a valid start frame (else infinite)

### SetEndFrame
```angelscript
void SetEndFrame(UMovieSceneSection Section, int EndFrame)
```
Set end frame

@param Section        The section within which to set the end frame
@param EndFrame The desired start frame for this section

### SetEndFrameBounded
```angelscript
void SetEndFrameBounded(UMovieSceneSection Section, bool bIsBounded)
```
Set end frame bounded

@param Section        The section to set whether the end frame is bounded or not
@param IsBounded The desired bounded state of the end frame

### SetEndFrameSeconds
```angelscript
void SetEndFrameSeconds(UMovieSceneSection Section, float32 EndTime)
```
Set end time in seconds

@param Section        The section within which to set the end time
@param EndTime The desired end time for this section

### SetRange
```angelscript
void SetRange(UMovieSceneSection Section, int StartFrame, int EndFrame)
```
Set range

@param Section        The section within which to set the range
@param StartFrame The desired start frame for this section
@param EndFrame The desired end frame for this section

### SetRangeSeconds
```angelscript
void SetRangeSeconds(UMovieSceneSection Section, float32 StartTime, float32 EndTime)
```
Set range in seconds

@param Section        The section within which to set the range
@param StartTime The desired start frame for this section
@param EndTime The desired end frame for this section

### SetStartFrame
```angelscript
void SetStartFrame(UMovieSceneSection Section, int StartFrame)
```
Set start frame

@param Section        The section within which to set the start frame
@param StartFrame The desired start frame for this section

### SetStartFrameBounded
```angelscript
void SetStartFrameBounded(UMovieSceneSection Section, bool bIsBounded)
```
Set start frame bounded

@param Section        The section to set whether the start frame is bounded or not
@param IsBounded The desired bounded state of the start frame

### SetStartFrameSeconds
```angelscript
void SetStartFrameSeconds(UMovieSceneSection Section, float32 StartTime)
```
Set start time in seconds

@param Section        The section within which to set the start time
@param StartTime The desired start time for this section

### StaticClass
```angelscript
UClass StaticClass()
```

