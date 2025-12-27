# UCommonUserWidget

**继承自**: `UUserWidget`

## 属性

### bDisplayInActionBar
- **类型**: `bool`

### bConsumePointerInput
- **类型**: `bool`

## 方法

### RegisterScrollRecipientExternal
```angelscript
void RegisterScrollRecipientExternal(const UWidget AnalogScrollRecipient)
```
Add a widget to the list of widgets to get scroll events for this input root node

### SetConsumePointerInput
```angelscript
void SetConsumePointerInput(bool bInConsumePointerInput)
```
Sets whether or not this widget will consume ALL pointer input that reaches it

### UnregisterScrollRecipientExternal
```angelscript
void UnregisterScrollRecipientExternal(const UWidget AnalogScrollRecipient)
```
Remove a widget from the list of widgets to get scroll events for this input root node

