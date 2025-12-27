# UParticleModuleSubUVMovie

**继承自**: `UParticleModuleSubUV`

## 属性

### FrameRate
- **类型**: `FRawDistributionFloat`
- **描述**: The frame rate the SubUV images should be 'flipped' thru at.

### StartingFrame
- **类型**: `int`
- **描述**: The starting image index for the SubUV (1 = the first frame).
Assumes order of Left->Right, Top->Bottom
If greater than the last frame, it will clamp to the last one.
If 0, then randomly selects a starting frame.

### bUseEmitterTime
- **类型**: `bool`

