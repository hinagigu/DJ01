# UUVEditorUVDistributeProperties

**继承自**: `UUVEditorUVTransformPropertiesBase`

UV Distribute Settings

## 属性

### DistributeMode
- **类型**: `EUVEditorDistributeMode`
- **描述**: Controls the distribution behavior

### Grouping
- **类型**: `EUVEditorAlignDistributeGroupingMode`
- **描述**: Controls how distribution considers grouping selected objects with respect to the distribution behavior.

### bEnableManualDistances
- **类型**: `bool`
- **描述**: If true, enable overriding distances used in the distribution behavior with manually entered values.

### ManualExtent
- **类型**: `float32`
- **描述**: For Edge and Center distribution modes, specify the desired overall distance within which to evenly place the edges or centers.

### ManualSpacing
- **类型**: `float32`
- **描述**: For Spacing and Remove Overlap distribution modes, specify the desired distance between objects.

