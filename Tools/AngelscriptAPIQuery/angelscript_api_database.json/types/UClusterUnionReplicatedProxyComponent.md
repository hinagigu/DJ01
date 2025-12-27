# UClusterUnionReplicatedProxyComponent

**继承自**: `UActorComponent`

This component lets us store replicated information about how any particular UPrimitiveComponent
should be attached to its parent cluster union. The benefits of using a separate components are:

    1) It lets us avoid adding any additional overhead into the UPrimitiveComponent.
 2) It lets the replicated information have the same net relevancy as the actor being added to the cluster union
    rather than having the same net relevancy as the cluster union (i.e. in the case of replicating this data in
    an array in the ClusterUnionComponent).
 3) It lets us pinpoint what exactly is being added/removed (vs if all this data was stored in an array) which lets
    us be a bit more efficient in terms of modifying the cluster union.

