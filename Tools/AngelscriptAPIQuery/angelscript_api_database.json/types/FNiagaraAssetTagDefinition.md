# FNiagaraAssetTagDefinition

An Asset Tag Definition defines a tag that can be added to various Niagara assets for sorting & filtering purposes.

## 属性

### AssetTag
- **类型**: `FText`
- **描述**: The Display Name used for this tag.

### AssetFlags
- **类型**: `int`
- **描述**: Select the asset types this tag can apply to. This is used to hide tags that can never apply for a given type.

### Description
- **类型**: `FText`
- **描述**: Further explanation of what this tag is about.

### DisplayType
- **类型**: `ENiagaraAssetTagDefinitionImportance`
- **描述**: Whether this tag should be shown directly or in the drop down for additional filters.

### Color
- **类型**: `FLinearColor`
- **描述**: The color used in UI to represent this tag.

## 方法

### opAssign
```angelscript
FNiagaraAssetTagDefinition& opAssign(FNiagaraAssetTagDefinition Other)
```

