# UPhysicsConstraintComponent

**继承自**: `USceneComponent`

This is effectively a joint that allows you to connect 2 rigid bodies together. You can create different types of joints using the various parameters of this component.

## 属性

### ConstraintActor1
- **类型**: `AActor`
- **描述**: Pointer to first Actor to constrain.

### ComponentName1
- **类型**: `FConstrainComponentPropName`
- **描述**: Name of first component property to constrain. If Actor1 is NULL, will look within Owner.
If this is NULL, will use RootComponent of Actor1

### ConstraintActor2
- **类型**: `AActor`
- **描述**: Pointer to second Actor to constrain.

### ComponentName2
- **类型**: `FConstrainComponentPropName`
- **描述**: Name of second component property to constrain. If Actor2 is NULL, will look within Owner.
If this is NULL, will use RootComponent of Actor2

### OnConstraintBroken
- **类型**: `FConstraintBrokenSignature`

### OnPlasticDeformation
- **类型**: `FPlasticDeformationEventSignature`

### ConstraintInstance
- **类型**: `FConstraintInstance`
- **描述**: All constraint settings

## 方法

### BreakConstraint
```angelscript
void BreakConstraint()
```
Break this constraint

### GetConstrainedComponents
```angelscript
void GetConstrainedComponents(UPrimitiveComponent& OutComponent1, FName& OutBoneName1, UPrimitiveComponent& OutComponent2, FName& OutBoneName2)
```
Get connected components and potential related attachement bones

### GetConstraint
```angelscript
FConstraintInstanceAccessor GetConstraint()
```
Gets the constraint object

### GetConstraintForce
```angelscript
void GetConstraintForce(FVector& OutLinearForce, FVector& OutAngularForce)
```
Retrieve the constraint force most recently applied to maintain this constraint. Returns 0 forces if the constraint is not initialized or broken.

### GetCurrentSwing1
```angelscript
float32 GetCurrentSwing1()
```
Gets the current Swing1 of the constraint

### GetCurrentSwing2
```angelscript
float32 GetCurrentSwing2()
```
Gets the current Swing2 of the constraint

### GetCurrentTwist
```angelscript
float32 GetCurrentTwist()
```
Gets the current Angular Twist of the constraint

### IsBroken
```angelscript
bool IsBroken()
```
Retrieve the status of constraint being broken.

### IsProjectionEnabled
```angelscript
bool IsProjectionEnabled()
```
Is projection enabled. See SetProjectionEnabled

### SetAngularBreakable
```angelscript
void SetAngularBreakable(bool bAngularBreakable, float32 AngularBreakThreshold)
```
Sets the Angular Breakable properties
     @param bAngularBreakable                Whether it is possible to break the joint with angular force
     @param AngularBreakThreshold    Torque needed to break the joint

### SetAngularDriveMode
```angelscript
void SetAngularDriveMode(EAngularDriveMode DriveMode)
```
Switches the angular drive mode between SLERP and Twist And Swing

     @param DriveMode        The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock

### SetAngularDriveParams
```angelscript
void SetAngularDriveParams(float32 PositionStrength, float32 VelocityStrength, float32 InForceLimit)
```
Sets the drive params for the angular drive.
    @param PositionStrength         Positional strength for the drive (stiffness)
    @param VelocityStrength         Velocity strength of the drive (damping)
    @param InForceLimit     Max force applied by the drive

### SetAngularOrientationTarget
```angelscript
void SetAngularOrientationTarget(FRotator InPosTarget)
```
Sets the target orientation for the angular drive.
    @param InPosTarget              Target orientation

### SetAngularPlasticity
```angelscript
void SetAngularPlasticity(bool bAngularPlasticity, float32 AngularPlasticityThreshold)
```
Sets the Angular Plasticity properties
     @param bAngularPlasticity               Whether it is possible to reset the target angle from the angular displacement
     @param AngularPlasticityThreshold       Degrees needed to reset the rest state of the joint

### SetAngularSwing1Limit
```angelscript
void SetAngularSwing1Limit(EAngularConstraintMotion MotionType, float32 Swing1LimitAngle)
```
Sets the Angular Swing1 Motion Type
     @param ConstraintType   New Constraint Type
     @param Swing1LimitAngle Size of limit in degrees

### SetAngularSwing2Limit
```angelscript
void SetAngularSwing2Limit(EAngularConstraintMotion MotionType, float32 Swing2LimitAngle)
```
Sets the Angular Swing2 Motion Type
     @param ConstraintType   New Constraint Type
     @param Swing2LimitAngle Size of limit in degrees

### SetAngularTwistLimit
```angelscript
void SetAngularTwistLimit(EAngularConstraintMotion ConstraintType, float32 TwistLimitAngle)
```
Sets the Angular Twist Motion Type
     @param ConstraintType   New Constraint Type
     @param TwistLimitAngle  Size of limit in degrees

### SetAngularVelocityDriveSLERP
```angelscript
void SetAngularVelocityDriveSLERP(bool bEnableSLERP)
```
Enables/Disables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP

     @param bEnableSLERP             Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

### SetAngularVelocityDriveTwistAndSwing
```angelscript
void SetAngularVelocityDriveTwistAndSwing(bool bEnableTwistDrive, bool bEnableSwingDrive)
```
Enables/Disables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing

     @param bEnableSwingDrive        Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param bEnableTwistDrive        Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

### SetAngularVelocityTarget
```angelscript
void SetAngularVelocityTarget(FVector InVelTarget)
```
Sets the target velocity for the angular drive.
    @param InVelTarget              Target velocity

### SetConstrainedComponents
```angelscript
void SetConstrainedComponents(UPrimitiveComponent Component1, FName BoneName1, UPrimitiveComponent Component2, FName BoneName2)
```
Directly specify component to connect. Will update frames based on current position.

### SetConstraintReferenceFrame
```angelscript
void SetConstraintReferenceFrame(EConstraintFrame Frame, FTransform RefFrame)
```
Pass in reference frame in. If the constraint is currently active, this will set its active local pose. Otherwise the change will take affect in InitConstraint.

### SetConstraintReferenceOrientation
```angelscript
void SetConstraintReferenceOrientation(EConstraintFrame Frame, FVector PriAxis, FVector SecAxis)
```
Pass in reference orientation in (maintains reference position). If the constraint is currently active, this will set its active local pose. Otherwise the change will take affect in InitConstraint.

### SetConstraintReferencePosition
```angelscript
void SetConstraintReferencePosition(EConstraintFrame Frame, FVector RefPosition)
```
Pass in reference position in (maintains reference orientation). If the constraint is currently active, this will set its active local pose. Otherwise the change will take affect in InitConstraint.

### SetContactTransferScale
```angelscript
void SetContactTransferScale(float32 ContactTransferScale)
```
Sets the contact transfer scale properties
     @param ContactTransferScale                Set the contact transfer scale for the parent of the joint

### SetDisableCollision
```angelscript
void SetDisableCollision(bool bDisableCollision)
```
If true, the collision between the two rigid bodies of the constraint will be disabled.

### SetLinearBreakable
```angelscript
void SetLinearBreakable(bool bLinearBreakable, float32 LinearBreakThreshold)
```
Sets the Linear Breakable properties
     @param bLinearBreakable         Whether it is possible to break the joint with linear force
     @param LinearBreakThreshold     Force needed to break the joint

### SetLinearDriveParams
```angelscript
void SetLinearDriveParams(float32 PositionStrength, float32 VelocityStrength, float32 InForceLimit)
```
Sets the drive params for the linear drive.
    @param PositionStrength         Positional strength for the drive (stiffness)
    @param VelocityStrength         Velocity strength of the drive (damping)
    @param InForceLimit     Max force applied by the drive

### SetLinearPlasticity
```angelscript
void SetLinearPlasticity(bool bLinearPlasticity, float32 LinearPlasticityThreshold, EConstraintPlasticityType PlasticityType)
```
Sets the Linear Plasticity properties
     @param bLinearPlasticity                    Whether it is possible to reset the target angle from the Linear displacement
     @param LinearPlasticityThreshold        Percent deformation needed to reset the rest length of the joint

### SetLinearPositionDrive
```angelscript
void SetLinearPositionDrive(bool bEnableDriveX, bool bEnableDriveY, bool bEnableDriveZ)
```
Enables/Disables linear position drive

    @param bEnableDriveX    Indicates whether the drive for the X-Axis should be enabled
    @param bEnableDriveY    Indicates whether the drive for the Y-Axis should be enabled
    @param bEnableDriveZ    Indicates whether the drive for the Z-Axis should be enabled

### SetLinearPositionTarget
```angelscript
void SetLinearPositionTarget(FVector InPosTarget)
```
Sets the target position for the linear drive.
    @param InPosTarget              Target position

### SetLinearVelocityDrive
```angelscript
void SetLinearVelocityDrive(bool bEnableDriveX, bool bEnableDriveY, bool bEnableDriveZ)
```
Enables/Disables linear position drive

    @param bEnableDriveX    Indicates whether the drive for the X-Axis should be enabled
    @param bEnableDriveY    Indicates whether the drive for the Y-Axis should be enabled
    @param bEnableDriveZ    Indicates whether the drive for the Z-Axis should be enabled

### SetLinearVelocityTarget
```angelscript
void SetLinearVelocityTarget(FVector InVelTarget)
```
Sets the target velocity for the linear drive.
    @param InVelTarget              Target velocity

### SetLinearXLimit
```angelscript
void SetLinearXLimit(ELinearConstraintMotion ConstraintType, float32 LimitSize)
```
Sets the LinearX Motion Type
     @param ConstraintType   New Constraint Type
     @param LimitSize                Size of limit

### SetLinearYLimit
```angelscript
void SetLinearYLimit(ELinearConstraintMotion ConstraintType, float32 LimitSize)
```
Sets the LinearY Motion Type
     @param ConstraintType   New Constraint Type
     @param LimitSize                Size of limit

### SetLinearZLimit
```angelscript
void SetLinearZLimit(ELinearConstraintMotion ConstraintType, float32 LimitSize)
```
Sets the LinearZ Motion Type
     @param ConstraintType   New Constraint Type
     @param LimitSize                Size of limit

### SetOrientationDriveSLERP
```angelscript
void SetOrientationDriveSLERP(bool bEnableSLERP)
```
Enables/Disables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP

     @param bEnableSLERP             Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

### SetOrientationDriveTwistAndSwing
```angelscript
void SetOrientationDriveTwistAndSwing(bool bEnableTwistDrive, bool bEnableSwingDrive)
```
Enables/Disables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

     @param bEnableSwingDrive        Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param bEnableTwistDrive        Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

### SetProjectionEnabled
```angelscript
void SetProjectionEnabled(bool bProjectionEnabled)
```
If true, joint projection is enabled. Projection is a semi-physics post-solve correction for fixing small errors, and a teleport for fixing larger errors. See SetProjectionParams

### SetProjectionParams
```angelscript
void SetProjectionParams(float32 ProjectionLinearAlpha, float32 ProjectionAngularAlpha, float32 ProjectionLinearTolerance, float32 ProjectionAngularTolerance)
```
Set the projection settings for use when projection is enabled. See SetProjectionEnabled.
For ragdolls you usually require that ProjectionLinearAlpha and ProjectionAngularAlpha be zero. They are most useful for cosmetic chains etc. ProjectionLinearTolerance and ProjectionAngularTolerance
are emergency error recovery settings and should only rarely affect the simulation. If the simulation is significantly affected by the Tolerance settings, it likely indicates a setup stability issue.

@param ProjectionLinearAlpha Controls the semi-physical correction of linear error remaining after the joint solve. Will add energy into the system. Best for joint chains connected to a kinematic.
@param ProjectionAngularAlpha Controls the semi-physical correction of angular error remaining after the joint solve. Will add energy into the system. Best for joint chains connected to a kinematic.
@param ProjectionLinearTolerance Linear errors above this will be corrected with a non-physical teleport.
@param ProjectionAngularTolerance Angular errors above this will be corrected with a non-physical teleport.

