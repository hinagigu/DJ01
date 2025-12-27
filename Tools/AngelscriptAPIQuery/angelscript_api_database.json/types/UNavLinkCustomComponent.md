# UNavLinkCustomComponent

**继承自**: `UNavRelevantComponent`

Encapsulates NavLinkCustomInterface interface, can be used with Actors not relevant for navigation

Additional functionality:
- can be toggled
- can create obstacle area for easier/forced separation of link end points
- can broadcast state changes to nearby agents

## 属性

### EnabledAreaClass
- **类型**: `TSubclassOf<UNavArea>`
- **描述**: area class to use when link is enabled

### DisabledAreaClass
- **类型**: `TSubclassOf<UNavArea>`
- **描述**: area class to use when link is disabled

### SupportedAgents
- **类型**: `FNavAgentSelector`
- **描述**: restrict area only to specified agents

### LinkRelativeStart
- **类型**: `FVector`
- **描述**: start point, relative to owner

### LinkRelativeEnd
- **类型**: `FVector`
- **描述**: end point, relative to owner

### LinkDirection
- **类型**: `ENavLinkDirection`
- **描述**: direction of link

### ObstacleOffset
- **类型**: `FVector`
- **描述**: offset of simple box obstacle

### ObstacleExtent
- **类型**: `FVector`
- **描述**: extent of simple box obstacle

### ObstacleAreaClass
- **类型**: `TSubclassOf<UNavArea>`
- **描述**: area class for simple box obstacle

### BroadcastRadius
- **类型**: `float32`
- **描述**: radius of state change broadcast

### BroadcastInterval
- **类型**: `float32`
- **描述**: interval for state change broadcast (0 = single broadcast)

### BroadcastChannel
- **类型**: `ECollisionChannel`
- **描述**: trace channel for state change broadcast

### bLinkEnabled
- **类型**: `bool`

### bNotifyWhenEnabled
- **类型**: `bool`

### bNotifyWhenDisabled
- **类型**: `bool`

### bCreateBoxObstacle
- **类型**: `bool`

