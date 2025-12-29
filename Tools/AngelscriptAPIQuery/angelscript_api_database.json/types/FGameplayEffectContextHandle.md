# FGameplayEffectContextHandle

Handle that wraps a FGameplayEffectContext or subclass, to allow it to be polymorphic and replicate properly

## 方法

### AddActors
```angelscript
void AddActors(TArray<AActor> InActors, bool bReset)
```

### AddHitResult
```angelscript
void AddHitResult(FHitResult InHitResult, bool bReset)
```

### AddInstigator
```angelscript
void AddInstigator(AActor InInstigator, AActor InEffectCauser)
```

### AddOrigin
```angelscript
void AddOrigin(FVector InOrigin)
```

### AddSourceObject
```angelscript
void AddSourceObject(UObject NewSourceObject)
```

### Clear
```angelscript
void Clear()
```

### GetAbility
```angelscript
const UGameplayAbility GetAbility()
```

### GetAbilityLevel
```angelscript
int GetAbilityLevel()
```

### GetActors
```angelscript
TArray<AActor> GetActors()
```

### GetEffectCauser
```angelscript
AActor GetEffectCauser()
```

### GetHitResult
```angelscript
bool GetHitResult(FHitResult& OutHitResult)
```

### GetInstigator
```angelscript
AActor GetInstigator()
```

### GetOrigin
```angelscript
FVector GetOrigin()
```

### GetOriginalInstigator
```angelscript
AActor GetOriginalInstigator()
```

### GetOriginalInstigatorAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetOriginalInstigatorAbilitySystemComponent()
```

### GetOwnedGameplayTags
```angelscript
void GetOwnedGameplayTags(FGameplayTagContainer& ActorTagContainer, FGameplayTagContainer& SpecTagContainer)
```

### GetSourceObject
```angelscript
UObject GetSourceObject()
```

### HasOrigin
```angelscript
bool HasOrigin()
```

### IsLocallyControlled
```angelscript
bool IsLocallyControlled()
```

### IsLocallyControlledPlayer
```angelscript
bool IsLocallyControlledPlayer()
```

### IsValid
```angelscript
bool IsValid()
```

### SetAbility
```angelscript
void SetAbility(const UGameplayAbility InGameplayAbility)
```

### SetEffectCauser
```angelscript
void SetEffectCauser(AActor NewEffectCauser)
```

### opAssign
```angelscript
FGameplayEffectContextHandle& opAssign(FGameplayEffectContextHandle Other)
```

