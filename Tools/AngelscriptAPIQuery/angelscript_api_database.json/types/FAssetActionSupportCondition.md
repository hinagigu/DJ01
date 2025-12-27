# FAssetActionSupportCondition

## 属性

### Filter
- **类型**: `FString`
- **描述**: This is a content browser styled filter.  For example, ..._N AND VirtualTextureStreaming=FALSE, would require that
asset tag VirtualTextureStreaming be false, and the asset name end in _N.

You can learn more about the content browser search syntax in the "Advanced Search Syntax" documentation.

### FailureReason
- **类型**: `FString`
- **描述**: This is the failure reason to reply to the user with if the condition above fails.
If you fill in the reason, it will override the default failure text in the tooltip for the function menu option.

### bShowInMenuIfFilterFails
- **类型**: `bool`
- **描述**: If this filter does not pass, show the corresponding functions from the menu anyways.
If true, the menu option will display with the error tooltip, but be disabled.
If false, the menu options will be removed entirely.

## 方法

### opAssign
```angelscript
FAssetActionSupportCondition& opAssign(FAssetActionSupportCondition Other)
```

