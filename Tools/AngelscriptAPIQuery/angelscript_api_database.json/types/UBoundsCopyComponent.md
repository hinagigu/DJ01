# UBoundsCopyComponent

**继承自**: `UActorComponent`

Component used to copy the bounds of another Actor.

## 属性

### BoundsSourceActor
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: Actor to copy the bounds from to set up the transform.

### bUseCollidingComponentsForSourceBounds
- **类型**: `bool`
- **描述**: If true, the source actor's bounds will include its colliding components bounds.

### bKeepOwnBoundsScale
- **类型**: `bool`
- **描述**: If true, the actor's scale will be changed so that after adjustment, its own bounds match the source bounds.

### bUseCollidingComponentsForOwnBounds
- **类型**: `bool`
- **描述**: If true, the actor's own bounds will include its colliding components bounds.

## 方法

### SetRotation
```angelscript
void SetRotation()
```
Copy the rotation from BoundsSourceActor to this component

### SetTransformToBounds
```angelscript
void SetTransformToBounds()
```
Set this component transform to include the BoundsSourceActor bounds

