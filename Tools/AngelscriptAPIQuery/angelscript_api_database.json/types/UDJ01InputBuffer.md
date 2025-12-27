# UDJ01InputBuffer

**继承自**: `UActorComponent`

UDJ01InputBuffer

输入缓冲组件 - 用于连招系统的预输入
添加到角色身上，缓存玩家在攻击动画中的输入

## 属性

### DefaultBufferDuration
- **类型**: `float32`
- **描述**: 默认缓冲有效期

## 方法

### BufferInput
```angelscript
void BufferInput(FGameplayTag AbilityTag, float32 BufferDuration)
```
添加缓冲输入

### ClearBuffer
```angelscript
void ClearBuffer()
```
清空所有缓冲

### ConsumeBufferedInput
```angelscript
bool ConsumeBufferedInput(FGameplayTag& OutAbilityTag)
```
消费缓冲输入 (返回最高优先级的有效输入)

### HasBufferedInput
```angelscript
bool HasBufferedInput(FGameplayTag AbilityTag)
```
检查是否有特定类型的缓冲输入

