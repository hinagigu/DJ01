# UStreamableRenderAsset

**继承自**: `UObject`

## 属性

### NumCinematicMipLevels
- **类型**: `int`

### NeverStream
- **类型**: `bool`

### bGlobalForceMipLevelsToBeResident
- **类型**: `bool`

## 方法

### SetForceMipLevelsToBeResident
```angelscript
void SetForceMipLevelsToBeResident(float32 Seconds, int CinematicLODGroupMask)
```
Tells the streaming system that it should force all mip-levels to be resident for a number of seconds.
@param Seconds                                        Duration in seconds
@param CinematicTextureGroups Bitfield indicating which texture groups that use extra high-resolution mips

