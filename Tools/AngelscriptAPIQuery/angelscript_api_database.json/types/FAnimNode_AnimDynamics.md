# FAnimNode_AnimDynamics

## 属性

### LinearDampingOverride
- **类型**: `float32`

### AngularDampingOverride
- **类型**: `float32`

### RelativeSpaceBone
- **类型**: `FBoneReference`
- **描述**: When in BoneRelative sim space, the simulation will use this bone as the origin

### BoundBone
- **类型**: `FBoneReference`
- **描述**: The bone to attach the physics body to, if bChain is true this is the top of the chain

### ChainEnd
- **类型**: `FBoneReference`
- **描述**: If bChain is true this is the bottom of the chain, otherwise ignored

### PhysicsBodyDefinitions
- **类型**: `TArray<FAnimPhysBodyDefinition>`

### GravityScale
- **类型**: `float32`

### GravityOverride
- **类型**: `FVector`

### LinearSpringConstant
- **类型**: `float32`

### AngularSpringConstant
- **类型**: `float32`

### WindScale
- **类型**: `float32`
- **描述**: Scale to apply to calculated wind velocities in the solver

### ComponentLinearAccScale
- **类型**: `FVector`
- **描述**: When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation.

### ComponentLinearVelScale
- **类型**: `FVector`
- **描述**: When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity.

### ComponentAppliedLinearAccClamp
- **类型**: `FVector`
- **描述**: When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large.

### AngularBiasOverride
- **类型**: `float32`

### NumSolverIterationsPreUpdate
- **类型**: `int`
- **描述**: Number of update passes on the linear and angular limits before we solve the position of the bodies recommended to be four times the value of NumSolverIterationsPostUpdate

### NumSolverIterationsPostUpdate
- **类型**: `int`
- **描述**: Number of update passes on the linear and angular limits after we solve the position of the bodies, recommended to be around a quarter of NumSolverIterationsPreUpdate

### SphericalLimits
- **类型**: `TArray<FAnimPhysSphericalLimit>`
- **描述**: List of available spherical limits for this node

### ExternalForce
- **类型**: `FVector`
- **描述**: An external force to apply to all bodies in the simulation when ticked, specified in world space

### PlanarLimits
- **类型**: `TArray<FAnimPhysPlanarLimit>`
- **描述**: List of available planar limits for this node

### SimulationSpace
- **类型**: `AnimPhysSimSpaceType`

### RetargetingSettings
- **类型**: `FRotationRetargetingInfo`
- **描述**: The settings for rotation retargeting

### ComponentPose
- **类型**: `FComponentSpacePoseLink`

### LODThreshold
- **类型**: `int`

### AlphaInputType
- **类型**: `EAnimAlphaInputType`

### bAlphaBoolEnabled
- **类型**: `bool`

### Alpha
- **类型**: `float32`

### AlphaScaleBias
- **类型**: `FInputScaleBias`

### AlphaBoolBlend
- **类型**: `FInputAlphaBoolBlend`

### AlphaCurveName
- **类型**: `FName`

### AlphaScaleBiasClamp
- **类型**: `FInputScaleBiasClamp`

### bUseSphericalLimits
- **类型**: `bool`

### bUsePlanarLimit
- **类型**: `bool`

### bDoUpdate
- **类型**: `bool`

### bDoEval
- **类型**: `bool`

### bOverrideLinearDamping
- **类型**: `bool`

### bOverrideAngularBias
- **类型**: `bool`

### bOverrideAngularDamping
- **类型**: `bool`

### bEnableWind
- **类型**: `bool`

### bUseGravityOverride
- **类型**: `bool`

### bGravityOverrideInSimSpace
- **类型**: `bool`

### bLinearSpring
- **类型**: `bool`

### bAngularSpring
- **类型**: `bool`

### bChain
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_AnimDynamics& opAssign(FAnimNode_AnimDynamics Other)
```

