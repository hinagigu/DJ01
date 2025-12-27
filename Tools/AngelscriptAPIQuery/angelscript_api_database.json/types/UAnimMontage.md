# UAnimMontage

**继承自**: `UAnimCompositeBase`

Any property you're adding to AnimMontage and parent class has to be considered for Child Asset

Child Asset is considered to be only asset mapping feature using everything else in the class
For example, you can just use all parent's setting  for the montage, but only remap assets
This isn't magic bullet unfortunately and it is consistent effort of keeping the data synced with parent
If you add new property, please make sure those property has to be copied for children.
If it does, please add the copy in the function RefreshParentAssetData

## 属性

### BlendModeIn
- **类型**: `EMontageBlendMode`

### BlendModeOut
- **类型**: `EMontageBlendMode`

### BlendIn
- **类型**: `FAlphaBlend`
- **描述**: Blend in option.

### BlendOut
- **类型**: `FAlphaBlend`
- **描述**: Blend out option. This is only used when it blends out itself. If it's interrupted by other montages, it will use new montage's BlendIn option to blend out.

### BlendOutTriggerTime
- **类型**: `float32`
- **描述**: Time from Sequence End to trigger blend out.
<0 means using BlendOutTime, so BlendOut finishes as Montage ends.
>=0 means using 'SequenceEnd - BlendOutTriggerTime' to trigger blend out.

### SyncGroup
- **类型**: `FName`
- **描述**: If you're using marker based sync for this montage, make sure to add sync group name. For now we only support one group

### SyncSlotIndex
- **类型**: `int`
- **描述**: Index of the slot track used for collecting sync markers

### bEnableAutoBlendOut
- **类型**: `bool`
- **描述**: When it hits end, it automatically blends out. If this is false, it won't blend out but keep the last pose until stopped explicitly

### BlendProfileIn
- **类型**: `UBlendProfile`

### BlendProfileOut
- **类型**: `UBlendProfile`

### PreviewBasePose
- **类型**: `UAnimSequence`
- **描述**: Preview Base pose for additive BlendSpace *

### TimeStretchCurve
- **类型**: `FTimeStretchCurve`
- **描述**: Time stretch curve will only be used when the montage has a non-default play rate

### TimeStretchCurveName
- **类型**: `FName`
- **描述**: Name of optional TimeStretchCurveName to look for in Montage. Time stretch curve will only be used when the montage has a non-default play rate

## 方法

### GetBlendInArgs
```angelscript
FAlphaBlendArgs GetBlendInArgs()
```

### GetBlendOutArgs
```angelscript
FAlphaBlendArgs GetBlendOutArgs()
```

### GetDefaultBlendInTime
```angelscript
float32 GetDefaultBlendInTime()
```

### GetDefaultBlendOutTime
```angelscript
float32 GetDefaultBlendOutTime()
```

### GetFirstAnimReference
```angelscript
UAnimSequenceBase GetFirstAnimReference()
```

### GetGroupName
```angelscript
FName GetGroupName()
```
Get the Montage's Group Name. This is the group from the first slot.

### GetNumSections
```angelscript
int GetNumSections()
```
Returns the number of sections this montage has

### GetSectionIndex
```angelscript
int GetSectionIndex(FName InSectionName)
```
Get SectionIndex from SectionName. Returns INDEX_None if not found

### GetSectionName
```angelscript
FName GetSectionName(int SectionIndex)
```
Get SectionName from SectionIndex. Returns NAME_None if not found

### IsDynamicMontage
```angelscript
bool IsDynamicMontage()
```

### IsValidAdditiveSlot
```angelscript
bool IsValidAdditiveSlot(FName SlotNodeName)
```
Check if this slot has a valid additive animation for the specified slot.
The slot name should not include the group name.
i.e. for "DefaultGroup.DefaultSlot", the slot name is "DefaultSlot".

### IsValidSectionName
```angelscript
bool IsValidSectionName(FName InSectionName)
```
@return true if valid section

