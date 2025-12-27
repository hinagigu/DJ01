# UDynamicMesh

**继承自**: `UObject`

UDynamicMesh is a UObject container for a FDynamicMesh3.

## 属性

### MeshModifiedBPEvent
- **类型**: `FOnDynamicMeshModifiedBP`

### bEnableMeshGenerator
- **类型**: `bool`
- **描述**: Controls whether the active Generator (if configured) will be applied when rebuilding the mesh

## 方法

### GetTriangleCount
```angelscript
int GetTriangleCount()
```
@return number of triangles in the mesh

### IsEmpty
```angelscript
bool IsEmpty()
```
@return true if the mesh has no triangles

### Reset
```angelscript
UDynamicMesh Reset()
```
Clear the internal mesh to an empty mesh.
This *does not* allocate a new mesh, so any existing mesh pointers/refs are still valid

### ResetToCube
```angelscript
UDynamicMesh ResetToCube()
```
Clear the internal mesh to a 100x100x100 cube with base at the origin.
This this instead of Reset() if an initially-empty mesh is undesirable (eg for a Component)

