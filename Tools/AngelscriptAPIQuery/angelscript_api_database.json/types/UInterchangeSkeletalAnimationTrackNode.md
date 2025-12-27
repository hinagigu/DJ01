# UInterchangeSkeletalAnimationTrackNode

**继承自**: `UInterchangeAnimationTrackBaseNode`

* Class to hold onto the relationships between a set of animation tracks and the bones, morph targets of a skeleton.

## 方法

### GetCustomAnimationSampleRate
```angelscript
bool GetCustomAnimationSampleRate(float& SampleRate)
```
Get the animation sample rate. Return false if the attribute is not set.

### GetCustomAnimationStartTime
```angelscript
bool GetCustomAnimationStartTime(float& StartTime)
```
Get the animation start time. Return false if the attribute is not set.

### GetCustomAnimationStopTime
```angelscript
bool GetCustomAnimationStopTime(float& StopTime)
```
Get the animation stop time. Return false if the attribute is not set.

### GetCustomSkeletonNodeUid
```angelscript
bool GetCustomSkeletonNodeUid(FString& AttributeValue)
```
Get the unique ID of the skeleton factory node. Return false if the attribute is not set.

### GetMorphTargetNodeAnimationPayloadKeys
```angelscript
void GetMorphTargetNodeAnimationPayloadKeys(TMap<FString,FString>& OutMorphTargetNodeAnimationPayloadKeyUids, TMap<FString,uint8>& OutMorphTargetNodeAnimationPayloadKeyTypes)
```

### GetSceneNodeAnimationPayloadKeys
```angelscript
void GetSceneNodeAnimationPayloadKeys(TMap<FString,FString>& OutSceneNodeAnimationPayloadKeyUids, TMap<FString,uint8>& OutSceneNodeAnimationPayloadKeyTypes)
```

### SetAnimationPayloadKeyForMorphTargetNodeUid
```angelscript
bool SetAnimationPayloadKeyForMorphTargetNodeUid(FString MorphTargetNodeUid, FString InUniqueId, EInterchangeAnimationPayLoadType InType)
```

### SetAnimationPayloadKeyForSceneNodeUid
```angelscript
bool SetAnimationPayloadKeyForSceneNodeUid(FString SceneNodeUid, FString InUniqueId, EInterchangeAnimationPayLoadType InType)
```

### SetCustomAnimationSampleRate
```angelscript
bool SetCustomAnimationSampleRate(float SampleRate)
```
Set the animation sample rate. Return false if the attribute could not be set.

### SetCustomAnimationStartTime
```angelscript
bool SetCustomAnimationStartTime(float StartTime)
```
Set the animation start time. Return false if the attribute could not be set.

### SetCustomAnimationStopTime
```angelscript
bool SetCustomAnimationStopTime(float StopTime)
```
Set the animation stop time. Return false if the attribute could not be set.

### SetCustomSkeletonNodeUid
```angelscript
bool SetCustomSkeletonNodeUid(FString AttributeValue)
```
Set the unique ID of the skeleton factory node. Return false if the attribute could not be set.

