# UInterchangeAnimationTrackSetInstanceNode

**继承自**: `UInterchangeAnimationTrackBaseNode`

Class to represent an animation that instances another animation track set node.

## 方法

### GetCustomDuration
```angelscript
bool GetCustomDuration(int& AttributeValue)
```
Get the level sequence instance duration in number of frames.

### GetCustomStartFrame
```angelscript
bool GetCustomStartFrame(int& AttributeValue)
```
Get the frame where the level sequence instance starts.

### GetCustomTimeScale
```angelscript
bool GetCustomTimeScale(float32& AttributeValue)
```
Get the time scale used for the level sequence instance.

### GetCustomTrackSetDependencyUid
```angelscript
bool GetCustomTrackSetDependencyUid(FString& AttributeValue)
```
Get the unique id of the level sequence this instance references.

### SetCustomDuration
```angelscript
bool SetCustomDuration(int AttributeValue)
```
Set the level sequence instance duration in number of frames.

### SetCustomStartFrame
```angelscript
bool SetCustomStartFrame(int AttributeValue)
```
Set the frame where the level sequence instance starts.

### SetCustomTimeScale
```angelscript
bool SetCustomTimeScale(float32 AttributeValue)
```
Set the time scale used for the level sequence instance.

### SetCustomTrackSetDependencyUid
```angelscript
bool SetCustomTrackSetDependencyUid(FString AttributeValue)
```
Set the unique id of the level sequence this instance references.

