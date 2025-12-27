# UEnhancedInputComponent

**继承自**: `UInputComponent`

Implement an Actor component for input bindings.

An Enhanced Input Component is a transient component that enables an Actor to bind enhanced actions to delegate functions, or monitor those actions.
Input components are processed from a stack managed by the PlayerController and processed by the PlayerInput.
These bindings will not consume input events, but this behaviour can be replicated using UInputMappingContext::Priority.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

