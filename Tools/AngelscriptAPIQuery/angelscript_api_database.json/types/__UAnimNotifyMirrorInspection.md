# __UAnimNotifyMirrorInspection

## 方法

### GetMirrorDataTable
```angelscript
const UMirrorDataTable GetMirrorDataTable(FAnimNotifyEventReference EventReference)
```
If the notify is mirrored, return the mirror data table that was active.

@param EventReference         The event to inspect

### IsTriggeredByMirroredAnimation
```angelscript
bool IsTriggeredByMirroredAnimation(FAnimNotifyEventReference EventReference)
```
Get whether the animation which triggered this notify was mirrored.

@param EventReference         The event to inspect

