# UMeshBudgetProjectSettings

**继承自**: `UDeveloperSettings`

## 属性

### bEnableStaticMeshBudget
- **类型**: `bool`
- **描述**: Enable/disable the static mesh budget.
Static mesh budget will auto assign a lod group to any static mesh when loading or importing the asset in the editor.
The auto budget will not override a static mesh lod group, user can control the lod group for a specific asset.
@note: When the static mesh budget is enable and properly configure, there will be no static mesh without a lod group in the editor.

### StaticMeshBudgetInfos
- **类型**: `TArray<FStaticMeshBudgetInfo>`
- **描述**: The static mesh budgets array.

