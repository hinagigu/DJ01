# FMaterialLayersFunctionsEditorOnlyData

## 属性

### LayerStates
- **类型**: `TArray<bool>`

### LayerNames
- **类型**: `TArray<FText>`

### RestrictToLayerRelatives
- **类型**: `TArray<bool>`

### RestrictToBlendRelatives
- **类型**: `TArray<bool>`

### LayerGuids
- **类型**: `TArray<FGuid>`
- **描述**: Guid that identifies each layer in this stack

### LayerLinkStates
- **类型**: `TArray<EMaterialLayerLinkState>`
- **描述**: State of each layer's link to parent material

### DeletedParentLayerGuids
- **类型**: `TArray<FGuid>`
- **描述**: List of Guids that exist in the parent material that have been explicitly deleted
This is needed to distinguish these layers from newly added layers in the parent material

## 方法

### opAssign
```angelscript
FMaterialLayersFunctionsEditorOnlyData& opAssign(FMaterialLayersFunctionsEditorOnlyData Other)
```

