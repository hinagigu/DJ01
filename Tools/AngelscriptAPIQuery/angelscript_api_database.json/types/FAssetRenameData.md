# FAssetRenameData

## 属性

### Asset
- **类型**: `TWeakObjectPtr<UObject>`
- **描述**: Object being renamed

### NewPackagePath
- **类型**: `FString`
- **描述**: New path to package without package name, ie /Game/SubDirectory

### NewName
- **类型**: `FString`
- **描述**: New package and asset name, new object path will be PackagePath/NewName.NewName

## 方法

### opAssign
```angelscript
FAssetRenameData& opAssign(FAssetRenameData Other)
```

