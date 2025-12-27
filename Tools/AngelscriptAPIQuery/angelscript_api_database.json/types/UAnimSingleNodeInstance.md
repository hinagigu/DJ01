# UAnimSingleNodeInstance

**继承自**: `UAnimInstance`

## 方法

### GetAnimationAsset
```angelscript
UAnimationAsset GetAnimationAsset()
```
Get the currently used asset

### GetLength
```angelscript
float32 GetLength()
```

### GetMirrorDataTable
```angelscript
const UMirrorDataTable GetMirrorDataTable()
```

### PlayAnim
```angelscript
void PlayAnim(bool bIsLooping, float32 InPlayRate, float32 InStartPosition)
```
For AnimSequence specific *

### SetAnimationAsset
```angelscript
void SetAnimationAsset(UAnimationAsset NewAsset, bool bIsLooping, float32 InPlayRate)
```
Set New Asset - calls InitializeAnimation, for now we need MeshComponent *

### SetBlendSpacePosition
```angelscript
void SetBlendSpacePosition(FVector InPosition)
```

### SetLooping
```angelscript
void SetLooping(bool bIsLooping)
```

### SetMirrorDataTable
```angelscript
void SetMirrorDataTable(const UMirrorDataTable MirrorDataTable)
```

### SetPlaying
```angelscript
void SetPlaying(bool bIsPlaying)
```

### SetPlayRate
```angelscript
void SetPlayRate(float32 InPlayRate)
```

### SetPosition
```angelscript
void SetPosition(float32 InPosition, bool bFireNotifies)
```

### SetPositionWithPreviousTime
```angelscript
void SetPositionWithPreviousTime(float32 InPosition, float32 InPreviousTime, bool bFireNotifies)
```

### SetPreviewCurveOverride
```angelscript
void SetPreviewCurveOverride(FName PoseName, float32 Value, bool bRemoveIfZero)
```
Set pose value

### SetReverse
```angelscript
void SetReverse(bool bInReverse)
```

### StopAnim
```angelscript
void StopAnim()
```

