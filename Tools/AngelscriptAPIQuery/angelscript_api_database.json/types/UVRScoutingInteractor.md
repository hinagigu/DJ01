# UVRScoutingInteractor

**继承自**: `UVREditorInteractor`

Represents the interactor in the world

## 属性

### FlyingIndicatorComponent
- **类型**: `UStaticMeshComponent`

### bReceivesEditorInput
- **类型**: `bool`

## 方法

### GetGizmoMode
```angelscript
EGizmoHandleTypes GetGizmoMode()
```
Gets the gizmo mode for selected object

### GetInputComponent
```angelscript
UInputComponent GetInputComponent()
```
Returns the current InputComponent. This will be NULL unless bReceivesEditorInput is set to true.

### GetReceivesEditorInput
```angelscript
bool GetReceivesEditorInput()
```

### SetGizmoMode
```angelscript
void SetGizmoMode(EGizmoHandleTypes InGizmoMode)
```
Sets the gizmo mode for selected object

### SetReceivesEditorInput
```angelscript
void SetReceivesEditorInput(bool bInValue)
```

