# FRigControl

## 属性

### ControlType
- **类型**: `ERigControlType`

### DisplayName
- **类型**: `FName`

### ParentName
- **类型**: `FName`

### ParentIndex
- **类型**: `int`

### SpaceName
- **类型**: `FName`

### SpaceIndex
- **类型**: `int`

### OffsetTransform
- **类型**: `FTransform`

### InitialValue
- **类型**: `FRigControlValue`
- **描述**: The value that a control is reset to during begin play or when the
control rig is instantiated.

### Value
- **类型**: `FRigControlValue`
- **描述**: The current value of the control.

### PrimaryAxis
- **类型**: `ERigControlAxis`

### bAnimatable
- **类型**: `bool`

### bLimitTranslation
- **类型**: `bool`

### bLimitRotation
- **类型**: `bool`

### bLimitScale
- **类型**: `bool`

### bDrawLimits
- **类型**: `bool`

### MinimumValue
- **类型**: `FRigControlValue`

### MaximumValue
- **类型**: `FRigControlValue`

### bGizmoEnabled
- **类型**: `bool`

### bGizmoVisible
- **类型**: `bool`

### GizmoName
- **类型**: `FName`

### GizmoTransform
- **类型**: `FTransform`

### GizmoColor
- **类型**: `FLinearColor`

### bIsTransientControl
- **类型**: `bool`

### ControlEnum
- **类型**: `UEnum`

### Name
- **类型**: `FName`

### Index
- **类型**: `int`

## 方法

### opAssign
```angelscript
FRigControl& opAssign(FRigControl Other)
```

