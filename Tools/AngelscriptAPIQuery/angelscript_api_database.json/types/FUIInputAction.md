# FUIInputAction

## 属性

### ActionTag
- **类型**: `FUIActionTag`
- **描述**: The UI.Action tag that acts as the universal identifier of this action.

### DefaultDisplayName
- **类型**: `FText`
- **描述**: Whenever a UI input action is bound, an override display name can optionally be provided.
This is the default generic display name of this action for use in the absence of such an override.

### KeyMappings
- **类型**: `TArray<FUIActionKeyMapping>`
- **描述**: All key mappings that will trigger this action

## 方法

### opAssign
```angelscript
FUIInputAction& opAssign(FUIInputAction Other)
```

