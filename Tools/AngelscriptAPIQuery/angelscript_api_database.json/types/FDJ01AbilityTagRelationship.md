# FDJ01AbilityTagRelationship

Struct that defines the relationship between different ability tags

## 属性

### AbilityTag
- **类型**: `FGameplayTag`
- **描述**: The tag that this container relationship is about. Single tag, but abilities can have multiple of these

### AbilityTagsToBlock
- **类型**: `FGameplayTagContainer`
- **描述**: The other ability tags that will be blocked by any ability using this tag

### AbilityTagsToCancel
- **类型**: `FGameplayTagContainer`
- **描述**: The other ability tags that will be canceled by any ability using this tag

### ActivationRequiredTags
- **类型**: `FGameplayTagContainer`
- **描述**: If an ability has the tag, this is implicitly added to the activation required tags of the ability

### ActivationBlockedTags
- **类型**: `FGameplayTagContainer`
- **描述**: If an ability has the tag, this is implicitly added to the activation blocked tags of the ability

## 方法

### opAssign
```angelscript
FDJ01AbilityTagRelationship& opAssign(FDJ01AbilityTagRelationship Other)
```

