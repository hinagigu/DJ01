# FClothPhysicalMeshData

Spatial simulation data for a mesh.

## 属性

### Vertices
- **类型**: `TArray<FVector3f>`
- **描述**: Positions of each simulation vertex

### Normals
- **类型**: `TArray<FVector3f>`
- **描述**: Normal at each vertex

### VertexColors
- **类型**: `TArray<FColor>`
- **描述**: Color at each vertex

### Indices
- **类型**: `TArray<uint>`
- **描述**: Indices of the simulation mesh triangles

### InverseMasses
- **类型**: `TArray<float32>`
- **描述**: Inverse mass for each vertex in the physical mesh

### SelfCollisionVertexSet
- **类型**: `TSet<int>`
- **描述**: Valid indices to use for self collisions (reduced set of Indices)

### MaxBoneWeights
- **类型**: `int`
- **描述**: Maximum number of bone weights of any vetex

### NumFixedVerts
- **类型**: `int`
- **描述**: Number of fixed verts in the simulation mesh (fixed verts are just skinned and do not simulate)

## 方法

### opAssign
```angelscript
FClothPhysicalMeshData& opAssign(FClothPhysicalMeshData Other)
```

