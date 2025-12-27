# UNiagaraDataInterfaceActorComponent

**继承自**: `UNiagaraDataInterface`

Data interface that gives you access to actor & component information.

## 属性

### SourceMode
- **类型**: `ENDIActorComponentSourceMode`
- **描述**: Controls how we find the actor / component we want to bind to.

### LocalPlayerIndex
- **类型**: `int`
- **描述**: , EditConditionHides))

### ActorOrComponentParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: User parameter binding to use, overrides SourceActor.  Can be set by Blueprint, etc.

### bRequireCurrentFrameData
- **类型**: `bool`
- **描述**: When this option is disabled, we use the previous frame's data for the skeletal mesh and can often issue the simulation early. This greatly
      reduces overhead and allows the game thread to run faster, but comes at a tradeoff if the dependencies might leave gaps or other visual artifacts.

