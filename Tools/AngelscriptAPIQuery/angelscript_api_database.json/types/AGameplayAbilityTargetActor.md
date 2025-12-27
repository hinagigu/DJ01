# AGameplayAbilityTargetActor

**继承自**: `AActor`

TargetActors are spawned to assist with ability targeting. They are spawned by ability tasks and create/determine the outgoing targeting data passed from one task to another

WARNING: These actors are spawned once per ability activation and in their default form are not very efficient
For most games you will need to subclass and heavily modify this actor, or you will want to implement similar functions in a game-specific actor or blueprint to avoid actor spawn costs
This class is not well tested by internal games, but it is a useful class to look at to learn how target replication occurs

## 属性

### ShouldProduceTargetDataOnServer
- **类型**: `bool`
- **描述**: The TargetData this class produces can be entirely generated on the server. We don't require the client to send us full or partial TargetData (possibly just a 'confirm')

### StartLocation
- **类型**: `FGameplayAbilityTargetingLocationInfo`
- **描述**: Describes where the targeting action starts, usually the player character or a socket on the player character. //UPROPERTY(BlueprintReadOnly, meta=(ExposeOnSpawn=true), Category=Targeting)

### PrimaryPC
- **类型**: `APlayerController`

### bDestroyOnConfirmation
- **类型**: `bool`

### SourceActor
- **类型**: `AActor`

### ReticleParams
- **类型**: `FWorldReticleParameters`
- **描述**: Parameters for world reticle. Usage of these parameters is dependent on the reticle.

### ReticleClass
- **类型**: `TSubclassOf<AGameplayAbilityWorldReticle>`

### Filter
- **类型**: `FGameplayTargetDataFilterHandle`
- **描述**: Using a special class for replication purposes.

### bDebug
- **类型**: `bool`

