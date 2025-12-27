# UInterchangeLevelSequenceFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

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
This function allow to retrieve one track dependency for this object.

### GetCustomAnimationTrackUidCount
```angelscript
int GetCustomAnimationTrackUidCount()
```
This function allow to retrieve the number of track dependencies for this object.

### GetCustomAnimationTrackUids
```angelscript
void GetCustomAnimationTrackUids(TArray<FString>& OutAnimationTrackUids)
```
This function allow to retrieve the track dependency for this object.

### GetCustomFrameRate
```angelscript
bool GetCustomFrameRate(float32& AttributeValue)
```
Get the frame rate for the animations in the level sequence.

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node want to create

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

