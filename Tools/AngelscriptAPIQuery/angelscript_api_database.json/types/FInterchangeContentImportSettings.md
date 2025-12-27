# FInterchangeContentImportSettings

## 属性

### DefaultPipelineStackOverride
- **类型**: `TMap<EInterchangeTranslatorAssetType,FName>`
- **描述**: Specifies a different pipeline stack for Interchange to use by default when importing specific types of assets.

### ShowImportDialogOverride
- **类型**: `TMap<EInterchangeTranslatorAssetType,FInterchangeDialogOverride>`
- **描述**: This tell interchange if the import dialog should show or not when importing a particular type of asset.

### PipelineStacks
- **类型**: `TMap<FName,FInterchangePipelineStack>`
- **描述**: Configures the pipeline stacks that are available when importing assets with Interchange.

### DefaultPipelineStack
- **类型**: `FName`
- **描述**: Specifies which pipeline stack Interchange should use by default.

### ImportDialogClass
- **类型**: `TSoftClassPtr<UInterchangePipelineConfigurationBase>`
- **描述**: Specifies the class that should be used to define the configuration dialog that Interchange shows on import.

### bShowImportDialog
- **类型**: `bool`
- **描述**: If enabled, the import option dialog will show when interchange import or re-import.

## 方法

### opAssign
```angelscript
FInterchangeContentImportSettings& opAssign(FInterchangeContentImportSettings Other)
```

