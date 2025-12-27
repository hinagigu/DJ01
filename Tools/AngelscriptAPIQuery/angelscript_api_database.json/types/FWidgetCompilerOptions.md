# FWidgetCompilerOptions

## 属性

### bAllowBlueprintTick
- **类型**: `bool`
- **描述**: If you disable this, these widgets these compiler options apply to will not be allowed to implement Tick.

### bAllowBlueprintPaint
- **类型**: `bool`
- **描述**: If you disable this, these widgets these compiler options apply to will not be allowed to implement Paint.

### PropertyBindingRule
- **类型**: `EPropertyBindingPermissionLevel`
- **描述**: Controls if you allow property bindings in widgets.  They can have a large performance impact if used.

### Rules
- **类型**: `TArray<TSoftClassPtr<UWidgetCompilerRule>>`
- **描述**: Custom rules.

## 方法

### opAssign
```angelscript
FWidgetCompilerOptions& opAssign(FWidgetCompilerOptions Other)
```

