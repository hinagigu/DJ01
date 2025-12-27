# UCrowdManager

**继承自**: `UCrowdManagerBase`

## 属性

### AvoidanceConfig
- **类型**: `TArray<FCrowdAvoidanceConfig>`
- **描述**: obstacle avoidance params

### SamplingPatterns
- **类型**: `TArray<FCrowdAvoidanceSamplingPattern>`
- **描述**: obstacle avoidance params

### MaxAgents
- **类型**: `int`
- **描述**: max number of agents supported by crowd

### MaxAgentRadius
- **类型**: `float32`
- **描述**: max radius of agent that can be added to crowd

### MaxAvoidedAgents
- **类型**: `int`
- **描述**: max number of neighbor agents for velocity avoidance

### MaxAvoidedWalls
- **类型**: `int`
- **描述**: max number of wall segments for velocity avoidance

### NavmeshCheckInterval
- **类型**: `float32`
- **描述**: how often should agents check their position after moving off navmesh?

### PathOptimizationInterval
- **类型**: `float32`
- **描述**: how often should agents try to optimize their paths?

### SeparationDirClamp
- **类型**: `float32`
- **描述**: clamp separation force to left/right when neighbor is behind (dot between forward and dirToNei, -1 = disabled)

### PathOffsetRadiusMultiplier
- **类型**: `float32`
- **描述**: agent radius multiplier for offsetting path around corners

### bResolveCollisions
- **类型**: `bool`

