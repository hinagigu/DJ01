# FXRMotionControllerData

## 属性

### bValid
- **类型**: `bool`

### DeviceName
- **类型**: `FName`

### ApplicationInstanceID
- **类型**: `FGuid`

### DeviceVisualType
- **类型**: `EXRVisualType`

### HandIndex
- **类型**: `EControllerHand`

### TrackingStatus
- **类型**: `ETrackingStatus`

### GripPosition
- **类型**: `FVector`
- **描述**: Vector representing an object being held in the player's hand

### GripRotation
- **类型**: `FQuat`
- **描述**: Quaternion representing an object being held in the player's hand

### AimPosition
- **类型**: `FVector`
- **描述**: For handheld controllers, gives a vector for pointing at objects

### AimRotation
- **类型**: `FQuat`
- **描述**: For handheld controllers, gives a quaternion for pointing at objects

### PalmPosition
- **类型**: `FVector`
- **描述**: For handheld controllers, gives a vector for representing the hand

### PalmRotation
- **类型**: `FQuat`
- **描述**: For handheld controllers, gives a quaternion for representing the hand

### HandKeyPositions
- **类型**: `TArray<FVector>`
- **描述**: The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

### HandKeyRotations
- **类型**: `TArray<FQuat>`
- **描述**: The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

### HandKeyRadii
- **类型**: `TArray<float32>`
- **描述**: The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

### bIsGrasped
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FXRMotionControllerData& opAssign(FXRMotionControllerData Other)
```

