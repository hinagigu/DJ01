# UAsyncPhysicsInputComponent

**继承自**: `UActorComponent`

## 方法

### GetDataToConsume
```angelscript
const UAsyncPhysicsData GetDataToConsume()
```
Get the async physics data to execute logic off of. This data should not be modified and will NOT make its way back. Should be called from async tick

### GetDataToWrite
```angelscript
UAsyncPhysicsData GetDataToWrite()
```
Get the async physics data to write to. This data will make its way to the async physics tick on client and server. Should not be called from async tick

### ServerRPCBufferInput
```angelscript
void ServerRPCBufferInput(UAsyncPhysicsData AsyncPhysicsData)
```

