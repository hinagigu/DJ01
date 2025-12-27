# UNiagaraDataInterfaceDynamicMesh

**继承自**: `UNiagaraDataInterface`

Data Interface that can create mesh geometry at runtime from triangle data (e.g. to render a custom generated mesh per particle)

## 属性

### Sections
- **类型**: `TArray<FNiagaraDynamicMeshSection>`
- **描述**: Sections to render, each section will generally result in a draw call.
Triangles are contiguous between sections, i.e. Section[1] triangles will begin after Section[0].NumTriangles

### Materials
- **类型**: `TArray<FNiagaraDynamicMeshMaterial>`
- **描述**: List of materials to use

### NumVertices
- **类型**: `int`
- **描述**: Allocates space for the number of vertices we will use, leave as zero if you intend to allocate dynamically via VM calls.

### NumTexCoords
- **类型**: `int`
- **描述**: Allocates space for the number of texture coordinates requested.

### bHasColors
- **类型**: `bool`
- **描述**: Allocates space for vertex colors when enabled.

### bHasTangentBasis
- **类型**: `bool`
- **描述**: Allocates space for tangent basis when enabled.

### bClearTrianglesPerFrame
- **类型**: `bool`
- **描述**: Should we auto clear section triangle allocations per frame or not.

### DefaultBounds
- **类型**: `FBox`
- **描述**: Should we auto clear section triangle allocations per frame or not.

