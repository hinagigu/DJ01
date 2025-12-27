# FComponentReference

Struct that allows for different ways to reference a component using TObjectPtr.
If just an Actor is specified, will return RootComponent of that Actor.

## 属性

### OtherActor
- **类型**: `TWeakObjectPtr<AActor>`

### ComponentProperty
- **类型**: `FName`

### PathToComponent
- **类型**: `FString`
- **描述**: Path to the component from its owner actor

## 方法

### GetComponent
```angelscript
UActorComponent GetComponent(AActor OwningActor)
```

### opAssign
```angelscript
FComponentReference& opAssign(FComponentReference Other)
```

