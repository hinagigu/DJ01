# ACameraActor

**继承自**: `AActor`

A CameraActor is a camera viewpoint that can be placed in a level.

## 属性

### AutoActivateForPlayer
- **类型**: `EAutoReceiveInput`
- **描述**: Specifies which player controller, if any, should automatically use this Camera when the controller is active.

### CameraComponent
- **类型**: `UCameraComponent`

### SceneComponent
- **类型**: `USceneComponent`

## 方法

### GetAutoActivatePlayerIndex
```angelscript
int GetAutoActivatePlayerIndex()
```
Returns index of the player for whom we auto-activate, or INDEX_NONE (-1) if disabled.

