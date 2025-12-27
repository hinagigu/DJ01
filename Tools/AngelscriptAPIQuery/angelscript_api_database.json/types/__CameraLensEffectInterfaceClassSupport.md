# __CameraLensEffectInterfaceClassSupport

## 方法

### GetInterfaceClass
```angelscript
TSubclassOf<AActor> GetInterfaceClass(FCameraLensInterfaceClassSupport CameraLens)
```
Returns the class represented by this lens effect wrapper...

### IsInterfaceClassValid
```angelscript
void IsInterfaceClassValid(FCameraLensInterfaceClassSupport CameraLens, EInterfaceValidResult& Result)
```
Check whether or not the interface class is valid

### SetInterfaceClass
```angelscript
void SetInterfaceClass(TSubclassOf<AActor> Class, FCameraLensInterfaceClassSupport& Var, EInterfaceValidResult& Result)
```
Set the represented class of the passed in variable. Note: Check the tooltips on the individual pins.
You cannot bypass the validation by connecting a wires to this node!!

@param Class MUST implement CameraLensEffectInterface - when connecting variables to the input, take care that the input class does in fact implement the interface.
@param Var The wrapper (for validation purposes) of the lens effect class.

