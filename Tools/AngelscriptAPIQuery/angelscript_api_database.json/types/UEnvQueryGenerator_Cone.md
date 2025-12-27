# UEnvQueryGenerator_Cone

**继承自**: `UEnvQueryGenerator_ProjectedPoints`

## 属性

### AlignedPointsDistance
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Distance between each point of the same angle

### ConeDegrees
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Maximum degrees of the generated cone

### AngleStep
- **类型**: `FAIDataProviderFloatValue`
- **描述**: The step of the angle increase. Angle step must be >=1
Smaller values generate less items

### Range
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Generation distance

### CenterActor
- **类型**: `TSubclassOf<UEnvQueryContext>`
- **描述**: The actor (or actors) that will generate a cone in their facing direction

### bIncludeContextLocation
- **类型**: `bool`

