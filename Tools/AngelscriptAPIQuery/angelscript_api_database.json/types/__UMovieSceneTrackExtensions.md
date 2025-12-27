# __UMovieSceneTrackExtensions

## 方法

### AddSection
```angelscript
UMovieSceneSection AddSection(UMovieSceneTrack Track)
```
Add a new section to this track

@param Track        The track to use
@return The newly create section if successful

### GetColorTint
```angelscript
FColor GetColorTint(UMovieSceneTrack Track)
```
Get the color tint for this track

@param Track        The track to get the color tint from
@return The color tint of the requested track

### GetDisplayName
```angelscript
FText GetDisplayName(UMovieSceneTrack Track)
```
Get this track's display name

@param Track        The track to use
@return This track's display name

### GetSections
```angelscript
TArray<UMovieSceneSection> GetSections(UMovieSceneTrack Track)
```
Access all this track's sections

@param Track        The track to use
@return An array of this track's sections

### GetSectionToKey
```angelscript
UMovieSceneSection GetSectionToKey(UMovieSceneTrack Track)
```
Get the section to key for this track

@param Track        The track to get the section to key for
@return The section to key for the requested track

### GetSortingOrder
```angelscript
int GetSortingOrder(UMovieSceneTrack Track)
```
Get the sorting order for this track

@param Track        The track to get the sorting order from
@return The sorting order of the requested track

### GetTrackRowDisplayName
```angelscript
FText GetTrackRowDisplayName(UMovieSceneTrack Track, int RowIndex)
```
Get this track row's display name

@param Track        The track to use
@param RowIndex The row index for the track
@return This track's display name

### RemoveSection
```angelscript
void RemoveSection(UMovieSceneTrack Track, UMovieSceneSection Section)
```
Remove the specified section

@param Track        The track to remove the section from, if present
@param Section      The section to remove

### SetColorTint
```angelscript
void SetColorTint(UMovieSceneTrack Track, FColor ColorTint)
```
Set the color tint for this track

@param Track        The track to set the color tint for
@param ColorTint The color tint to set

### SetDisplayName
```angelscript
void SetDisplayName(UMovieSceneTrack Track, FText InName)
```
Set this track's display name

@param Track        The track to use
@param InName The name for this track

### SetSectionToKey
```angelscript
void SetSectionToKey(UMovieSceneTrack Track, UMovieSceneSection Section)
```
Set the section to key for this track. When properties for this section are modified externally,
this section will receive those modifications and act accordingly (add/update keys). This is
especially useful when there are multiple overlapping sections.

@param Track        The track to set the section to key for
@param Section      The section to key for this track

### SetSortingOrder
```angelscript
void SetSortingOrder(UMovieSceneTrack Track, int SortingOrder)
```
Set the sorting order for this track

@param Track        The track to get the sorting order from
@param SortingOrder The sorting order to set

### SetTrackRowDisplayName
```angelscript
void SetTrackRowDisplayName(UMovieSceneTrack Track, FText InName, int RowIndex)
```
Set this track row's display name

@param Track        The track to use
@param InName The name for this track
@param RowIndex The row index for the track

### StaticClass
```angelscript
UClass StaticClass()
```

