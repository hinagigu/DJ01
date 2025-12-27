# FGameplayCueNotify_SpawnResult

FGameplayCueNotify_SpawnResult

    Temporary structure used to track results of spawning components.

## 属性

### FxSystemComponents
- **类型**: `TArray<TObjectPtr<UFXSystemComponent>>`
- **描述**: List of FX components spawned.  There may be null pointers here as it matches the defined order.

### AudioComponents
- **类型**: `TArray<TObjectPtr<UAudioComponent>>`
- **描述**: List of audio components spawned.  There may be null pointers here as it matches the defined order.

### CameraShakes
- **类型**: `TArray<TObjectPtr<UCameraShakeBase>>`
- **描述**: List of camera shakes played.  There will be one camera shake per local player controller if shake is played in world.

### ForceFeedbackComponent
- **类型**: `UForceFeedbackComponent`
- **描述**: Force feedback component that was spawned.  This is only valid when force feedback is set to play in world.

### DecalComponent
- **类型**: `UDecalComponent`
- **描述**: Spawned decal component.  This may be null.

## 方法

### opAssign
```angelscript
FGameplayCueNotify_SpawnResult& opAssign(FGameplayCueNotify_SpawnResult Other)
```

