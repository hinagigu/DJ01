# FGameFeatureAbilitiesEntry

FGameFeatureAbilitiesEntry
GameFeature 中添加 Abilities 的配置条目

## 属性

### ActorClass
- **类型**: `TSoftClassPtr<AActor>`
- **描述**: 目标 Actor 类

### GrantedAbilities
- **类型**: `TArray<FDJ01AbilityGrant>`
- **描述**: 要授予的 Ability 列表

### GrantedAttributes
- **类型**: `TArray<FDJ01AttributeSetGrant>`
- **描述**: 要授予的 AttributeSet 列表

### GrantedAbilitySets
- **类型**: `TArray<TSoftObjectPtr<UDJ01AbilitySet>>`
- **描述**: 要授予的 AbilitySet 列表

## 方法

### opAssign
```angelscript
FGameFeatureAbilitiesEntry& opAssign(FGameFeatureAbilitiesEntry Other)
```

