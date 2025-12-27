# UMediaPlaylist

**继承自**: `UObject`

Implements a media play list.

## 属性

### Items
- **类型**: `TArray<TObjectPtr<UMediaSource>>`
- **描述**: List of media sources to play.

## 方法

### Add
```angelscript
bool Add(UMediaSource MediaSource)
```
Add a media source to the play list.

@param MediaSource The media source to append.
@return true if the media source was added, false otherwise.
@see AddFile, AddUrl, Insert, RemoveAll, Remove, Replace

### AddFile
```angelscript
bool AddFile(FString FilePath)
```
Add a media file path to the play list.

@param FilePath The file path to add.
@return true if the file was added, false otherwise.
@see Add, AddUrl, Insert, RemoveAll, Remove, Replace

### AddUrl
```angelscript
bool AddUrl(FString Url)
```
Add a media URL to the play list.

@param Url The URL to add.
@return true if the URL was added, false otherwise.
@see Add, AddFile, Insert, RemoveAll, Remove, Replace

### Get
```angelscript
UMediaSource Get(int Index)
```
Get the media source at the specified index.

@param Index The index of the media source to get.
@return The media source, or nullptr if the index doesn't exist.
@see GetNext, GetRandom

### GetNext
```angelscript
UMediaSource GetNext(int& InOutIndex)
```
Get the next media source in the play list.

@param InOutIndex Index of the current media source (will contain the new index).
@return The media source after the current one, or nullptr if the list is empty.
@see , GetPrevious, GetRandom

### GetPrevious
```angelscript
UMediaSource GetPrevious(int& InOutIndex)
```
Get the previous media source in the play list.

@param InOutIndex Index of the current media source (will contain the new index).
@return The media source before the current one, or nullptr if the list is empty.
@see , GetNext, GetRandom

### GetRandom
```angelscript
UMediaSource GetRandom(int& OutIndex)
```
Get a random media source in the play list.

@param OutIndex Will contain the index of the returned media source.
@return The random media source, or nullptr if the list is empty.
@see Get, GetNext, GetPrevious

### Insert
```angelscript
void Insert(UMediaSource MediaSource, int Index)
```
Insert a media source into the play list at the given position.

@param MediaSource The media source to insert.
@param Index The index to insert into.
@see Add, Remove, RemoveAll, Replace

### Num
```angelscript
int Num()
```
Get the number of media sources in the play list.

@return Number of media sources.

### Remove
```angelscript
bool Remove(UMediaSource MediaSource)
```
Remove all occurrences of the given media source in the play list.

@param MediaSource The media source to remove.
@return true if the media source was removed, false otherwise.
@see Add, Insert, Remove, Replace

### RemoveAt
```angelscript
bool RemoveAt(int Index)
```
Remove the media source at the specified position.

@param Index The index of the media source to remove.
@return true if the media source was removed, false otherwise.
@see Add, Insert, RemoveAll, Replace

### Replace
```angelscript
bool Replace(int Index, UMediaSource Replacement)
```
Replace the media source at the specified position.

@param Index The index of the media source to replace.
@param Replacement The replacement media source.
@return true if the media source was replaced, false otherwise.
@see Add, Insert, RemoveAll, RemoveAt

