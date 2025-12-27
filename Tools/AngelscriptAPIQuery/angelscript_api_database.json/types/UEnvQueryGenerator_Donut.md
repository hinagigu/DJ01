# UEnvQueryGenerator_Donut

**继承自**: `UEnvQueryGenerator_ProjectedPoints`

## 属性

### InnerRadius
- **类型**: `FAIDataProviderFloatValue`
- **描述**: min distance between point and context

### OuterRadius
- **类型**: `FAIDataProviderFloatValue`
- **描述**: max distance between point and context

### NumberOfRings
- **类型**: `FAIDataProviderIntValue`
- **描述**: number of rings to generate

### PointsPerRing
- **类型**: `FAIDataProviderIntValue`
- **描述**: number of items to generate for each ring

### ArcDirection
- **类型**: `FEnvDirection`
- **描述**: If you generate items on a piece of circle you define direction of Arc cut here

### ArcAngle
- **类型**: `FAIDataProviderFloatValue`
- **描述**: If you generate items on a piece of circle you define angle of Arc cut here

### bUseSpiralPattern
- **类型**: `bool`
- **描述**: If true, the rings of the wheel will be rotated in a spiral pattern.  If false, they will all be at a zero
rotation, looking more like the spokes on a wheel.

### Center
- **类型**: `TSubclassOf<UEnvQueryContext>`
- **描述**: context

### bDefineArc
- **类型**: `bool`

