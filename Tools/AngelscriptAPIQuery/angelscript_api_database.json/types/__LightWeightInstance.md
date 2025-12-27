# __LightWeightInstance

## 方法

### ConvertActorToLightWeightInstance
```angelscript
FActorInstanceHandle ConvertActorToLightWeightInstance(AActor Actor)
```
Returns a handle to the light weight representation and destroys Actor if successful; Returns a handle to Actor otherwise

### CreateNewLightWeightInstance
```angelscript
FActorInstanceHandle CreateNewLightWeightInstance(UClass ActorClass, FTransform Transform, UDataLayerInstance Layer, UWorld World)
```
Returns a handle to a new light weight instance that represents an object of type ActorClass

