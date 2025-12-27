# UBehaviorTreeComponent

**继承自**: `UBrainComponent`

## 属性

### DefaultBehaviorTreeAsset
- **类型**: `UBehaviorTree`

## 方法

### AddCooldownTagDuration
```angelscript
void AddCooldownTagDuration(FGameplayTag CooldownTag, float32 CooldownDuration, bool bAddToExistingDuration)
```
add to the cooldown tag's duration

### GetTagCooldownEndTime
```angelscript
float GetTagCooldownEndTime(FGameplayTag CooldownTag)
```
@return the cooldown tag end time, 0.0f if CooldownTag is not found

### SetDynamicSubtree
```angelscript
void SetDynamicSubtree(FGameplayTag InjectTag, UBehaviorTree BehaviorAsset)
```
assign subtree to RunBehaviorDynamic task specified by tag.

