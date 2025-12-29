# FGameplayAbilityActorInfo

FGameplayAbilityActorInfo

Cached data associated with an Actor using an Ability.
        -Initialized from an AActor* in InitFromActor
        -Abilities use this to know what to actor upon. E.g., instead of being coupled to a specific actor class.
        -These are generally passed around as pointers to support polymorphism.
        -Projects can override UAbilitySystemGlobals::AllocAbilityActorInfo to override the default struct type that is created.

## 方法

### ClearActorInfo
```angelscript
void ClearActorInfo()
```

### GetAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetAbilitySystemComponent()
```

### GetAffectedAnimInstanceTag
```angelscript
FName GetAffectedAnimInstanceTag()
```

### GetAnimInstance
```angelscript
UAnimInstance GetAnimInstance()
```

### GetAnimInstanceFromSkeletalMesh
```angelscript
UAnimInstance GetAnimInstanceFromSkeletalMesh()
```

### GetAvatarActor
```angelscript
AActor GetAvatarActor()
```

### GetMovementComponent
```angelscript
UMovementComponent GetMovementComponent()
```

### GetOwnerActor
```angelscript
AActor GetOwnerActor()
```

### GetPlayerController
```angelscript
APlayerController GetPlayerController()
```

### GetSkeletalMeshComponent
```angelscript
USkeletalMeshComponent GetSkeletalMeshComponent()
```

### InitFromActor
```angelscript
void InitFromActor(AActor OwnerActor, AActor AvatarActor, UAbilitySystemComponent InAbilitySystemComponent)
```

### IsLocallyControlled
```angelscript
bool IsLocallyControlled()
```

### IsLocallyControlledPlayer
```angelscript
bool IsLocallyControlledPlayer()
```

### IsNetAuthority
```angelscript
bool IsNetAuthority()
```

### SetAbilitySystemComponent
```angelscript
void SetAbilitySystemComponent(UAbilitySystemComponent Component)
```

### SetAffectedAnimInstanceTag
```angelscript
void SetAffectedAnimInstanceTag(FName Name)
```

### SetAnimInstance
```angelscript
void SetAnimInstance(UAnimInstance Instance)
```

### SetAvatarActor
```angelscript
void SetAvatarActor(AActor Actor)
```

### SetMovementComponent
```angelscript
void SetMovementComponent(UMovementComponent Instance)
```

### SetOwnerActor
```angelscript
void SetOwnerActor(AActor Actor)
```

### SetPlayerController
```angelscript
void SetPlayerController(APlayerController Controller)
```

### SetSkeletalMeshComponent
```angelscript
void SetSkeletalMeshComponent(USkeletalMeshComponent Component)
```

### opAssign
```angelscript
FGameplayAbilityActorInfo& opAssign(FGameplayAbilityActorInfo Other)
```

