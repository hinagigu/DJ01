# UPrimaryGameLayout

**继承自**: `UCommonUserWidget`

The primary game UI layout of your game.  This widget class represents how to layout, push and display all layers
of the UI for a single player.  Each player in a split-screen game will receive their own primary game layout.

## 方法

### RegisterLayer
```angelscript
void RegisterLayer(FGameplayTag LayerTag, UCommonActivatableWidgetContainerBase LayerWidget)
```
Register a layer that widgets can be pushed onto.

