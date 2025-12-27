# FFileServerReady

Implements a message that is published by file servers when they're ready to accept connections.

## 属性

### AddressList
- **类型**: `TArray<FString>`
- **描述**: Holds the list of IP addresses that the file server is listening on.

### InstanceId
- **类型**: `FGuid`
- **描述**: Holds the file server's application identifier.

## 方法

### opAssign
```angelscript
FFileServerReady& opAssign(FFileServerReady Other)
```

