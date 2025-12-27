# UNiagaraDataInterfaceRigidMeshCollisionQuery

**继承自**: `UNiagaraDataInterface`

Data Interface used to collide against static meshes - whether it is the mesh distance field or a physics asset's collision primitive

## 属性

### ActorTags
- **类型**: `TArray<FName>`
- **描述**: Set of tags used to match against actors when searching for RigidBody providers.  Empty tags will be ignored, and only a single
              tag is required for an actor to be matched.

### ComponentTags
- **类型**: `TArray<FName>`
- **描述**: Set of tags used to match against components when searching for RigidBody providers.  Empty tags will be ignored, and only a
              single tag is required for a component to be matched.

### SourceActors
- **类型**: `TArray<TSoftObjectPtr<AActor>>`
- **描述**: Hardcoded references to actors that will be used as RigidBody providers.

### OnlyUseMoveable
- **类型**: `bool`
- **描述**: If enabled only actors that are considered moveable will be searched for RigidBodies.

### UseComplexCollisions
- **类型**: `bool`
- **描述**: If enabled, complex collisions will be searched for.

### bFilterByObjectType
- **类型**: `bool`
- **描述**: If enabled, FindActors will use filtering based on ObjectType instead of Channel.

### GlobalSearchAllowed
- **类型**: `bool`

### GlobalSearchForced
- **类型**: `bool`

### GlobalSearchFallback_Unscripted
- **类型**: `bool`

### MaxNumPrimitives
- **类型**: `int`
- **描述**: Maximum number of RigidBody represented by this DataInterface.

