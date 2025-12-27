# __PhysicsObject

## 方法

### ApplyRadialImpulse
```angelscript
void ApplyRadialImpulse(UPrimitiveComponent Component, FVector Origin, float32 Radius, float32 Strength, ERadialImpulseFalloff Falloff, bool bApplyStrain, float32 Strain, bool bVelChange, float32 MinValue, float32 MaxValue)
```
Apply a physics radial impulse with an optional strain on a specific component
Effect is applied within a sphere. When using linear falloff the effect will be minimum at the outer edge of the sphere and maximum at its center
@param Component              Primitive component to apply the impulse / strain on
@param Origin                 Positition of the origin of the radial effect in world space
@param Radius                 Radius of the radial effect ( beyond the radius, impulse will not be applied )
@param Strength               Strength of the impulse to apply ( Unit : (Kg * m / s) or ( m /s ) if bVelChange is true
@param FallOff                Type of falloff to use ( constant, linear )
@param bApplyStrain   Whether or not to apply strain on top of the impulse ( for destructible objects )
@param Strain                 If bApplyStrain is true, Strain to apply to the physics particles ( for destructible objects )
@param bVelChange             If true, impulse Strength parameter is interpretation as a change of velocity
@param MinValue               When using linear falloff, this define the falloff value at the outer edge of the sphere
@param MaxValue               When using linear falloff, this define the falloff value at the center of the sphere

### ExtractClosestPhysicsObjectResults
```angelscript
bool ExtractClosestPhysicsObjectResults(FClosestPhysicsObjectResult Result, FName& OutName)
```

### GetClosestPhysicsObjectFromWorldLocation
```angelscript
FClosestPhysicsObjectResult GetClosestPhysicsObjectFromWorldLocation(UPrimitiveComponent Component, FVector WorldLocation)
```

### GetPhysicsObjectWorldTransform
```angelscript
FTransform GetPhysicsObjectWorldTransform(UPrimitiveComponent Component, FName BoneName)
```

