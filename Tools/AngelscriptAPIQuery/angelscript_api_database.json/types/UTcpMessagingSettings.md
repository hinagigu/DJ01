# UTcpMessagingSettings

**继承自**: `UObject`

## 属性

### EnableTransport
- **类型**: `bool`
- **描述**: Whether the TCP transport channel is enabled

### ListenEndpoint
- **类型**: `FString`
- **描述**: The IP endpoint to listen for incoming connections.

The format is IP_ADDRESS:PORT_NUMBER or blank to disable listening.

### ConnectToEndpoints
- **类型**: `TArray<FString>`
- **描述**: The IP endpoints to try to establish outgoing connection to.

Use this setting to connect to a remote peer.
The format is IP_ADDRESS:PORT_NUMBER.

### ConnectionRetryDelay
- **类型**: `int`
- **描述**: Delay time between attempts to re-establish outgoing connections that become disconnected or fail to connect
0 disables reconnection

### ConnectionRetryPeriod
- **类型**: `int`
- **描述**: Period time during which attempts to re-establish outgoing connections that become disconnected or fail to connect
0 means it will be retried only once

