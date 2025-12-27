# FLevelEditorPlayNetworkEmulationSettings

## 属性

### bIsNetworkEmulationEnabled
- **类型**: `bool`
- **描述**: When true will apply the emulation settings when launching the game

### EmulationTarget
- **类型**: `NetworkEmulationTarget`

### CurrentProfile
- **类型**: `FString`
- **描述**: The profile name of the settings currently applied

### OutPackets
- **类型**: `FNetworkEmulationPacketSettings`
- **描述**: Settings that add latency and packet loss to all outgoing packets

### InPackets
- **类型**: `FNetworkEmulationPacketSettings`
- **描述**: Settings that add latency and packet loss to all incoming packets

## 方法

### opAssign
```angelscript
FLevelEditorPlayNetworkEmulationSettings& opAssign(FLevelEditorPlayNetworkEmulationSettings Other)
```

