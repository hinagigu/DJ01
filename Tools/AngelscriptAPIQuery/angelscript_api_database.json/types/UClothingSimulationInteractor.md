# UClothingSimulationInteractor

**继承自**: `UObject`

If a clothing simulation is able to be interacted with at runtime then a derived
interactor should be created, and at least the basic API implemented for that
simulation.
Only write to the simulation and context during the call to Sync, as that is
guaranteed to be a safe place to access this data.

## 方法

### ClothConfigUpdated
```angelscript
void ClothConfigUpdated()
```
Called to update the cloth config without restarting the simulation.

### DisableGravityOverride
```angelscript
void DisableGravityOverride()
```
Disable any currently set gravity override.

### EnableGravityOverride
```angelscript
void EnableGravityOverride(FVector InVector)
```
Set a new gravity override and enable the override.

### GetClothingInteractor
```angelscript
UClothingInteractor GetClothingInteractor(FString ClothingAssetName)
```
Return a cloth interactor for this simulation.

### GetNumCloths
```angelscript
int GetNumCloths()
```
Return the number of cloths run by the simulation.

### GetNumDynamicParticles
```angelscript
int GetNumDynamicParticles()
```
Return the number of dynamic (simulated) particles.

### GetNumIterations
```angelscript
int GetNumIterations()
```
Return the solver number of iterations.
This could be different from the number set if the simulation hasn't updated yet.

### GetNumKinematicParticles
```angelscript
int GetNumKinematicParticles()
```
Return the number of kinematic (animated) particles.

### GetNumSubsteps
```angelscript
int GetNumSubsteps()
```
Return the solver number of subdivisions./
This could be different from the number set if the simulation hasn't updated yet.

### GetSimulationTime
```angelscript
float32 GetSimulationTime()
```
Return the instant average simulation time in ms.

### PhysicsAssetUpdated
```angelscript
void PhysicsAssetUpdated()
```
Called to update collision status without restarting the simulation.

### SetAnimDriveSpringStiffness
```angelscript
void SetAnimDriveSpringStiffness(float32 InStiffness)
```
Set the stiffness of the spring force for the animation drive.

### SetMaxNumIterations
```angelscript
void SetMaxNumIterations(int MaxNumIterations)
```
Set the maximum number of solver iterations.

### SetNumIterations
```angelscript
void SetNumIterations(int NumIterations)
```
Set the number of time dependent solver iterations.

### SetNumSubsteps
```angelscript
void SetNumSubsteps(int NumSubsteps)
```
Set the number of substeps or subdivisions.

