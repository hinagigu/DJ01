# UDynamicMeshComponent

**继承自**: `UBaseDynamicMeshComponent`

UDynamicMeshComponent is a mesh component similar to UProceduralMeshComponent,
except it bases the renderable geometry off an internal UDynamicMesh instance (which
encapsulates a FDynamicMesh3).

There is extensive support for partial updates to render buffers, customizing colors,
internally decomposing the mesh into separate chunks for more efficient render updates,
and support for attaching a 'Postprocessor' to generate a render mesh on-the-fly
See comment sections below for details.

## 属性

### CollisionType
- **类型**: `ECollisionTraceFlag`

### bUseAsyncCooking
- **类型**: `bool`

### bEnableComplexCollision
- **类型**: `bool`

### bDeferCollisionUpdates
- **类型**: `bool`

### AggGeom
- **类型**: `FKAggregateGeom`
- **描述**: Simplified collision representation for the mesh component

## 方法

### ConfigureMaterialSet
```angelscript
void ConfigureMaterialSet(TArray<UMaterialInterface> NewMaterialSet)
```
Set new list of Materials for the Mesh. Dynamic Mesh Component does not have
Slot Names, so the size of the Material Set should be the same as the number of
different Material IDs on the mesh MaterialID attribute

### EnableComplexAsSimpleCollision
```angelscript
void EnableComplexAsSimpleCollision()
```
calls SetComplexAsSimpleCollisionEnabled(true, true)

### GetTangentsType
```angelscript
EDynamicMeshComponentTangentsMode GetTangentsType()
```

### NotifyMeshModified
```angelscript
void NotifyMeshModified()
```
Notify the Component that it's DynamicMesh has been modified externally. This will result in all Rendering Data
for the Component being rebuilt on the next frame (internally the Scene Proxy is fully destroyed and rebuilt).

You must use this function if the mesh triangulation has been modified, or if polygroups or material assignments
have been changed, or if Normal/UV/Color topology has changed (ie new split-vertices have been introduced).
If only vertex attribute values (position, normals, UVs, colors) have been modified, then
Notify Vertex Attributes Updated can be used to do a faster update.

### NotifyMeshVertexAttributesModified
```angelscript
void NotifyMeshVertexAttributesModified(bool bPositions, bool bNormals, bool bUVs, bool bColors)
```
Notify the Component that vertex attribute values of it's DynamicMesh have been modified externally. This will result in
Rendering vertex buffers being updated. This update path is more efficient than doing a full Notify Mesh Updated.

@warning it is invalid to call this function if (1) the mesh triangulation has also been changed, (2) triangle MaterialIDs have been changed,
or (3) any attribute overlay (normal, color, UV) topology has been modified, ie split-vertices have been added/removed.
Behavior of this function is undefined in these cases and may crash. If you are unsure, use Notify Mesh Updated.

### SetComplexAsSimpleCollisionEnabled
```angelscript
void SetComplexAsSimpleCollisionEnabled(bool bEnabled, bool bImmediateUpdate)
```
If bEnabled=true, sets bEnableComplexCollision=true and CollisionType=CTF_UseComplexAsSimple
If bEnabled=true, sets bEnableComplexCollision=false and CollisionType=CTF_UseDefault
@param bImmediateUpdate if true, UpdateCollision(true) is called

### SetDeferredCollisionUpdatesEnabled
```angelscript
void SetDeferredCollisionUpdatesEnabled(bool bEnabled, bool bImmediateUpdate)
```
Set value of bDeferCollisionUpdates, when enabled, collision is not automatically recomputed each time the mesh changes.
@param bImmediateUpdate if true, UpdateCollision(true) is called if bEnabled=false, ie to force a collision rebuild

### SetDynamicMesh
```angelscript
void SetDynamicMesh(UDynamicMesh NewMesh)
```
Replace the current UDynamicMesh with a new one, and transfer ownership of NewMesh to this Component.
This can be used to (eg) assign a UDynamicMesh created with NewObject in the Transient Package to this Component.
@warning If NewMesh is owned/Outer'd to another DynamicMeshComponent, a GLEO error may occur if that Component is serialized.

### SetTangentsType
```angelscript
void SetTangentsType(EDynamicMeshComponentTangentsMode NewTangentsType)
```

### UpdateCollision
```angelscript
void UpdateCollision(bool bOnlyIfPending)
```
Force an update of the Collision/Physics data for this Component.
@param bOnlyIfPending only update if a collision update is pending, ie the underlying DynamicMesh changed and bDeferCollisionUpdates is enabled

### ValidateMaterialSlots
```angelscript
bool ValidateMaterialSlots(bool bCreateIfMissing, bool bDeleteExtraSlots)
```
Compute the maximum MaterialID on the DynamicMesh, and ensure that Material Slots match.
Pass both arguments as false to just do a check.
@param bCreateIfMissing if true, add extra (empty) Material Slots to match max MaterialID
@param bDeleteExtraSlots if true, extra Material Slots beyond max MaterialID are removed
@return true if at the end of this function, Material Slot Count == Max MaterialID

