# UMovieSceneMetaData

**继承自**: `UObject`

Movie scene meta-data that is stored on UMovieScene assets
Meta-data is retrieved through ULevelSequence::FindMetaData<ULevelSequenceMetaData>()

## 方法

### GetAuthor
```angelscript
FString GetAuthor()
```
@return The author for this metadata

### GetCreated
```angelscript
FDateTime GetCreated()
```
@return The created date for this metadata

### GetNotes
```angelscript
FString GetNotes()
```
@return The notes for this metadata

### SetAuthor
```angelscript
void SetAuthor(FString InAuthor)
```
Set this metadata's author

### SetCreated
```angelscript
void SetCreated(FDateTime InCreated)
```
Set this metadata's created date

### SetNotes
```angelscript
void SetNotes(FString InNotes)
```
Set this metadata's notes

