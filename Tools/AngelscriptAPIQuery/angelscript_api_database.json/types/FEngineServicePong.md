# FEngineServicePong

Implements a message for responding to a request to discover engine instances on the network.

## 属性

### CurrentLevel
- **类型**: `FString`
- **描述**: Holds the name of the currently loaded level, if any.

### EngineVersion
- **类型**: `int`
- **描述**: Holds the engine version.

### HasBegunPlay
- **类型**: `bool`
- **描述**: Holds a flag indicating whether game play has begun.

### InstanceId
- **类型**: `FGuid`
- **描述**: Holds the instance identifier.

### InstanceType
- **类型**: `FString`
- **描述**: Holds the type of the engine instance.

### SessionId
- **类型**: `FGuid`
- **描述**: Holds the identifier of the session that the application belongs to.

### WorldTimeSeconds
- **类型**: `float32`
- **描述**: Holds the time in seconds since the world was loaded.

## 方法

### opAssign
```angelscript
FEngineServicePong& opAssign(FEngineServicePong Other)
```

