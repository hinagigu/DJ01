# UZeroOutRootBoneModifier

**继承自**: `UAnimationModifier`

Adjust root motion to be relative to the first frame. Optionally cut the start and end sections of the animation that don't have motion on the root.
      This was written to be used when capturing Character Movement motion via Take Recorder. Take Recorder outputs an animation captured from
      a character moving in game in world space, and this modifier zeroes out the root. The animation can then be exported to fbx to be animated against.

## 属性

### bClipStartFramesWithNoMotion
- **类型**: `bool`

### bClipEndFramesWithNoMotion
- **类型**: `bool`

