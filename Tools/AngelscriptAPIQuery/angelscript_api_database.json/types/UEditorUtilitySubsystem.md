# UEditorUtilitySubsystem

**继承自**: `UEditorSubsystem`

## 属性

### OnBeginPIE
- **类型**: `FOnEditorUtilityPIEEvent`

### OnEndPIE
- **类型**: `FOnEditorUtilityPIEEvent`

## 方法

### CanRun
```angelscript
bool CanRun(UObject Asset)
```

### CloseTabByID
```angelscript
bool CloseTabByID(FName NewTabID)
```
Given an ID for a tab, try to find and close an existing tab. Returns true if it found a tab to close.

### DoesTabExist
```angelscript
bool DoesTabExist(FName NewTabID)
```
Given an ID for a tab, try to find an existing tab. Returns true if it found a tab.

### FindUtilityWidgetFromBlueprint
```angelscript
UEditorUtilityWidget FindUtilityWidgetFromBlueprint(UEditorUtilityWidgetBlueprint InBlueprint)
```
Given an editor utility widget blueprint, get the widget it creates. This will return a null pointer if the widget is not currently in a tab.

### RegisterAndExecuteTask
```angelscript
void RegisterAndExecuteTask(UEditorUtilityTask NewTask, UEditorUtilityTask OptionalParentTask)
```

### RegisterTabAndGetID
```angelscript
void RegisterTabAndGetID(UEditorUtilityWidgetBlueprint InBlueprint, FName& NewTabID)
```

### RegisterTabAndGetIDGeneratedClass
```angelscript
void RegisterTabAndGetIDGeneratedClass(UWidgetBlueprintGeneratedClass InGeneratedWidgetBlueprint, FName& NewTabID)
```

### ReleaseInstanceOfAsset
```angelscript
void ReleaseInstanceOfAsset(UObject Asset)
```
Allow startup object to be garbage collected

### SpawnAndRegisterTab
```angelscript
UEditorUtilityWidget SpawnAndRegisterTab(UEditorUtilityWidgetBlueprint InBlueprint)
```

### SpawnAndRegisterTabAndGetID
```angelscript
UEditorUtilityWidget SpawnAndRegisterTabAndGetID(UEditorUtilityWidgetBlueprint InBlueprint, FName& NewTabID)
```

### SpawnAndRegisterTabAndGetIDGeneratedClass
```angelscript
UEditorUtilityWidget SpawnAndRegisterTabAndGetIDGeneratedClass(UWidgetBlueprintGeneratedClass InGeneratedWidgetBlueprint, FName& NewTabID)
```

### SpawnAndRegisterTabGeneratedClass
```angelscript
UEditorUtilityWidget SpawnAndRegisterTabGeneratedClass(UWidgetBlueprintGeneratedClass InGeneratedWidgetBlueprint)
```

### SpawnAndRegisterTabWithId
```angelscript
UEditorUtilityWidget SpawnAndRegisterTabWithId(UEditorUtilityWidgetBlueprint InBlueprint, FName InTabID)
```
Unlike SpawnAndRegisterTabAndGetID allows spawn tab while providing TabID from Python scripts or BP

### SpawnAndRegisterTabWithIdGeneratedClass
```angelscript
UEditorUtilityWidget SpawnAndRegisterTabWithIdGeneratedClass(UWidgetBlueprintGeneratedClass InGeneratedWidgetBlueprint, FName InTabID)
```
Unlike SpawnAndRegisterTabAndGetID allows spawn tab while providing TabID from Python scripts or BP

### SpawnRegisteredTabByID
```angelscript
bool SpawnRegisteredTabByID(FName NewTabID)
```
Given an ID for a tab, try to find a tab spawner that matches, and then spawn a tab. Returns true if it was able to find a matching tab spawner

### TryRun
```angelscript
bool TryRun(UObject Asset)
```

### TryRunClass
```angelscript
bool TryRunClass(UClass ObjectClass)
```

### UnregisterTabByID
```angelscript
bool UnregisterTabByID(FName TabID)
```
Given an ID for a tab, try to close and unregister a tab that was registered through this subsystem

