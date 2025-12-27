# UMeshDescriptionBase

**继承自**: `UObject`

## 方法

### ComputePolygonTriangulation
```angelscript
void ComputePolygonTriangulation(FPolygonID PolygonID)
```
Generates triangles and internal edges for the given polygon

### CreateEdge
```angelscript
FEdgeID CreateEdge(FVertexID VertexID0, FVertexID VertexID1)
```
Adds a new edge to the mesh and returns its ID

### CreateEdgeWithID
```angelscript
void CreateEdgeWithID(FEdgeID EdgeID, FVertexID VertexID0, FVertexID VertexID1)
```
Adds a new edge to the mesh with the given ID

### CreatePolygon
```angelscript
FPolygonID CreatePolygon(FPolygonGroupID PolygonGroupID, TArray<FVertexInstanceID>& VertexInstanceIDs, TArray<FEdgeID>& NewEdgeIDs)
```
Adds a new polygon to the mesh and returns its ID. This will also make any missing edges, and all constituent triangles.

### CreatePolygonGroup
```angelscript
FPolygonGroupID CreatePolygonGroup()
```
Adds a new polygon group to the mesh and returns its ID

### CreatePolygonGroupWithID
```angelscript
void CreatePolygonGroupWithID(FPolygonGroupID PolygonGroupID)
```
Adds a new polygon group to the mesh with the given ID

### CreatePolygonWithID
```angelscript
void CreatePolygonWithID(FPolygonID PolygonID, FPolygonGroupID PolygonGroupID, TArray<FVertexInstanceID>& VertexInstanceIDs, TArray<FEdgeID>& NewEdgeIDs)
```
Adds a new polygon to the mesh with the given ID. This will also make any missing edges, and all constituent triangles.

### CreateTriangle
```angelscript
FTriangleID CreateTriangle(FPolygonGroupID PolygonGroupID, TArray<FVertexInstanceID> VertexInstanceIDs, TArray<FEdgeID>& NewEdgeIDs)
```
Adds a new triangle to the mesh and returns its ID. This will also make an encapsulating polygon, and any missing edges.

### CreateTriangleWithID
```angelscript
void CreateTriangleWithID(FTriangleID TriangleID, FPolygonGroupID PolygonGroupID, TArray<FVertexInstanceID> VertexInstanceIDs, TArray<FEdgeID>& NewEdgeIDs)
```
Adds a new triangle to the mesh with the given ID. This will also make an encapsulating polygon, and any missing edges.

### CreateVertex
```angelscript
FVertexID CreateVertex()
```
Adds a new vertex to the mesh and returns its ID

### CreateVertexInstance
```angelscript
FVertexInstanceID CreateVertexInstance(FVertexID VertexID)
```
Adds a new vertex instance to the mesh and returns its ID

### CreateVertexInstanceWithID
```angelscript
void CreateVertexInstanceWithID(FVertexInstanceID VertexInstanceID, FVertexID VertexID)
```
Adds a new vertex instance to the mesh with the given ID

### CreateVertexWithID
```angelscript
void CreateVertexWithID(FVertexID VertexID)
```
Adds a new vertex to the mesh with the given ID

### DeleteEdge
```angelscript
void DeleteEdge(FEdgeID EdgeID, TArray<FVertexID>& OrphanedVertices)
```
Deletes an edge from a mesh

### DeletePolygon
```angelscript
void DeletePolygon(FPolygonID PolygonID, TArray<FEdgeID>& OrphanedEdges, TArray<FVertexInstanceID>& OrphanedVertexInstances, TArray<FPolygonGroupID>& OrphanedPolygonGroups)
```
Deletes a polygon from the mesh

### DeletePolygonGroup
```angelscript
void DeletePolygonGroup(FPolygonGroupID PolygonGroupID)
```
Deletes a polygon group from the mesh

### DeleteTriangle
```angelscript
void DeleteTriangle(FTriangleID TriangleID, TArray<FEdgeID>& OrphanedEdges, TArray<FVertexInstanceID>& OrphanedVertexInstances, TArray<FPolygonGroupID>& OrphanedPolygonGroupsPtr)
```
Deletes a triangle from the mesh

### DeleteVertex
```angelscript
void DeleteVertex(FVertexID VertexID)
```
Deletes a vertex from the mesh

### DeleteVertexInstance
```angelscript
void DeleteVertexInstance(FVertexInstanceID VertexInstanceID, TArray<FVertexID>& OrphanedVertices)
```
Deletes a vertex instance from a mesh

### Empty
```angelscript
void Empty()
```
Empty the mesh description

### GetEdgeConnectedPolygons
```angelscript
void GetEdgeConnectedPolygons(FEdgeID EdgeID, TArray<FPolygonID>& OutConnectedPolygonIDs)
```
Returns the polygons connected to this edge

### GetEdgeConnectedTriangles
```angelscript
void GetEdgeConnectedTriangles(FEdgeID EdgeID, TArray<FTriangleID>& OutConnectedTriangleIDs)
```
Returns reference to an array of triangle IDs connected to this edge

### GetEdgeCount
```angelscript
int GetEdgeCount()
```
Returns the number of edges

### GetEdgeVertex
```angelscript
FVertexID GetEdgeVertex(FEdgeID EdgeID, int VertexNumber)
```
Returns the vertex ID corresponding to one of the edge endpoints

### GetEdgeVertices
```angelscript
void GetEdgeVertices(FEdgeID EdgeID, TArray<FVertexID>& OutVertexIDs)
```
Returns a pair of vertex IDs defining the edge

### GetNumEdgeConnectedPolygons
```angelscript
int GetNumEdgeConnectedPolygons(FEdgeID EdgeID)
```
Returns the number of polygons connected to this edge

### GetNumEdgeConnectedTriangles
```angelscript
int GetNumEdgeConnectedTriangles(FEdgeID EdgeID)
```
Returns the number of triangles connected to this edge

### GetNumPolygonGroupPolygons
```angelscript
int GetNumPolygonGroupPolygons(FPolygonGroupID PolygonGroupID)
```
Returns the number of polygons in this polygon group

### GetNumPolygonInternalEdges
```angelscript
int GetNumPolygonInternalEdges(FPolygonID PolygonID)
```
Return the number of internal edges in this polygon

### GetNumPolygonTriangles
```angelscript
int GetNumPolygonTriangles(FPolygonID PolygonID)
```
Return the number of triangles which comprise this polygon

### GetNumPolygonVertices
```angelscript
int GetNumPolygonVertices(FPolygonID PolygonID)
```
Returns the number of vertices this polygon has

### GetNumVertexConnectedEdges
```angelscript
int GetNumVertexConnectedEdges(FVertexID VertexID)
```
Returns number of edges connected to this vertex

### GetNumVertexConnectedPolygons
```angelscript
int GetNumVertexConnectedPolygons(FVertexID VertexID)
```
Returns the number of polygons connected to this vertex

### GetNumVertexConnectedTriangles
```angelscript
int GetNumVertexConnectedTriangles(FVertexID VertexID)
```
Returns number of triangles connected to this vertex

### GetNumVertexInstanceConnectedPolygons
```angelscript
int GetNumVertexInstanceConnectedPolygons(FVertexInstanceID VertexInstanceID)
```
Returns the number of polygons connected to this vertex instance.

### GetNumVertexInstanceConnectedTriangles
```angelscript
int GetNumVertexInstanceConnectedTriangles(FVertexInstanceID VertexInstanceID)
```
Returns the number of triangles connected to this vertex instance

### GetNumVertexVertexInstances
```angelscript
int GetNumVertexVertexInstances(FVertexID VertexID)
```
Returns number of vertex instances created from this vertex

### GetPolygonAdjacentPolygons
```angelscript
void GetPolygonAdjacentPolygons(FPolygonID PolygonID, TArray<FPolygonID>& OutPolygonIDs)
```
Populates the passed array with adjacent polygons

### GetPolygonCount
```angelscript
int GetPolygonCount()
```
Returns the number of polygons

### GetPolygonGroupCount
```angelscript
int GetPolygonGroupCount()
```
Returns the number of polygon groups

### GetPolygonGroupPolygons
```angelscript
void GetPolygonGroupPolygons(FPolygonGroupID PolygonGroupID, TArray<FPolygonID>& OutPolygonIDs)
```
Returns the polygons associated with the given polygon group

### GetPolygonInternalEdges
```angelscript
void GetPolygonInternalEdges(FPolygonID PolygonID, TArray<FEdgeID>& OutEdgeIDs)
```
Populate the provided array with a list of edges which are internal to the polygon, i.e. those which separate
          constituent triangles.

### GetPolygonPerimeterEdges
```angelscript
void GetPolygonPerimeterEdges(FPolygonID PolygonID, TArray<FEdgeID>& OutEdgeIDs)
```
Returns the edges which form the polygon perimeter

### GetPolygonPolygonGroup
```angelscript
FPolygonGroupID GetPolygonPolygonGroup(FPolygonID PolygonID)
```
Return the polygon group associated with a polygon

### GetPolygonTriangles
```angelscript
void GetPolygonTriangles(FPolygonID PolygonID, TArray<FTriangleID>& OutTriangleIDs)
```
Return reference to an array of triangle IDs which comprise this polygon

### GetPolygonVertexInstances
```angelscript
void GetPolygonVertexInstances(FPolygonID PolygonID, TArray<FVertexInstanceID>& OutVertexInstanceIDs)
```
Returns reference to an array of VertexInstance IDs forming the perimeter of this polygon

### GetPolygonVertices
```angelscript
void GetPolygonVertices(FPolygonID PolygonID, TArray<FVertexID>& OutVertexIDs)
```
Returns the vertices which form the polygon perimeter

### GetTriangleAdjacentTriangles
```angelscript
void GetTriangleAdjacentTriangles(FTriangleID TriangleID, TArray<FTriangleID>& OutTriangleIDs)
```
Returns the adjacent triangles to this triangle

### GetTriangleCount
```angelscript
int GetTriangleCount()
```
Returns the number of triangles

### GetTriangleEdges
```angelscript
void GetTriangleEdges(FTriangleID TriangleID, TArray<FEdgeID>& OutEdgeIDs)
```
Returns the edges which define this triangle

### GetTrianglePolygon
```angelscript
FPolygonID GetTrianglePolygon(FTriangleID TriangleID)
```
Get the polygon which contains this triangle

### GetTrianglePolygonGroup
```angelscript
FPolygonGroupID GetTrianglePolygonGroup(FTriangleID TriangleID)
```
Get the polygon group which contains this triangle

### GetTriangleVertexInstance
```angelscript
FVertexInstanceID GetTriangleVertexInstance(FTriangleID TriangleID, int Index)
```
Get the specified vertex instance by index

### GetTriangleVertexInstances
```angelscript
void GetTriangleVertexInstances(FTriangleID TriangleID, TArray<FVertexInstanceID>& OutVertexInstanceIDs)
```
Get the vertex instances which define this triangle

### GetTriangleVertices
```angelscript
void GetTriangleVertices(FTriangleID TriangleID, TArray<FVertexID>& OutVertexIDs)
```
Returns the vertices which define this triangle

### GetVertexAdjacentVertices
```angelscript
void GetVertexAdjacentVertices(FVertexID VertexID, TArray<FVertexID>& OutAdjacentVertexIDs)
```
Returns the vertices adjacent to this vertex

### GetVertexConnectedEdges
```angelscript
void GetVertexConnectedEdges(FVertexID VertexID, TArray<FEdgeID>& OutEdgeIDs)
```
Returns reference to an array of Edge IDs connected to this vertex

### GetVertexConnectedPolygons
```angelscript
void GetVertexConnectedPolygons(FVertexID VertexID, TArray<FPolygonID>& OutConnectedPolygonIDs)
```
Returns the polygons connected to this vertex

### GetVertexConnectedTriangles
```angelscript
void GetVertexConnectedTriangles(FVertexID VertexID, TArray<FTriangleID>& OutConnectedTriangleIDs)
```
Returns the triangles connected to this vertex

### GetVertexCount
```angelscript
int GetVertexCount()
```
Returns the number of vertices

### GetVertexInstanceConnectedPolygons
```angelscript
void GetVertexInstanceConnectedPolygons(FVertexInstanceID VertexInstanceID, TArray<FPolygonID>& OutConnectedPolygonIDs)
```
Returns the polygons connected to this vertex instance

### GetVertexInstanceConnectedTriangles
```angelscript
void GetVertexInstanceConnectedTriangles(FVertexInstanceID VertexInstanceID, TArray<FTriangleID>& OutConnectedTriangleIDs)
```
Returns reference to an array of Triangle IDs connected to this vertex instance

### GetVertexInstanceCount
```angelscript
int GetVertexInstanceCount()
```
Returns the number of vertex instances

### GetVertexInstanceForPolygonVertex
```angelscript
FVertexInstanceID GetVertexInstanceForPolygonVertex(FPolygonID PolygonID, FVertexID VertexID)
```
Return the vertex instance which corresponds to the given vertex on the given polygon, or INDEX_NONE

### GetVertexInstanceForTriangleVertex
```angelscript
FVertexInstanceID GetVertexInstanceForTriangleVertex(FTriangleID TriangleID, FVertexID VertexID)
```
Return the vertex instance which corresponds to the given vertex on the given triangle, or INDEX_NONE

### GetVertexInstancePairEdge
```angelscript
FEdgeID GetVertexInstancePairEdge(FVertexInstanceID VertexInstanceID0, FVertexInstanceID VertexInstanceID1)
```
Returns the edge ID defined by the two given vertex instance IDs, if there is one; otherwise INDEX_NONE

### GetVertexInstanceVertex
```angelscript
FVertexID GetVertexInstanceVertex(FVertexInstanceID VertexInstanceID)
```
Returns the vertex ID associated with the given vertex instance

### GetVertexPairEdge
```angelscript
FEdgeID GetVertexPairEdge(FVertexID VertexID0, FVertexID VertexID1)
```
Returns the edge ID defined by the two given vertex IDs, if there is one; otherwise INDEX_NONE

### GetVertexPosition
```angelscript
FVector GetVertexPosition(FVertexID VertexID)
```
Gets a vertex position

### GetVertexVertexInstances
```angelscript
void GetVertexVertexInstances(FVertexID VertexID, TArray<FVertexInstanceID>& OutVertexInstanceIDs)
```
Returns reference to an array of VertexInstance IDs instanced from this vertex

### IsEdgeInternal
```angelscript
bool IsEdgeInternal(FEdgeID EdgeID)
```
Determine whether a given edge is an internal edge between triangles of a polygon

### IsEdgeInternalToPolygon
```angelscript
bool IsEdgeInternalToPolygon(FEdgeID EdgeID, FPolygonID PolygonID)
```
Determine whether a given edge is an internal edge between triangles of a specific polygon

### IsEdgeValid
```angelscript
bool IsEdgeValid(FEdgeID EdgeID)
```
Returns whether the passed edge ID is valid

### IsEmpty
```angelscript
bool IsEmpty()
```
Return whether the mesh description is empty

### IsPolygonGroupValid
```angelscript
bool IsPolygonGroupValid(FPolygonGroupID PolygonGroupID)
```
Returns whether the passed polygon group ID is valid

### IsPolygonValid
```angelscript
bool IsPolygonValid(FPolygonID PolygonID)
```
Returns whether the passed polygon ID is valid

### IsTrianglePartOfNgon
```angelscript
bool IsTrianglePartOfNgon(FTriangleID TriangleID)
```
Determines if this triangle is part of an n-gon

### IsTriangleValid
```angelscript
bool IsTriangleValid(FTriangleID TriangleID)
```
Returns whether the passed triangle ID is valid

### IsVertexInstanceValid
```angelscript
bool IsVertexInstanceValid(FVertexInstanceID VertexInstanceID)
```
Returns whether the passed vertex instance ID is valid

### IsVertexOrphaned
```angelscript
bool IsVertexOrphaned(FVertexID VertexID)
```
Returns whether a given vertex is orphaned, i.e. it doesn't form part of any polygon

### IsVertexValid
```angelscript
bool IsVertexValid(FVertexID VertexID)
```
Returns whether the passed vertex ID is valid

### ReserveNewEdges
```angelscript
void ReserveNewEdges(int NumberOfNewEdges)
```
Reserves space for this number of new edges

### ReserveNewPolygonGroups
```angelscript
void ReserveNewPolygonGroups(int NumberOfNewPolygonGroups)
```
Reserves space for this number of new polygon groups

### ReserveNewPolygons
```angelscript
void ReserveNewPolygons(int NumberOfNewPolygons)
```
Reserves space for this number of new polygons

### ReserveNewTriangles
```angelscript
void ReserveNewTriangles(int NumberOfNewTriangles)
```
Reserves space for this number of new triangles

### ReserveNewVertexInstances
```angelscript
void ReserveNewVertexInstances(int NumberOfNewVertexInstances)
```
Reserves space for this number of new vertex instances

### ReserveNewVertices
```angelscript
void ReserveNewVertices(int NumberOfNewVertices)
```
Reserves space for this number of new vertices

### ReversePolygonFacing
```angelscript
void ReversePolygonFacing(FPolygonID PolygonID)
```
Reverse the winding order of the vertices of this polygon

### SetPolygonPolygonGroup
```angelscript
void SetPolygonPolygonGroup(FPolygonID PolygonID, FPolygonGroupID PolygonGroupID)
```
Sets the polygon group associated with a polygon

### SetPolygonVertexInstances
```angelscript
void SetPolygonVertexInstances(FPolygonID PolygonID, TArray<FVertexInstanceID> VertexInstanceIDs)
```
Set the vertex instance at the given index around the polygon to the new value

### SetVertexPosition
```angelscript
void SetVertexPosition(FVertexID VertexID, FVector Position)
```
Sets a vertex position

