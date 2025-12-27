# FVersionedNiagaraScriptData

Struct containing all of the data that can be different between different script versions.

## 属性

### ModuleUsageBitmask
- **类型**: `int`
- **描述**: When used as a module, what are the appropriate script types for referencing this module?

### Category
- **类型**: `FText`
- **描述**: Used to break up scripts of the same Usage type in UI display.

### AssetTagDefinitionReferences
- **类型**: `TArray<FNiagaraAssetTagDefinitionReference>`

### bSuggested
- **类型**: `bool`
- **描述**: If true, this script will be added to a 'Suggested' category at the top of menus during searches

### ProvidedDependencies
- **类型**: `TArray<FName>`
- **描述**: Array of Ids of dependencies provided by this module to other modules on the stack (e.g. 'ProvidesNormalizedAge')

### RequiredDependencies
- **类型**: `TArray<FNiagaraModuleDependency>`
- **描述**: Dependencies required by this module from other modules on the stack

### DeprecationRecommendation
- **类型**: `UNiagaraScript`
- **描述**: Which script to use if this is deprecated.

### bUsePythonScriptConversion
- **类型**: `bool`
- **描述**: If true then a python script will be executed when changing from this script to the selected deprectation recommendation. This allows the current script to transfer its inputs to the new script.

### ConversionScriptExecution
- **类型**: `ENiagaraPythonUpdateScriptReference`
- **描述**: Reference to a python script that is executed when the user updates from a previous version to this version.

### PythonConversionScript
- **类型**: `FString`
- **描述**: Python script to run when converting this script to the recommended deprecation update script.

### ConversionScriptAsset
- **类型**: `FFilePath`
- **描述**: Asset reference to a python script to run when converting this script to the recommended deprecation update script.

### ConversionUtility
- **类型**: `TSubclassOf<UNiagaraConvertInPlaceUtilityBase>`
- **描述**: Custom logic to convert the contents of an existing script assignment to this script.

### ExperimentalMessage
- **类型**: `FText`
- **描述**: The message to display when a function is marked experimental.

### NoteMessage
- **类型**: `FText`
- **描述**: A message to display when adding the module to the stack. This is useful to highlight pitfalls or weird behavior of the module.

### DebugDrawMessage
- **类型**: `FText`
- **描述**: A message to display on UI actions handling debug draw state.

### LibraryVisibility
- **类型**: `ENiagaraScriptLibraryVisibility`
- **描述**: Defines if this script is visible to the user when searching for modules to add to an emitter.

### NumericOutputTypeSelectionMode
- **类型**: `ENiagaraNumericOutputTypeSelectionMode`
- **描述**: The mode to use when deducing the type of numeric output pins from the types of the input pins.

### Description
- **类型**: `FText`

### Keywords
- **类型**: `FText`
- **描述**: A list of space separated keywords which can be used to find this script in editor menus.

### CollapsedViewFormat
- **类型**: `FText`
- **描述**: The format for the text to display in the stack if the value is collapsed.
This supports formatting placeholders for the function inputs, for example "myfunc({0}, {1})" will be converted to "myfunc(1.23, Particles.Position)".

### InlineExpressionFormat
- **类型**: `TArray<FNiagaraInlineDynamicInputFormatToken>`

### InlineGraphFormat
- **类型**: `TArray<FNiagaraInlineDynamicInputFormatToken>`

### ScriptMetaData
- **类型**: `TMap<FName,FString>`
- **描述**: Script Metadata

### InputSections
- **类型**: `TArray<FNiagaraStackSection>`

### bExperimental
- **类型**: `bool`

### bCanBeUsedForTypeConversions
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FVersionedNiagaraScriptData& opAssign(FVersionedNiagaraScriptData Other)
```

