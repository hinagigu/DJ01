# UEnvQueryGenerator_ActorsOfClass

**继承自**: `UEnvQueryGenerator`

## 属性

### SearchedActorClass
- **类型**: `TSubclassOf<AActor>`

### GenerateOnlyActorsInRadius
- **类型**: `FAIDataProviderBoolValue`
- **描述**: If true, this will only returns actors of the specified class within the SearchRadius of the SearchCenter context.  If false, it will return ALL actors of the specified class in the world.

### SearchRadius
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Max distance of path between point and context.  NOTE: Zero and negative values will never return any results if
UseRadius is true.  "Within" requires Distance < Radius.  Actors ON the circle (Distance == Radius) are excluded.

### SearchCenter
- **类型**: `TSubclassOf<UEnvQueryContext>`
- **描述**: context

