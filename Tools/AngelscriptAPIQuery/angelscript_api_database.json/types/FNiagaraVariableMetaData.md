# FNiagaraVariableMetaData

## 属性

### Description
- **类型**: `FText`

### CategoryName
- **类型**: `FText`

### DisplayUnit
- **类型**: `EUnit`
- **描述**: The unit to display next to input fields for this parameter - note that this is only a visual indicator and does not change any of the calculations.

### bAdvancedDisplay
- **类型**: `bool`
- **描述**: Declares that this input is advanced and should only be visible if expanded inputs have been expanded.

### bDisplayInOverviewStack
- **类型**: `bool`
- **描述**: Declares that this parameter's value will be shown in the overview node if it's set to a local value.

### InlineParameterSortPriority
- **类型**: `int`
- **描述**: Affects the sort order for parameters shown inline in the overview. Use a smaller number to push it to the top. Defaults to zero.

### bOverrideColor
- **类型**: `bool`
- **描述**: The color used to display a parameter in the overview. If no color is specified, the type color is used.

### InlineParameterColorOverride
- **类型**: `FLinearColor`
- **描述**: The color used to display a parameter in the overview. If no color is specified, the type color is used.

### InlineParameterEnumOverrides
- **类型**: `TArray<FNiagaraEnumParameterMetaData>`
- **描述**: The index of the entry maps to the index of an enum value. Useful for overriding how an enum parameter is displayed in the overview.

### bEnableBoolOverride
- **类型**: `bool`
- **描述**: Useful to override inline bool visualization in the overview.

### InlineParameterBoolOverride
- **类型**: `FNiagaraBoolParameterMetaData`
- **描述**: Useful to override inline bool visualization in the overview.

### EditorSortPriority
- **类型**: `int`
- **描述**: Affects the sort order in the editor stacks. Use a smaller number to push it to the top. Defaults to zero.

### bInlineEditConditionToggle
- **类型**: `bool`
- **描述**: Declares the associated input is used as an inline edit condition toggle, so it should be hidden and edited as a
      checkbox inline with the input which was designated as its edit condition.

### EditCondition
- **类型**: `FNiagaraInputConditionMetadata`
- **描述**: Declares the associated input should be conditionally editable based on the value of another input.

### VisibleCondition
- **类型**: `FNiagaraInputConditionMetadata`
- **描述**: Declares the associated input should be conditionally visible based on the value of another input.

### PropertyMetaData
- **类型**: `TMap<FName,FString>`
- **描述**: Property Metadata

### ParentAttribute
- **类型**: `FName`
- **描述**: If set, this attribute is visually displayed as a child under the given parent attribute. Currently, only static switches are supported as parent attributes!

### AlternateAliases
- **类型**: `TArray<FName>`
- **描述**: List of alternate/previous names for this variable. Note that this is not normally needed if you rename through the UX. However, if you delete and then add a different variable, intending for it to match, you will likely want to add the prior name here.

You may need to restart and reload assets after making this change to have it take effect on already loaded assets.

### WidgetCustomization
- **类型**: `FNiagaraInputParameterCustomization`
- **描述**: Changes how the input is displayed.

## 方法

### opAssign
```angelscript
FNiagaraVariableMetaData& opAssign(FNiagaraVariableMetaData Other)
```

