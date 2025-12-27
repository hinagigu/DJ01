# UParticleModuleLocationDirect

**继承自**: `UParticleModuleLocationBase`

## 属性

### Location
- **类型**: `FRawDistributionVector`
- **描述**: The location of the particle at a give time. Retrieved using the particle RelativeTime.
IMPORTANT: the particle location is set to this value, thereby over-writing any previous module impacts.

### LocationOffset
- **类型**: `FRawDistributionVector`
- **描述**: An offset to apply to the position retrieved from the Location calculation.
The offset is retrieved using the EmitterTime.
The offset will remain constant over the life of the particle.

### ScaleFactor
- **类型**: `FRawDistributionVector`
- **描述**: Scales the velocity of the object at a given point in the time-line.

### Direction
- **类型**: `FRawDistributionVector`
- **描述**: Currently unused.

