# UInterchangeAnimationTrackSetNode

**继承自**: `UInterchangeBaseNode`

Class to represent a set of animation track nodes that share the same frame rate.

## 方法

### AddCustomAnimationTrackUid
```angelscript
bool AddCustomAnimationTrackUid(FString AnimationTrackUid)
```
Add one track dependency to this object.

### GetCustomAnimationTrackUid
```angelscript
void GetCustomAnimationTrackUid(int Index, FString& OutAnimationTrackUid)
```
Retrieve one track dependency for this object.

### GetCustomAnimationTrackUidCount
```angelscript
int GetCustomAnimationTrackUidCount()
```
Retrieve the number of track dependencies for this object.

### GetCustomAnimationTrackUids
```angelscript
void GetCustomAnimationTrackUids(TArray<FString>& OutAnimationTrackUids)
```
Retrieve the track dependency for this object.

### GetCustomFrameRate
```angelscript
bool GetCustomFrameRate(float32& AttributeValue)
```
Get the frame rate for the animations in the level sequence.

### RemoveCustomAnimationTrackUid
```angelscript
bool RemoveCustomAnimationTrackUid(FString AnimationTrackUid)
```
Remove one track dependency from this object.

### SetCustomFrameRate
```angelscript
bool SetCustomFrameRate(float32 AttributeValue)
```
Set the frame rate for the animations in the level sequence.

