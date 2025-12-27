# FDirectoryWidgetCompilerOptions

## 属性

### Directory
- **类型**: `FDirectoryPath`
- **描述**: The directory to limit the rules effects to.

### IgnoredWidgets
- **类型**: `TArray<TSoftObjectPtr<UWidgetBlueprint>>`
- **描述**: These widgets are ignored, and they will use the next most applicable directory to determine their rules.

### Options
- **类型**: `FWidgetCompilerOptions`
- **描述**: The directory specific compiler options for these widgets.

## 方法

### opAssign
```angelscript
FDirectoryWidgetCompilerOptions& opAssign(FDirectoryWidgetCompilerOptions Other)
```

