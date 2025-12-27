# UMockDataMeshTrackerComponent

**继承自**: `USceneComponent`

The MeshTrackerComponent class manages requests for environmental mesh data, processes the results and provides
them to the calling system. The calling system is able request environmental mesh data within a specified area.
Various other search criteria can be set via this class's public properties.  Mesh data requests are processed
on a separate thread.  Once a mesh data request has been processed the calling system will be notified via an
FOnMeshTrackerUpdated broadcast.

## 属性

### OnMeshTrackerUpdated
- **类型**: `FOnMockDataMeshTrackerUpdated__MockDataMeshTrackerComponent`

### ScanWorld
- **类型**: `bool`

### RequestNormals
- **类型**: `bool`

### RequestVertexConfidence
- **类型**: `bool`

### VertexColorMode
- **类型**: `EMeshTrackerVertexColorMode`

### BlockVertexColors
- **类型**: `TArray<FColor>`

### VertexColorFromConfidenceZero
- **类型**: `FLinearColor`

### VertexColorFromConfidenceOne
- **类型**: `FLinearColor`

### UpdateInterval
- **类型**: `float32`

## 方法

### ConnectMRMesh
```angelscript
void ConnectMRMesh(UMRMeshComponent InMRMeshPtr)
```
Sets the procedural mesh component that will store and display the environmental mesh results.
@param InMRMeshPtr The procedural mesh component to store the query result in.

### DisconnectMRMesh
```angelscript
void DisconnectMRMesh(UMRMeshComponent InMRMeshPtr)
```
Unlinks the current procedural mesh component from the mesh tracking system.
@param InMRMeshPtr The procedural mesh component to unlink from the mesh tracking system.

