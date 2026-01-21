# UComboGraphNodeBase

**继承自**: `UObject`

Base Class for all Combo Graph nodes (Edges, Anim based and conduit)

Holds information and API related to debug states.

## 属性

### ChildrenNodes
- **类型**: `TArray<TObjectPtr<UComboGraphNodeBase>>`

### ParentNodes
- **类型**: `TArray<TObjectPtr<UComboGraphNodeBase>>`

### Edges
- **类型**: `TMap<TObjectPtr<UComboGraphNodeBase>,TObjectPtr<UComboGraphEdge>>`

### NodeTitle
- **类型**: `FText`
- **描述**: When not empty, will draw title with specified value instead of using Animation Asset name (Montage or Sequence)

### ContextMenuName
- **类型**: `FText`
- **描述**: ContextMenuName is used in Combo Graph to generate context menu items (upon right click in the graph to add new nodes)

Split up ContextMenuName by "|" to create a top category if there is more than one level.

You can leave this empty to exclude this class from being considered when Combo Graph generates a context menu.

### bIncludeClassNameInContextMenu
- **类型**: `bool`
- **描述**: Set it to false to prevent context menu in graph to include the BP Class name

## 方法

### GetEdge
```angelscript
UComboGraphEdge GetEdge(UComboGraphNodeBase ChildNode)
```

### IsLeafNode
```angelscript
bool IsLeafNode()
```

