# FAssetData

A struct to hold important information about an assets found by the Asset Registry
This struct is transient and should never be serialized

## 属性

### PackageName
- **类型**: `FName`
- **描述**: The name of the package in which the asset is found, this is the full long package name such as /Game/Path/Package

### PackagePath
- **类型**: `FName`
- **描述**: The path to the package in which the asset is found, this is /Game/Path with the Package stripped off

### AssetName
- **类型**: `FName`
- **描述**: The name of the asset without the package

### AssetClassPath
- **类型**: `FTopLevelAssetPath`
- **描述**: The path name of the asset's class

## 方法

### GetSoftObjectPath
```angelscript
FSoftObjectPath GetSoftObjectPath()
```

### GetObjectPathString
```angelscript
FString GetObjectPathString()
```

### IsInstanceOf
```angelscript
bool IsInstanceOf(const UClass BaseClass, bool bResolveClass)
```

### opAssign
```angelscript
FAssetData& opAssign(FAssetData Other)
```

