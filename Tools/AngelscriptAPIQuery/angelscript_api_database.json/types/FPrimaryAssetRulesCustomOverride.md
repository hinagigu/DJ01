# FPrimaryAssetRulesCustomOverride

Apply primary asset rules to groups of primary assets, using type + filter directory or string

## 属性

### PrimaryAssetType
- **类型**: `FPrimaryAssetType`
- **描述**: Which type to apply rules for

### FilterDirectory
- **类型**: `FDirectoryPath`
- **描述**: Will only apply to files in this directory

### FilterString
- **类型**: `FString`
- **描述**: Game-specific string defining which assets to apply this to

### Rules
- **类型**: `FPrimaryAssetRules`
- **描述**: What to overrides the rules with

## 方法

### opAssign
```angelscript
FPrimaryAssetRulesCustomOverride& opAssign(FPrimaryAssetRulesCustomOverride Other)
```

