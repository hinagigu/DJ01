# UWidgetEditingProjectSettings

**继承自**: `UDeveloperSettings`

Implements the settings for the UMG Editor Project Settings

## 属性

### DefaultCompilerOptions
- **类型**: `FWidgetCompilerOptions`

### DirectoryCompilerOptions
- **类型**: `TArray<FDirectoryWidgetCompilerOptions>`

### bShowWidgetsFromEngineContent
- **类型**: `bool`

### bShowWidgetsFromDeveloperContent
- **类型**: `bool`

### CategoriesToHide
- **类型**: `TArray<FString>`

### WidgetClassesToHide
- **类型**: `TArray<FSoftClassPath>`

### bUseWidgetTemplateSelector
- **类型**: `bool`
- **描述**: Enables a dialog that lets you select a root widget before creating a widget blueprint

### CommonRootWidgetClasses
- **类型**: `TArray<TSoftClassPtr<UPanelWidget>>`
- **描述**: This list populates the common class section of the root widget selection dialog

### DefaultRootWidget
- **类型**: `TSubclassOf<UPanelWidget>`
- **描述**: The panel widget to place at the root of all newly constructed widget blueprints. Can be empty.

### bUseEditorConfigPaletteFiltering
- **类型**: `bool`
- **描述**: Set true to filter all categories and widgets out in the palette, selectively enabling them later via permission lists.

### bUseUserWidgetParentClassViewerSelector
- **类型**: `bool`
- **描述**: Enables a dialog that lets you select the parent class in a tree view.

### bUseUserWidgetParentDefaultClassViewerSelector
- **类型**: `bool`
- **描述**: Enables a dialog that lets you select the parent class in a default view.

### bEnableMakeVariable
- **类型**: `bool`
- **描述**: Set true to enable the Is Variable checkbox in the UMG editor DetailView.

### bEnableWidgetAnimationEditor
- **类型**: `bool`
- **描述**: Set true to hide widget animation related elements in the UMG editor.

### bEnablePaletteWindow
- **类型**: `bool`
- **描述**: Set true to enabled the Palette window in the UMG editor.

### bEnableLibraryWindow
- **类型**: `bool`
- **描述**: Set true to enabled the LIbrary window in the UMG editor.

### bEnableHierarchyWindow
- **类型**: `bool`
- **描述**: Set true to enabled the Widget Hierarchy window in the UMG editor.

### bEnableBindWidgetWindow
- **类型**: `bool`
- **描述**: Set true to enabled the Bind Widget window in the UMG editor.

### bEnableNavigationSimulationWindow
- **类型**: `bool`
- **描述**: Set true to enabled the Navigation Simulation window in the UMG editor.

### bCanCallInitializedWithoutPlayerContext
- **类型**: `bool`
- **描述**: The default value of bCanCallInitializedWithoutPlayerContext.

### FavoriteWidgetParentClasses
- **类型**: `TArray<TSoftClassPtr<UUserWidget>>`
- **描述**: The list of parent classes to choose from for newly constructed widget blueprints.
The classes must have empty widget hierarchies.

### DebugResolutions
- **类型**: `TArray<FDebugResolution>`

