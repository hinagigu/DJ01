# UClusterUnionComponent

**继承自**: `UPrimitiveComponent`

This does the bulk of the work exposing a physics cluster union to the game thread.
This component needs to be a primitive component primarily because of how physics
proxies need to be registered with the solver with an association with a primitive component.
This component can be used as part of AClusterUnionActor or on its own as its list of
clustered components/actors can be specified dynamically at runtime and/or statically
on asset creation.

The cluster union component needs to not only maintain a game thread representation of what's happening on the
physics thread but it also needs to make sure this data gets replicated to every client. A general model of how
the data flow happens is as follows:

 [Server GT Command] -> [Server PT Command] -> [Server Modifies PT Data] -> [Server Sync PT Data back to GT Data].

This enables GT control over what happens to the cluster union BUT ALSO maintains a physics-first approach
to the cluster union where a physics event can possibly cause the cluster union to break.

The GT data is replicated from the server to the clients either via the FClusterUnionReplicatedData on the cluster union component
or per-child component data is replicated via the UClusterUnionReplicatedProxyComponent. Generally, the same flow is
replicated on the client. The only exception is for replicating the X/R/V/W properties on the cluster union particle which does
a GT -> PT data sync. There's no particula reason this happens...it just mirrors the single particle physics proxy here.

## 属性

### OnComponentAddedEvent
- **类型**: `FOnClusterUnionAddedComponent`

### OnComponentRemovedEvent
- **类型**: `FOnClusterUnionRemovedComponent`

### OnComponentBoundsChangedEvent
- **类型**: `FOnClusterUnionBoundsChanged`

### ClusteredComponentsReferences
- **类型**: `TArray<FComponentReference>`
- **描述**: These are the statically clustered components. These should
be specified in the editor and never change.

### GravityGroupIndexOverride
- **类型**: `int`
- **描述**: If set to a value not equal to -1, will manually set the cluster union's gravity group
instead of automatically inheriting it from its children particles.

### bEnableDamageFromCollision
- **类型**: `bool`

## 方法

### AddComponentToCluster
```angelscript
void AddComponentToCluster(UPrimitiveComponent InComponent, TArray<int> BoneIds, bool bRebuildGeometry)
```

### GetActors
```angelscript
TArray<AActor> GetActors()
```

### GetPrimitiveComponents
```angelscript
TArray<UPrimitiveComponent> GetPrimitiveComponents()
```

### RemoveComponentBonesFromCluster
```angelscript
void RemoveComponentBonesFromCluster(UPrimitiveComponent InComponent, TArray<int> BoneIds)
```

### RemoveComponentFromCluster
```angelscript
void RemoveComponentFromCluster(UPrimitiveComponent InComponent)
```

### SetEnableDamageFromCollision
```angelscript
void SetEnableDamageFromCollision(bool bValue)
```

### SetIsAnchored
```angelscript
void SetIsAnchored(bool bIsAnchored)
```

