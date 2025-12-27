# __UToolMenuEntryExtensions

## 方法

### BreakScriptSlateIcon
```angelscript
void BreakScriptSlateIcon(FScriptSlateIcon InValue, FName& StyleSetName, FName& StyleName, FName& SmallStyleName)
```

### BreakStringCommand
```angelscript
void BreakStringCommand(FToolMenuStringCommand InValue, EToolMenuStringCommandType& Type, FName& CustomType, FString& String)
```

### BreakToolMenuOwner
```angelscript
void BreakToolMenuOwner(FToolMenuOwner InValue, FName& Name)
```

### GetLabel
```angelscript
FText GetLabel(FToolMenuEntry Target)
```

### GetToolTip
```angelscript
FText GetToolTip(FToolMenuEntry Target)
```

### InitMenuEntry
```angelscript
FToolMenuEntry InitMenuEntry(FName InOwner, FName InName, FText InLabel, FText InToolTip, EToolMenuStringCommandType CommandType, FName CustomCommandType, FString CommandString)
```

### MakeScriptSlateIcon
```angelscript
FScriptSlateIcon MakeScriptSlateIcon(FName StyleSetName, FName StyleName, FName SmallStyleName)
```

### MakeStringCommand
```angelscript
FToolMenuStringCommand MakeStringCommand(EToolMenuStringCommandType Type, FName CustomType, FString String)
```

### MakeToolMenuOwner
```angelscript
FToolMenuOwner MakeToolMenuOwner(FName Name)
```

### SetIcon
```angelscript
void SetIcon(FToolMenuEntry& Target, FName StyleSetName, FName StyleName, FName SmallStyleName)
```

### SetLabel
```angelscript
void SetLabel(FToolMenuEntry& Target, FText Label)
```

### SetStringCommand
```angelscript
void SetStringCommand(FToolMenuEntry& Target, EToolMenuStringCommandType Type, FName CustomType, FString String)
```

### SetToolTip
```angelscript
void SetToolTip(FToolMenuEntry& Target, FText ToolTip)
```

### StaticClass
```angelscript
UClass StaticClass()
```

