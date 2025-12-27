# FGameplayTag

A single gameplay tag, which represents a hierarchical name of the form x.y that is registered in the GameplayTagsManager
You can filter the gameplay tags displayed in the editor using, meta = (Categories = "Tag1.Tag2.Tag3"))

## 方法

### opEquals
```angelscript
bool opEquals(FGameplayTag Other)
```

### GetTagName
```angelscript
FName GetTagName()
```

### ToString
```angelscript
FString ToString()
```

### GetGameplayTagParents
```angelscript
FGameplayTagContainer GetGameplayTagParents()
```

### GetSingleTagContainer
```angelscript
FGameplayTagContainer GetSingleTagContainer()
```

### IsValid
```angelscript
bool IsValid()
```

### MatchesAny
```angelscript
bool MatchesAny(FGameplayTagContainer ContainerToCheck)
```

### MatchesAnyExact
```angelscript
bool MatchesAnyExact(FGameplayTagContainer ContainerToCheck)
```

### MatchesTag
```angelscript
bool MatchesTag(FGameplayTag TagToCheck)
```

### MatchesTagDepth
```angelscript
int MatchesTagDepth(FGameplayTag TagToCheck)
```

### MatchesTagExact
```angelscript
bool MatchesTagExact(FGameplayTag TagToCheck)
```

### RequestDirectParent
```angelscript
FGameplayTag RequestDirectParent()
```

### opAssign
```angelscript
FGameplayTag& opAssign(FGameplayTag Other)
```

