# UFractureCollisionSettings

**继承自**: `UFractureToolSettings`

Settings related to the collision properties of the fractured mesh pieces

## 属性

### bAddSamplesForCollision
- **类型**: `bool`
- **描述**: If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles)
These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately

Note this is *only* useful for simulations that use particle-implicit collisions

### PointSpacing
- **类型**: `float32`
- **描述**: The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

