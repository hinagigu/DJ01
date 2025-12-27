# UBodySetupCore

**继承自**: `UObject`

## 属性

### PhysicsType
- **类型**: `EPhysicsType`
- **描述**: If simulated it will use physics, if kinematic it will not be affected by physics, but can interact with physically simulated bodies. Default will inherit from OwnerComponent's behavior.

### CollisionTraceFlag
- **类型**: `ECollisionTraceFlag`
- **描述**: Collision Trace behavior - by default, it will keep simple(convex)/complex(per-poly) separate *

### CollisionReponse
- **类型**: `EBodyCollisionResponse`
- **描述**: Collision Type for this body. This eventually changes response to collision to others *

