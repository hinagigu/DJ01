# FRigControlSettings

## 属性

### AnimationType
- **类型**: `ERigControlAnimationType`

### ControlType
- **类型**: `ERigControlType`

### DisplayName
- **类型**: `FName`

### PrimaryAxis
- **类型**: `ERigControlAxis`

### LimitEnabled
- **类型**: `TArray<FRigControlLimitEnabled>`

### bDrawLimits
- **类型**: `bool`

### MinimumValue
- **类型**: `FRigControlValue`
- **描述**: The minimum limit of the control's value

### MaximumValue
- **类型**: `FRigControlValue`
- **描述**: The maximum limit of the control's value

### bShapeVisible
- **类型**: `bool`

### ShapeVisibility
- **类型**: `ERigControlVisibility`

### ShapeName
- **类型**: `FName`

### ShapeColor
- **类型**: `FLinearColor`

### bIsTransientControl
- **类型**: `bool`
- **描述**: If the control is transient and only visible in the control rig editor

### ControlEnum
- **类型**: `UEnum`

### Customization
- **类型**: `FRigControlElementCustomization`

### DrivenControls
- **类型**: `TArray<FRigElementKey>`

### bGroupWithParentControl
- **类型**: `bool`

### bRestrictSpaceSwitching
- **类型**: `bool`

### FilteredChannels
- **类型**: `TArray<ERigControlTransformChannel>`

### PreferredRotationOrder
- **类型**: `EEulerRotationOrder`

### bUsePreferredRotationOrder
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FRigControlSettings& opAssign(FRigControlSettings Other)
```

