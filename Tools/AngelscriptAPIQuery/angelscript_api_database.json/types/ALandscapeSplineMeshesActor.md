# ALandscapeSplineMeshesActor

**继承自**: `APartitionActor`

This class is only intended to be used by UWorldPartitionLandscapeSplineMeshesBuilder which extracts and clones
landscape spline and control point static meshes into partitioned actors

This serves as an optimization as these actors will be streamed at runtime

## 属性

### StaticMeshComponents
- **类型**: `TArray<TObjectPtr<UStaticMeshComponent>>`

