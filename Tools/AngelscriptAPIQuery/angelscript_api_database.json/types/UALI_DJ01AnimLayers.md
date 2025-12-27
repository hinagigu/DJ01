# UALI_DJ01AnimLayers

**继承自**: `UInterface`

## 方法

### FullBody_FallLoopState
```angelscript
FPoseLink FullBody_FallLoopState()
```

### FullBody_IdleState
```angelscript
FPoseLink FullBody_IdleState()
```
全身移动层 - Idle/Walk/Run 的主要混合逻辑
主动画蓝图在状态机中调用此层

### FullBody_JumpStartState
```angelscript
FPoseLink FullBody_JumpStartState()
```

### FullBody_LandState
```angelscript
FPoseLink FullBody_LandState()
```

### FullBody_MovingState
```angelscript
FPoseLink FullBody_MovingState()
```

### UpperBody_Overlay
```angelscript
FPoseLink UpperBody_Overlay()
```
上身攻击覆盖 - 在移动时只覆盖上半身
用于轻攻击等可边走边打的动作

