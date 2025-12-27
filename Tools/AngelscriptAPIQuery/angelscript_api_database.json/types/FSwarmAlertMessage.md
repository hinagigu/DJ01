# FSwarmAlertMessage

## 属性

### JobGuid
- **类型**: `FGuid`
- **描述**: The Job Guid

### AlertLevel
- **类型**: `uint8`
- **描述**: The type of alert

### ObjectGuid
- **类型**: `FGuid`
- **描述**: The identifier for the object that is associated with the issue

### TypeId
- **类型**: `int`
- **描述**: App-specific identifier for the type of the object

### TextMessage
- **类型**: `FString`
- **描述**: Generic text message for informational purposes

## 方法

### opAssign
```angelscript
FSwarmAlertMessage& opAssign(FSwarmAlertMessage Other)
```

