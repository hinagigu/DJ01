# __PhysicsThread

## 方法

### AddForce
```angelscript
void AddForce(FBodyInstanceAsyncPhysicsTickHandle Handle, FVector Force, bool bAccelChange)
```
Add a force to a single rigid body.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

@param  Force            Force vector to apply. Magnitude indicates strength of force.
@param  bAccelChange If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).

