# FAnimNode_LayeredBoneBlend

Layered blend (per bone); has dynamic number of blendposes that can blend per different bone sets

## 属性

### BasePose
- **类型**: `FPoseLink`

### BlendPoses
- **类型**: `TArray<FPoseLink>`

### BlendMode
- **类型**: `ELayeredBoneBlendMode`
- **描述**: Whether to use branch filters or a blend mask to specify an input pose per-bone influence

### BlendMasks
- **类型**: `TArray<TObjectPtr<UBlendProfile>>`
- **描述**: The blend masks to use for our layer inputs. Allows the use of per-bone alphas.
Blend masks are used when BlendMode is BlendMask.

### LayerSetup
- **类型**: `TArray<FInputBlendPose>`
- **描述**: Configuration for the parts of the skeleton to blend for each layer. Allows
certain parts of the tree to be blended out or omitted from the pose.
LayerSetup is used when BlendMode is BranchFilter.

### BlendWeights
- **类型**: `TArray<float32>`

### bMeshSpaceRotationBlend
- **类型**: `bool`

### bMeshSpaceScaleBlend
- **类型**: `bool`

### CurveBlendOption
- **类型**: `ECurveBlendOption`

### bBlendRootMotionBasedOnRootBone
- **类型**: `bool`
- **描述**: Whether to incorporate the per-bone blend weight of the root bone when lending root motion

### LODThreshold
- **类型**: `int`

## 方法

### opAssign
```angelscript
FAnimNode_LayeredBoneBlend& opAssign(FAnimNode_LayeredBoneBlend Other)
```

