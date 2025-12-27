# USkeleton

**继承自**: `UObject`

USkeleton : that links between mesh and animation
        - Bone hierarchy for animations
        - Bone/track linkup between mesh and animation
        - Retargetting related

## 属性

### CompatibleSkeletons
- **类型**: `TArray<TSoftObjectPtr<USkeleton>>`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### AssetUserDataEditorOnly
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

## 方法

### AddCompatibleSkeleton
```angelscript
void AddCompatibleSkeleton(const USkeleton SourceSkeleton)
```

### AddCompatibleSkeletonSoft
```angelscript
void AddCompatibleSkeletonSoft(TSoftObjectPtr<USkeleton> SourceSkeleton)
```

### GetBlendProfile
```angelscript
UBlendProfile GetBlendProfile(FName InProfileName)
```
Get the specified blend profile by name

