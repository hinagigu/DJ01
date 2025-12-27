# UTargetTagRequirementsGameplayEffectComponent

**继承自**: `UGameplayEffectComponent`

Specifies tag requirements that the Target (owner of the Gameplay Effect) must have if this GE should apply or continue to execute

## 属性

### ApplicationTagRequirements
- **类型**: `FGameplayTagRequirements`
- **描述**: Tag requirements the target must have for this GameplayEffect to be applied. This is pass/fail at the time of application. If fail, this GE fails to apply.

### OngoingTagRequirements
- **类型**: `FGameplayTagRequirements`
- **描述**: Once Applied, these tags requirements are used to determined if the GameplayEffect is "on" or "off". A GameplayEffect can be off and do nothing, but still applied.

### RemovalTagRequirements
- **类型**: `FGameplayTagRequirements`
- **描述**: Tag requirements that if met will remove this effect. Also prevents effect application.

