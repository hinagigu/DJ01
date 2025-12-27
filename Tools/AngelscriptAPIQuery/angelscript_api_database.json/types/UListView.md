# UListView

**继承自**: `UListViewBase`

A virtualized list that allows up to thousands of items to be displayed.

An important distinction to keep in mind here is "Item" vs. "Entry"
The list itself is based on a list of n items, but only creates as many entry widgets as can fit on screen.
For example, a scrolling ListView of 200 items with 5 currently visible will only have created 5 entry widgets.

To make a widget usable as an entry in a ListView, it must inherit from the IUserObjectListEntry interface.

## 属性

### WidgetStyle
- **类型**: `FTableViewStyle`

### ScrollBarStyle
- **类型**: `FScrollBarStyle`

### Orientation
- **类型**: `EOrientation`

### ConsumeMouseWheel
- **类型**: `EConsumeMouseWheel`

### bClearSelectionOnClick
- **类型**: `bool`

### bIsFocusable
- **类型**: `bool`

### bReturnFocusToSelection
- **类型**: `bool`

### BP_OnEntryInitialized
- **类型**: `FOnListEntryInitializedDynamic`

### BP_OnItemClicked
- **类型**: `FSimpleListItemEventDynamic`

### BP_OnItemDoubleClicked
- **类型**: `FSimpleListItemEventDynamic`

### BP_OnItemIsHoveredChanged
- **类型**: `FOnItemIsHoveredChangedDynamic`

### BP_OnItemSelectionChanged
- **类型**: `FOnListItemSelectionChangedDynamic`

### BP_OnItemScrolledIntoView
- **类型**: `FOnListItemScrolledIntoViewDynamic`

### BP_OnListViewScrolled
- **类型**: `FOnListViewScrolledDynamic`

### EntrySpacing
- **类型**: `float32`

### SelectionMode
- **类型**: `ESelectionMode`

### HorizontalEntrySpacing
- **类型**: `float32`

### VerticalEntrySpacing
- **类型**: `float32`

## 方法

### AddItem
```angelscript
void AddItem(UObject Item)
```
Adds an the item to the list

### CancelScrollIntoView
```angelscript
void CancelScrollIntoView()
```
Cancels a previous request to scroll and item into view.

### ClearSelection
```angelscript
void ClearSelection()
```
Clear selection

### GetNumItemsSelected
```angelscript
int GetNumItemsSelected()
```
Gets the number of items currently selected in the list

### GetSelectedItem
```angelscript
UObject GetSelectedItem()
```
Gets the first selected item, if any; recommended that you only use this for single selection lists.

### GetSelectedItems
```angelscript
bool GetSelectedItems(TArray<UObject>& Items)
```
Gets a list of all the currently selected items

### IsItemVisible
```angelscript
bool IsItemVisible(UObject Item)
```
Gets whether the entry for the given object is currently visible in the list

### NavigateToItem
```angelscript
void NavigateToItem(UObject Item)
```
Requests that the given item is navigated to, scrolling it into view if needed.

### ScrollItemIntoView
```angelscript
void ScrollItemIntoView(UObject Item)
```
Requests that the given item is scrolled into view

### SetItemSelection
```angelscript
void SetItemSelection(UObject Item, bool bSelected)
```
Sets whether the given item is selected.

### SetListItems
```angelscript
void SetListItems(TArray<UObject> InListItems)
```
Sets the array of objects to display rows for in the list

### SetSelectedItem
```angelscript
void SetSelectedItem(UObject Item)
```
Sets the given item as the sole selected item.

### ClearListItems
```angelscript
void ClearListItems()
```
Removes all items from the list

### GetHorizontalEntrySpacing
```angelscript
float32 GetHorizontalEntrySpacing()
```
Get the horizontal spacing between entries.

### GetIndexForItem
```angelscript
int GetIndexForItem(const UObject Item)
```
Returns the index that the specified item is at. Will return the first found, or -1 for not found

### GetItemAt
```angelscript
UObject GetItemAt(int Index)
```
Returns the item at the given index

### GetListItems
```angelscript
TArray<UObject> GetListItems()
```
Gets the list of all items in the list.
Note that each of these items only has a corresponding entry widget when visible. Use GetDisplayedEntryWidgets to get the currently displayed widgets.

### GetNumItems
```angelscript
int GetNumItems()
```
Returns the total number of items

### GetVerticalEntrySpacing
```angelscript
float32 GetVerticalEntrySpacing()
```
Get the vertical spacing between entries.

### IsRefreshPending
```angelscript
bool IsRefreshPending()
```
Returns true if a refresh is pending and the list will be rebuilt on the next tick

### NavigateToIndex
```angelscript
void NavigateToIndex(int Index)
```
Requests that the item at the given index navigated to, scrolling it into view if needed.

### RemoveItem
```angelscript
void RemoveItem(UObject Item)
```
Removes an the item from the list

### ScrollIndexIntoView
```angelscript
void ScrollIndexIntoView(int Index)
```
Requests that the item at the given index is scrolled into view

### SetSelectedIndex
```angelscript
void SetSelectedIndex(int Index)
```
Sets the item at the given index as the sole selected item.

### SetSelectionMode
```angelscript
void SetSelectionMode(ESelectionMode SelectionMode)
```
Sets the new selection mode, preserving the current selection where possible.

