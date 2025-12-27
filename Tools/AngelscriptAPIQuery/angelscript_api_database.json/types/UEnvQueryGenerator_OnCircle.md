# UEnvQueryGenerator_OnCircle

**继承自**: `UEnvQueryGenerator_ProjectedPoints`

## 属性

### CircleRadius
- **类型**: `FAIDataProviderFloatValue`
- **描述**: max distance of path between point and context

### PointOnCircleSpacingMethod
- **类型**: `EPointOnCircleSpacingMethod`
- **描述**: how we are choosing where the points are in the circle

### SpaceBetween
- **类型**: `FAIDataProviderFloatValue`
- **描述**: items will be generated on a circle this much apart

### NumberOfPoints
- **类型**: `FAIDataProviderIntValue`
- **描述**: this many items will be generated on a circle

### ArcDirection
- **类型**: `FEnvDirection`
- **描述**: If you generate items on a piece of circle you define direction of Arc cut here

### ArcAngle
- **类型**: `FAIDataProviderFloatValue`
- **描述**: If you generate items on a piece of circle you define angle of Arc cut here

### CircleCenter
- **类型**: `TSubclassOf<UEnvQueryContext>`
- **描述**: context

### bIgnoreAnyContextActorsWhenGeneratingCircle
- **类型**: `bool`
- **描述**: ignore tracing into context actors when generating the circle

### CircleCenterZOffset
- **类型**: `FAIDataProviderFloatValue`
- **描述**: context offset

### TraceData
- **类型**: `FEnvTraceData`
- **描述**: horizontal trace for nearest obstacle

### bDefineArc
- **类型**: `bool`

