# FGeometryCollectionDebugDrawActorSelectedRigidBody

FGeometryCollectionDebugDrawActorSelectedRigidBody
  Structure used to select a rigid body id with a picking tool through a detail customization.

## 属性

### Id
- **类型**: `int`
- **描述**: Id of the selected rigid body whose to visualize debug informations. Use -1 to visualize all Geometry Collections.

### Solver
- **类型**: `AChaosSolverActor`
- **描述**: Chaos RBD Solver. Will use the world's default solver actor if null.

## 方法

### opAssign
```angelscript
FGeometryCollectionDebugDrawActorSelectedRigidBody& opAssign(FGeometryCollectionDebugDrawActorSelectedRigidBody Other)
```

