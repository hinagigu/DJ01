# UInterchangeAnimationTrackNode

**继承自**: `UInterchangeAnimationTrackBaseNode`

Class to represent an animation on the property of a camera, light, or scene node
The list of supported properties is enumerated in EInterchangeAnimatedProperty.

## 方法

### GetCustomActorDependencyUid
```angelscript
bool GetCustomActorDependencyUid(FString& DependencyUid)
```
Get the actor dependency to this object.

### GetCustomAnimationPayloadKey
```angelscript
bool GetCustomAnimationPayloadKey(FInterchangeAnimationPayLoadKey& AnimationPayLoadKey)
```
Get the payload key needed to retrieve the animation for this track.

### GetCustomFrameCount
```angelscript
bool GetCustomFrameCount(int& AttributeValue)
```
Get the number of frames for the animation of this track.

### GetCustomPropertyTrack
```angelscript
bool GetCustomPropertyTrack(FName& PropertyTrack)
```

### GetCustomTargetedProperty
```angelscript
bool GetCustomTargetedProperty(int& TargetedProperty)
```

### SetCustomActorDependencyUid
```angelscript
bool SetCustomActorDependencyUid(FString DependencyUid)
```
Set the actor dependency to this object.

### SetCustomAnimationPayloadKey
```angelscript
bool SetCustomAnimationPayloadKey(FString InUniqueId, EInterchangeAnimationPayLoadType InType)
```
Set the payload key needed to retrieve the animation for this track.

### SetCustomFrameCount
```angelscript
bool SetCustomFrameCount(int AttributeValue)
```
Set the number of frames for the animation of this track.

### SetCustomPropertyTrack
```angelscript
bool SetCustomPropertyTrack(FName PropertyTrack)
```
Set the property animated by this track. Usually the name of a UMovieSceneTrack, e.g for UMovieSceneColorTrack -> Color

### SetCustomTargetedProperty
```angelscript
bool SetCustomTargetedProperty(int TargetedProperty)
```

