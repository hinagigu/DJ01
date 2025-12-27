# UEditorUtilityLibrary

**继承自**: `UBlueprintFunctionLibrary`

Expose editor utility functions to Blutilities

## 方法

### GetActorReference
```angelscript
AActor GetActorReference(FString PathToActor)
```
Attempts to find the actor specified by PathToActor in the current editor world
@param        PathToActor     The path to the actor (e.g. PersistentLevel.PlayerStart)
@return       A reference to the actor, or none if it wasn't found

