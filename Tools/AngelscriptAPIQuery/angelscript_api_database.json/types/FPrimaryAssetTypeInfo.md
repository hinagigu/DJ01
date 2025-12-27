# FPrimaryAssetTypeInfo

Structure with publicly exposed information about an asset type. These can be loaded out of a config file or constructed at runtime

## 属性

### PrimaryAssetType
- **类型**: `FName`
- **描述**: The logical name for this type of Primary Asset

### AssetBaseClass
- **类型**: `TSoftClassPtr<UObject>`
- **描述**: Base Class of all assets of this type

### bHasBlueprintClasses
- **类型**: `bool`
- **描述**: True if the assets loaded are blueprints classes, false if they are normal UObjects

### bIsEditorOnly
- **类型**: `bool`
- **描述**: If true this type will not cause anything to be cooked; the AssetManager will use instances of this type to
define chunk assignments and NeverCook rules, but will ignore AlwaysCook rules. Assets labeled by instances
of this type will need to be reference by another PrimaryAsset, or by something outside the AssetManager,
to be cooked.

### Directories
- **类型**: `TArray<FDirectoryPath>`
- **描述**: Directories to search for this asset type

### SpecificAssets
- **类型**: `TArray<FSoftObjectPath>`
- **描述**: Individual assets to scan

### Rules
- **类型**: `FPrimaryAssetRules`
- **描述**: Default management rules for this type, individual assets can be overridden

## 方法

### opAssign
```angelscript
FPrimaryAssetTypeInfo& opAssign(FPrimaryAssetTypeInfo Other)
```

