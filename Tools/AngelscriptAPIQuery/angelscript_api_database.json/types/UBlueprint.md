# UBlueprint

**继承自**: `UBlueprintCore`

Blueprints are special assets that provide an intuitive, node-based interface that can be used to create new types of Actors
and script level events; giving designers and gameplay programmers the tools to quickly create and iterate gameplay from
within Unreal Editor without ever needing to write a line of code.

## 属性

### ShouldCookPropertyGuidsValue
- **类型**: `EShouldCookBlueprintPropertyGuids`
- **描述**: Whether to include the property GUIDs for the generated class in a cooked build.
@note This option may slightly increase memory usage in a cooked build, but can avoid needing to add CoreRedirect data for Blueprint classes stored within SaveGame archives.

### CompileMode
- **类型**: `EBlueprintCompileMode`
- **描述**: The mode that will be used when compiling this class.

### BlueprintDisplayName
- **类型**: `FString`
- **描述**: Overrides the BP's display name in the editor UI

### BlueprintDescription
- **类型**: `FString`
- **描述**: Shows up in the content browser tooltip when the blueprint is hovered

### BlueprintNamespace
- **类型**: `FString`
- **描述**: The namespace of this blueprint (if set, the Blueprint will be treated differently for the context menu)

### BlueprintCategory
- **类型**: `FString`
- **描述**: The category of the Blueprint, used to organize this Blueprint class when displayed in palette windows

### HideCategories
- **类型**: `TArray<FString>`
- **描述**: Additional HideCategories. These are added to HideCategories from parent.

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

### bRunConstructionScriptOnDrag
- **类型**: `bool`

### bRunConstructionScriptInSequencer
- **类型**: `bool`

### bGenerateConstClass
- **类型**: `bool`

### bGenerateAbstractClass
- **类型**: `bool`

### bDeprecate
- **类型**: `bool`

