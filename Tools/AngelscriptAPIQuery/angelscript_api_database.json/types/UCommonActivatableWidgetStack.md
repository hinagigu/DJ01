# UCommonActivatableWidgetStack

**继承自**: `UCommonActivatableWidgetContainerBase`

A display stack of ActivatableWidget elements.

- Only the widget at the top of the stack is displayed and activated. All others are deactivated.
- When that top-most displayed widget deactivates, it's automatically removed and the preceding entry is displayed/activated.
- If RootContent is provided, it can never be removed regardless of activation state

## 属性

### RootContentWidgetClass
- **类型**: `TSubclassOf<UCommonActivatableWidget>`
- **描述**: Optional widget to auto-generate as the permanent root element of the stack

