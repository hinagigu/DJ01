# UEditorUtilityWidget

**继承自**: `UUserWidget`

## 属性

### TabDisplayName
- **类型**: `FText`

### HelpText
- **类型**: `FString`

### bAlwaysReregisterWithWindowsMenu
- **类型**: `bool`
- **描述**: Should this widget always be re-added to the windows menu once it's opened

### bAutoRunDefaultAction
- **类型**: `bool`

## 方法

### Run
```angelscript
void Run()
```
The default action called when the widget is invoked if bAutoRunDefaultAction=true (it is never called otherwise)

