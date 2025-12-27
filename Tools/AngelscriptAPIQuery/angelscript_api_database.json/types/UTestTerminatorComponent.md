# UTestTerminatorComponent

**继承自**: `UActorComponent`

UTestTerminatorComponent

This component is used as an acknowledge mechanism to ensure that replication
of the ATestTermiantor actor has occurred.

This mechanism is based on component replication and server RPC.
This component is attached to the player controller by the ATestTerminator actor.

## 方法

### ServerTerminatorReplicated
```angelscript
void ServerTerminatorReplicated()
```

