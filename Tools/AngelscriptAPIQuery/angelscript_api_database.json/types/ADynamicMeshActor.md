# ADynamicMeshActor

**继承自**: `AActor`

ADynamicMeshActor is an Actor that has a USimpleDynamicMeshComponent as it's RootObject.

## 属性

### bEnableComputeMeshPool
- **类型**: `bool`

### DynamicMeshComponent
- **类型**: `UDynamicMeshComponent`

## 方法

### AllocateComputeMesh
```angelscript
UDynamicMesh AllocateComputeMesh()
```
Request a compute mesh from the Pool, which will return a previously-allocated mesh or add and return a new one. If the Pool is disabled, a new UDynamicMesh will be allocated and returned.

### FreeAllComputeMeshes
```angelscript
void FreeAllComputeMeshes()
```
Release all compute meshes that the Pool has allocated, and then release them from the Pool, so that they will be garbage-collected

### GetComputeMeshPool
```angelscript
UDynamicMeshPool GetComputeMeshPool()
```
Access the compute mesh pool

### GetDynamicMeshComponent
```angelscript
UDynamicMeshComponent GetDynamicMeshComponent()
```

### ReleaseAllComputeMeshes
```angelscript
void ReleaseAllComputeMeshes()
```
Release all compute meshes that the Pool has allocated

### ReleaseComputeMesh
```angelscript
bool ReleaseComputeMesh(UDynamicMesh Mesh)
```
Release a compute mesh back to the Pool

