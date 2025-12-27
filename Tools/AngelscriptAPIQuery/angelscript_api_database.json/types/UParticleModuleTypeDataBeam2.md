# UParticleModuleTypeDataBeam2

**继承自**: `UParticleModuleTypeDataBase`

## 属性

### BeamMethod
- **类型**: `EBeam2Method`
- **描述**: The method with which to form the beam(s). Must be one of the following:
        PEB2M_Distance  - Use the distance property to emit a beam along the X-axis of the emitter.
        PEB2M_Target    - Emit a beam from the source to the supplied target.
        PEB2M_Branch    - Currently unimplemented.

### TextureTile
- **类型**: `int`
- **描述**: The number of times to tile the texture along each beam.
Overridden by TextureTilingDistance if it is > 0.0.
    1st UV set only. 2nd UV set does not Tile.

### TextureTileDistance
- **类型**: `float32`
- **描述**: The distance per texture tile.
    1st UV set only. 2nd UV set does not Tile.

### Sheets
- **类型**: `int`
- **描述**: The number of sheets to render

### MaxBeamCount
- **类型**: `int`
- **描述**: The number of live beams

### Speed
- **类型**: `float32`
- **描述**: The speed at which the beam should move from source to target when firing up.
    '0' indicates instantaneous

### InterpolationPoints
- **类型**: `int`
- **描述**: Indicates whether the beam should be interpolated.
    <= 0 --> no
    >  0 --> yes (and is equal to the number of interpolation steps that should be taken.

### UpVectorStepSize
- **类型**: `int`
- **描述**: The approach to use for determining the Up vector(s) for the beam.

0 indicates that the Up FVector should be calculated at EVERY point in the beam.
1 indicates a single Up FVector should be determined at the start of the beam and used at every point.
N indicates an Up FVector should be calculated every N points of the beam and interpolated between them.
    [NOTE: This mode is currently unsupported.]

### BranchParentName
- **类型**: `FName`
- **描述**: The name of the emitter to branch from (if mode is PEB2M_Branch)
MUST BE IN THE SAME PARTICLE SYSTEM!

### Distance
- **类型**: `FRawDistributionFloat`
- **描述**: The distance along the X-axis to stretch the beam
Distance is only used if BeamMethod is PEB2M_Distance

### TaperMethod
- **类型**: `EBeamTaperMethod`
- **描述**: Tapering mode - one of the following:
PEBTM_None              - No tapering is applied
PEBTM_Full              - Taper the beam relative to source-->target, regardless of current beam length
PEBTM_Partial   - Taper the beam relative to source-->location, 0=source,1=endpoint

### TaperFactor
- **类型**: `FRawDistributionFloat`
- **描述**: Tapering factor, 0 = source of beam, 1 = target

### TaperScale
- **类型**: `FRawDistributionFloat`
- **描述**: Tapering scaling
    This is intended to be either a constant, uniform or a ParticleParam.
    If a curve is used, 0/1 mapping of source/target... which could be integrated into
    the taper factor itself, and therefore makes no sense.

### bAlwaysOn
- **类型**: `bool`

### RenderGeometry
- **类型**: `bool`

### RenderDirectLine
- **类型**: `bool`

### RenderLines
- **类型**: `bool`

### RenderTessellation
- **类型**: `bool`

