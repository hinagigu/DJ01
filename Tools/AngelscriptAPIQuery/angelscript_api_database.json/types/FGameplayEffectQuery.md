# FGameplayEffectQuery

Every set condition within this query must match in order for the query to match. i.e. individual query elements are ANDed together.

## 属性

### CustomMatchDelegate_BP
- **类型**: `FActiveGameplayEffectQueryCustomMatch_Dynamic`
- **描述**: BP-exposed delegate for providing custom matching conditions.

### OwningTagQuery
- **类型**: `FGameplayTagQuery`

### EffectTagQuery
- **类型**: `FGameplayTagQuery`

### SourceTagQuery
- **类型**: `FGameplayTagQuery`

### SourceAggregateTagQuery
- **类型**: `FGameplayTagQuery`

### ModifyingAttribute
- **类型**: `FGameplayAttribute`

### EffectSource
- **类型**: `const UObject`

### EffectDefinition
- **类型**: `TSubclassOf<UGameplayEffect>`

## 方法

### opAssign
```angelscript
FGameplayEffectQuery& opAssign(FGameplayEffectQuery Other)
```

