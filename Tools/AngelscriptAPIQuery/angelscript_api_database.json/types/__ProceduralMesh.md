# __ProceduralMesh

## 方法

### CalculateTangentsForMesh
```angelscript
void CalculateTangentsForMesh(TArray<FVector> Vertices, TArray<int> Triangles, TArray<FVector2D> UVs, TArray<FVector>& Normals, TArray<FProcMeshTangent>& Tangents)
```
Automatically generate normals and tangent vectors for a mesh
UVs are required for correct tangent generation.

### ConvertQuadToTriangles
```angelscript
void ConvertQuadToTriangles(TArray<int>& Triangles, int Vert0, int Vert1, int Vert2, int Vert3)
```
Add a quad, specified by four indices, to a triangle index buffer as two triangles.

### CopyProceduralMeshFromStaticMeshComponent
```angelscript
void CopyProceduralMeshFromStaticMeshComponent(UStaticMeshComponent StaticMeshComponent, int LODIndex, UProceduralMeshComponent ProcMeshComponent, bool bCreateCollision)
```
Copy materials from StaticMeshComponent to ProceduralMeshComponent.

### CreateGridMeshSplit
```angelscript
void CreateGridMeshSplit(int NumX, int NumY, TArray<int>& Triangles, TArray<FVector>& Vertices, TArray<FVector2D>& UVs, TArray<FVector2D>& UV1s, float32 GridSpacing)
```
Generate a vertex buffer, index buffer and UVs for a grid mesh where each quad is split, with standard 0-1 UVs on UV0 and point sampled texel center UVs for UV1.
@param  NumX                    Number of vertices in X direction (must be >= 2)
@param  NumY                    Number of vertices in y direction (must be >= 2)
@out    Triangles               Output index buffer
@out    Vertices                Output vertex buffer
@out    UVs                             Out UVs
@out    UV1s                    Out UV1s
@param  GridSpacing             Size of each quad in world units

### CreateGridMeshTriangles
```angelscript
void CreateGridMeshTriangles(int NumX, int NumY, bool bWinding, TArray<int>& Triangles)
```
Generate an index buffer for a grid of quads.
@param  NumX                    Number of vertices in X direction (must be >= 2)
@param  NumY                    Number of vertices in y direction (must be >= 2)
@param  bWinding                Reverses winding of indices generated for each quad
@out    Triangles               Output index buffer

### CreateGridMeshWelded
```angelscript
void CreateGridMeshWelded(int NumX, int NumY, TArray<int>& Triangles, TArray<FVector>& Vertices, TArray<FVector2D>& UVs, float32 GridSpacing)
```
Generate a vertex buffer, index buffer and UVs for a tessellated grid mesh.
@param  NumX                    Number of vertices in X direction (must be >= 2)
@param  NumY                    Number of vertices in y direction (must be >= 2)
@out    Triangles               Output index buffer
@out    Vertices                Output vertex buffer
@out    UVs                             Out UVs
@param  GridSpacing             Size of each quad in world units

### GenerateBoxMesh
```angelscript
void GenerateBoxMesh(FVector BoxRadius, TArray<FVector>& Vertices, TArray<int>& Triangles, TArray<FVector>& Normals, TArray<FVector2D>& UVs, TArray<FProcMeshTangent>& Tangents)
```
Generate vertex and index buffer for a simple box, given the supplied dimensions. Normals, UVs and tangents are also generated for each vertex.

### GetSectionFromProceduralMesh
```angelscript
void GetSectionFromProceduralMesh(UProceduralMeshComponent InProcMesh, int SectionIndex, TArray<FVector>& Vertices, TArray<int>& Triangles, TArray<FVector>& Normals, TArray<FVector2D>& UVs, TArray<FProcMeshTangent>& Tangents)
```
Grab geometry data from a ProceduralMeshComponent.

### GetSectionFromStaticMesh
```angelscript
void GetSectionFromStaticMesh(UStaticMesh InMesh, int LODIndex, int SectionIndex, TArray<FVector>& Vertices, TArray<int>& Triangles, TArray<FVector>& Normals, TArray<FVector2D>& UVs, TArray<FProcMeshTangent>& Tangents)
```
Grab geometry data from a StaticMesh asset.

### SliceProceduralMesh
```angelscript
void SliceProceduralMesh(UProceduralMeshComponent InProcMesh, FVector PlanePosition, FVector PlaneNormal, bool bCreateOtherHalf, UProceduralMeshComponent& OutOtherHalfProcMesh, EProcMeshSliceCapOption CapOption, UMaterialInterface CapMaterial)
```
Slice the ProceduralMeshComponent (including simple convex collision) using a plane. Optionally create 'cap' geometry.
@param  InProcMesh                              ProceduralMeshComponent to slice
@param  PlanePosition                   Point on the plane to use for slicing, in world space
@param  PlaneNormal                             Normal of plane used for slicing. Geometry on the positive side of the plane will be kept.
@param  bCreateOtherHalf                If true, an additional ProceduralMeshComponent (OutOtherHalfProcMesh) will be created using the other half of the sliced geometry
@param  OutOtherHalfProcMesh    If bCreateOtherHalf is set, this is the new component created. Its owner will be the same as the supplied InProcMesh.
@param  CapOption                               If and how to create 'cap' geometry on the slicing plane
@param  CapMaterial                             If creating a new section for the cap, assign this material to that section

