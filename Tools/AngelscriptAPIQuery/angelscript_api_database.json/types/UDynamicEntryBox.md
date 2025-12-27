# UDynamicEntryBox

**继承自**: `UDynamicEntryBoxBase`

A special box panel that auto-generates its entries at both design-time and runtime.
Useful for cases where you can have a varying number of entries, but it isn't worth the effort or conceptual overhead to set up a list/tile view.
Note that entries here are *not* virtualized as they are in the list views, so generally this should be avoided if you intend to scroll through lots of items.

No children can be manually added in the designer - all are auto-generated based on the given entry class.

## 属性

### NumDesignerPreviewEntries
- **类型**: `int`

### EntryWidgetClass
- **类型**: `TSubclassOf<UUserWidget>`

## 方法

### CreateEntry
```angelscript
UUserWidget CreateEntry()
```
Creates and establishes a new dynamic entry in the box

### CreateEntryOfClass
```angelscript
UUserWidget CreateEntryOfClass(TSubclassOf<UUserWidget> EntryClass)
```
Creates and establishes a new dynamic entry in the box using the specified class instead of the default.

### RemoveEntry
```angelscript
void RemoveEntry(UUserWidget EntryWidget)
```

### Reset
```angelscript
void Reset(bool bDeleteWidgets)
```
Clear out the box entries, optionally deleting the underlying Slate widgets entirely as well.

