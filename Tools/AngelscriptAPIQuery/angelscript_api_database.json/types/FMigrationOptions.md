# FMigrationOptions

## 属性

### bPrompt
- **类型**: `bool`
- **描述**: Prompt user for confirmation (always false through scripting)

### bIgnoreDependencies
- **类型**: `bool`
- **描述**: Ignore dependencies of assets, only migrate the given assets. usefull for automation. This will not migrate the actors of a OFPA (one file per actor) level

### AssetConflict
- **类型**: `EAssetMigrationConflict`
- **描述**: What to do when Assets are conflicting on the destination

### OrphanFolder
- **类型**: `FString`
- **描述**: Destination for assets that don't have a corresponding content folder. If left empty those assets are not migrated. (Not used by the new migration)

## 方法

### opAssign
```angelscript
FMigrationOptions& opAssign(FMigrationOptions Other)
```

