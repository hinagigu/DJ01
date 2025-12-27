# UGameNetworkManagerSettings

**继承自**: `UObject`

Holds the settings for the AGameNetworkManager class.

## 属性

### MinDynamicBandwidth
- **类型**: `int`
- **描述**: Minimum bandwidth dynamically set per connection.

### MaxDynamicBandwidth
- **类型**: `int`
- **描述**: Maximum bandwidth dynamically set per connection.

### TotalNetBandwidth
- **类型**: `int`
- **描述**: Total available bandwidth for listen server, split dynamically across net connections.

### BadPingThreshold
- **类型**: `int`
- **描述**: The point we determine the server is either delaying packets or has bad upstream.

### StandbyRxCheatTime
- **类型**: `float32`
- **描述**: The amount of time without packets before triggering the cheat code.

### StandbyTxCheatTime
- **类型**: `float32`
- **描述**: The amount of time without packets before triggering the cheat code.

### PercentMissingForRxStandby
- **类型**: `float32`
- **描述**: The percentage of clients missing RX data before triggering the standby code.

### PercentMissingForTxStandby
- **类型**: `float32`
- **描述**: The percentage of clients missing TX data before triggering the standby code.

### PercentForBadPing
- **类型**: `float32`
- **描述**: The percentage of clients with bad ping before triggering the standby code.

### JoinInProgressStandbyWaitTime
- **类型**: `float32`
- **描述**: The amount of time to wait before checking a connection for standby issues.

### bIsStandbyCheckingEnabled
- **类型**: `bool`

