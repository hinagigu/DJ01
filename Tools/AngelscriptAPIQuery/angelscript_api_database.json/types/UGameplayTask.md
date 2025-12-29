# UGameplayTask

**继承自**: `UObject`

## 方法

### EndTask
```angelscript
void EndTask()
```
Called explicitly to end the task (usually by the task itself). Calls OnDestroy.
    @NOTE: you need to call EndTask before sending out any "on completed" delegates.
    If you don't the task will still be in an "active" state while the event receivers may
    assume it's already "finished"

### ReadyForActivation
```angelscript
void ReadyForActivation()
```

