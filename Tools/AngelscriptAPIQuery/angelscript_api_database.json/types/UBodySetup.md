# UBodySetup

**继承自**: `UBodySetupCore`

BodySetup contains all collision information that is associated with a single asset.
A single BodySetup instance is shared among many BodyInstances so that geometry data is not duplicated.
Assets typically implement a GetBodySetup function that is used during physics state creation.

@see GetBodySetup
@see FBodyInstance

## 属性

### AggGeom
- **类型**: `FKAggregateGeom`
- **描述**: Simplified collision representation of this

### PhysMaterial
- **类型**: `UPhysicalMaterial`
- **描述**: Physical material to use for simple collision on this body. Encodes information about density, friction etc.

### WalkableSlopeOverride
- **类型**: `FWalkableSlopeOverride`
- **描述**: Custom walkable slope setting for this body.

### DefaultInstance
- **类型**: `FBodyInstance`
- **描述**: Default properties of the body instance, copied into objects on instantiation, was URB_BodyInstance

### bConsiderForBounds
- **类型**: `bool`

### bDoubleSidedGeometry
- **类型**: `bool`

### bNeverNeedsCookedCollisionData
- **类型**: `bool`

