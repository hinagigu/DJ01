# UListViewBase

**继承自**: `UWidget`

Bare-bones base class to make creating custom UListView widgets easier.
Child classes should also inherit from ITypedUMGListView<T> to get a basic public ListView API for free.

Child classes will own the actual SListView<T> widgets, but this provides some boilerplate functionality for generating entries.
To generate a row for the child list, use GenerateTypedRow with the appropriate SObjectTableRow<T> type for your list

Additionally, the entry widget class can be filtered for a particular class and interface with the EntryClass and EntryInterface metadata arguments
This can be specified either on the class directly (see below) or on any BindWidget FProperty

Example:
class UMyUserWidget : public UUserWidget
{
            UPROPERTY(BindWidget, meta = (EntryClass = MyListEntryWidget))
            UListView* ListView_InventoryItems;
}

## 属性

### BP_OnEntryGenerated
- **类型**: `FOnListEntryGeneratedDynamic`

### EntryWidgetClass
- **类型**: `TSubclassOf<UUserWidget>`

### bEnableScrollAnimation
- **类型**: `bool`

### bInEnableTouchAnimatedScrolling
- **类型**: `bool`

### AllowOverscroll
- **类型**: `bool`
- **描述**: Disable to stop scrollbars from activating inertial overscrolling

### bEnableRightClickScrolling
- **类型**: `bool`
- **描述**: True to allow right click drag scrolling.

### bEnableTouchScrolling
- **类型**: `bool`
- **描述**: True to allow scrolling using touch input.

### bIsPointerScrollingEnabled
- **类型**: `bool`
- **描述**: Enable/Disable scrolling using Touch or Mouse.

### bEnableFixedLineOffset
- **类型**: `bool`

### FixedLineScrollOffset
- **类型**: `float32`
- **描述**: Optional fixed offset (in lines) to always apply to the top/left (depending on orientation) of the list.
If provided, all non-inertial means of scrolling will settle with exactly this offset of the topmost entry.
Ex: A value of 0.25 would cause the topmost full entry to be offset down by a quarter length of the preceeding entry.

### bAllowDragging
- **类型**: `bool`

### BP_OnEntryReleased
- **类型**: `FOnListEntryReleasedDynamic`

### NumDesignerPreviewEntries
- **类型**: `int`
- **描述**: The number of dummy item entry widgets to preview in the widget designer

### WheelScrollMultiplier
- **类型**: `float32`

## 方法

### GetDisplayedEntryWidgets
```angelscript
TArray<UUserWidget> GetDisplayedEntryWidgets()
```
Gets all of the list entry widgets currently being displayed by the list

### GetScrollOffset
```angelscript
float32 GetScrollOffset()
```
Get the scroll offset of this view (in items)

### RegenerateAllEntries
```angelscript
void RegenerateAllEntries()
```
Full regeneration of all entries in the list. Note that the entry UWidget instances will not be destroyed, but they will be released and re-generated.
In other words, entry widgets will not receive Destruct/Construct events. They will receive OnEntryReleased and IUserObjectListEntry implementations will receive OnListItemObjectSet.

### RequestRefresh
```angelscript
void RequestRefresh()
```
Sets the list to refresh on the next tick.

Note that refreshing, from a list perspective, is limited to accounting for discrepancies between items and entries.
In other words, it will only release entries that no longer have items and generate entries for new items (or newly visible items).

It does NOT account for changes within existing items - that is up to the item to announce and an entry to listen to as needed.
This can be onerous to set up for simple cases, so it's also reasonable (though not ideal) to call RegenerateAllEntries when changes within N list items need to be reflected.

### ScrollToBottom
```angelscript
void ScrollToBottom()
```
Scroll the entire list down to the bottom-most item

### ScrollToTop
```angelscript
void ScrollToTop()
```
Scroll the entire list up to the first item

### SetIsPointerScrollingEnabled
```angelscript
void SetIsPointerScrollingEnabled(bool bInIsPointerScrollingEnabled)
```
Enable/Disable the ability of the list to scroll. This should be use as a temporary disable.

### SetScrollbarVisibility
```angelscript
void SetScrollbarVisibility(ESlateVisibility InVisibility)
```

### SetScrollOffset
```angelscript
void SetScrollOffset(float32 InScrollOffset)
```
Set the scroll offset of this view (in items)

### SetWheelScrollMultiplier
```angelscript
void SetWheelScrollMultiplier(float32 NewWheelScrollMultiplier)
```

