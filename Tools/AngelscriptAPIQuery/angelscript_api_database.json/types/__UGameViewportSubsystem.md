# __UGameViewportSubsystem

## 方法

### SetWidgetSlotDesiredSize
```angelscript
FGameViewportWidgetSlot SetWidgetSlotDesiredSize(FGameViewportWidgetSlot Slot, FVector2D Size)
```
Helper function to set the desired size in the viewport for the Slot.

### SetWidgetSlotPosition
```angelscript
FGameViewportWidgetSlot SetWidgetSlotPosition(FGameViewportWidgetSlot Slot, const UWidget Widget, FVector2D Position, bool bRemoveDPIScale)
```
Helper function to set the position in the viewport for the Slot.
@param Position The 2D position to set the widget to in the viewport.
@param bRemoveDPIScale If you've already calculated inverse DPI, set this to false.
Otherwise inverse DPI is applied to the position so that when the location is scaled
by DPI, it ends up in the expected position.

### StaticClass
```angelscript
UClass StaticClass()
```

### Get
```angelscript
UGameViewportSubsystem Get()
```

