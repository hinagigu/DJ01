# UInterchangeAnimationTrackBaseNode

**继承自**: `UInterchangeBaseNode`

Abstract class providing the minimal services required for an animation track node.

## 方法

### GetCustomCompletionMode
```angelscript
bool GetCustomCompletionMode(int& AttributeValue)
```
Get how the actor's animated property behaves once this animation is complete.
The output value will be clamped to the range of values defined in EInterchangeAimationCompletionMode.

### SetCustomCompletionMode
```angelscript
bool SetCustomCompletionMode(int AttributeValue)
```
Set how the actor's animated property should behave once its animation completes.

