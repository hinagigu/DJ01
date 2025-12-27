# FBroadphaseSettings

Settings pertaining to which PhysX broadphase to use, and settings for MBP if that is the chosen broadphase type

## 属性

### bUseMBPOnClient
- **类型**: `bool`
- **描述**: Whether to use MBP (Multi Broadphase Pruning

### bUseMBPOnServer
- **类型**: `bool`

### bUseMBPOuterBounds
- **类型**: `bool`
- **描述**: Whether to have MBP grid over concentrated inner bounds with loose outer bounds

### MBPBounds
- **类型**: `FBox`
- **描述**: Total bounds for MBP, must cover the game world or collisions are disabled for out of bounds actors

### MBPOuterBounds
- **类型**: `FBox`
- **描述**: Total bounds for MBP, should cover absolute maximum bounds of the game world where physics is required

### MBPNumSubdivs
- **类型**: `uint`
- **描述**: Number of times to subdivide the MBP bounds, final number of regions is MBPNumSubdivs^2

## 方法

### opAssign
```angelscript
FBroadphaseSettings& opAssign(FBroadphaseSettings Other)
```

