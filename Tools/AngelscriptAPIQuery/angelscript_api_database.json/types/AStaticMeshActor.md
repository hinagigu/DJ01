# AStaticMeshActor

**继承自**: `AActor`

StaticMeshActor is an instance of a UStaticMesh in the world.
Static meshes are geometry that do not animate or otherwise deform, and are more efficient to render than other types of geometry.
Static meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.

@see https://docs.unrealengine.com/latest/INT/Engine/Actors/StaticMeshActor/
@see UStaticMesh

## 属性

### StaticMeshComponent
- **类型**: `UStaticMeshComponent`

### bStaticMeshReplicateMovement
- **类型**: `bool`
- **描述**: This static mesh should replicate movement. Automatically sets the RemoteRole and bReplicateMovement flags. Meant to be edited on placed actors (those other two properties are not)

### StaticMeshPhysicsReplicationMode
- **类型**: `EPhysicsReplicationMode`
- **描述**: Set which replication mode to use for this static mesh instance if it both replicates and simulates physics.

### NavigationGeometryGatheringMode
- **类型**: `ENavDataGatheringMode`

## 方法

### SetMobility
```angelscript
void SetMobility(EComponentMobility InMobility)
```
Function to change mobility type

