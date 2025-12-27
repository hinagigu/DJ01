# __ULegacyCameraShake

## 方法

### StartLegacyCameraShake
```angelscript
ULegacyCameraShake StartLegacyCameraShake(APlayerCameraManager PlayerCameraManager, TSubclassOf<ULegacyCameraShake> ShakeClass, float32 Scale, ECameraShakePlaySpace PlaySpace, FRotator UserPlaySpaceRot)
```
Backwards compatible method used by core BP redirectors. This is needed because the return value is specifically a legacy camera shake,
which some BP logic often uses directly to set oscillator/anim properties.

### StartLegacyCameraShakeFromSource
```angelscript
ULegacyCameraShake StartLegacyCameraShakeFromSource(APlayerCameraManager PlayerCameraManager, TSubclassOf<ULegacyCameraShake> ShakeClass, UCameraShakeSourceComponent SourceComponent, float32 Scale, ECameraShakePlaySpace PlaySpace, FRotator UserPlaySpaceRot)
```
Backwards compatible method used by core BP redirectors. This is needed because the return value is specifically a legacy camera shake,
which some BP logic often uses directly to set oscillator/anim properties.

### StaticClass
```angelscript
UClass StaticClass()
```

