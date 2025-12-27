# UMaterialFunction

**继承自**: `UMaterialFunctionInterface`

A Material Function is a collection of material expressions that can be reused in different materials

## 属性

### Description
- **类型**: `FString`
- **描述**: Description of the function which will be displayed as a tooltip wherever the function is used.

### UserExposedCaption
- **类型**: `FString`
- **描述**: Name of the function to be displayed on the node within the material editor instead of the asset name.

### LibraryCategoriesText
- **类型**: `TArray<FText>`
- **描述**: Categories that this function belongs to in the material function library.
Ideally categories should be chosen carefully so that there are not too many.

### PreviewBlendMode
- **类型**: `EBlendMode`
- **描述**: Determines the blend mode when previewing a material function.

### bExposeToLibrary
- **类型**: `bool`

### bPrefixParameterNames
- **类型**: `bool`

### bEnableExecWire
- **类型**: `bool`

### bEnableNewHLSLGenerator
- **类型**: `bool`

