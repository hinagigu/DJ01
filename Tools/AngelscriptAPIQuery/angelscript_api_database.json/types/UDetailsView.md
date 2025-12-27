# UDetailsView

**继承自**: `UPropertyViewBase`

The details view allows you to display the value of an object properties.

## 属性

### bAllowFiltering
- **类型**: `bool`
- **描述**: True if we allow filtering through search and the filter dropdown menu.

### bAllowFavoriteSystem
- **类型**: `bool`
- **描述**: If false, the current properties editor will never display the favorite system

### bShowModifiedPropertiesOption
- **类型**: `bool`
- **描述**: True if you want to show the 'Show Only Modified Properties'. Only valid in conjunction with bAllowFiltering

### bShowKeyablePropertiesOption
- **类型**: `bool`
- **描述**: True if you want to show the 'Show Only Keyable Properties'. Only valid in conjunction with bAllowFiltering

### bShowAnimatedPropertiesOption
- **类型**: `bool`
- **描述**: True if you want to show the 'Show Only Animated Properties'. Only valid in conjunction with bAllowFiltering

### ColumnWidth
- **类型**: `float32`
- **描述**: The default column width

### bShowScrollBar
- **类型**: `bool`
- **描述**: If false, the details panel's scrollbar will always be hidden. Useful when embedding details panels in widgets that either grow to accommodate them, or with scrollbars of their own.

### bForceHiddenPropertyVisibility
- **类型**: `bool`
- **描述**: If true, all properties will be visible, not just those with CPF_Edit

### ViewIdentifier
- **类型**: `FName`
- **描述**: Identifier for this details view; NAME_None if this view is anonymous

### CategoriesToShow
- **类型**: `TArray<FName>`
- **描述**: Which categories to show in the details panel. If both this and the Properties To Show lists are empty, all properties will show.

### PropertiesToShow
- **类型**: `TArray<FName>`
- **描述**: Which properties to show in the details panel. If both this and the Categories To Show lists are empty, all properties will show.

