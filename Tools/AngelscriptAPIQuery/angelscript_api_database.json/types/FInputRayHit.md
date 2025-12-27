# FInputRayHit

* FInputRayHit is returned by various hit-test interface functions.
* Generally this is intended to be returned as the result of a hit-test with a FInputDeviceRay

## 属性

### bHit
- **类型**: `bool`
- **描述**: true if ray hit something, false otherwise

### HitDepth
- **类型**: `float`
- **描述**: distance along ray at which intersection occurred

### HitNormal
- **类型**: `FVector`
- **描述**: Normal at hit point, if available

### bHasHitNormal
- **类型**: `bool`
- **描述**: True if HitNormal was set

### HitIdentifier
- **类型**: `int`
- **描述**: Client-defined integer identifier for hit object/element/target/etc

### HitObject
- **类型**: `TWeakObjectPtr<UObject>`
- **描述**: Client-defined pointer for UObject-derived hit owners.
HitOwner and HitObject should be set to the same pointer if the HitOwner derives from UObject.

## 方法

### opAssign
```angelscript
FInputRayHit& opAssign(FInputRayHit Other)
```

