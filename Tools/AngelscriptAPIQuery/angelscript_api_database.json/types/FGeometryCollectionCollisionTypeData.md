# FGeometryCollectionCollisionTypeData

## 属性

### CollisionType
- **类型**: `ECollisionTypeEnum`
- **描述**: *  CollisionType defines how to initialize the rigid collision structures.

### ImplicitType
- **类型**: `EImplicitTypeEnum`
- **描述**: *  CollisionType defines how to initialize the rigid collision structures.

### LevelSet
- **类型**: `FGeometryCollectionLevelSetData`
- **描述**: *  LevelSet Resolution data for rasterization.

### CollisionParticles
- **类型**: `FGeometryCollectionCollisionParticleData`
- **描述**: *  Collision Particle data for surface samples during Particle-LevelSet collisions.

### CollisionObjectReductionPercentage
- **类型**: `float32`
- **描述**: *  Uniform scale on the collision body. (def: 0)

### CollisionMarginFraction
- **类型**: `float32`
- **描述**: A collision margin is a fraction of size used by some boxes and convex shapes to improve collision detection results.
The core geometry of shapes that support a margin are reduced in size by the margin, and the margin
is added back on during collision detection. The net result is a shape of the same size but with rounded corners.

## 方法

### opAssign
```angelscript
FGeometryCollectionCollisionTypeData& opAssign(FGeometryCollectionCollisionTypeData Other)
```

