# UFractureRemoveOnBreakSettings

**继承自**: `UFractureToolSettings`

## 属性

### Enabled
- **类型**: `bool`
- **描述**: whether or not the remove on fracture is enabled

### PostBreakTimer
- **类型**: `FVector2f`
- **描述**: Min/Max time after break before removal starts

### ClusterCrumbling
- **类型**: `bool`
- **描述**: When set, clusters will crumble when post break timer expires, non clusters will simply use the removal timer

### RemovalTimer
- **类型**: `FVector2f`
- **描述**: Min/Max time for how long removal lasts - not applicable when cluster crumbling is on

