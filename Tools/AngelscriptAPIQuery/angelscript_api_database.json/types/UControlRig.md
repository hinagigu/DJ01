# UControlRig

**继承自**: `URigVMHost`

Runs logic for mapping input data to transforms (the "Rig")

## 属性

### OnControlSelected_BP
- **类型**: `FOnControlSelectedBP__ControlRig`

## 方法

### ClearControlSelection
```angelscript
bool ClearControlSelection()
```

### CreateTransformableControlHandle
```angelscript
UTransformableControlHandle CreateTransformableControlHandle(FName ControlName)
```
Creates a transformable control handle for the specified control to be used by the constraints system. Should use the UObject from
      ConstraintsScriptingLibrary::GetManager(UWorld* InWorld)

### CurrentControlSelection
```angelscript
TArray<FName> CurrentControlSelection()
```

### GetHierarchy
```angelscript
URigHierarchy GetHierarchy()
```

### GetHostingActor
```angelscript
AActor GetHostingActor()
```
Find the actor the rig is bound to, if any

### IsControlSelected
```angelscript
bool IsControlSelected(FName InControlName)
```

### RequestConstruction
```angelscript
void RequestConstruction()
```
Requests to perform construction during the next execution

### SelectControl
```angelscript
void SelectControl(FName InControlName, bool bSelect)
```

### SupportsBackwardsSolve
```angelscript
bool SupportsBackwardsSolve()
```
Contains a backwards solve event

