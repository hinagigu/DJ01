# UClothConfigNv

**继承自**: `UClothConfigCommon`

## 属性

### ClothingWindMethod
- **类型**: `EClothingWindMethodNv`
- **描述**: How wind should be processed, Accurate uses drag and lift to make the cloth react differently, legacy applies similar forces to all clothing without drag and lift (similar to APEX)

### VerticalConstraint
- **类型**: `FClothConstraintSetupNv`
- **描述**: Constraint data for vertical constraints

### HorizontalConstraint
- **类型**: `FClothConstraintSetupNv`
- **描述**: Constraint data for horizontal constraints

### BendConstraint
- **类型**: `FClothConstraintSetupNv`
- **描述**: Constraint data for bend constraints

### ShearConstraint
- **类型**: `FClothConstraintSetupNv`
- **描述**: Constraint data for shear constraints

### SelfCollisionRadius
- **类型**: `float32`
- **描述**: Size of self collision spheres centered on each vert

### SelfCollisionStiffness
- **类型**: `float32`
- **描述**: Stiffness of the spring force that will resolve self collisions

### SelfCollisionCullScale
- **类型**: `float32`
- **描述**: Scale to use for the radius of the culling checks for self collisions.
Any other self collision body within the radius of this check will be culled.
This helps performance with higher resolution meshes by reducing the number
of colliding bodies within the cloth. Reducing this will have a negative
effect on performance!

### Damping
- **类型**: `FVector`
- **描述**: Damping of particle motion per-axis

### Friction
- **类型**: `float32`
- **描述**: Friction of the surface when colliding

### WindDragCoefficient
- **类型**: `float32`
- **描述**: Drag coefficient for wind calculations, higher values mean wind has more lateral effect on cloth

### WindLiftCoefficient
- **类型**: `float32`
- **描述**: Lift coefficient for wind calculations, higher values make cloth rise easier in wind

### LinearDrag
- **类型**: `FVector`
- **描述**: Drag applied to linear particle movement per-axis

### AngularDrag
- **类型**: `FVector`
- **描述**: Drag applied to angular particle movement, higher values should limit material bending (per-axis)

### LinearInertiaScale
- **类型**: `FVector`
- **描述**: Scale for linear particle inertia, how much movement should translate to linear motion (per-axis)

### AngularInertiaScale
- **类型**: `FVector`
- **描述**: Scale for angular particle inertia, how much movement should translate to angular motion (per-axis)

### CentrifugalInertiaScale
- **类型**: `FVector`
- **描述**: Scale for centrifugal particle inertia, how much movement should translate to angular motion (per-axis)

### SolverFrequency
- **类型**: `float32`
- **描述**: Frequency of the position solver, lower values will lead to stretchier, bouncier cloth

### StiffnessFrequency
- **类型**: `float32`
- **描述**: Frequency for stiffness calculations, lower values will degrade stiffness of constraints

### GravityScale
- **类型**: `float32`
- **描述**: Scale of gravity effect on particles

### GravityOverride
- **类型**: `FVector`
- **描述**: Direct gravity override value

### bUseGravityOverride
- **类型**: `bool`
- **描述**: Use gravity override value vs gravity scale

### TetherStiffness
- **类型**: `float32`
- **描述**: Scale for stiffness of particle tethers between each other

### TetherLimit
- **类型**: `float32`
- **描述**: Scale for the limit of particle tethers (how far they can separate)

### CollisionThickness
- **类型**: `float32`
- **描述**: 'Thickness' of the simulated cloth, used to adjust collisions

### AnimDriveSpringStiffness
- **类型**: `float32`
- **描述**: Default spring stiffness for anim drive if an anim drive is in use

### AnimDriveDamperStiffness
- **类型**: `float32`
- **描述**: Default damper stiffness for anim drive if an anim drive is in use

