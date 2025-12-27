# UOctreeDynamicMeshComponent

**继承自**: `UBaseDynamicMeshComponent`

UOctreeDynamicMeshComponent is a mesh component similar to UProceduralMeshComponent,
except it bases the renderable geometry off an internal FDynamicMesh3 instance.
The class generally has the same capabilities as UDynamicMeshComponent.

A FDynamicMeshOctree3 is available to dynamically track the triangles of the mesh
(however the client is responsible for updating this octree).
Based on the Octree, the mesh is partitioned into chunks that are stored in separate
RenderBuffers in the FOctreeDynamicMeshSceneProxy.
Calling NotifyMeshUpdated() will result in only the "dirty" chunks being updated,
rather than the entire mesh.

(So, if you don't need this capability, and don't want to update an Octree, use UDynamicMeshComponent!)

## 方法

### SetDynamicMesh
```angelscript
void SetDynamicMesh(UDynamicMesh NewMesh)
```

