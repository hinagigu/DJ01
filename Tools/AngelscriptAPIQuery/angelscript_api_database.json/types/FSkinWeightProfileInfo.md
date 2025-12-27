# FSkinWeightProfileInfo

Structure storing user facing properties, and is used to identify profiles at the SkeletalMesh level

## 属性

### Name
- **类型**: `FName`
- **描述**: Name of the Skin Weight Profile

### DefaultProfile
- **类型**: `FPerPlatformBool`
- **描述**: Whether or not this Profile should be considered the Default loaded for specific LODs rather than the original Skin Weights of the Skeletal Mesh

### DefaultProfileFromLODIndex
- **类型**: `FPerPlatformInt`
- **描述**: When DefaultProfile is set any LOD below this LOD Index will override the Skin Weights of the Skeletal Mesh with the Skin Weights from this Profile

## 方法

### opAssign
```angelscript
FSkinWeightProfileInfo& opAssign(FSkinWeightProfileInfo Other)
```

