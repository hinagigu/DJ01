# UMotionControllerComponent

**继承自**: `UPrimitiveComponent`

## 属性

### CurrentTrackingStatus
- **类型**: `ETrackingStatus`
- **描述**: The tracking status for the device (e.g. full tracking, inertial tracking only, no tracking)

### PlayerIndex
- **类型**: `int`

### MotionSource
- **类型**: `FName`

### bDisableLowLatencyUpdate
- **类型**: `bool`

## 方法

### GetAngularVelocity
```angelscript
bool GetAngularVelocity(FRotator& OutAngularVelocity)
```
If the motion tracking system provides angular velocity at this time OutAngularVelocity will be that velocity in deg/s in unreal world space and the function will return true. Note that it is not difficult to rotate a controller at more than 0.5 or 1 rotation per second briefly and some mathmatical operations(such as conversion to quaternion) lose rotations beyond 180 degrees or 360 degrees..  In some cases that is OK becuase the resulting final rotation is the same, but in some cases it would generate incorrect results.   If angular velocity is unavailable it will return false.

### GetHandJointPosition
```angelscript
FVector GetHandJointPosition(int jointIndex, bool& bValueFound)
```

### GetLinearAcceleration
```angelscript
bool GetLinearAcceleration(FVector& OutLinearAcceleration)
```
If the motion tracking system provides linear acceleration at this time the vector will be that acceleration in cm/(s^2) in unreal world space and the function will return true.  If acceleration is unavailable it will return false.

### GetLinearVelocity
```angelscript
bool GetLinearVelocity(FVector& OutLinearVelocity)
```
If the motion tracking system provides linear velocity at this time the vector will be that velocity in cm/s in unreal world space and the function will return true.  If velocity is unavailable it will return false.

### GetParameterValue
```angelscript
float32 GetParameterValue(FName InName, bool& bValueFound)
```
Returns the value of a custom parameter on the current in use Motion Controller (see member InUseMotionController). Only valid for the duration of OnMotionControllerUpdated

### IsTracked
```angelscript
bool IsTracked()
```
Whether or not this component had a valid tracked device this frame

### OnMotionControllerUpdated
```angelscript
void OnMotionControllerUpdated()
```
Blueprint Implementable function for responding to updated data from a motion controller (so we can use custom parameter values from it)

### SetAssociatedPlayerIndex
```angelscript
void SetAssociatedPlayerIndex(int NewPlayer)
```

### SetTrackingMotionSource
```angelscript
void SetTrackingMotionSource(FName NewSource)
```

