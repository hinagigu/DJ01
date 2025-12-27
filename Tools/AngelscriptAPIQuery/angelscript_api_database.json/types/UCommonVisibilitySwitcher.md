# UCommonVisibilitySwitcher

**继承自**: `UOverlay`

Basic switcher that toggles visibility on its children to only show one widget at a time. Activates visible widget if possible.

## 属性

### ShownVisibility
- **类型**: `ESlateVisibility`

### bAutoActivateSlot
- **类型**: `bool`
- **描述**: Whether or not to automatically activate a slot when it becomes visible

### bActivateFirstSlotOnAdding
- **类型**: `bool`
- **描述**: Whether or not to activate the first slot if one is added dynamically

## 方法

### ActivateVisibleSlot
```angelscript
void ActivateVisibleSlot()
```

### DeactivateVisibleSlot
```angelscript
void DeactivateVisibleSlot()
```

### DecrementActiveWidgetIndex
```angelscript
void DecrementActiveWidgetIndex(bool bAllowWrapping)
```

### GetActiveWidget
```angelscript
UWidget GetActiveWidget()
```

### GetActiveWidgetIndex
```angelscript
int GetActiveWidgetIndex()
```

### IncrementActiveWidgetIndex
```angelscript
void IncrementActiveWidgetIndex(bool bAllowWrapping)
```

### IsCurrentlySwitching
```angelscript
bool IsCurrentlySwitching()
```

### SetActiveWidget
```angelscript
void SetActiveWidget(const UWidget Widget)
```

### SetActiveWidgetIndex
```angelscript
void SetActiveWidgetIndex(int Index)
```

