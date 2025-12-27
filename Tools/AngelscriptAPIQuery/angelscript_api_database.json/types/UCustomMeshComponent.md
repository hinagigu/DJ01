# UCustomMeshComponent

**继承自**: `UMeshComponent`

Component that allows you to specify custom triangle mesh geometry

## 方法

### AddCustomMeshTriangles
```angelscript
void AddCustomMeshTriangles(TArray<FCustomMeshTriangle> Triangles)
```
Add to the geometry to use on this triangle mesh.  This may cause an allocation.  Use SetCustomMeshTriangles() instead when possible to reduce allocations.

### ClearCustomMeshTriangles
```angelscript
void ClearCustomMeshTriangles()
```
Removes all geometry from this triangle mesh.  Does not deallocate memory, allowing new geometry to reuse the existing allocation.

### SetCustomMeshTriangles
```angelscript
bool SetCustomMeshTriangles(TArray<FCustomMeshTriangle> Triangles)
```
Set the geometry to use on this triangle mesh

