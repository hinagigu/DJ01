# FGameplayTagContainer

A Tag Container holds a collection of FGameplayTags, tags are included explicitly by adding them, and implicitly from adding child tags

## 属性

### GameplayTags
- **类型**: `TArray<FGameplayTag>`
- **描述**: Array of gameplay tags

## 方法

### AddLeafTag
```angelscript
void AddLeafTag(FGameplayTag TagToAdd)
```

### AddTag
```angelscript
void AddTag(FGameplayTag TagToAdd)
```

### AddTagFast
```angelscript
void AddTagFast(FGameplayTag TagToAdd)
```

### Filter
```angelscript
FGameplayTagContainer Filter(FGameplayTagContainer OtherContainer)
```

### FilterExact
```angelscript
FGameplayTagContainer FilterExact(FGameplayTagContainer OtherContainer)
```

### First
```angelscript
FGameplayTag First()
```

### GetGameplayTagParents
```angelscript
FGameplayTagContainer GetGameplayTagParents()
```

### HasAll
```angelscript
bool HasAll(FGameplayTagContainer ContainerToCheck)
```

### HasAllExact
```angelscript
bool HasAllExact(FGameplayTagContainer ContainerToCheck)
```

### HasAny
```angelscript
bool HasAny(FGameplayTagContainer ContainerToCheck)
```

### HasAnyExact
```angelscript
bool HasAnyExact(FGameplayTagContainer ContainerToCheck)
```

### HasTag
```angelscript
bool HasTag(FGameplayTag TagToCheck)
```

### HasTagExact
```angelscript
bool HasTagExact(FGameplayTag TagToCheck)
```

### IsEmpty
```angelscript
bool IsEmpty()
```

### IsValid
```angelscript
bool IsValid()
```

### Last
```angelscript
FGameplayTag Last()
```

### MatchesQuery
```angelscript
bool MatchesQuery(FGameplayTagQuery Query)
```

### Num
```angelscript
int Num()
```

### RemoveTag
```angelscript
bool RemoveTag(FGameplayTag TagToRemove)
```

### RemoveTags
```angelscript
void RemoveTags(FGameplayTagContainer TagsToRemove)
```

### opAssign
```angelscript
FGameplayTagContainer& opAssign(FGameplayTagContainer Other)
```

