# __SkeletalControl

## 方法

### ConvertToSkeletalControl
```angelscript
FSkeletalControlReference ConvertToSkeletalControl(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a skeletal control from an anim node

### ConvertToSkeletalControlPure
```angelscript
void ConvertToSkeletalControlPure(FAnimNodeReference Node, FSkeletalControlReference& SkeletalControl, bool& Result)
```
Get a skeletal control from an anim node (pure)

### GetAlpha
```angelscript
float32 GetAlpha(FSkeletalControlReference SkeletalControl)
```
Get the alpha value of this skeletal control

### SetAlpha
```angelscript
FSkeletalControlReference SetAlpha(FSkeletalControlReference SkeletalControl, float32 Alpha)
```
Set the alpha value of this skeletal control

