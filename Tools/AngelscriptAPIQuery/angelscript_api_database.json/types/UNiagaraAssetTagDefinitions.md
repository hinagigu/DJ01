# UNiagaraAssetTagDefinitions

**继承自**: `UObject`

An asset to define multiple tag definitions; used to sort and categorize Niagara assets.

## 属性

### DisplayName
- **类型**: `FText`
- **描述**: The display name to use when listing this asset in the Niagara Asset Browser

### Description
- **类型**: `FText`
- **描述**: A description for this group of tags. Used for tooltips.

### TagDefinitions
- **类型**: `TArray<FNiagaraAssetTagDefinition>`

### bDisplayTagsAsFlatList
- **类型**: `bool`
- **描述**: If true, no 'parent' entry for this asset will be displayed in the Niagara Asset Browser. Instead a flat list of the contained tags will be added.

### SortOrder
- **类型**: `int`
- **描述**: Tags are sorted by asset sort order first, then individually. That means tags of asset with sort order [0] come before tags of asset with sort order [1].

