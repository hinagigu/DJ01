# UBlueprintEditorSettings

**继承自**: `UDeveloperSettings`

## 属性

### bDrawMidpointArrowsInBlueprints
- **类型**: `bool`
- **描述**: Should arrows indicating data/execution flow be drawn halfway along wires?

### bShowGraphInstructionText
- **类型**: `bool`
- **描述**: Determines if lightweight tutorial text shows up at the top of empty blueprint graphs

### bHideUnrelatedNodes
- **类型**: `bool`
- **描述**: If true, fade nodes which are not connected to the selected nodes

### bShowShortTooltips
- **类型**: `bool`
- **描述**: If true, use short tooltips whenever possible

### bEnableInputTriggerSupportWarnings
- **类型**: `bool`
- **描述**: If enabled Input Action nodes will hide unsupported trigger pins and give warnings when using unsupported triggers.
This warning only works with triggers set up in an Input Action, not Input Mapping Contexts.

### bSplitContextTargetSettings
- **类型**: `bool`
- **描述**: If enabled, we'll save off your chosen target setting based off of the context (allowing you to have different preferences based off what you're operating on).

### bExposeAllMemberComponentFunctions
- **类型**: `bool`
- **描述**: If enabled, then ALL component functions are exposed to the context menu (when the contextual target is a component owner). Ignores "ExposeFunctionCategories" metadata for components.

### bShowContextualFavorites
- **类型**: `bool`
- **描述**: If enabled, then a separate section with your Blueprint favorites will be pined to the top of the context menu.

### bExposeDeprecatedFunctions
- **类型**: `bool`
- **描述**: If enabled, deprecated functions will be visible in the context menu and will be available for override implementation. By default, functions marked as deprecated are not exposed in either case.

### bCompactCallOnMemberNodes
- **类型**: `bool`
- **描述**: If enabled, then call-on-member actions will be spawned as a single node (instead of a GetMember + FunctionCall node).

### bFlattenFavoritesMenus
- **类型**: `bool`
- **描述**: If enabled, then your Blueprint favorites will be uncategorized, leaving you with less nested categories to sort through.

### bAutoCastObjectConnections
- **类型**: `bool`
- **描述**: If enabled, then you'll be able to directly connect arbitrary object pins together (a pure cast node will be injected automatically).

### bShowViewportOnSimulate
- **类型**: `bool`
- **描述**: If true will show the viewport tab when simulate is clicked.

### bSpawnDefaultBlueprintNodes
- **类型**: `bool`
- **描述**: If set will spawn default "ghost" event nodes in new Blueprints, modifiable in the [DefaultEventNodes] section of EditorPerProjectUserSettings

### bHideConstructionScriptComponentsInDetailsView
- **类型**: `bool`
- **描述**: If set will exclude components added in a Blueprint class Construction Script from the component details view

### bNavigateToNativeFunctionsFromCallNodes
- **类型**: `bool`
- **描述**: If set, double clicking on a call function node will attempt to navigate an open C++ editor to the native source definition

### bDoubleClickNavigatesToParent
- **类型**: `bool`
- **描述**: Double click to navigate up to the parent graph

### bEnableTypePromotion
- **类型**: `bool`
- **描述**: Allows for pin types to be promoted to others, i.e. float to double

### TypePromotionPinDenyList
- **类型**: `TSet<FName>`
- **描述**: If a pin type is within this list, then it will never be marked as a possible promotable function.

### AdditionalBlueprintCategories
- **类型**: `TArray<FAdditionalBlueprintCategory>`
- **描述**: List of additional category names to show in Blueprints, optionally filtered by parent class type.

### BreakpointReloadMethod
- **类型**: `EBlueprintBreakpointReloadMethod`
- **描述**: How to handle previously-set breakpoints on reload.

### bEnablePinValueInspectionTooltips
- **类型**: `bool`
- **描述**: If enabled, pin tooltips during PIE will be interactive

### bEnableNamespaceEditorFeatures
- **类型**: `bool`
- **描述**: Whether to enable namespace importing and filtering features in the Blueprint editor

### NamespacesToAlwaysInclude
- **类型**: `TArray<FString>`
- **描述**: A list of namespace identifiers that the Blueprint editor should always import by default. Requires Blueprint namespace features to be enabled and only applies to the current local user. Editing this list will also cause any visible Blueprint editor windows to be closed.

### bEnableContextMenuTimeSlicing
- **类型**: `bool`
- **描述**: When the Blueprint graph context menu is invoked (e.g. by right-clicking in the graph or dragging off a pin), do not block the UI while populating the available actions list.

### ContextMenuTimeSlicingThresholdMs
- **类型**: `int`
- **描述**: The maximum amount of time (in milliseconds) allowed per frame for Blueprint graph context menu building when the non-blocking option is enabled. Larger values will complete the menu build in fewer frames, but will also make the UI feel less responsive. Smaller values will make the UI feel more responsive, but will also take longer to fully populate the menu.

### bIncludeActionsForSelectedAssetsInContextMenu
- **类型**: `bool`
- **描述**: If enabled, invoking the Blueprint graph context menu with one or more compatible assets selected in the Content Browser will generate an additional set of pre-bound menu actions when the "Context Sensitive" option is enabled. For example, selecting a Static Mesh asset in the Content Browser will result in an extra "Add Static Mesh Component" menu action that's already bound to the selected asset.

### bLimitAssetActionBindingToSingleSelectionOnly
- **类型**: `bool`
- **描述**: Only generate pre-bound "Add Component" actions when there is a single asset selected in the Content Browser. If more than one asset is selected, pre-bound "Add Component" actions will not be generated. Enabling this option can improve UI responsiveness and decrease the time it takes to build the context menu, while still preserving the ability to include actions pre-bound to the selected asset.

### bLoadSelectedAssetsForContextMenuActionBinding
- **类型**: `bool`
- **描述**: When generating pre-bound "Add Component" actions, any selected assets that are not yet loaded will be synchronously loaded as part of building the Blueprint Graph context menu. Enabling this option will ensure that all pre-bound actions for all selected assets are included in the menu, but load times may also affect editor UI responsiveness while the context menu is building.

### bDoNotMarkAllInstancesDirtyOnDefaultValueChange
- **类型**: `bool`
- **描述**: If enabled, assets containing Blueprint instances (e.g. maps) will not be marked dirty when default values are edited, unless it results in the instance becoming realigned with the new default value.

### bFavorPureCastNodes
- **类型**: `bool`
- **描述**: If enabled, then placed cast nodes will default to their "pure" form (meaning: without execution pins).

### SaveOnCompile
- **类型**: `ESaveOnCompile`
- **描述**: Determines when to save Blueprints post-compile

### bJumpToNodeErrors
- **类型**: `bool`
- **描述**: When enabled, if a blueprint has compiler errors, then the graph will jump and focus on the first node generating an error

### bAllowExplicitImpureNodeDisabling
- **类型**: `bool`
- **描述**: If enabled, nodes can be explicitly disabled via context menu when right-clicking on impure nodes in the Blueprint editor. Disabled nodes will not be compiled, but also will not break existing connections.

### bShowActionMenuItemSignatures
- **类型**: `bool`
- **描述**: If enabled, tooltips on action menu items will show the associated action's signature id (can be used to setup custom favorites menus).

### bBlueprintNodeUniqueNames
- **类型**: `bool`
- **描述**: If enabled, blueprint nodes in the event graph will display with unique names rather than their display name.

### NodeTemplateCacheCapMB
- **类型**: `float32`
- **描述**: The node template cache is used to speed up blueprint menuing. This determines the peak data size for that cache.

### AllowIndexAllBlueprints
- **类型**: `EFiBIndexAllPermission`
- **描述**: Whether to enable the "Index All" action in the Find-in-Blueprints search window when blueprint assets with an out-of-date index (search metadata) are found and whether to allow automatic resaving. WARNING: Only allow "Index All" if your project is small enough that all assets can be loaded in memory at once. Only enable saving if you are allowed to potentially checkout and resave all assets.

### BaseClassesToAllowRecompilingDuringPlayInEditor
- **类型**: `TArray<TSoftClassPtr<UObject>>`
- **描述**: Any blueprint deriving from one of these base classes will be allowed to recompile during Play-in-Editor
(This setting exists both as an editor preference and project setting, and will be allowed if listed in either place)

