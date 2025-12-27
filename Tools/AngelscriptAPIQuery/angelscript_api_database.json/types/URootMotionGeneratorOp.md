# URootMotionGeneratorOp

**继承自**: `URetargetOpBase`

## 属性

### SourceRootBone
- **类型**: `FName`
- **描述**: The root of the source skeleton.

### TargetRootBone
- **类型**: `FName`
- **描述**: The root of the target skeleton.

### TargetPelvisBone
- **类型**: `FName`
- **描述**: The pelvis of the target skeleton.

### RootMotionSource
- **类型**: `ERootMotionSource`
- **描述**: Where to copy the root motion from.
Copy From Source Root: copies the motion from the source root bone, but scales it according to relative height difference.
Generate From Target Pelvis: uses the retargeted Pelvis motion to generate root motion.
NOTE: Generating root motion from the Pelvis

### RootHeightSource
- **类型**: `ERootMotionHeightSource`
- **描述**: How to set the height of the root bone.
Copy Height From Source: copies the height of the root bone on the source skeleton's root bone.
Snap To Ground: sets the root bone height to the ground plane (Z=0).

### bPropagateToNonRetargetedChildren
- **类型**: `bool`
- **描述**: Will transform all children of the target root that are not themselves part of a retarget chain.

### bMaintainOffsetFromPelvis
- **类型**: `bool`
- **描述**: Applies only when generating root motion from the Pelvis.
Maintains the offset between the root and pelvis as recorded in the target retarget pose.
If false, the root bone is placed directly under the Pelvis bone.

### bRotateWithPelvis
- **类型**: `bool`
- **描述**: Applies only when generating root motion from the Pelvis.
When true, the applied offset will be rotated by the Pelvis.
(NOTE: This may cause unwanted rotations, for example if Pelvis Yaw is animated.)

### GlobalOffset
- **类型**: `FTransform`
- **描述**: A manual offset to apply in global space to the root bone.

