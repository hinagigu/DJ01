# UEnhancedInputComponent

**继承自**: `UInputComponent`

Implement an Actor component for input bindings.

An Enhanced Input Component is a transient component that enables an Actor to bind enhanced actions to delegate functions, or monitor those actions.
Input components are processed from a stack managed by the PlayerController and processed by the PlayerInput.
These bindings will not consume input events, but this behaviour can be replicated using UInputMappingContext::Priority.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

## 方法

### SetShouldFireDelegatesInEditor
```angelscript
void SetShouldFireDelegatesInEditor(bool bInNewValue)
```

### ShouldFireDelegatesInEditor
```angelscript
bool ShouldFireDelegatesInEditor()
```

### HasBindings
```angelscript
bool HasBindings()
```

### ClearActionEventBindings
```angelscript
void ClearActionEventBindings()
```

### ClearActionValueBindings
```angelscript
void ClearActionValueBindings()
```

### ClearDebugKeyBindings
```angelscript
void ClearDebugKeyBindings()
```

### ClearActionBindings
```angelscript
void ClearActionBindings()
```

### ClearBindingsForObject
```angelscript
void ClearBindingsForObject(UObject InOwner)
```

### RemoveActionEventBinding
```angelscript
bool RemoveActionEventBinding(int BindingIndex)
```

### RemoveDebugKeyBinding
```angelscript
bool RemoveDebugKeyBinding(int BindingIndex)
```

### RemoveActionValueBinding
```angelscript
bool RemoveActionValueBinding(int BindingIndex)
```

### RemoveBindingByHandle
```angelscript
bool RemoveBindingByHandle(uint BindingIndex)
```

### RemoveBinding
```angelscript
bool RemoveBinding(FInputBindingHandle BindingToRemove)
```

### RemoveBinding
```angelscript
bool RemoveBinding(FEnhancedInputActionEventBinding BindingToRemove)
```

### RemoveBinding
```angelscript
bool RemoveBinding(FEnhancedInputActionValueBinding BindingToRemove)
```

### RemoveBinding
```angelscript
bool RemoveBinding(FInputDebugKeyBinding BindingToRemove)
```

### BindAction
```angelscript
FEnhancedInputActionEventBinding& BindAction(const UInputAction Action, ETriggerEvent TriggerEvent, FEnhancedInputActionHandlerDynamicSignature Delegate)
```

### BindActionValue
```angelscript
FEnhancedInputActionValueBinding& BindActionValue(const UInputAction Action)
```

### BindDebugKey
```angelscript
FInputDebugKeyBinding& BindDebugKey(FInputChord Chord, EInputEvent KeyEvent, FInputDebugKeyHandlerDynamicSignature Delegate, bool bExecuteWhenPaused)
```

### GetBoundActionValue
```angelscript
FInputActionValue GetBoundActionValue(const UInputAction Action)
```

