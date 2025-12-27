# UPhysicalAnimationComponent

**继承自**: `UActorComponent`

## 属性

### StrengthMultiplyer
- **类型**: `float32`

## 方法

### ApplyPhysicalAnimationProfileBelow
```angelscript
void ApplyPhysicalAnimationProfileBelow(FName BodyName, FName ProfileName, bool bIncludeSelf, bool bClearNotFound)
```
Applies the physical animation profile to the body given and all bodies below.
@param  BodyName                     The body from which we'd like to start applying the physical animation profile. Finds all bodies below in the skeleton hierarchy. None implies all bodies
@param  ProfileName          The physical animation profile we'd like to apply. For each body in the physics asset we search for physical animation settings with this name.
@param  bIncludeSelf         Whether to include the provided body name in the list of bodies we act on (useful to ignore for cases where a root has multiple children)
@param  bClearNotFound       If true, bodies without the given profile name will have any existing physical animation settings cleared. If false, bodies without the given profile name are left untouched.

### ApplyPhysicalAnimationSettings
```angelscript
void ApplyPhysicalAnimationSettings(FName BodyName, FPhysicalAnimationData PhysicalAnimationData)
```
Applies the physical animation settings to the body given.

### ApplyPhysicalAnimationSettingsBelow
```angelscript
void ApplyPhysicalAnimationSettingsBelow(FName BodyName, FPhysicalAnimationData PhysicalAnimationData, bool bIncludeSelf)
```
Applies the physical animation settings to the body given and all bodies below.

### GetBodyTargetTransform
```angelscript
FTransform GetBodyTargetTransform(FName BodyName)
```
Returns the target transform for the given body. If physical animation component is not controlling this body, returns its current transform.

### SetSkeletalMeshComponent
```angelscript
void SetSkeletalMeshComponent(USkeletalMeshComponent InSkeletalMeshComponent)
```
Sets the skeletal mesh we are driving through physical animation. Will erase any existing physical animation data.

### SetStrengthMultiplyer
```angelscript
void SetStrengthMultiplyer(float32 InStrengthMultiplyer)
```
Updates strength multiplyer and any active motors

