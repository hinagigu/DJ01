# UFractureRadialSettings

**继承自**: `UFractureToolSettings`

## 属性

### Center
- **类型**: `FVector`
- **描述**: Center of generated pattern. Only used when "Use Gizmo" is disabled

### Normal
- **类型**: `FVector`
- **描述**: Normal to plane in which sites are generated. Only used when "Use Gizmo" is disabled

### AngularSteps
- **类型**: `int`
- **描述**: Number of angular steps

### AngleOffset
- **类型**: `float32`
- **描述**: Angle offset at each radial step (in degrees)

### AngularNoise
- **类型**: `float32`
- **描述**: Amount of global variation to apply to each angular step (in degrees)

### Radius
- **类型**: `float32`
- **描述**: Pattern radius (in cm)

### RadialSteps
- **类型**: `int`
- **描述**: Number of radial steps

### RadialStepExponent
- **类型**: `float32`
- **描述**: Radial steps will follow a distribution based on this exponent, i.e., Pow(distance from center, RadialStepExponent)

### RadialMinStep
- **类型**: `float32`
- **描述**: Minimum radial separation between any two voronoi points (in cm)

### RadialNoise
- **类型**: `float32`
- **描述**: Amount of global variation to apply to each radial step (in cm)

### RadialVariability
- **类型**: `float32`
- **描述**: Amount to randomly displace each Voronoi site radially (in cm)

### AngularVariability
- **类型**: `float32`
- **描述**: Amount to randomly displace each Voronoi site in angle (in degrees)

### AxialVariability
- **类型**: `float32`
- **描述**: Amount to randomly displace each Voronoi site in the direction of the rotation axis (in cm)

