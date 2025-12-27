# UVOIPTalker

**继承自**: `UActorComponent`

## 属性

### Settings
- **类型**: `FVoiceSettings`

## 方法

### BPOnTalkingBegin
```angelscript
void BPOnTalkingBegin(UAudioComponent AudioComponent)
```
Blueprint native event for when this player starts speaking.

### BPOnTalkingEnd
```angelscript
void BPOnTalkingEnd()
```
Blueprint native event for when this player stops speaking.

### GetVoiceLevel
```angelscript
float32 GetVoiceLevel()
```
Get the current level of how loud this player is speaking. Will return 0.0
if player is not talking.

### RegisterWithPlayerState
```angelscript
void RegisterWithPlayerState(APlayerState OwningState)
```
This function sets up this talker with a specific player.
It is necessary to use this to properly control a specific player's voice
and receive events.

