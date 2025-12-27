# UPhysicsAssetEditorOptions

**继承自**: `UObject`

## 属性

### PhysicsBlend
- **类型**: `float32`
- **描述**: Lets you manually control the physics/animation

### bUpdateJointsFromAnimation
- **类型**: `bool`
- **描述**: Lets you manually control the physics/animation

### PhysicsUpdateMode
- **类型**: `EPhysicsTransformUpdateMode`
- **描述**: Determines whether simulation of root body updates component transform

### PokePauseTime
- **类型**: `float32`
- **描述**: Time between poking ragdoll and starting to blend back.

### PokeBlendTime
- **类型**: `float32`
- **描述**: Time taken to blend from physics to animation.

### GravScale
- **类型**: `float32`
- **描述**: Scale factor for the gravity used in the simulation

### GravityOverrideZ
- **类型**: `float32`
- **描述**: Gravity override used in the simulation

### bUseGravityOverride
- **类型**: `bool`
- **描述**: Toggle gravity override vs gravity scale

### MaxFPS
- **类型**: `int`
- **描述**: Max FPS for simulation in PhysicsAssetEditor. This is helpful for targeting the same FPS as your game. -1 means disabled

### HandleLinearDamping
- **类型**: `float32`
- **描述**: Linear damping of mouse spring forces

### HandleLinearStiffness
- **类型**: `float32`
- **描述**: Linear stiffness of mouse spring forces

### HandleAngularDamping
- **类型**: `float32`
- **描述**: Angular damping of mouse spring forces

### HandleAngularStiffness
- **类型**: `float32`
- **描述**: Angular stiffness of mouse spring forces

### InterpolationSpeed
- **类型**: `float32`
- **描述**: How quickly we interpolate the physics target transform for mouse spring forces

### PokeStrength
- **类型**: `float32`
- **描述**: Strength of the impulse used when poking with left mouse button

### InteractionDistance
- **类型**: `float32`
- **描述**: Raycast distance when poking or grabbing

### bResetClothWhenSimulating
- **类型**: `bool`
- **描述**: When set, cloth will reset each time simulation is toggled

