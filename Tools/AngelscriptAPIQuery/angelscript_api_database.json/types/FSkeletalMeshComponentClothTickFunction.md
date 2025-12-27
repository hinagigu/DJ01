# FSkeletalMeshComponentClothTickFunction

Tick function that prepares and simulates cloth

## 属性

### TickGroup
- **类型**: `ETickingGroup`
- **描述**: Defines the minimum tick group for this tick function. These groups determine the relative order of when objects tick during a frame update.
Given prerequisites, the tick may be delayed.

@see ETickingGroup
@see FTickFunction::AddPrerequisite()

### EndTickGroup
- **类型**: `ETickingGroup`
- **描述**: Defines the tick group that this tick function must finish in. These groups determine the relative order of when objects tick during a frame update.

@see ETickingGroup

### TickInterval
- **类型**: `float32`
- **描述**: The frequency in seconds at which this tick function will be executed.  If less than or equal to 0 then it will tick every frame

### bTickEvenWhenPaused
- **类型**: `bool`

### bStartWithTickEnabled
- **类型**: `bool`

### bAllowTickOnDedicatedServer
- **类型**: `bool`

