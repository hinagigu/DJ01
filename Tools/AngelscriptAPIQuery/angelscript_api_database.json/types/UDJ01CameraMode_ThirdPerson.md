# UDJ01CameraMode_ThirdPerson

**继承自**: `UDJ01CameraMode`

UDJ01CameraMode_ThirdPerson

     A basic third person camera mode.

## 属性

### TargetOffsetCurve
- **类型**: `const UCurveVector`
- **描述**: Curve that defines local-space offsets from the target using the view pitch to evaluate the curve.

### bUseRuntimeFloatCurves
- **类型**: `bool`
- **描述**: UE-103986: Live editing of RuntimeFloatCurves during PIE does not work (unlike curve assets).
Once that is resolved this will become the default and TargetOffsetCurve will be removed.

### TargetOffsetX
- **类型**: `FRuntimeFloatCurve`

### TargetOffsetY
- **类型**: `FRuntimeFloatCurve`

### TargetOffsetZ
- **类型**: `FRuntimeFloatCurve`

### CrouchOffsetBlendMultiplier
- **类型**: `float32`

### PenetrationBlendInTime
- **类型**: `float32`

### PenetrationBlendOutTime
- **类型**: `float32`

### bPreventPenetration
- **类型**: `bool`

### bDoPredictiveAvoidance
- **类型**: `bool`

### CollisionPushOutDistance
- **类型**: `float32`

### ReportPenetrationPercent
- **类型**: `float32`

### PenetrationAvoidanceFeelers
- **类型**: `TArray<FDJ01PenetrationAvoidanceFeeler>`
- **描述**: These are the feeler rays that are used to find where to place the camera.
Index: 0  : This is the normal feeler we use to prevent collisions.
Index: 1+ : These feelers are used if you bDoPredictiveAvoidance=true, to scan for potential impacts if the player
            were to rotate towards that direction and primitively collide the camera so that it pulls in before
            impacting the occluder.

