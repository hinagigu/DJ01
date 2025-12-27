# UParticleSystemComponent

**继承自**: `UFXSystemComponent`

A particle emitter.

## 属性

### LODMethod
- **类型**: `ParticleSystemLODMethod`

### InstanceParameters
- **类型**: `TArray<FParticleSysParam>`

### OnParticleSpawn
- **类型**: `FParticleSpawnSignature`

### OnParticleBurst
- **类型**: `FParticleBurstSignature`

### OnParticleDeath
- **类型**: `FParticleDeathSignature`

### OnParticleCollide
- **类型**: `FParticleCollisionSignature`

### SecondsBeforeInactive
- **类型**: `float32`

### CustomTimeDilation
- **类型**: `float32`

### AutoAttachParent
- **类型**: `TWeakObjectPtr<USceneComponent>`

### AutoAttachSocketName
- **类型**: `FName`

### AutoAttachLocationRule
- **类型**: `EAttachmentRule`

### AutoAttachRotationRule
- **类型**: `EAttachmentRule`

### AutoAttachScaleRule
- **类型**: `EAttachmentRule`

### OnSystemFinished
- **类型**: `FOnSystemFinished`

### Template
- **类型**: `UParticleSystem`

### bResetOnDetach
- **类型**: `bool`

### bAllowRecycling
- **类型**: `bool`

### bAutoManageAttachment
- **类型**: `bool`

### bAutoAttachWeldSimulatedBodies
- **类型**: `bool`

### bOverrideLODMethod
- **类型**: `bool`

## 方法

### BeginTrails
```angelscript
void BeginTrails(FName InFirstSocketName, FName InSecondSocketName, ETrailWidthMode InWidthMode, float32 InWidth)
```
Begins all trail emitters in this component.

@param        InFirstSocketName       The name of the first socket for the trail.
@param        InSecondSocketName      The name of the second socket for the trail.
@param        InWidthMode                     How the width value is applied to the trail.
@param        InWidth                         The width of the trail.

### CreateNamedDynamicMaterialInstance
```angelscript
UMaterialInstanceDynamic CreateNamedDynamicMaterialInstance(FName InName, UMaterialInterface SourceMaterial)
```
Creates a Dynamic Material Instance for the specified named material override, optionally from the supplied material.
@param Name - The slot name of the material to replace.  If invalid, the material is unchanged and NULL is returned.

### EndTrails
```angelscript
void EndTrails()
```
Ends all trail emitters in this component.

### GenerateParticleEvent
```angelscript
void GenerateParticleEvent(FName InEventName, float32 InEmitterTime, FVector InLocation, FVector InDirection, FVector InVelocity)
```
Record a kismet event.

@param  InEventName                             The name of the event that fired.
@param  InEmitterTime                   The emitter time when the event fired.
@param  InLocation                              The location of the particle when the event fired.
@param  InVelocity                              The velocity of the particle when the event fired.
@param  InNormal                                Normal vector of the collision in coordinate system of the returner. Zero=none.

### GetBeamEndPoint
```angelscript
bool GetBeamEndPoint(int EmitterIndex, FVector& OutEndPoint)
```
Get the beam end point

@param  EmitterIndex            The index of the emitter to get the value of

@return true            EmitterIndex is valid and End point is set - OutEndPoint is valid
                false           EmitterIndex invalid or End point is not set - OutEndPoint is invalid

### GetBeamSourcePoint
```angelscript
bool GetBeamSourcePoint(int EmitterIndex, int SourceIndex, FVector& OutSourcePoint)
```
Get the beam source point

@param  EmitterIndex            The index of the emitter to get
@param  SourceIndex                     Which beam within the emitter to get
@param  OutSourcePoint          Value of source point

@return true            EmitterIndex and SourceIndex are valid - OutSourcePoint is valid
                false           EmitterIndex or SourceIndex is invalid - OutSourcePoint is invalid

### GetBeamSourceStrength
```angelscript
bool GetBeamSourceStrength(int EmitterIndex, int SourceIndex, float32& OutSourceStrength)
```
Get the beam source strength

@param  EmitterIndex            The index of the emitter to get
@param  SourceIndex                     Which beam within the emitter to get
@param  OutSourceStrength               Value of source tangent

@return true            EmitterIndex and SourceIndex are valid - OutSourceStrength is valid
                false           EmitterIndex or SourceIndex is invalid - OutSourceStrength is invalid

### GetBeamSourceTangent
```angelscript
bool GetBeamSourceTangent(int EmitterIndex, int SourceIndex, FVector& OutTangentPoint)
```
Get the beam source tangent

@param  EmitterIndex            The index of the emitter to get
@param  SourceIndex                     Which beam within the emitter to get
@param  OutTangentPoint         Value of source tangent

@return true            EmitterIndex and SourceIndex are valid - OutTangentPoint is valid
                false           EmitterIndex or SourceIndex is invalid - OutTangentPoint is invalid

### GetBeamTargetPoint
```angelscript
bool GetBeamTargetPoint(int EmitterIndex, int TargetIndex, FVector& OutTargetPoint)
```
Get the beam target point

@param  EmitterIndex            The index of the emitter to get
@param  TargetIndex                     Which beam within the emitter to get
@param  OutTargetPoint          Value of target point

@return true            EmitterIndex and TargetIndex are valid - OutTargetPoint is valid
                false           EmitterIndex or TargetIndex is invalid - OutTargetPoint is invalid

### GetBeamTargetStrength
```angelscript
bool GetBeamTargetStrength(int EmitterIndex, int TargetIndex, float32& OutTargetStrength)
```
Get the beam target strength

@param  EmitterIndex            The index of the emitter to get
@param  TargetIndex                     Which beam within the emitter to get
@param  OutTargetStrength       Value of target tangent

@return true            EmitterIndex and TargetIndex are valid - OutTargetStrength is valid
                false           EmitterIndex or TargetIndex is invalid - OutTargetStrength is invalid

### GetBeamTargetTangent
```angelscript
bool GetBeamTargetTangent(int EmitterIndex, int TargetIndex, FVector& OutTangentPoint)
```
Get the beam target tangent

@param  EmitterIndex            The index of the emitter to get
@param  TargetIndex                     Which beam within the emitter to get
@param  OutTangentPoint         Value of target tangent

@return true            EmitterIndex and TargetIndex are valid - OutTangentPoint is valid
                false           EmitterIndex or TargetIndex is invalid - OutTangentPoint is invalid

### GetNamedMaterial
```angelscript
UMaterialInterface GetNamedMaterial(FName InName)
```
Returns a named material. If this named material is not found, returns NULL.

### GetNumActiveParticles
```angelscript
int GetNumActiveParticles()
```
Get the current number of active particles in this system

### SetBeamEndPoint
```angelscript
void SetBeamEndPoint(int EmitterIndex, FVector NewEndPoint)
```
Set the beam end point

@param  EmitterIndex            The index of the emitter to set it on
@param  NewEndPoint                     The value to set it to

### SetBeamSourcePoint
```angelscript
void SetBeamSourcePoint(int EmitterIndex, FVector NewSourcePoint, int SourceIndex)
```
Set the beam source point

@param  EmitterIndex            The index of the emitter to set it on
@param  NewSourcePoint          The value to set it to
@param  SourceIndex                     Which beam within the emitter to set it on

### SetBeamSourceStrength
```angelscript
void SetBeamSourceStrength(int EmitterIndex, float32 NewSourceStrength, int SourceIndex)
```
Set the beam source strength

@param  EmitterIndex            The index of the emitter to set it on
@param  NewSourceStrength       The value to set it to
@param  SourceIndex                     Which beam within the emitter to set it on

### SetBeamSourceTangent
```angelscript
void SetBeamSourceTangent(int EmitterIndex, FVector NewTangentPoint, int SourceIndex)
```
Set the beam source tangent

@param  EmitterIndex            The index of the emitter to set it on
@param  NewTangentPoint         The value to set it to
@param  SourceIndex                     Which beam within the emitter to set it on

### SetBeamTargetPoint
```angelscript
void SetBeamTargetPoint(int EmitterIndex, FVector NewTargetPoint, int TargetIndex)
```
Set the beam target point

@param  EmitterIndex            The index of the emitter to set it on
@param  NewTargetPoint          The value to set it to
@param  TargetIndex                     Which beam within the emitter to set it on

### SetBeamTargetStrength
```angelscript
void SetBeamTargetStrength(int EmitterIndex, float32 NewTargetStrength, int TargetIndex)
```
Set the beam target strength

@param  EmitterIndex            The index of the emitter to set it on
@param  NewTargetStrength       The value to set it to
@param  TargetIndex                     Which beam within the emitter to set it on

### SetBeamTargetTangent
```angelscript
void SetBeamTargetTangent(int EmitterIndex, FVector NewTangentPoint, int TargetIndex)
```
Set the beam target tangent

@param  EmitterIndex            The index of the emitter to set it on
@param  NewTangentPoint         The value to set it to
@param  TargetIndex                     Which beam within the emitter to set it on

### SetMaterialParameter
```angelscript
void SetMaterialParameter(FName ParameterName, UMaterialInterface Param)
```
Set a named material instance parameter on this ParticleSystemComponent.
Updates the parameter if it already exists, or creates a new entry if not.

### SetTemplate
```angelscript
void SetTemplate(UParticleSystem NewTemplate)
```
Change the ParticleSystem used by this ParticleSystemComponent

### SetTrailSourceData
```angelscript
void SetTrailSourceData(FName InFirstSocketName, FName InSecondSocketName, ETrailWidthMode InWidthMode, float32 InWidth)
```
Sets the defining data for all trails in this component.

@param        InFirstSocketName       The name of the first socket for the trail.
@param        InSecondSocketName      The name of the second socket for the trail.
@param        InWidthMode                     How the width value is applied to the trail.
@param        InWidth                         The width of the trail.

