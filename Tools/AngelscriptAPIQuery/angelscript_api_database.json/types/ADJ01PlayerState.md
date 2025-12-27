# ADJ01PlayerState

**继承自**: `AModularPlayerState`

ADJ01PlayerState

     Base player state class used by this project.
     玩家状态类，持有玩家的 AbilitySystemComponent。
     在Lyra架构中，ASC由PlayerState持有而非Pawn，这样可以在Pawn死亡/重生时保持技能状态。

## 属性

### AbilitySystemComponent
- **类型**: `UDJ01AbilitySystemComponent`
- **描述**: 玩家的 AbilitySystemComponent，用于管理技能、属性和效果

## 方法

### AddStatTagStack
```angelscript
void AddStatTagStack(FGameplayTag Tag, int StackCount)
```
Adds a specified number of stacks to the tag (does nothing if StackCount is below 1)

### GetDJ01AbilitySystemComponent
```angelscript
UDJ01AbilitySystemComponent GetDJ01AbilitySystemComponent()
```
获取玩家的 AbilitySystemComponent

### GetDJ01PlayerController
```angelscript
ADJ01PlayerController GetDJ01PlayerController()
```

### GetSquadId
```angelscript
int GetSquadId()
```
Returns the Squad ID of the squad the player belongs to.

### GetStatTagStackCount
```angelscript
int GetStatTagStackCount(FGameplayTag Tag)
```
Returns the stack count of the specified tag (or 0 if the tag is not present)

### GetTeamId
```angelscript
int GetTeamId()
```
Returns the Team ID of the team the player belongs to.

### HasStatTag
```angelscript
bool HasStatTag(FGameplayTag Tag)
```
Returns true if there is at least one stack of the specified tag

### RemoveStatTagStack
```angelscript
void RemoveStatTagStack(FGameplayTag Tag, int StackCount)
```
Removes a specified number of stacks from the tag (does nothing if StackCount is below 1)

