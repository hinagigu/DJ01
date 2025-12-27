# UNiagaraDataChannel_Islands

**继承自**: `UNiagaraDataChannel`

Data channel that will automatically sub-divide the world into discreet "islands" based on location.

## 属性

### Mode
- **类型**: `ENiagraDataChannel_IslandMode`
- **描述**: Controls how islands are placed and sized.

### InitialExtents
- **类型**: `FVector`
- **描述**: Starting extents of the island's bounds.

### MaxExtents
- **类型**: `FVector`
- **描述**: The maximum total extents of each island. If a new element would grow the bounds beyond this size then a new island is created.

### PerElementExtents
- **类型**: `FVector`
- **描述**: The extents for every element entered into this data channel.
We use this to pad the ends of islands to ensure that all data in an island will be covered.

### Systems
- **类型**: `TArray<TSoftObjectPtr<UNiagaraSystem>>`
- **描述**: One or more Niagara Systems to spawn that will consume the data in this island.
Each island will have an instance of these systems created.
These systems are intended to consume data for this whole island and generate effects that cover the whole island.
The actual bounds of each of these system instances will be set to the current total bounds of the island.

### IslandPoolSize
- **类型**: `int`
- **描述**: How many pre-allocated islands to keep in the pool. Higher values will incur a larger standing memory cost but will reduce activation times for new islands.

### DebugDrawSettings
- **类型**: `FNDCIslandDebugDrawSettings`

