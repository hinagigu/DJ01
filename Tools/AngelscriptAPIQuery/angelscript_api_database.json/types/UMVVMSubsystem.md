# UMVVMSubsystem

**继承自**: `UEngineSubsystem`

## 方法

### DoesWidgetTreeContainedWidget
```angelscript
bool DoesWidgetTreeContainedWidget(const UWidgetTree WidgetTree, const UWidget ViewWidget)
```

### GetAvailableBinding
```angelscript
FMVVMAvailableBinding GetAvailableBinding(const UClass Class, FMVVMBindingName BindingName, const UClass Accessor)
```
@return The AvailableBinding from a BindingName.

### GetAvailableBindings
```angelscript
TArray<FMVVMAvailableBinding> GetAvailableBindings(const UClass Class, const UClass Accessor)
```
@return The list of all the AvailableBindings that are available for the Class.

### GetViewFromUserWidget
```angelscript
UMVVMView GetViewFromUserWidget(const UUserWidget UserWidget)
```

