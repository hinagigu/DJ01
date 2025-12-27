# UTreeView

**继承自**: `UListView`

Similar to ListView, but can display a hierarchical tree of elements.
The base items source for the tree identifies the root items, each of which can have n associated child items.
There is no hard limit to the nesting - child items can have children and so on

To make a widget usable as an entry in a TreeView, it must inherit from the IUserObjectListEntry interface.

## 属性

### BP_OnGetItemChildren
- **类型**: `FOnGetItemChildrenDynamic`
- **描述**: Called to get the list of children (if any) that correspond to the given item. Only called if the native C++ version of the event is not bound.

### BP_OnItemExpansionChanged
- **类型**: `FOnItemExpansionChangedDynamic`

## 方法

### CollapseAll
```angelscript
void CollapseAll()
```
Collapses all currently expanded items

### ExpandAll
```angelscript
void ExpandAll()
```
Expands all items with children

### SetItemExpansion
```angelscript
void SetItemExpansion(UObject Item, bool bExpandItem)
```
Attempts to expand/collapse the given item (only relevant if the item has children)

