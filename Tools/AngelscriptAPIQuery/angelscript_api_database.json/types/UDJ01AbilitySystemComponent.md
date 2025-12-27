# UDJ01AbilitySystemComponent

**继承自**: `UAbilitySystemComponent`

UDJ01AbilitySystemComponent

    Base ability system component class used by this project.

## 方法

### ClientNotifyAbilityFailed
```angelscript
void ClientNotifyAbilityFailed(const UGameplayAbility Ability, FGameplayTagContainer FailureReason)
```
Notify client that an ability failed to activate

### GetAttributeSetByTag
```angelscript
const UAttributeSet GetAttributeSetByTag(FGameplayTag AttributeSetTag)
```
通过 Tag 获取属性集
@param AttributeSetTag - 属性集的标识 Tag
@return 对应的属性集实例，如果不存在则返回 nullptr

