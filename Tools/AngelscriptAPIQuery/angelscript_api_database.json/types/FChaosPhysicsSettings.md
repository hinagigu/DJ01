# FChaosPhysicsSettings

Settings container for Chaos physics engine settings, accessed in Chaos through a setting provider interface.
See: IChaosSettingsProvider

## 属性

### DefaultThreadingModel
- **类型**: `EChaosThreadingMode`
- **描述**: Default threading model to use on module initialisation. Can be switched at runtime using p.Chaos.ThreadingModel

### DedicatedThreadTickMode
- **类型**: `EChaosSolverTickMode`
- **描述**: The framerate/timestep ticking mode when running with a dedicated thread

### DedicatedThreadBufferMode
- **类型**: `EChaosBufferMode`
- **描述**: The buffering mode to use when running with a dedicated thread

## 方法

### opAssign
```angelscript
FChaosPhysicsSettings& opAssign(FChaosPhysicsSettings Other)
```

