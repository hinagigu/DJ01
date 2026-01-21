# UMVVMDeveloperProjectSettings

**继承自**: `UDeveloperSettings`

Implements the settings for the MVVM Editor

## 属性

### FieldSelectorPermissions
- **类型**: `TMap<FSoftClassPath,FMVVMDeveloperProjectWidgetSettings>`
- **描述**: Permission list for filtering which properties are visible in UI.

### AllowedExecutionMode
- **类型**: `TSet<EMVVMExecutionMode>`
- **描述**: Permission list for filtering which execution mode is allowed.

### AllowedContextCreationType
- **类型**: `TSet<EMVVMBlueprintViewModelContextCreationType>`
- **描述**: Permission list for filtering which context creation type is allowed.

### bAllowBindingFromDetailView
- **类型**: `bool`
- **描述**: Binding can be made from the DetailView Bind option.

### bAllowGeneratedViewModelSetter
- **类型**: `bool`
- **描述**: When generating a source in the viewmodel editor, allow the compiler to generate a setter function.

### bAllowLongSourcePath
- **类型**: `bool`
- **描述**: When generating a binding with a long source path, allow the compiler to generate a new viewmodel source.

### bShowDetailViewOptionInBindingPanel
- **类型**: `bool`
- **描述**: For the binding list widget, allow the user to edit the binding in the detail view.

### bShowViewSettings
- **类型**: `bool`
- **描述**: For the binding list widget and the viewmodel panel, allow the user to edit the view settings in the detail view.

### bShowDeveloperGenerateGraphSettings
- **类型**: `bool`
- **描述**: For the binding list widget, allow the user to generate a copy of the binding/event graph.

### bAllowConversionFunctionGeneratedGraphInEditor
- **类型**: `bool`
- **描述**: When a conversion function requires a wrapper graph, add and save the generated graph to the blueprint.

### bAllowBindingEvent
- **类型**: `bool`
- **描述**: When binding to a multicast delegate property, allow to create an event.

### bCanCreateViewModelInView
- **类型**: `bool`
- **描述**: Allow to create an instanced viewmodel directly in the view editor.

### bExposeViewModelInstanceInEditor
- **类型**: `bool`
- **描述**: When a viewmodel is set to Create Instance, allow modifying the viewmodel instance in the editor on all instances of the owning widget.
The per-viewmodel setting "Expose Instance In Editor" overrides this.

### ConversionFunctionFilter
- **类型**: `EMVVMDeveloperConversionFunctionFilterType`
- **描述**: Permission list for filtering which execution mode is allowed.

### AllowedClassForConversionFunctions
- **类型**: `TSet<FSoftClassPath>`
- **描述**: Individual class that are allowed to be uses as conversion functions.

### FilterSettings
- **类型**: `FMVVMViewBindingFilterSettings`
- **描述**: Settings for filtering the list of available properties and functions on binding creation.

