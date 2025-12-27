# UPoseAsset

**继承自**: `UAnimationAsset`

Pose Asset that can be blended by weight of curves

## 属性

### bAdditivePose
- **类型**: `bool`
- **描述**: Whether or not Additive Pose or not - these are property that needs post process, so

### RetargetSource
- **类型**: `FName`
- **描述**: Base pose to use when retargeting

### RetargetSourceAsset
- **类型**: `TSoftObjectPtr<USkeletalMesh>`
- **描述**: If RetargetSource is set to Default (None), this is asset for the base pose to use when retargeting. Transform data will be saved in RetargetSourceAssetReferencePose.

### SourceAnimation
- **类型**: `UAnimSequence`

## 方法

### GetBasePoseName
```angelscript
FName GetBasePoseName()
```
Returns base pose name, only valid when additive, NAME_None indicates reference pose

### GetPoseNames
```angelscript
void GetPoseNames(TArray<FName>& PoseNames)
```
Returns the name of all contained poses

### RenamePose
```angelscript
void RenamePose(FName OriginalPoseName, FName NewPoseName)
```
Renames a specific pose

### SetBasePoseName
```angelscript
bool SetBasePoseName(FName NewBasePoseName)
```
Set base pose index by name, NAME_None indicates reference pose - returns true if set successfully

### UpdatePoseFromAnimation
```angelscript
void UpdatePoseFromAnimation(UAnimSequence AnimSequence)
```
Contained poses are re-generated from the provided Animation Sequence

