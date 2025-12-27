# UCommonTabListWidgetBase

**继承自**: `UCommonUserWidget`

Base class for a list of selectable tabs that correspondingly activate and display an arbitrary widget in a linked switcher

## 属性

### OnTabSelected
- **类型**: `FOnTabSelected__CommonTabListWidgetBase`

### OnTabButtonCreation
- **类型**: `FOnTabButtonCreation__CommonTabListWidgetBase`

### OnTabButtonRemoval
- **类型**: `FOnTabButtonRemoval__CommonTabListWidgetBase`

### OnTabListRebuilt
- **类型**: `FOnTabListRebuilt__CommonTabListWidgetBase`

### NextTabInputActionData
- **类型**: `FDataTableRowHandle`

### PreviousTabInputActionData
- **类型**: `FDataTableRowHandle`

### NextTabEnhancedInputAction
- **类型**: `UInputAction`

### PreviousTabEnhancedInputAction
- **类型**: `UInputAction`

### bAutoListenForInput
- **类型**: `bool`

### bDeferRebuildingTabList
- **类型**: `bool`
- **描述**: Whether to defer until next tick rebuilding tab list when inserting new tab (rather than adding to the end).
Useful if inserting multiple tabs in the same tick as the tab list will only be rebuilt once.

## 方法

### DisableTabWithReason
```angelscript
void DisableTabWithReason(FName TabNameID, FText Reason)
```
Disables the tab associated with the given ID with a reason

### GetActiveTab
```angelscript
FName GetActiveTab()
```
@return The currently active (selected) tab

### GetLinkedSwitcher
```angelscript
UCommonAnimatedSwitcher GetLinkedSwitcher()
```
@return The switcher that this tab list is associated with and manipulates

### GetSelectedTabId
```angelscript
FName GetSelectedTabId()
```

### GetTabButtonBaseByID
```angelscript
UCommonButtonBase GetTabButtonBaseByID(FName TabNameID)
```
Returns the tab button matching the ID, if found

### GetTabCount
```angelscript
int GetTabCount()
```

### GetTabIdAtIndex
```angelscript
FName GetTabIdAtIndex(int Index)
```

### HandlePostLinkedSwitcherChanged_BP
```angelscript
void HandlePostLinkedSwitcherChanged_BP()
```

### HandlePreLinkedSwitcherChanged_BP
```angelscript
void HandlePreLinkedSwitcherChanged_BP()
```

### HandleTabCreation
```angelscript
void HandleTabCreation(FName TabNameID, UCommonButtonBase TabButton)
```

### HandleTabRemoval
```angelscript
void HandleTabRemoval(FName TabNameID, UCommonButtonBase TabButton)
```

### RegisterTab
```angelscript
bool RegisterTab(FName TabNameID, TSubclassOf<UCommonButtonBase> ButtonWidgetType, UWidget ContentWidget, int TabIndex)
```
INDEX_NONE

### RemoveAllTabs
```angelscript
void RemoveAllTabs()
```

### RemoveTab
```angelscript
bool RemoveTab(FName TabNameID)
```

### SelectTabByID
```angelscript
bool SelectTabByID(FName TabNameID, bool bSuppressClickFeedback)
```
Selects the tab registered under the provided name ID
@param TabNameID The name ID for the tab given when registered

### SetLinkedSwitcher
```angelscript
void SetLinkedSwitcher(UCommonAnimatedSwitcher CommonSwitcher)
```
Establishes the activatable widget switcher instance that this tab list should interact with
@param CommonSwitcher The switcher that this tab list should be associated with and manipulate

### SetListeningForInput
```angelscript
void SetListeningForInput(bool bShouldListen)
```

### SetTabEnabled
```angelscript
void SetTabEnabled(FName TabNameID, bool bEnable)
```
Sets whether the tab associated with the given ID is enabled/disabled

### SetTabInteractionEnabled
```angelscript
void SetTabInteractionEnabled(FName TabNameID, bool bEnable)
```
Sets whether the tab associated with the given ID is interactable

### SetTabVisibility
```angelscript
void SetTabVisibility(FName TabNameID, ESlateVisibility NewVisibility)
```
Sets the visibility of the tab associated with the given ID

