# UBlueprintEditorProjectSettings

**继承自**: `UDeveloperSettings`

## 属性

### DefaultChildActorTreeViewMode
- **类型**: `EChildActorComponentTreeViewVisualizationMode`
- **描述**: Default view mode to use for child actor components in a Blueprint actor's component tree hierarchy (experimental).

### NamespacesToAlwaysInclude
- **类型**: `TArray<FString>`
- **描述**: A list of namespace identifiers that all Blueprint assets in the project should import by default. Requires Blueprint namespace features to be enabled in editor preferences. Editing this list will also cause any visible Blueprint editor windows to be closed.

### DisabledCompilerMessagesExceptEditor
- **类型**: `TArray<FName>`
- **描述**: List of compiler messages that have been suppressed outside of full, interactive editor sessions for
the current project - useful for silencing warnings that were added to the engine after
project inception and are going to be addressed as they are found by content authors

### DisabledCompilerMessages
- **类型**: `TArray<FName>`
- **描述**: List of compiler messages that have been suppressed completely - message suppression is only
advisable when using blueprints that you cannot update and are raising innocuous warnings.
If useless messages are being raised prefer to contact support rather than disabling messages

### SuppressedDeprecationMessages
- **类型**: `TArray<FString>`
- **描述**: List of deprecated UProperties/UFunctions to supress warning messages for - useful for source changes
that would otherwise cause content warnings
The easiest way to populate this list is using the context menu on nodes with deprecated references

### BaseClassesToAllowRecompilingDuringPlayInEditor
- **类型**: `TArray<TSoftClassPtr<UObject>>`
- **描述**: Any blueprint deriving from one of these base classes will be allowed to recompile during Play-in-Editor
(This setting exists both as an editor preference and project setting, and will be allowed if listed in either place)

### bValidateUnloadedSoftActorReferences
- **类型**: `bool`

### bEnableChildActorExpansionInTreeView
- **类型**: `bool`

