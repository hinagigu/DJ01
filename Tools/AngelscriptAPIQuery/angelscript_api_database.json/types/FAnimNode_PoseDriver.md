# FAnimNode_PoseDriver

RBF based orientation driver

## 属性

### SourcePose
- **类型**: `FPoseLink`

### SourceBones
- **类型**: `TArray<FBoneReference>`
- **描述**: Bone to use for driving parameters based on its orientation

### EvalSpaceBone
- **类型**: `FBoneReference`
- **描述**: Optional other bone space to use when reading SourceBone transform.
If not specified, the local space of SourceBone will be used. (ie relative to parent bone)

### bEvalFromRefPose
- **类型**: `bool`
- **描述**: Evaluate SourceBone transform relative from its Reference Pose.
This is recommended when using Swing and Twist Angle as Distance Method, since the twist will be computed from RefPose.

If not specified, the local space of SourceBone will be used. (ie relative to parent bone)
This mode won't work in conjunction with EvalSpaceBone;

### OnlyDriveBones
- **类型**: `TArray<FBoneReference>`
- **描述**: List of bones that will modified by this node. If no list is provided, all bones bones with a track in the PoseAsset will be modified

### PoseTargets
- **类型**: `TArray<FPoseDriverTarget>`
- **描述**: Targets used to compare with current pose and drive morphs/poses

### RBFParams
- **类型**: `FRBFParams`
- **描述**: Parameters used by RBF solver

### DriveSource
- **类型**: `EPoseDriverSource`
- **描述**: Which part of the transform is read

### DriveOutput
- **类型**: `EPoseDriverOutput`
- **描述**: Whether we should drive poses or curves

### LODThreshold
- **类型**: `int`
- **描述**: * Max LOD that this node is allowed to run
* For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
* when the component LOD becomes 3, it will stop update/evaluate
* currently transition would be issue and that has to be re-visited

### PoseAsset
- **类型**: `UPoseAsset`

### BlendWeight
- **类型**: `float32`
- **描述**: Last encountered blendweight for this node

### InternalTimeAccumulator
- **类型**: `float32`
- **描述**: Accumulated time used to reference the asset in this node

## 方法

### opAssign
```angelscript
FAnimNode_PoseDriver& opAssign(FAnimNode_PoseDriver Other)
```

