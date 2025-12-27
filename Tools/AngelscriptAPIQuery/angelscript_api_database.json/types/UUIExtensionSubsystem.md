# UUIExtensionSubsystem

**继承自**: `UWorldSubsystem`

## 方法

### RegisterExtensionAsData
```angelscript
FUIExtensionHandle RegisterExtensionAsData(FGameplayTag ExtensionPointTag, UObject Data, int Priority)
```
Registers the extension as data for any extension point that can make use of it.

### RegisterExtensionAsDataForContext
```angelscript
FUIExtensionHandle RegisterExtensionAsDataForContext(FGameplayTag ExtensionPointTag, UObject ContextObject, UObject Data, int Priority)
```
Registers the extension as data for any extension point that can make use of it.

### RegisterExtensionAsWidget
```angelscript
FUIExtensionHandle RegisterExtensionAsWidget(FGameplayTag ExtensionPointTag, TSubclassOf<UUserWidget> WidgetClass, int Priority)
```

### RegisterExtensionAsWidgetForContext
```angelscript
FUIExtensionHandle RegisterExtensionAsWidgetForContext(FGameplayTag ExtensionPointTag, TSubclassOf<UUserWidget> WidgetClass, UObject ContextObject, int Priority)
```
Registers the widget (as data) for a specific player.  This means the extension points will receive a UIExtensionForPlayer data object
that they can look at to determine if it's for whatever they consider their player.

### RegisterExtensionPoint
```angelscript
FUIExtensionPointHandle RegisterExtensionPoint(FGameplayTag ExtensionPointTag, EUIExtensionPointMatch ExtensionPointTagMatchType, TArray<UClass> AllowedDataClasses, FExtendExtensionPointDynamicDelegate ExtensionCallback)
```

### UnregisterExtension
```angelscript
void UnregisterExtension(FUIExtensionHandle ExtensionHandle)
```

### UnregisterExtensionPoint
```angelscript
void UnregisterExtensionPoint(FUIExtensionPointHandle ExtensionPointHandle)
```

