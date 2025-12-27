# __AnimNodeRigidBody

## 方法

### ConvertToRigidBodyAnimNode
```angelscript
FRigidBodyAnimNodeReference ConvertToRigidBodyAnimNode(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a rigid body anim node context from an anim node context

### ConvertToRigidBodyAnimNodePure
```angelscript
void ConvertToRigidBodyAnimNodePure(FAnimNodeReference Node, FRigidBodyAnimNodeReference& RigidBodyAnimNode, bool& Result)
```
Get a rigid body anim node context from an anim node context (pure)

### SetOverridePhysicsAsset
```angelscript
FRigidBodyAnimNodeReference SetOverridePhysicsAsset(FRigidBodyAnimNodeReference Node, UPhysicsAsset PhysicsAsset)
```
Set the physics asset on the rigid body anim graph node (RBAN).

