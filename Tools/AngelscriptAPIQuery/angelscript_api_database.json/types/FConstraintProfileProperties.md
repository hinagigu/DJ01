# FConstraintProfileProperties

Container for properties of a physics constraint that can be easily swapped at runtime. This is useful for switching different setups when going from ragdoll to standup for example

## 属性

### ProjectionLinearTolerance
- **类型**: `float32`
- **描述**: If the joint error is above this distance after the solve phase, the child body will be teleported to fix the error. Only used if bEnableProjection is true.

### ProjectionAngularTolerance
- **类型**: `float32`
- **描述**: If the joint error is above this distance after the solve phase, the child body will be teleported to fix the error. Only used if bEnableProjection is true.

### ProjectionLinearAlpha
- **类型**: `float32`
- **描述**: How much semi-physical linear projection correction to apply [0-1]. Only used if bEnableProjection is true and if hard limits are used.

### ProjectionAngularAlpha
- **类型**: `float32`
- **描述**: How much semi-physical angular projection correction to apply [0-1]. Only used if bEnableProjection is true and if hard limits are used.

### ShockPropagationAlpha
- **类型**: `float32`
- **描述**: How much shock propagation to apply [0-1]. Shock propagation increases the mass of the parent body for the last iteration of the
position and velocity solve phases. This can help stiffen up joint chains, but is also prone to introducing energy down the chain
especially at high alpha. Only used in bEnableShockPropagation is true.

### LinearBreakThreshold
- **类型**: `float32`
- **描述**: Force needed to break the distance constraint.

### LinearPlasticityThreshold
- **类型**: `float32`
- **描述**: [Chaos Only] Percent threshold from center of mass distance needed to reset the linear drive position target. This value can be greater than 1.

### AngularBreakThreshold
- **类型**: `float32`
- **描述**: Torque needed to break the joint.

### AngularPlasticityThreshold
- **类型**: `float32`
- **描述**: [Chaos Only] Degree threshold from target angle needed to reset the target angle.

### ContactTransferScale
- **类型**: `float32`
- **描述**: [Chaos Only] Colliison transfer on parent from the joints child. Range is 0.0-MAX

### LinearLimit
- **类型**: `FLinearConstraint`

### ConeLimit
- **类型**: `FConeConstraint`

### TwistLimit
- **类型**: `FTwistConstraint`

### LinearDrive
- **类型**: `FLinearDriveConstraint`

### AngularDrive
- **类型**: `FAngularDriveConstraint`

### LinearPlasticityType
- **类型**: `EConstraintPlasticityType`
- **描述**: Whether linear plasticity has a operation mode [free]

### bDisableCollision
- **类型**: `bool`

### bParentDominates
- **类型**: `bool`

### bEnableShockPropagation
- **类型**: `bool`

### bEnableProjection
- **类型**: `bool`

### bEnableMassConditioning
- **类型**: `bool`

### bAngularBreakable
- **类型**: `bool`

### bAngularPlasticity
- **类型**: `bool`

### bLinearBreakable
- **类型**: `bool`

### bLinearPlasticity
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FConstraintProfileProperties& opAssign(FConstraintProfileProperties Other)
```

