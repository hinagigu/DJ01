# UAnimationAsset

**继承自**: `UObject`

## 属性

### MetaData
- **类型**: `TArray<TObjectPtr<UAnimMetaData>>`
- **描述**: Meta data that can be saved with the asset

You can query by GetMetaData function

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

### PreviewPoseAsset
- **类型**: `UPoseAsset`
- **描述**: The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset// @todo: note that this doesn't retarget right now

## 方法

### FindMetaDataByClass
```angelscript
UAnimMetaData FindMetaDataByClass(TSubclassOf<UAnimMetaData> MetaDataClass)
```
Returns the first metadata of the specified class

### GetPlayLength
```angelscript
float32 GetPlayLength()
```

### SetPreviewSkeletalMesh
```angelscript
void SetPreviewSkeletalMesh(USkeletalMesh PreviewMesh)
```
Sets or updates the preview skeletal mesh

