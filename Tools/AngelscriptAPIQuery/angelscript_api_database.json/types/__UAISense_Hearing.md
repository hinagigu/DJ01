# __UAISense_Hearing

## 方法

### ReportNoiseEvent
```angelscript
void ReportNoiseEvent(FVector NoiseLocation, float32 Loudness, AActor Instigator, float32 MaxRange, FName Tag)
```
Report a noise event.

@param NoiseLocation Location of the noise.
@param Loudness Loudness of the noise. If MaxRange is non-zero, modifies MaxRange, otherwise modifies the squared distance of the sensor's range.
@param Instigator Actor that triggered the noise.
@param MaxRange Max range at which the sound can be heard, multiplied by Loudness. Values <= 0 mean no limit (still limited by listener's range however).
@param Tag Identifier for the event.

### StaticClass
```angelscript
UClass StaticClass()
```

