# __UAnimNotify

## 方法

### GetCurrentAnimationNotifyStateTime
```angelscript
float32 GetCurrentAnimationNotifyStateTime(FAnimNotifyEventReference EventReference)
```
Gets the current time in seconds relative to the start of the notify state, clamped to the range of the notify
state

@param EventReference                The event to inspect
@return  the current time in seconds relative to the start of the notify state, clamped to the range of the
                     notify state

### GetCurrentAnimationNotifyStateTimeRatio
```angelscript
float32 GetCurrentAnimationNotifyStateTimeRatio(FAnimNotifyEventReference EventReference)
```
Gets the current time as a ratio (0 -> 1) relative to the start of the notify state

@param EventReference                The event to inspect
@return  the current time as a ratio (0 -> 1) relative to the start of the notify state

### GetCurrentAnimationTime
```angelscript
float32 GetCurrentAnimationTime(FAnimNotifyEventReference EventReference)
```
Get the current anim notify time in seconds for when this notify was fired

@param EventReference                The event to inspect
@return the time in seconds through the current animation for when this notify was fired

### GetCurrentAnimationTimeRatio
```angelscript
float32 GetCurrentAnimationTimeRatio(FAnimNotifyEventReference EventReference)
```
Get the current anim notify time as a ratio (0 -> 1) through the animation for when this notify was fired

@param EventReference                The event to inspect
@return the time as a ratio (0 -> 1) through the animation for when this notify was fired

### NotifyStateReachedEnd
```angelscript
bool NotifyStateReachedEnd(FAnimNotifyEventReference EventReference)
```
Get whether the notify state reached the end (was not cancelled)

@param EventReference         The event to inspect

### StaticClass
```angelscript
UClass StaticClass()
```

