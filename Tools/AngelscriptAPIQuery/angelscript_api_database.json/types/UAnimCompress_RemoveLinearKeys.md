# UAnimCompress_RemoveLinearKeys

**继承自**: `UAnimCompress`

## 属性

### MaxPosDiff
- **类型**: `float32`
- **描述**: Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression.

### MaxAngleDiff
- **类型**: `float32`
- **描述**: Maximum angle difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression.

### MaxScaleDiff
- **类型**: `float32`
- **描述**: Maximum Scale difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression.

### MaxEffectorDiff
- **类型**: `float32`
- **描述**: As keys are tested for removal, we monitor the effects all the way down to the end effectors.
If their position changes by more than this amount as a result of removing a key, the key will be retained.
This value is used for all bones except the end-effectors parent.

### MinEffectorDiff
- **类型**: `float32`
- **描述**: As keys are tested for removal, we monitor the effects all the way down to the end effectors.
If their position changes by more than this amount as a result of removing a key, the key will be retained.
This value is used for the end-effectors parent, allowing tighter restrictions near the end of a skeletal chain.

### EffectorDiffSocket
- **类型**: `float32`
- **描述**: Error threshold for End Effectors with Sockets attached to them.
Typically more important bone, where we want to be less aggressive with compression.

### ParentKeyScale
- **类型**: `float32`
- **描述**: A scale value which increases the likelihood that a bone will retain a key if it's parent also had a key at the same time position.
Higher values can remove shaking artifacts from the animation, at the cost of compression.

### bRetarget
- **类型**: `bool`

### bActuallyFilterLinearKeys
- **类型**: `bool`

