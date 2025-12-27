# UAbilityTask_WaitTargetData

**继承自**: `UAbilityTask`

Wait for targeting actor (spawned from parameter) to provide data. Can be set not to end upon outputting data. Can be ended by task name.

WARNING: These actors are spawned once per ability activation and in their default form are not very efficient
For most games you will need to subclass and heavily modify this actor, or you will want to implement similar functions in a game-specific actor or blueprint to avoid actor spawn costs
This task is not well tested by internal games, but it is a useful class to look at to learn how target replication occurs

## 属性

### ValidData
- **类型**: `FWaitTargetDataDelegate`

### Cancelled
- **类型**: `FWaitTargetDataDelegate`

