# FValidateAssetsResults

## 属性

### NumRequested
- **类型**: `int`
- **描述**: Total amount of assets that were gathered to validate.

### NumChecked
- **类型**: `int`
- **描述**: Amount of tested assets

### NumValid
- **类型**: `int`
- **描述**: Amount of assets without errors or warnings

### NumInvalid
- **类型**: `int`
- **描述**: Amount of assets with errors

### NumSkipped
- **类型**: `int`
- **描述**: Amount of assets skipped

### NumWarnings
- **类型**: `int`
- **描述**: Amount of assets with warnings

### NumUnableToValidate
- **类型**: `int`
- **描述**: Amount of assets that could not be validated

### bAssetLimitReached
- **类型**: `bool`
- **描述**: True if FValidateAssetSettings::MaxAssetsToValidation was reached

### AssetsDetails
- **类型**: `TMap<FString,FValidateAssetsDetails>`
- **描述**: Per asset details
Indexed by object path
Only returned if FValidateAssetsSettings::bCollectPerAssetDetails is true.

## 方法

### opAssign
```angelscript
FValidateAssetsResults& opAssign(FValidateAssetsResults Other)
```

