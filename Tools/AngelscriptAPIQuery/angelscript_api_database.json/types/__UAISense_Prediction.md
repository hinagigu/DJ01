# __UAISense_Prediction

## 方法

### RequestControllerPredictionEvent
```angelscript
void RequestControllerPredictionEvent(AAIController Requestor, AActor PredictedActor, float32 PredictionTime)
```
Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
    Location is being predicted based on PredicterActor's current location and velocity

### RequestPawnPredictionEvent
```angelscript
void RequestPawnPredictionEvent(APawn Requestor, AActor PredictedActor, float32 PredictionTime)
```
Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
    Location is being predicted based on PredicterActor's current location and velocity

### StaticClass
```angelscript
UClass StaticClass()
```

