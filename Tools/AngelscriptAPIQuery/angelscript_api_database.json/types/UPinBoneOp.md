# UPinBoneOp

**继承自**: `URetargetOpBase`

## 属性

### BonesToPin
- **类型**: `TArray<FPinBoneData>`

### PinTo
- **类型**: `ERetargetSourceOrTarget`
- **描述**: The bone, on the target skeleton to pin to.

### PinType
- **类型**: `EPinBoneType`
- **描述**: Apply this pin to the full transform, or just translation or rotation only.

### bMaintainOffset
- **类型**: `bool`
- **描述**: Maintain the original offset between the BoneToPin and BoneToPinTo

### GlobalOffset
- **类型**: `FTransform`
- **描述**: A manual offset to apply in global space

### LocalOffset
- **类型**: `FTransform`
- **描述**: A manual offset to apply in local space

