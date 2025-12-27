# FARFilter

A struct to serve as a filter for Asset Registry queries. (mirrored in ARFilter.h)

## 属性

### PackageNames
- **类型**: `TArray<FName>`

### PackagePaths
- **类型**: `TArray<FName>`

### SoftObjectPaths
- **类型**: `TArray<FSoftObjectPath>`

### ClassPaths
- **类型**: `TArray<FTopLevelAssetPath>`

### RecursiveClassPathsExclusionSet
- **类型**: `TSet<FTopLevelAssetPath>`

### bRecursivePaths
- **类型**: `bool`

### bRecursiveClasses
- **类型**: `bool`

### bIncludeOnlyOnDiskAssets
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FARFilter& opAssign(FARFilter Other)
```

