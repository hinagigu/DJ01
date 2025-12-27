# AOnlineBeaconClient

**继承自**: `AOnlineBeacon`

Base class for any unique beacon connectivity, paired with an AOnlineBeaconHostObject implementation

This is the actual actor that replicates across client/server and where all RPCs occur
On the host, the life cycle is managed by an AOnlineBeaconHostObject
On the client, the life cycle is managed by the game

## 方法

### ClientOnConnected
```angelscript
void ClientOnConnected()
```
Called on the server side to open up the actor channel that will allow RPCs to occur
(DO NOT OVERLOAD, implement OnConnected() instead)

