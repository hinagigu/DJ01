# URadialForceComponent

**继承自**: `USceneComponent`

Used to emit a radial force or impulse that can affect physics objects and or destructible objects.

## 属性

### Radius
- **类型**: `float32`

### Falloff
- **类型**: `ERadialImpulseFalloff`

### ImpulseStrength
- **类型**: `float32`

### ForceStrength
- **类型**: `float32`

### DestructibleDamage
- **类型**: `float32`

### ObjectTypesToAffect
- **类型**: `TArray<EObjectTypeQuery>`
- **描述**: The object types that are affected by this radial force

### bImpulseVelChange
- **类型**: `bool`

### bIgnoreOwningActor
- **类型**: `bool`

## 方法

### AddObjectTypeToAffect
```angelscript
void AddObjectTypeToAffect(EObjectTypeQuery ObjectType)
```
Add an object type for this radial force to affect

### FireImpulse
```angelscript
void FireImpulse()
```
Fire a single impulse

### RemoveObjectTypeToAffect
```angelscript
void RemoveObjectTypeToAffect(EObjectTypeQuery ObjectType)
```
Remove an object type that is affected by this radial force

