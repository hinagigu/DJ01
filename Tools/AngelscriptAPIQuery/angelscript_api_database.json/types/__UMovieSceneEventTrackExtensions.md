# __UMovieSceneEventTrackExtensions

## 方法

### AddEventRepeaterSection
```angelscript
UMovieSceneEventRepeaterSection AddEventRepeaterSection(UMovieSceneEventTrack InTrack)
```
Create a new event repeater section for the given track

@param Track        The event track to add the new event repeater section to
@return The newly created event repeater section

### AddEventTriggerSection
```angelscript
UMovieSceneEventTriggerSection AddEventTriggerSection(UMovieSceneEventTrack InTrack)
```
Create a new event trigger section for the given track

@param Track        The event track to add the new event trigger section to
@return The newly created event trigger section

### GetBoundObjectPropertyClass
```angelscript
UClass GetBoundObjectPropertyClass(FMovieSceneEvent EventKey)
```
* Return the class of the bound object property
*
* @param EventKey    The event key to get the bound object property from
* @return The class of the bound object property

### StaticClass
```angelscript
UClass StaticClass()
```

