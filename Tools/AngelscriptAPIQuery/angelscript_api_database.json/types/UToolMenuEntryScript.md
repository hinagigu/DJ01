# UToolMenuEntryScript

**继承自**: `UObject`

## 属性

### Data
- **类型**: `FToolMenuEntryScriptData`

## 方法

### CanExecute
```angelscript
bool CanExecute(FToolMenuContext Context)
```

### ConstructMenuEntry
```angelscript
void ConstructMenuEntry(UToolMenu Menu, FName SectionName, FToolMenuContext Context)
```

### Execute
```angelscript
void Execute(FToolMenuContext Context)
```

### GetCheckState
```angelscript
ECheckBoxState GetCheckState(FToolMenuContext Context)
```

### GetIcon
```angelscript
FScriptSlateIcon GetIcon(FToolMenuContext Context)
```

### GetLabel
```angelscript
FText GetLabel(FToolMenuContext Context)
```

### GetToolTip
```angelscript
FText GetToolTip(FToolMenuContext Context)
```

### InitEntry
```angelscript
void InitEntry(FName OwnerName, FName Menu, FName Section, FName Name, FText Label, FText ToolTip)
```

### IsVisible
```angelscript
bool IsVisible(FToolMenuContext Context)
```

### RegisterMenuEntry
```angelscript
void RegisterMenuEntry()
```

