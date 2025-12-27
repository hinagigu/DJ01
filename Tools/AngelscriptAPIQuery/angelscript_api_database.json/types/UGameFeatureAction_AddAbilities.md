# UGameFeatureAction_AddAbilities

**继承自**: `UGameFeatureAction_WorldActionBase`

UGameFeatureAction_AddAbilities

负责向指定类型的 Actor 授予 Abilities、AttributeSets 和 AbilitySets 的 GameFeatureAction。
这样可以通过 GameFeature 动态配置角色的技能和属性，而非在代码中硬编码。

## 属性

### AbilitiesList
- **类型**: `TArray<FGameFeatureAbilitiesEntry>`
- **描述**: 要处理的 Abilities 列表配置

