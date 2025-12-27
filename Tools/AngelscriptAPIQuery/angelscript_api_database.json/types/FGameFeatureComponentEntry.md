# FGameFeatureComponentEntry

Description of a component to add to a type of actor when this game feature is enabled
(the actor class must be game feature aware, it does not happen magically)
@TODO: Write more documentation here about how to make an actor game feature / modular gameplay aware

## 属性

### ActorClass
- **类型**: `TSoftClassPtr<AActor>`
- **描述**: The base actor class to add a component to

### ComponentClass
- **类型**: `TSoftClassPtr<UActorComponent>`
- **描述**: The component class to add to the specified type of actor

### AdditionFlags
- **类型**: `uint8`
- **描述**: Observe these rules when adding the component, if any

### bClientComponent
- **类型**: `bool`

### bServerComponent
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FGameFeatureComponentEntry& opAssign(FGameFeatureComponentEntry Other)
```

