# UMediaPlayer

**继承自**: `UObject`

Implements a media player asset that can play movies and other media sources.

## 属性

### OnEndReached
- **类型**: `FOnMediaPlayerMediaEvent`

### OnMediaClosed
- **类型**: `FOnMediaPlayerMediaEvent`

### OnMediaOpened
- **类型**: `FOnMediaPlayerMediaOpened`

### OnMediaOpenFailed
- **类型**: `FOnMediaPlayerMediaOpenFailed`

### OnPlaybackResumed
- **类型**: `FOnMediaPlayerMediaEvent`

### OnPlaybackSuspended
- **类型**: `FOnMediaPlayerMediaEvent`

### OnSeekCompleted
- **类型**: `FOnMediaPlayerMediaEvent`

### OnTracksChanged
- **类型**: `FOnMediaPlayerMediaEvent`

### OnMetadataChanged
- **类型**: `FOnMediaPlayerMediaEvent`

### CacheAhead
- **类型**: `FTimespan`
- **描述**: Duration of samples to cache ahead of the play head.

@see CacheBehind, CacheBehindGame

### CacheBehind
- **类型**: `FTimespan`
- **描述**: Duration of samples to cache behind the play head (when not running as game).

@see CacheAhead, CacheBehindGame

### CacheBehindGame
- **类型**: `FTimespan`
- **描述**: Duration of samples to cache behind the play head (when running as game).

@see CacheAhead, CacheBehind

### NativeAudioOut
- **类型**: `bool`
- **描述**: Output any audio via the operating system's sound mixer instead of a Sound Wave asset.

If enabled, the assigned Sound Wave asset will be ignored. The SetNativeVolume
function can then be used to change the audio output volume at runtime. Note that
not all media player plug-ins may support native audio output on all platforms.

@see SetNativeVolume

### PlayOnOpen
- **类型**: `bool`

### AffectedByPIEHandling
- **类型**: `bool`

### Shuffle
- **类型**: `bool`

### Loop
- **类型**: `bool`

### HorizontalFieldOfView
- **类型**: `float32`

### VerticalFieldOfView
- **类型**: `float32`

## 方法

### CanPause
```angelscript
bool CanPause()
```
Check whether media playback can be paused right now.

Playback can be paused if the media supports pausing and if it is currently playing.

@return true if pausing playback can be paused, false otherwise.
@see CanPlay, Pause

### CanPlaySource
```angelscript
bool CanPlaySource(UMediaSource MediaSource)
```
Check whether the specified media source can be played by this player.

If a desired player name is set for this player, it will only check
whether that particular player type can play the specified source.

@param MediaSource The media source to check.
@return true if the media source can be opened, false otherwise.
@see CanPlayUrl, SetDesiredPlayerName

### CanPlayUrl
```angelscript
bool CanPlayUrl(FString Url)
```
Check whether the specified URL can be played by this player.

If a desired player name is set for this player, it will only check
whether that particular player type can play the specified URL.

@param Url The URL to check.
@see CanPlaySource, SetDesiredPlayerName

### Close
```angelscript
void Close()
```
Close the currently open media, if any.

@see OnMediaClosed, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Pause, Play

### GetAudioTrackChannels
```angelscript
int GetAudioTrackChannels(int TrackIndex, int FormatIndex)
```
Get the number of channels in the specified audio track.

@param TrackIndex Index of the audio track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Number of channels.
@see GetAudioTrackSampleRate, GetAudioTrackType

### GetAudioTrackSampleRate
```angelscript
int GetAudioTrackSampleRate(int TrackIndex, int FormatIndex)
```
Get the sample rate of the specified audio track.

@param TrackIndex Index of the audio track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Samples per second.
@see GetAudioTrackChannels, GetAudioTrackType

### GetAudioTrackType
```angelscript
FString GetAudioTrackType(int TrackIndex, int FormatIndex)
```
Get the type of the specified audio track format.

@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Audio format type string.
@see GetAudioTrackSampleRate, GetAudioTrackSampleRate

### GetDesiredPlayerName
```angelscript
FName GetDesiredPlayerName()
```
Get the name of the current desired native player.

@return The name of the desired player, or NAME_None if not set.
@see SetDesiredPlayerName

### GetDisplayTime
```angelscript
FTimespan GetDisplayTime()
```
Get the media's current playback time as appropriate for display.

@return Playback time.
@see GetDuration, Seek

### GetDisplayTimeStamp
```angelscript
UMediaTimeStampInfo GetDisplayTimeStamp()
```
Get the media's current playback timestamp as appropriate for display.

@return Playback timestamp.
@see GetDuration, Seek

### GetDuration
```angelscript
FTimespan GetDuration()
```
Get the media's duration.

@return A time span representing the duration.
@see GetTime, Seek

### GetHorizontalFieldOfView
```angelscript
float32 GetHorizontalFieldOfView()
```
Get the current horizontal field of view (only for 360 videos).

@return Horizontal field of view (in Euler degrees).
@see GetVerticalFieldOfView, GetViewRotation, SetHorizontalFieldOfView

### GetMediaMetadataItems
```angelscript
TMap<FString,FMediaMetadataItemsBPT> GetMediaMetadataItems()
```
This is the blueprint accessible version of the GetMediaMetadata.
@return Map with arrays of FMediaMetaDataItem entries describing any metadata found in the current stream
@note Listen to EMediaEvent::MetadataChanged to catch updates to this data

### GetMediaName
```angelscript
FText GetMediaName()
```
Get the human readable name of the currently loaded media source.

@return Media source name, or empty text if no media is opened
@see GetPlayerName, GetUrl

### GetNumTrackFormats
```angelscript
int GetNumTrackFormats(EMediaPlayerTrack TrackType, int TrackIndex)
```
Get the number of formats of the specified track.

@param TrackType The type of media tracks.
@param TrackIndex The index of the track.
@return Number of formats.
@see GetNumTracks, GetSelectedTrack, SelectTrack

### GetNumTracks
```angelscript
int GetNumTracks(EMediaPlayerTrack TrackType)
```
Get the number of tracks of the given type.

@param TrackType The type of media tracks.
@return Number of tracks.
@see GetNumTrackFormats, GetSelectedTrack, SelectTrack

### GetPlaybackTimeRange
```angelscript
FFloatInterval GetPlaybackTimeRange(EMediaTimeRangeBPType InRangeToGet)
```
Blueprint accessible version of GetPlaybackTimeRange.
This returns the range truncated into a blueprint usable float interval and should not
be used for live streams as 32 bit floats can not store wallclock times with enough precision.

### GetPlayerName
```angelscript
FName GetPlayerName()
```
Get the name of the current native media player.

@return Player name, or NAME_None if not available.
@see GetMediaName

### GetPlaylist
```angelscript
UMediaPlaylist GetPlaylist()
```
Get the current play list.

Media players always have a valid play list. In C++ code you can use
the GetPlaylistRef to get a reference instead of a pointer to it.

@return The play list.
@see GetPlaylistIndex, GetPlaylistRef

### GetPlaylistIndex
```angelscript
int GetPlaylistIndex()
```
Get the current play list index.

@return Play list index.
@see GetPlaylist

### GetRate
```angelscript
float32 GetRate()
```
Get the media's current playback rate.

@return The playback rate.
@see SetRate, SupportsRate

### GetSelectedTrack
```angelscript
int GetSelectedTrack(EMediaPlayerTrack TrackType)
```
Get the index of the currently selected track of the given type.

@param TrackType The type of track to get.
@return The index of the selected track, or INDEX_NONE if no track is active.
@see GetNumTracks, GetTrackFormat, SelectTrack

### GetSupportedRates
```angelscript
void GetSupportedRates(TArray<FFloatRange>& OutRates, bool Unthinned)
```
Get the supported playback rates.

@param Unthinned Whether the rates are for unthinned playback.
@param Will contain the the ranges of supported rates.
@see SetRate, SupportsRate

### GetTime
```angelscript
FTimespan GetTime()
```
Get the media's current playback time.

@return Playback time.
@see GetDuration, Seek

### GetTimeDelay
```angelscript
FTimespan GetTimeDelay()
```
Delay of the player's time.

@return Delay added to the player's time used to manually sync multiple sources.
@see SetTimeDelay

### GetTimeStamp
```angelscript
UMediaTimeStampInfo GetTimeStamp()
```
Get the media's current playback timestamp.

@return Playback timestamp.
@see GetDuration, Seek

### GetTrackDisplayName
```angelscript
FText GetTrackDisplayName(EMediaPlayerTrack TrackType, int TrackIndex)
```
Get the human readable name of the specified track.

@param TrackType The type of track.
@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@return Display name.
@see GetNumTracks, GetTrackLanguage

### GetTrackFormat
```angelscript
int GetTrackFormat(EMediaPlayerTrack TrackType, int TrackIndex)
```
Get the index of the active format of the specified track type.

@param TrackType The type of track.
@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@return The index of the selected format.
@see GetNumTrackFormats, GetSelectedTrack, SetTrackFormat

### GetTrackLanguage
```angelscript
FString GetTrackLanguage(EMediaPlayerTrack TrackType, int TrackIndex)
```
Get the language tag of the specified track.

@param TrackType The type of track.
@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@return Language tag, i.e. "en-US" for English, or "und" for undefined.
@see GetNumTracks, GetTrackDisplayName

### GetUrl
```angelscript
FString GetUrl()
```
Get the URL of the currently loaded media, if any.

@return Media URL, or empty string if no media was loaded.
@see OpenUrl

### GetVerticalFieldOfView
```angelscript
float32 GetVerticalFieldOfView()
```
Get the current vertical field of view (only for 360 videos).

@return Vertical field of view (in Euler degrees), or 0.0 if not available.
@see GetHorizontalFieldOfView, GetViewRotation, SetVerticalFieldOfView

### GetVideoTrackAspectRatio
```angelscript
float32 GetVideoTrackAspectRatio(int TrackIndex, int FormatIndex)
```
Get the aspect ratio of the specified video track.

@param TrackIndex Index of the video track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Aspect ratio.
@see GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackFrameRates, GetVideoTrackType

### GetVideoTrackDimensions
```angelscript
FIntPoint GetVideoTrackDimensions(int TrackIndex, int FormatIndex)
```
Get the current dimensions of the specified video track.

@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Video dimensions (in pixels).
@see GetVideoTrackAspectRatio, GetVideoTrackFrameRate, GetVideoTrackFrameRates, GetVideoTrackType

### GetVideoTrackFrameRate
```angelscript
float32 GetVideoTrackFrameRate(int TrackIndex, int FormatIndex)
```
Get the frame rate of the specified video track.

@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Frame rate (in frames per second).
@see GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRates, GetVideoTrackType, SetVideoTrackFrameRate

### GetVideoTrackFrameRates
```angelscript
FFloatRange GetVideoTrackFrameRates(int TrackIndex, int FormatIndex)
```
Get the supported range of frame rates of the specified video track.

@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Frame rate range (in frames per second).
@see GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackType

### GetVideoTrackType
```angelscript
FString GetVideoTrackType(int TrackIndex, int FormatIndex)
```
Get the type of the specified video track format.

@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@return Video format type string.
@see GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackFrameRates

### GetViewRotation
```angelscript
FRotator GetViewRotation()
```
Get the current view rotation (only for 360 videos).

@return View rotation, or zero rotator if not available.
@see GetHorizontalFieldOfView, GetVerticalFieldOfView, SetViewRotation

### HasError
```angelscript
bool HasError()
```
Check whether the player is in an error state.

When the player is in an error state, no further operations are possible.
The current media must be closed, and a new media source must be opened
before the player can be used again. Errors are usually caused by faulty
media files or interrupted network connections.

@see IsReady

### IsBuffering
```angelscript
bool IsBuffering()
```
Check whether playback is buffering data.

@return true if looping, false otherwise.
@see IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady

### IsClosed
```angelscript
bool IsClosed()
```
Whether media is currently closed.

@return true if media is closed, false otherwise.

### IsConnecting
```angelscript
bool IsConnecting()
```
Check whether the player is currently connecting to a media source.

@return true if connecting, false otherwise.
@see IsBuffering, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady

### IsLooping
```angelscript
bool IsLooping()
```
Check whether playback is looping.

@return true if looping, false otherwise.
@see IsBuffering, IsConnecting, IsPaused, IsPlaying, IsPreparing, IsReady, SetLooping

### IsPaused
```angelscript
bool IsPaused()
```
Check whether playback is currently paused.

@return true if playback is paused, false otherwise.
@see CanPause, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady, Pause

### IsPlaying
```angelscript
bool IsPlaying()
```
Check whether playback has started.

@return true if playback has started, false otherwise.
@see CanPlay, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady, Play

### IsPreparing
```angelscript
bool IsPreparing()
```
Check whether the media is currently opening or buffering.

@return true if playback is being prepared, false otherwise.
@see CanPlay, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsReady, Play

### IsReady
```angelscript
bool IsReady()
```
Check whether media is ready for playback.

A player is ready for playback if it has a media source opened that
finished preparing and is not in an error state.

@return true if media is ready, false otherwise.
@see HasError, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing

### Next
```angelscript
bool Next()
```
Open the next item in the current play list.

The player will start playing the new media source if it was playing
something previously, otherwise it will only open the media source.

@return true on success, false otherwise.
@see Close, OpenUrl, OpenSource, Play, Previous, SetPlaylist

### OpenFile
```angelscript
bool OpenFile(FString FilePath)
```
Opens the specified media file path.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!

@param FilePath The file path to open.
@return true if the file path will be opened, false otherwise.
@see GetUrl, Close, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Reopen

### OpenPlaylist
```angelscript
bool OpenPlaylist(UMediaPlaylist InPlaylist)
```
Open the first media source in the specified play list.

@param InPlaylist The play list to open.
@return true if the source will be opened, false otherwise.
@see Close, OpenFile, OpenPlaylistIndex, OpenSource, OpenUrl, Reopen

### OpenPlaylistIndex
```angelscript
bool OpenPlaylistIndex(UMediaPlaylist InPlaylist, int Index)
```
Open a particular media source in the specified play list.

@param InPlaylist The play list to open.
@param Index The index of the source to open.
@return true if the source will be opened, false otherwise.
@see Close, OpenFile, OpenPlaylist, OpenSource, OpenUrl, Reopen

### OpenSource
```angelscript
bool OpenSource(UMediaSource MediaSource)
```
Open the specified media source.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!

@param MediaSource The media source to open.
@return true if the source will be opened, false otherwise.
@see Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenUrl, Reopen

### OpenSourceLatent
```angelscript
void OpenSourceLatent(FLatentActionInfo LatentInfo, UMediaSource MediaSource, FMediaPlayerOptions Options, bool& bSuccess)
```
Open the specified media source with options using a latent action.

A result of true indicates that the player successfully completed all requested operations.

@param MediaSource The media source to open.
@param Options The media player options to apply.
@param bSuccess  All requested operations have completed successfully.
@see Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenUrl, Reopen

### OpenSourceWithOptions
```angelscript
bool OpenSourceWithOptions(UMediaSource MediaSource, FMediaPlayerOptions Options)
```
Open the specified media source with supplied options applied.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!

@param MediaSource The media source to open.
@param Options The media player options to apply.
@return true if the source will be opened, false otherwise.
@see Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenUrl, Reopen

### OpenUrl
```angelscript
bool OpenUrl(FString Url)
```
Opens the specified media URL.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!

@param Url The URL to open.
@return true if the URL will be opened, false otherwise.
@see GetUrl, Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, Reopen

### Pause
```angelscript
bool Pause()
```
Pauses media playback.

This is the same as setting the playback rate to 0.0.

@return true if playback is being paused, false otherwise.
@see CanPause, Close, Next, Play, Previous, Rewind, Seek

### Play
```angelscript
bool Play()
```
Starts media playback.

This is the same as setting the playback rate to 1.0.

@return true if playback is starting, false otherwise.
@see CanPlay, GetRate, Next, Pause, Previous, SetRate

### PlayAndSeek
```angelscript
void PlayAndSeek()
```
Starts playback from the media opened event, but can be used elsewhere.

### Previous
```angelscript
bool Previous()
```
Open the previous item in the current play list.

The player will start playing the new media source if it was playing
something previously, otherwise it will only open the media source.

@return true on success, false otherwise.
@see Close, Next, OpenUrl, OpenSource, Play, SetPlaylist

### Reopen
```angelscript
bool Reopen()
```
Reopens the currently opened media or play list.

@return true if the media will be opened, false otherwise.
@see Close, Open, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl

### Rewind
```angelscript
bool Rewind()
```
Rewinds the media to the beginning.

This is the same as seeking to zero time.

@return true if rewinding, false otherwise.
@see GetTime, Seek

### Seek
```angelscript
bool Seek(FTimespan Time)
```
Seeks to the specified playback time.

@param Time The playback time to set.
@return true on success, false otherwise.
@see GetTime, Rewind

### SelectTrack
```angelscript
bool SelectTrack(EMediaPlayerTrack TrackType, int TrackIndex)
```
Select the active track of the given type.

The selected track will use its currently active format. Active formats will
be remembered on a per track basis. The first available format is active by
default. To switch the track format, use SetTrackFormat instead.

@param TrackType The type of track to select.
@param TrackIndex The index of the track to select, or INDEX_NONE to deselect.
@return true if the track was selected, false otherwise.
@see GetNumTracks, GetSelectedTrack, SetTrackFormat

### SetBlockOnTime
```angelscript
void SetBlockOnTime(FTimespan Time)
```
Set the time on which to block.

If set, this player will block in TickInput or TickFetch until the video sample
for the specified time are actually available.

@param Time The time to block on, or FTimespan::MinValue to disable.

### SetDesiredPlayerName
```angelscript
void SetDesiredPlayerName(FName PlayerName)
```
Set the name of the desired native player.

@param PlayerName The name of the player to set.
@see GetDesiredPlayerName

### SetLooping
```angelscript
bool SetLooping(bool Looping)
```
Enables or disables playback looping.

@param Looping Whether playback should be looped.
@return true on success, false otherwise.
@see IsLooping

### SetMediaOptions
```angelscript
void SetMediaOptions(const UMediaSource Options)
```
Sets the media options used by the player.

@param Options Options to pass to the player.

### SetNativeVolume
```angelscript
bool SetNativeVolume(float32 Volume)
```
Set the volume on the native player if not mixing with Sound Wave asset.

The SetNativeVolume can be used to change the audio output volume at runtime. Note that
not all media player plug-ins may support native audio output on all platforms.

@param Volume The volume to set.
@return true on success, false otherwise.
@see NativeAudioOut

### SetPlaybackTimeRange
```angelscript
bool SetPlaybackTimeRange(FFloatInterval InTimeRange)
```
Blueprint accessible version of SetPlaybackTimeRange().
The range is set through a blueprint usable float interval which may not have enough
precision to represent the range accurately.

### SetRate
```angelscript
bool SetRate(float32 Rate)
```
Changes the media's playback rate.

@param Rate The playback rate to set.
@return true on success, false otherwise.
@see GetRate, SupportsRate

### SetTimeDelay
```angelscript
void SetTimeDelay(FTimespan TimeDelay)
```
Delay of the player's time.

This setting can be used to manually sync multiple sources.
Set to 1 seconds, if you would like that Player to play 1 second behind its current time.
If the value is too big, it is possible that the player would not hold that frame for that long.
@return true on success, false otherwise.
@see GetTimeDelay

### SetTrackFormat
```angelscript
bool SetTrackFormat(EMediaPlayerTrack TrackType, int TrackIndex, int FormatIndex)
```
Set the format on the specified track.

Selecting the format will not switch to the specified track. To switch
tracks, use SelectTrack instead. If the track is already selected, the
format change will be applied immediately.

@param TrackType The type of track to update.
@param TrackIndex The index of the track to update.
@param FormatIndex The index of the format to select (must be valid).
@return true if the track was selected, false otherwise.
@see GetNumTrackFormats, GetNumTracks, GetTrackFormat, SelectTrack

### SetVideoTrackFrameRate
```angelscript
bool SetVideoTrackFrameRate(int TrackIndex, int FormatIndex, float32 FrameRate)
```
Set the frame rate of the specified video track.

@param TrackIndex The index of the track, or INDEX_NONE for the selected one.
@param FormatIndex Index of the track format, or INDEX_NONE for the selected one.
@param FrameRate The frame rate to set (must be in range of format's supported frame rates).
@return true on success, false otherwise.
@see GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackFrameRates, GetVideoTrackType

### SetViewField
```angelscript
bool SetViewField(float32 Horizontal, float32 Vertical, bool Absolute)
```
Set the field of view (only for 360 videos).

@param Horizontal Horizontal field of view (in Euler degrees).
@param Vertical Vertical field of view (in Euler degrees).
@param Whether the field of view change should be absolute (true) or relative (false).
@return true on success, false otherwise.
@see GetHorizontalFieldOfView, GetVerticalFieldOfView, SetViewRotation

### SetViewRotation
```angelscript
bool SetViewRotation(FRotator Rotation, bool Absolute)
```
Set the view's rotation (only for 360 videos).

@param Rotation The desired view rotation.
@param Whether the rotation change should be absolute (true) or relative (false).
@return true on success, false otherwise.
@see GetViewRotation, SetViewField

### SupportsPlaybackTimeRange
```angelscript
bool SupportsPlaybackTimeRange()
```
Check whether the player supports playing back of range within the media.

@return true if playing back a range is supported, false otherwise.
@see GetPlaybackTimeRange, SetPlaybackTimeRange

### SupportsRate
```angelscript
bool SupportsRate(float32 Rate, bool Unthinned)
```
Check whether the specified playback rate is supported.

@param Rate The playback rate to check.
@param Unthinned Whether no frames should be dropped at the given rate.
@see SupportsScrubbing, SupportsSeeking

### SupportsScrubbing
```angelscript
bool SupportsScrubbing()
```
Check whether the currently loaded media supports scrubbing.

@return true if scrubbing is supported, false otherwise.
@see SupportsRate, SupportsSeeking

### SupportsSeeking
```angelscript
bool SupportsSeeking()
```
Check whether the currently loaded media can jump to a certain position.

@return true if seeking is supported, false otherwise.
@see SupportsRate, SupportsScrubbing

