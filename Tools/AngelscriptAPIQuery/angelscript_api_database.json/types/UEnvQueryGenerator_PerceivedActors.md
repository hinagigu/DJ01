# UEnvQueryGenerator_PerceivedActors

**继承自**: `UEnvQueryGenerator`

Gathers actors perceived by context

## 属性

### AllowedActorClass
- **类型**: `TSubclassOf<AActor>`
- **描述**: If set will be used to filter results

### SearchRadius
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Additional distance limit imposed on the items generated. Perception's range limit still applies.

### ListenerContext
- **类型**: `TSubclassOf<UEnvQueryContext>`
- **描述**: The perception listener to use as a source of information

### SenseToUse
- **类型**: `TSubclassOf<UAISense>`
- **描述**: If set will be used to filter gathered results so that only actors perceived with a given sense are considered

### bIncludeKnownActors
- **类型**: `bool`
- **描述**: Indicates whether to include all actors known via perception (TRUE) or just the ones actively being perceived
at the moment (example "currently visible" as opposed to "seen and the perception stimulus haven't expired yet").
@see FAIStimulus.bExpired

