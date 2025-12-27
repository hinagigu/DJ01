# UNavCollision

**继承自**: `UNavCollisionBase`

## 属性

### CylinderCollision
- **类型**: `TArray<FNavCollisionCylinder>`
- **描述**: list of nav collision cylinders

### BoxCollision
- **类型**: `TArray<FNavCollisionBox>`
- **描述**: list of nav collision boxes

### AreaClass
- **类型**: `TSubclassOf<UNavArea>`
- **描述**: navigation area type that will be use when this static mesh is used as
    a navigation obstacle. See bIsDynamicObstacle.
    Empty AreaClass means the default obstacle class will be used

### bGatherConvexGeometry
- **类型**: `bool`

### bCreateOnClient
- **类型**: `bool`

