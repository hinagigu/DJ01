# USkeletalBodySetup

**继承自**: `UBodySetup`

## 属性

### CurrentPhysicalAnimationProfile
- **类型**: `FPhysicalAnimationProfile`
- **描述**: dummy place for customization inside phat. Profiles are ordered dynamically and we need a static place for detail customization

### bSkipScaleFromAnimation
- **类型**: `bool`
- **描述**: If true we ignore scale changes from animation. This is useful for subtle scale animations like breathing where the physics collision should remain unchanged

