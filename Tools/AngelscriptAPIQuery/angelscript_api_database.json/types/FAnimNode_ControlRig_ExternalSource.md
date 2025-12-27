# FAnimNode_ControlRig_ExternalSource

Animation node that allows animation ControlRig output to be used in an animation graph

## 属性

### Source
- **类型**: `FPoseLink`

### bResetInputPoseToInitial
- **类型**: `bool`
- **描述**: If this is checked the rig's pose needs to be reset to its initial
prior to evaluating the rig.

### bTransferInputPose
- **类型**: `bool`
- **描述**: If this is checked the bone pose coming from the AnimBP will be
transferred into the Control Rig.

### bTransferInputCurves
- **类型**: `bool`
- **描述**: If this is checked the curves coming from the AnimBP will be
transferred into the Control Rig.

### bTransferPoseInGlobalSpace
- **类型**: `bool`
- **描述**: Transferring the pose in global space guarantees a global pose match,
while transferring in local space ensures a match of the local transforms.
In general transforms only differ if the hierarchy topology differs
between the Control Rig and the skeleton used in the AnimBP.
Note: Turning this off can potentially improve performance.

### InputBonesToTransfer
- **类型**: `TArray<FBoneReference>`
- **描述**: An inclusive list of bones to transfer as part
of the input pose transfer phase.
If this list is empty all bones will be transferred.

### OutputBonesToTransfer
- **类型**: `TArray<FBoneReference>`
- **描述**: An inclusive list of bones to transfer as part
of the output pose transfer phase.
If this list is empty all bones will be transferred.

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`

### EventQueue
- **类型**: `TArray<FControlRigAnimNodeEventName>`
- **描述**: The customized event queue to run

## 方法

### opAssign
```angelscript
FAnimNode_ControlRig_ExternalSource& opAssign(FAnimNode_ControlRig_ExternalSource Other)
```

