# UMVVMEditorSubsystem

**继承自**: `UEditorSubsystem`

## 方法

### AddBinding
```angelscript
FMVVMBlueprintViewBinding& AddBinding(UWidgetBlueprint WidgetBlueprint)
```

### AddEvent
```angelscript
UMVVMBlueprintViewEvent AddEvent(UWidgetBlueprint WidgetBlueprint)
```

### AddInstancedViewModel
```angelscript
FGuid AddInstancedViewModel(UWidgetBlueprint WidgetBlueprint)
```

### AddViewModel
```angelscript
FGuid AddViewModel(UWidgetBlueprint WidgetBlueprint, const UClass ViewModel)
```

### GetAvailableConversionFunctions
```angelscript
TArray<UFunction> GetAvailableConversionFunctions(const UWidgetBlueprint WidgetBlueprint, FMVVMBlueprintPropertyPath Source, FMVVMBlueprintPropertyPath Destination)
```

### GetChildViewModels
```angelscript
TArray<FMVVMAvailableBinding> GetChildViewModels(TSubclassOf<UObject> Class, TSubclassOf<UObject> Accessor)
```

### GetConversionFunction
```angelscript
UFunction GetConversionFunction(const UWidgetBlueprint WidgetBlueprint, FMVVMBlueprintViewBinding Binding, bool bSourceToDestination)
```

### GetConversionFunctionGraph
```angelscript
UEdGraph GetConversionFunctionGraph(const UWidgetBlueprint WidgetBlueprint, FMVVMBlueprintViewBinding Binding, bool bSourceToDestination)
```

### GetConversionFunctionNode
```angelscript
UK2Node_CallFunction GetConversionFunctionNode(const UWidgetBlueprint WidgetBlueprint, FMVVMBlueprintViewBinding Binding, bool bSourceToDestination)
```

### GetView
```angelscript
UMVVMBlueprintView GetView(const UWidgetBlueprint WidgetBlueprint)
```

### IsSimpleConversionFunctionA
```angelscript
bool IsSimpleConversionFunctionA(const UFunction Function)
```

### IsValidConversionFunction
```angelscript
bool IsValidConversionFunction(const UWidgetBlueprint WidgetBlueprint, const UFunction Function, FMVVMBlueprintPropertyPath Source, FMVVMBlueprintPropertyPath Destination)
```

### RemoveBinding
```angelscript
void RemoveBinding(UWidgetBlueprint WidgetBlueprint, FMVVMBlueprintViewBinding Binding)
```

### RemoveEvent
```angelscript
void RemoveEvent(UWidgetBlueprint WidgetBlueprint, UMVVMBlueprintViewEvent Event)
```

### RemoveViewModel
```angelscript
void RemoveViewModel(UWidgetBlueprint WidgetBlueprint, FName ViewModel)
```

### RenameViewModel
```angelscript
bool RenameViewModel(UWidgetBlueprint WidgetBlueprint, FName ViewModel, FName NewViewModel, FText& OutError)
```

### ReparentViewModel
```angelscript
bool ReparentViewModel(UWidgetBlueprint WidgetBlueprint, FName ViewModel, const UClass NewViewModel, FText& OutError)
```

### RequestView
```angelscript
UMVVMBlueprintView RequestView(UWidgetBlueprint WidgetBlueprint)
```

### VerifyViewModelRename
```angelscript
bool VerifyViewModelRename(UWidgetBlueprint WidgetBlueprint, FName ViewModel, FName NewViewModel, FText& OutError)
```

