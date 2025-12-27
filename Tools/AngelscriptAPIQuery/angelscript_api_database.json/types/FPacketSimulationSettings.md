# FPacketSimulationSettings

Holds the packet simulation settings in one place

## 属性

### PktLoss
- **类型**: `int`
- **描述**: When set, will cause calls to FlushNet to drop packets.
Value is treated as % of packets dropped (i.e. 0 = None, 100 = All).
No general pattern / ordering is guaranteed.
Clamped between 0 and 100.

Works with all other settings.

### PktLossMaxSize
- **类型**: `int`
- **描述**: Sets the maximum size of packets in bytes that will be dropped
according to the PktLoss setting. Default is INT_MAX.

Works with all other settings.

### PktLossMinSize
- **类型**: `int`
- **描述**: Sets the minimum size of packets in bytes that will be dropped
according to the PktLoss setting. Default is 0.

Works with all other settings.

### PktOrder
- **类型**: `int`
- **描述**: When set, will cause calls to FlushNet to change ordering of packets at random.
Value is treated as a bool (i.e. 0 = False, anything else = True).
This works by randomly selecting packets to be delayed until a subsequent call to FlushNet.

Takes precedence over PktDup and PktLag.

### PktDup
- **类型**: `int`
- **描述**: When set, will cause calls to FlushNet to duplicate packets.
Value is treated as % of packets duplicated (i.e. 0 = None, 100 = All).
No general pattern / ordering is guaranteed.
Clamped between 0 and 100.

Cannot be used with PktOrder or PktLag.

### PktLag
- **类型**: `int`
- **描述**: When set, will cause calls to FlushNet to delay packets.
Value is treated as millisecond lag.

Cannot be used with PktOrder.

### PktLagVariance
- **类型**: `int`
- **描述**: When set, will cause PktLag to use variable lag instead of constant.
Value is treated as millisecond lag range (e.g. -GivenVariance <= 0 <= GivenVariance).

Can only be used when PktLag is enabled.

### PktLagMin
- **类型**: `int`
- **描述**: If set lag values will randomly fluctuate between Min and Max.
Ignored if PktLag value is set

### PktLagMax
- **类型**: `int`

### PktIncomingLagMin
- **类型**: `int`
- **描述**: Set a value to add a minimum delay in milliseconds to incoming
packets before they are processed.

### PktIncomingLagMax
- **类型**: `int`
- **描述**: The maximum delay in milliseconds to add to incoming
packets before they are processed.

### PktIncomingLoss
- **类型**: `int`
- **描述**: The ratio of incoming packets that will be dropped
to simulate packet loss

### PktJitter
- **类型**: `int`
- **描述**: Causes sent packets to have a variable latency that fluctuates from [PktLagMin] to [PktLagMin+PktJitter]
Note that this will cause packet loss on the receiving end.

## 方法

### opAssign
```angelscript
FPacketSimulationSettings& opAssign(FPacketSimulationSettings Other)
```

