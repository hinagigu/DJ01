# UBTTask_PlayAnimation

**继承自**: `UBTTaskNode`

Play indicated AnimationAsset on Pawn controlled by BT
Note that this node is generic and is handing multiple special cases,
If you want a more efficient solution you'll need to implement it yourself (or wait for our BTTask_PlayCharacterAnimation)

## 属性

### AnimationToPlay
- **类型**: `UAnimationAsset`
- **描述**: Animation asset to play. Note that it needs to match the skeleton of pawn this BT is controlling

### bLooping
- **类型**: `bool`

### bNonBlocking
- **类型**: `bool`

