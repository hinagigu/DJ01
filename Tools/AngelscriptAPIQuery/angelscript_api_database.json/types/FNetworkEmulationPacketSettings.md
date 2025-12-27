# FNetworkEmulationPacketSettings

## 属性

### MinLatency
- **类型**: `int`
- **描述**: Minimum latency to add to packets

### MaxLatency
- **类型**: `int`
- **描述**: Maximum latency to add to packets. We use a random value between the minimum and maximum (when 0 = always the minimum value)

### PacketLossPercentage
- **类型**: `int`
- **描述**: Ratio of packets to randomly drop (0 = none, 100 = all)

## 方法

### opAssign
```angelscript
FNetworkEmulationPacketSettings& opAssign(FNetworkEmulationPacketSettings Other)
```

