# FInheritedTagContainer

Structure that is used to combine tags from parent and child blueprints in a safe way

## 属性

### CombinedTags
- **类型**: `FGameplayTagContainer`
- **描述**: CombinedTags = Inherited - Removed + Added

### Added
- **类型**: `FGameplayTagContainer`

### Removed
- **类型**: `FGameplayTagContainer`

## 方法

### AddTag
```angelscript
void AddTag(FGameplayTag TagToAdd)
```

### RemoveTag
```angelscript
void RemoveTag(FGameplayTag TagToRemove)
```

### opAssign
```angelscript
FInheritedTagContainer& opAssign(FInheritedTagContainer Other)
```

