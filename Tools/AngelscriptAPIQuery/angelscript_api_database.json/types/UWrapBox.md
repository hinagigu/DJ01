# UWrapBox

**继承自**: `UPanelWidget`

Arranges widgets left-to-right or top-to-bottom dependently of the orientation.  When the widgets exceed the wrapSize it will place widgets on the next line.

* Many Children
* Flows
* Wraps

## 属性

### WrapSize
- **类型**: `float32`

### bExplicitWrapSize
- **类型**: `bool`

### Orientation
- **类型**: `EOrientation`

### InnerSlotPadding
- **类型**: `FVector2D`

### HorizontalAlignment
- **类型**: `EHorizontalAlignment`

## 方法

### AddChildToWrapBox
```angelscript
UWrapBoxSlot AddChildToWrapBox(UWidget Content)
```

### SetHorizontalAlignment
```angelscript
void SetHorizontalAlignment(EHorizontalAlignment InHorizontalAlignment)
```

### SetInnerSlotPadding
```angelscript
void SetInnerSlotPadding(FVector2D InPadding)
```
Sets the inner slot padding goes between slots sharing borders

