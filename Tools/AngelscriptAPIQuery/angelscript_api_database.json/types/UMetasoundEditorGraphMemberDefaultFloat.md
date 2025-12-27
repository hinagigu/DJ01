# UMetasoundEditorGraphMemberDefaultFloat

**继承自**: `UMetasoundEditorGraphMemberDefaultLiteral`

## 属性

### Default
- **类型**: `float32`

### ClampDefault
- **类型**: `bool`

### Range
- **类型**: `FVector2D`

### WidgetType
- **类型**: `EMetasoundMemberDefaultWidget`

### WidgetOrientation
- **类型**: `EOrientation`

### WidgetValueType
- **类型**: `EMetasoundMemberDefaultWidgetValueType`

### VolumeWidgetUseLinearOutput
- **类型**: `bool`
- **描述**: If true, output linear value. Otherwise, output dB value. The volume widget itself will always display the value in dB. The Default Value and Range are linear.

### VolumeWidgetDecibelRange
- **类型**: `FVector2D`
- **描述**: Range in decibels. This will be converted to the linear range in the Default Value category.

