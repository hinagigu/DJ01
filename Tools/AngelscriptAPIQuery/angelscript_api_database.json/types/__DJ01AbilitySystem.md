# __DJ01AbilitySystem

## 方法

### GetAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetAbilitySystemComponent(AActor Actor)
```
从 Actor 获取 AbilitySystemComponent
支持直接实现 IAbilitySystemInterface 的 Actor 或通过 PlayerState 持有 ASC 的 Pawn

### GetAttributeSetByTag
```angelscript
const UAttributeSet GetAttributeSetByTag(AActor Actor, FGameplayTag AttributeSetTag)
```
通过 Tag 从 Actor 获取属性集
@param Actor - 拥有 ASC 的 Actor（角色、PlayerState 等）
@param AttributeSetTag - 属性集的标识 Tag（如 AttributeSet.Health）
@return 对应的属性集实例，如果不存在则返回 nullptr

### GetAttributeSetByTagFromASC
```angelscript
const UAttributeSet GetAttributeSetByTagFromASC(UDJ01AbilitySystemComponent ASC, FGameplayTag AttributeSetTag)
```
通过 Tag 从 ASC 获取属性集

### GetDJ01AbilitySystemComponent
```angelscript
UDJ01AbilitySystemComponent GetDJ01AbilitySystemComponent(AActor Actor)
```
从 Actor 获取 DJ01AbilitySystemComponent

