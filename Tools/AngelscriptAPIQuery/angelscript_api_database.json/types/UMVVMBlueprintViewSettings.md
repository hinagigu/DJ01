# UMVVMBlueprintViewSettings

**继承自**: `UObject`

## 属性

### bInitializeSourcesOnConstruct
- **类型**: `bool`
- **描述**: Auto initialize the view sources when the Widget is constructed.
If false, the user will have to initialize the sources manually.
It prevents the sources evaluating until you are ready.

### bInitializeBindingsOnConstruct
- **类型**: `bool`
- **描述**: Auto initialize the view bindings when the Widget is constructed.
If false, the user will have to initialize the bindings manually.
It prevents bindings execution and improves performance when you know the widget won't be visible.
@note All bindings are executed when the view is automatically initialized or manually initialized.
@note Sources needs to be initialized before initializing the bindings.
@note When Sources is manually initialized, the bindings will also be initialized if this is true.

### bInitializeEventsOnConstruct
- **类型**: `bool`
- **描述**: Auto initialize the view events when the Widget is constructed.
If false, the user will have to initialize the event manually.

