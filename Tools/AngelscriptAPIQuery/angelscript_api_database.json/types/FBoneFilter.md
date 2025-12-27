# FBoneFilter

## 属性

### bExcludeSelf
- **类型**: `bool`
- **描述**: * Do not include the joint specified
*
* This option will work differently based on EBoneFilterActionOption
* If EBoneFilterActionOption is Remove, it will exclude itself and only remove children
* For example, if you specify hand, it will only include children of hand(all fingers),
* not the hand itself if this is true
*
* But if the EBoneFilterActionOption is Keep, it will exclude itself but include all parents of it
* You can't remove joint without children removed, and you can't keep without your parents

### BoneName
- **类型**: `FName`
- **描述**: Name of Bone Name

## 方法

### opAssign
```angelscript
FBoneFilter& opAssign(FBoneFilter Other)
```

