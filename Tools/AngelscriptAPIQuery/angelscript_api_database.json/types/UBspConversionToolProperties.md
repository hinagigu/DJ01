# UBspConversionToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### ConversionMode
- **类型**: `EBspConversionMode`

### bIncludeVolumes
- **类型**: `bool`
- **描述**: Whether to consider BSP volumes to be valid conversion targets.

### bRemoveConvertedVolumes
- **类型**: `bool`
- **描述**: Whether to remove any selected BSP volumes after using them to create a static mesh.

### bExplicitSubtractiveBrushSelection
- **类型**: `bool`
- **描述**: Whether subtractive brushes have to be explicitly selected to be part of the conversion. If false, all
       subtractive brushes in the level will be used.

### bRemoveConvertedSubtractiveBrushes
- **类型**: `bool`
- **描述**: Whether subtractive brushes used in a conversion should be removed. Only acts on explicitly selected
       subtractive brushes.

### bCacheBrushes
- **类型**: `bool`
- **描述**: Caches individual brush conversions in "convert then combine" mode during a single invocation of
       the tool. Only useful if changing selections or properties after starting the tool. Cleared on tool shutdown.

### bShowPreview
- **类型**: `bool`
- **描述**: Determines whether a dynamic preview is shown. Note that this introduces non-background computations
      at each event that changes the result, rather than only performing a computation on Accept.

