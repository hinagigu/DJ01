# UAnimationModifier

**继承自**: `UObject`

## 属性

### bReapplyPostOwnerChange
- **类型**: `bool`
- **描述**: If this is set to true then the animation modifier will call it's reapply function after any change made to the owning asset.

## 方法

### OnApply
```angelscript
void OnApply(UAnimSequence AnimationSequence)
```
Executed when the Animation is initialized (native event for debugging / testing purposes)

### OnRevert
```angelscript
void OnRevert(UAnimSequence AnimationSequence)
```

