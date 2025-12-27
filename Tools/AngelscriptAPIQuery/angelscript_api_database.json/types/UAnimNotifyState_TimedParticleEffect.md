# UAnimNotifyState_TimedParticleEffect

**继承自**: `UAnimNotifyState`

Timed Particle Effect Notify
Allows a looping particle effect to be played in an animation that will activate
at the beginning of the notify and deactivate at the end.

## 属性

### PSTemplate
- **类型**: `UParticleSystem`
- **描述**: The particle system to spawn for the notify state

### SocketName
- **类型**: `FName`
- **描述**: The socket or bone to attach the system to

### LocationOffset
- **类型**: `FVector`
- **描述**: Offset from the socket or bone to place the particle system

### RotationOffset
- **类型**: `FRotator`
- **描述**: Rotation offset from the socket or bone for the particle system

### bDestroyAtEnd
- **类型**: `bool`
- **描述**: Whether the particle system should be immediately destroyed at the end of the notify state or be allowed to finish

