# UEnvQueryTest_GameplayTags

**继承自**: `UEnvQueryTest`

EnvQueryTest_GameplayTags attempts to cast items to IGameplayTagAssetInterface and test their tags with TagQueryToMatch.
The behavior of IGameplayTagAssetInterface-less items is configured by bRejectIncompatibleItems.

## 属性

### TagQueryToMatch
- **类型**: `FGameplayTagQuery`

### bRejectIncompatibleItems
- **类型**: `bool`
- **描述**: This controls how to treat actors that do not implement IGameplayTagAssetInterface.
When set to True, actors that do not implement the interface will be ignored, meaning
they will not be scored and will not be considered when filtering.
When set to False, actors that do not implement the interface will be included in
filter and score operations with a zero score.

