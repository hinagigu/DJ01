# UComboGraphGameplayTasksComponent

**继承自**: `UGameplayTasksComponent`

Internal helper actor component spawned from Combo Graph task mainly to handle sending replicated gameplay event
to transition from a node to another on input press.

This component shouldn't be Blueprintable nor BlueprintSpawnableComponent, child class can however.

## 方法

### SendGameplayEventReplicated
```angelscript
void SendGameplayEventReplicated(FGameplayTag EventTag, FGameplayEventData Payload, bool bSendOnlyOnAuthority)
```
This function is functionally the same as SendGameplayEventToActor (from Ability System Blueprint Library),
except it can be used to also replicate the event on server.

@param EventTag Gameplay Tag to use for the Event
@param Payload Gameplay Event Data to send along the event
@param bSendOnlyOnAuthority Whether to send the event only on server or on both server and local client

### ServerSendGameplayEvent
```angelscript
void ServerSendGameplayEvent(FGameplayTag EventTag, FGameplayEventData Payload)
```

