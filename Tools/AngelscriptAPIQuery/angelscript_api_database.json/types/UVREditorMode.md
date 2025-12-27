# UVREditorMode

**继承自**: `UVREditorModeBase`

VR Editor Mode. Extends editor viewports with functionality for VR controls and object manipulation

## 属性

### InteractorClass
- **类型**: `TSoftClassPtr<UVREditorInteractor>`

### TeleporterClass
- **类型**: `TSoftClassPtr<AVREditorTeleporter>`

## 方法

### GetWorldScaleFactor
```angelscript
float32 GetWorldScaleFactor()
```
Gets the world scale factor, which can be multiplied by a scale vector to convert to room space

### IsInGameView
```angelscript
bool IsInGameView()
```
Returns whether game view is currently active.

### SetGameView
```angelscript
void SetGameView(bool bGameView)
```
Display the scene more closely to how it would appear at runtime (as opposed to edit time).

