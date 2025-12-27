# UTileView

**继承自**: `UListView`

A ListView that presents the contents as a set of tiles all uniformly sized.

To make a widget usable as an entry in a TileView, it must inherit from the IUserObjectListEntry interface.

## 属性

### TileAlignment
- **类型**: `EListItemAlignment`
- **描述**: The method by which to align the tile entries in the available space for the tile view

### bWrapHorizontalNavigation
- **类型**: `bool`
- **描述**: True to allow left/right navigation to wrap back to the tile on the opposite edge

### ScrollbarDisabledVisibility
- **类型**: `ESlateVisibility`
- **描述**: Set the visibility of the Scrollbar when it's not needed

### bEntrySizeIncludesEntrySpacing
- **类型**: `bool`
- **描述**: True if entry dimensions should be the sum of the entry widget dimensions and the spacing.
This means the size of the entry widget will be adjusted so that the summation of the widget size and entry spacing always equals entry size.

## 方法

### GetEntryHeight
```angelscript
float32 GetEntryHeight()
```
Gets the height of tile entries

### GetEntryWidth
```angelscript
float32 GetEntryWidth()
```
Gets the width of tile entries

### SetEntryHeight
```angelscript
void SetEntryHeight(float32 NewHeight)
```
Sets the height of every tile entry

### SetEntryWidth
```angelscript
void SetEntryWidth(float32 NewWidth)
```
Sets the width of every tile entry

