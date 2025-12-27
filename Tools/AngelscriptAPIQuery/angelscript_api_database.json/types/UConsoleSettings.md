# UConsoleSettings

**继承自**: `UObject`

Implements the settings for the UConsole class.

## 属性

### MaxScrollbackSize
- **类型**: `int`
- **描述**: The maximum number of lines the console keeps in its output history.

### ManualAutoCompleteList
- **类型**: `TArray<FAutoCompleteCommand>`
- **描述**: Manual list of auto-complete commands and info specified in BaseInput.ini

### AutoCompleteMapPaths
- **类型**: `TArray<FString>`
- **描述**: List of relative paths (e.g. Content/Maps) to search for map names for auto-complete usage. Specified in BaseInput.ini.

### BackgroundOpacityPercentage
- **类型**: `float32`
- **描述**: Amount of transparency of the console background.

### bOrderTopToBottom
- **类型**: `bool`
- **描述**: Whether we legacy bottom-to-top ordering or regular top-to-bottom ordering

### bDisplayHelpInAutoComplete
- **类型**: `bool`
- **描述**: Display the first line of any available help text in the auto-complete window, if a description isn't available

### InputColor
- **类型**: `FColor`
- **描述**: The color used for text input.

### HistoryColor
- **类型**: `FColor`
- **描述**: The color used for the previously typed commands history.

### AutoCompleteCommandColor
- **类型**: `FColor`
- **描述**: The autocomplete color used for executable commands.

### AutoCompleteCVarColor
- **类型**: `FColor`
- **描述**: The autocomplete color used for mutable CVars.

### AutoCompleteFadedColor
- **类型**: `FColor`
- **描述**: The autocomplete color used for command descriptions and read-only CVars.

