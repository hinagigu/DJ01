# UEnhancedInputWorldSubsystem

**继承自**: `UWorldSubsystem`

Per world input subsystem that allows you to bind input delegates to actors without an owning Player Controller.
This should be used when an actor needs to receive input delegates but will never have an owning Player Controller.
For example, you can add input delegates to unlock a door when the user has a certain set of keys pressed.
Be sure to enable input on the actor, or else the input delegates won't fire!

Note: if you do have an actor with an owning Player Controller use the local player input subsystem instead.

## 方法

### AddActorInputComponent
```angelscript
void AddActorInputComponent(AActor Actor)
```
Adds this Actor's input component onto the stack to be processed by this subsystem's tick function

### RemoveActorInputComponent
```angelscript
bool RemoveActorInputComponent(AActor Actor)
```
Removes this Actor's input component from the stack to be processed by this subsystem's tick function

