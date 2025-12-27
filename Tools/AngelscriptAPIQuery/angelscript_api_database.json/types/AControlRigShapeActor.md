# AControlRigShapeActor

**继承自**: `AActor`

An actor used to represent a rig control

## 属性

### StaticMeshComponent
- **类型**: `UStaticMeshComponent`

### bSelected
- **类型**: `bool`

### bHovered
- **类型**: `bool`

## 方法

### GetGlobalTransform
```angelscript
FTransform GetGlobalTransform()
```

### IsEnabled
```angelscript
bool IsEnabled()
```
Get whether the control is enabled/disabled

### IsHovered
```angelscript
bool IsHovered()
```
Get whether the control is hovered

### IsSelectedInEditor
```angelscript
bool IsSelectedInEditor()
```
Get whether the control is selected/unselected

### OnEnabledChanged
```angelscript
void OnEnabledChanged(bool bIsEnabled)
```
Event called when the enabled state of this control has changed

### OnHoveredChanged
```angelscript
void OnHoveredChanged(bool bIsSelected)
```
Event called when the hovered state of this control has changed

### OnManipulatingChanged
```angelscript
void OnManipulatingChanged(bool bIsManipulating)
```
Event called when the manipulating state of this control has changed

### OnSelectionChanged
```angelscript
void OnSelectionChanged(bool bIsSelected)
```
Event called when the selection state of this control has changed

### OnTransformChanged
```angelscript
void OnTransformChanged(FTransform NewTransform)
```
Event called when the transform of this control has changed

### SetEnabled
```angelscript
void SetEnabled(bool bInEnabled)
```
Set the control to be enabled/disabled

### SetGlobalTransform
```angelscript
void SetGlobalTransform(FTransform InTransform)
```
this returns root component transform based on attach
when there is no attach, it is based on 0

### SetHovered
```angelscript
void SetHovered(bool bInHovered)
```
Set the control to be hovered

### SetSelectable
```angelscript
void SetSelectable(bool bInSelectable)
```
Set the control to be selected/unselected

### SetSelected
```angelscript
void SetSelected(bool bInSelected)
```
Set the control to be selected/unselected

