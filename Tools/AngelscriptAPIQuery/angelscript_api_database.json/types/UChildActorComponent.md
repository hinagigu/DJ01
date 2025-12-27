# UChildActorComponent

**继承自**: `USceneComponent`

A component that spawns an Actor when registered, and destroys it when unregistered.

## 属性

### ChildActor
- **类型**: `AActor`
- **描述**: The actor that we spawned and own

### ChildActorClass
- **类型**: `TSubclassOf<AActor>`

### bChildActorIsTransient
- **类型**: `bool`

## 方法

### SetChildActorClass
```angelscript
void SetChildActorClass(TSubclassOf<AActor> InClass)
```
Sets the class to use for the child actor.
If called on a template component (owned by a CDO), the properties of any existing child actor template will be copied as best possible to the template.
If called on a component instance in a world (and the class is changing), the created ChildActor will use the class defaults as template.
@param InClass The Actor subclass to spawn as a child actor

