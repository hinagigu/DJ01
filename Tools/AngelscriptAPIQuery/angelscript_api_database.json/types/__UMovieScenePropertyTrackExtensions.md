# __UMovieScenePropertyTrackExtensions

## 方法

### GetByteTrackEnum
```angelscript
UEnum GetByteTrackEnum(UMovieSceneByteTrack Track)
```
Get this byte track's enum

@param Track        The track to use
@return The enum for this byte track

### GetObjectPropertyClass
```angelscript
UClass GetObjectPropertyClass(UMovieSceneObjectPropertyTrack Track)
```
Get this object property track's property class

@param Track        The track to use
@return The property class for this object property track

### GetPropertyName
```angelscript
FName GetPropertyName(UMovieScenePropertyTrack Track)
```
Get this track's property name

@param Track        The track to use
@return This track's property name

### GetPropertyPath
```angelscript
FString GetPropertyPath(UMovieScenePropertyTrack Track)
```
Get this track's property path

@param Track        The track to use
@return This track's property path

### GetUniqueTrackName
```angelscript
FName GetUniqueTrackName(UMovieScenePropertyTrack Track)
```
Get this track's unique name

@param Track        The track to use
@return This track's unique name

### SetByteTrackEnum
```angelscript
void SetByteTrackEnum(UMovieSceneByteTrack Track, UEnum InEnum)
```
Set this byte track's enum

@param Track        The track to use
@param InEnum The enum to set

### SetObjectPropertyClass
```angelscript
void SetObjectPropertyClass(UMovieSceneObjectPropertyTrack Track, UClass PropertyClass)
```
Set this object property track's property class

@param Track        The track to use
@param PropertyClass The property class to set

### SetPropertyNameAndPath
```angelscript
void SetPropertyNameAndPath(UMovieScenePropertyTrack Track, FName InPropertyName, FString InPropertyPath)
```
Set this track's property name and path

@param Track        The track to use
@param InPropertyName The property name
@param InPropertyPath The property path

### StaticClass
```angelscript
UClass StaticClass()
```

