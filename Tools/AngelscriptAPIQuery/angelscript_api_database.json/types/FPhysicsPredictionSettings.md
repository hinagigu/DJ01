# FPhysicsPredictionSettings

Physics Prediction Settings

## 属性

### bEnablePhysicsPrediction
- **类型**: `bool`
- **描述**: Enable networked physics prediction (experimental)
Note: If an AActor::PhysicsReplicationMode is set to use Resimulation this will allow physics to cache history which is required by resimulation replication.
Note: This can also affect how physics is solved even when not using resimulation.

### bEnablePhysicsResimulation
- **类型**: `bool`
- **描述**: Forces the PlayerController to sync inputs as used in Physics Prediction.
Only enable this if actively using a custom solution that needs this enabled for resimulation.
This is automatically enabled when using the recommended NetworkPhysicsComponent on a pawn to handle Rewind / Resimulation.

### ResimulationErrorThreshold
- **类型**: `float32`
- **描述**: Distance in centimeters before a state discrepancy triggers a resimulation

### MaxSupportedLatencyPrediction
- **类型**: `float32`
- **描述**: Amount of RTT (Round Trip Time) latency for the prediction to support in milliseconds.

## 方法

### opAssign
```angelscript
FPhysicsPredictionSettings& opAssign(FPhysicsPredictionSettings Other)
```

