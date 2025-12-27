# ALevelBounds

**继承自**: `AActor`

Defines level bounds
Updates bounding box automatically based on actors transformation changes or holds fixed user defined bounding box
Uses only actors where AActor::IsLevelBoundsRelevant() == true

## 属性

### BoxComponent
- **类型**: `UBoxComponent`
- **描述**: Bounding box for the level bounds.

### bAutoUpdateBounds
- **类型**: `bool`
- **描述**: Whether to automatically update actor bounds based on all relevant actors bounds belonging to the same level

