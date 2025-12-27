# UGameViewportSubsystem

**继承自**: `UEngineSubsystem`

## 方法

### AddWidget
```angelscript
bool AddWidget(UWidget Widget, FGameViewportWidgetSlot Slot)
```
Adds it to the game's viewport.

### AddWidgetForPlayer
```angelscript
bool AddWidgetForPlayer(UWidget Widget, ULocalPlayer Player, FGameViewportWidgetSlot Slot)
```
Adds the widget to the game's viewport in the section dedicated to the player. This is valuable in a split screen
game where you need to only show a widget over a player's portion of the viewport.

### GetWidgetSlot
```angelscript
FGameViewportWidgetSlot GetWidgetSlot(const UWidget Widget)
```
The slot info from previously added widget or info that is store for later.

### IsWidgetAdded
```angelscript
bool IsWidgetAdded(const UWidget Widget)
```
@return true if the widget was added to the viewport using AddWidget or AddWidgetForPlayer.

### RemoveWidget
```angelscript
void RemoveWidget(UWidget Widget)
```
Removes the widget from the viewport.

### SetWidgetSlot
```angelscript
void SetWidgetSlot(UWidget Widget, FGameViewportWidgetSlot Slot)
```
Update the slot info of a previously added widget or Store the slot info for later use.

