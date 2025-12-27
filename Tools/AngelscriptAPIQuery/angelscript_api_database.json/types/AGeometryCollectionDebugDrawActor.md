# AGeometryCollectionDebugDrawActor

**继承自**: `AActor`

## 属性

### bDebugDrawWholeCollection
- **类型**: `bool`
- **描述**: Show debug visualization for the rest of the geometry collection related to the current rigid body id selection.

### bDebugDrawHierarchy
- **类型**: `bool`
- **描述**: Show debug visualization for the top level node rather than the bottom leaf nodes of a cluster's hierarchy. * Only affects Clustering and Geometry visualization.

### bDebugDrawClustering
- **类型**: `bool`
- **描述**: Show debug visualization for all clustered children associated to the current rigid body id selection.

### HideGeometry
- **类型**: `EGeometryCollectionDebugDrawActorHideGeometry`
- **描述**: Geometry visibility setting. Select the part of the geometry to hide in order to better visualize the debug information.

### bShowRigidBodyId
- **类型**: `bool`
- **描述**: Display the selected rigid body's id.

### bShowRigidBodyCollision
- **类型**: `bool`
- **描述**: Show the selected rigid body's collision volume.

### bCollisionAtOrigin
- **类型**: `bool`
- **描述**: Show the selected rigid body's collision volume at the origin, in local space.

### bShowRigidBodyTransform
- **类型**: `bool`
- **描述**: Show the selected rigid body's transform.

### bShowRigidBodyInertia
- **类型**: `bool`
- **描述**: Show the selected rigid body's inertia tensor box.

### bShowRigidBodyVelocity
- **类型**: `bool`
- **描述**: Show the selected rigid body's linear and angular velocity.

### bShowRigidBodyForce
- **类型**: `bool`
- **描述**: Show the selected rigid body's applied force and torque.

### bShowRigidBodyInfos
- **类型**: `bool`
- **描述**: Show the selected rigid body's on screen text information.

### bShowTransformIndex
- **类型**: `bool`
- **描述**: Show the transform index for the selected rigid body's associated cluster nodes.

### bShowTransform
- **类型**: `bool`
- **描述**: Show the transform for the selected rigid body's associated cluster nodes.

### bShowParent
- **类型**: `bool`
- **描述**: Show a link from the selected rigid body's associated cluster nodes to their parent's nodes.

### bShowLevel
- **类型**: `bool`
- **描述**: Show the hierarchical level for the selected rigid body's associated cluster nodes.

### bShowConnectivityEdges
- **类型**: `bool`
- **描述**: Show the connectivity edges for the selected rigid body's associated cluster nodes.

### bShowGeometryIndex
- **类型**: `bool`
- **描述**: Show the geometry index for the selected rigid body's associated geometries.

### bShowGeometryTransform
- **类型**: `bool`
- **描述**: Show the geometry transform for the selected rigid body's associated geometries.

### bShowBoundingBox
- **类型**: `bool`
- **描述**: Show the bounding box for the selected rigid body's associated geometries.

### bShowFaces
- **类型**: `bool`
- **描述**: Show the faces for the selected rigid body's associated geometries.

### bShowFaceIndices
- **类型**: `bool`
- **描述**: Show the face indices for the selected rigid body's associated geometries.

### bShowFaceNormals
- **类型**: `bool`
- **描述**: Show the face normals for the selected rigid body's associated geometries.

### bShowSingleFace
- **类型**: `bool`
- **描述**: Enable single face visualization for the selected rigid body's associated geometries.

### SingleFaceIndex
- **类型**: `int`
- **描述**: The index of the single face to visualize.

### bShowVertices
- **类型**: `bool`
- **描述**: Show the vertices for the selected rigid body's associated geometries.

### bShowVertexIndices
- **类型**: `bool`
- **描述**: Show the vertex indices for the selected rigid body's associated geometries.

### bShowVertexNormals
- **类型**: `bool`
- **描述**: Show the vertex normals for the selected rigid body's associated geometries.

### bUseActiveVisualization
- **类型**: `bool`
- **描述**: Adapt visualization depending of the cluster nodes' hierarchical level.

### PointThickness
- **类型**: `float32`
- **描述**: Thickness of points when visualizing vertices.

### LineThickness
- **类型**: `float32`
- **描述**: Thickness of lines when visualizing faces, normals, ...etc.

### bTextShadow
- **类型**: `bool`
- **描述**: Draw shadows under the displayed text.

### TextScale
- **类型**: `float32`
- **描述**: Scale of the font used to display text.

### NormalScale
- **类型**: `float32`
- **描述**: Scale factor used for visualizing normals.

### AxisScale
- **类型**: `float32`
- **描述**: Scale of the axis used for visualizing all transforms.

### ArrowScale
- **类型**: `float32`
- **描述**: Size of arrows used for visualizing normals, breaking information, ...etc.

### RigidBodyIdColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the rigid body ids.

### RigidBodyTransformScale
- **类型**: `float32`
- **描述**: Scale for rigid body transform visualization.

### RigidBodyCollisionColor
- **类型**: `FColor`
- **描述**: Color used for collision primitives visualization.

### RigidBodyInertiaColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the rigid body inertia tensor box.

### RigidBodyVelocityColor
- **类型**: `FColor`
- **描述**: Color used for rigid body velocities visualization.

### RigidBodyForceColor
- **类型**: `FColor`
- **描述**: Color used for rigid body applied force and torque visualization.

### RigidBodyInfoColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the rigid body infos.

### TransformIndexColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the transform indices.

### TransformScale
- **类型**: `float32`
- **描述**: Scale for cluster transform visualization.

### LevelColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the levels.

### ParentColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the link from the parents.

### ConnectivityEdgeThickness
- **类型**: `float32`
- **描述**: Line thickness used for the visualization of the rigid clustering connectivity edges.

### GeometryIndexColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the geometry indices.

### GeometryTransformScale
- **类型**: `float32`
- **描述**: Scale for geometry transform visualization.

### BoundingBoxColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the bounding boxes.

### FaceColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the faces.

### FaceIndexColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the face indices.

### FaceNormalColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the face normals.

### SingleFaceColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the single face.

### VertexColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the vertices.

### VertexIndexColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the vertex indices.

### VertexNormalColor
- **类型**: `FColor`
- **描述**: Color used for the visualization of the vertex normals.

