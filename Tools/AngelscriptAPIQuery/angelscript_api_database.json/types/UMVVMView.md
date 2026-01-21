# UMVVMView

**继承自**: `UUserWidgetExtension`

Instance UMVVMClassExtension_View for the UUserWdiget

## 属性

### bLogBinding
- **类型**: `bool`
- **描述**: Should log when a binding is executed.

## 方法

### AreBindingsInitialized
```angelscript
bool AreBindingsInitialized()
```
The bindings were initialized, manually or automatically.

### AreEventsInitialized
```angelscript
bool AreEventsInitialized()
```
The events were initialized, manually or automatically.

### AreSourcesInitialized
```angelscript
bool AreSourcesInitialized()
```
The sources were initialized, manually or automatically.

### InitializeBindings
```angelscript
void InitializeBindings()
```
Initialize the bindings if they are not already initialized.
Initializing the bindings will execute them.

### InitializeEvents
```angelscript
void InitializeEvents()
```
Initialize the events if they are not already initialized.

### InitializeSources
```angelscript
void InitializeSources()
```
Initialize the sources if they are not already initialized.
Initializing the sources will also initialize the bindings if the option bInitializeBindingsOnConstruct is enabled.
@note A sources can be a viewmodel or any other object used by a binding.

### UninitializeBindings
```angelscript
void UninitializeBindings()
```
Uninitialize the bindings if they are already initialized.

### UninitializeEvents
```angelscript
void UninitializeEvents()
```
Uninitialize the events if they are already initialized.

### UninitializeSources
```angelscript
void UninitializeSources()
```
Uninitialize the sources if they are already initialized.
It will uninitialized the bindings.

