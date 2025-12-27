# FGameplayAbilityActorInfo

FGameplayAbilityActorInfo

Cached data associated with an Actor using an Ability.
        -Initialized from an AActor* in InitFromActor
        -Abilities use this to know what to actor upon. E.g., instead of being coupled to a specific actor class.
        -These are generally passed around as pointers to support polymorphism.
        -Projects can override UAbilitySystemGlobals::AllocAbilityActorInfo to override the default struct type that is created.

## 属性

### OwnerActor
- **类型**: `TWeakObjectPtr<AActor>`
- **描述**: The actor that owns the abilities, shouldn't be null

### AvatarActor
- **类型**: `TWeakObjectPtr<AActor>`
- **描述**: The physical representation of the owner, used for targeting and animation. This will often be null!

### PlayerController
- **类型**: `TWeakObjectPtr<APlayerController>`
- **描述**: PlayerController associated with the owning actor. This will often be null!

### AbilitySystemComponent
- **类型**: `TWeakObjectPtr<UAbilitySystemComponent>`
- **描述**: Ability System component associated with the owner actor, shouldn't be null

### SkeletalMeshComponent
- **类型**: `TWeakObjectPtr<USkeletalMeshComponent>`
- **描述**: Skeletal mesh of the avatar actor. Often null

### AnimInstance
- **类型**: `TWeakObjectPtr<UAnimInstance>`
- **描述**: Anim instance of the avatar actor. Often null

### MovementComponent
- **类型**: `TWeakObjectPtr<UMovementComponent>`
- **描述**: Movement component of the avatar actor. Often null

### AffectedAnimInstanceTag
- **类型**: `FName`
- **描述**: The linked Anim Instance that this component will play montages in. Use NAME_None for the main anim instance.

## 方法

### opAssign
```angelscript
FGameplayAbilityActorInfo& opAssign(FGameplayAbilityActorInfo Other)
```

