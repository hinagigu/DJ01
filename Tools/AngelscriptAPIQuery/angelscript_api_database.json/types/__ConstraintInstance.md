# __ConstraintInstance

## 方法

### CopyParams
```angelscript
void CopyParams(FConstraintInstanceAccessor& Accessor, FConstraintInstanceAccessor& SourceAccessor, bool bKeepPosition, bool bKeepRotation)
```
Copies all properties from one constraint to another
@param Accessor       Constraint accessor to write to
@param SourceAccessor Constraint accessor to read from
@param bKeepPosition  Whether to keep original constraint positions
@param bKeepRotation  Whether to keep original constraint rotations

### GetAngularBreakable
```angelscript
void GetAngularBreakable(FConstraintInstanceAccessor& Accessor, bool& bAngularBreakable, float32& AngularBreakThreshold)
```
Gets Constraint Angular Breakable properties
     @param Accessor                                 Constraint accessor to query
     @param bAngularBreakable                Whether it is possible to break the joint with angular force
     @param AngularBreakThreshold    Torque needed to break the joint

### GetAngularDriveMode
```angelscript
void GetAngularDriveMode(FConstraintInstanceAccessor& Accessor, EAngularDriveMode& OutDriveMode)
```
Gets the angular drive mode ( SLERP or Twist And Swing)
     @param Accessor         Constraint accessor to query
     @param OutDriveMode     The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock

### GetAngularDriveParams
```angelscript
void GetAngularDriveParams(FConstraintInstanceAccessor& Accessor, float32& OutPositionStrength, float32& OutVelocityStrength, float32& OutForceLimit)
```
Gets the drive params for the angular drive.
     @param Accessor                         Constraint accessor to query
     @param OutPositionStrength      Positional strength for the drive (stiffness)
     @param OutVelocityStrength      Velocity strength of the drive (damping)
     @param OutForceLimit            Max force applied by the drive

### GetAngularLimits
```angelscript
void GetAngularLimits(FConstraintInstanceAccessor& Accessor, EAngularConstraintMotion& Swing1MotionType, float32& Swing1LimitAngle, EAngularConstraintMotion& Swing2MotionType, float32& Swing2LimitAngle, EAngularConstraintMotion& TwistMotionType, float32& TwistLimitAngle)
```
Gets Constraint Angular Motion Ranges
     @param Accessor                         Constraint accessor to query
     @param Swing1MotionType         Type of swing motion ( first axis )
     @param Swing1LimitAngle         Size of limit in degrees in [0, 180] range
 @param Swing2MotionType             Type of swing motion ( second axis )
     @param Swing2LimitAngle         Size of limit in degrees in [0, 180] range
 @param TwistMotionType              Type of twist motion
     @param TwistLimitAngle          Size of limit in degrees in [0, 180] range

### GetAngularOrientationTarget
```angelscript
void GetAngularOrientationTarget(FConstraintInstanceAccessor& Accessor, FRotator& OutPosTarget)
```
Gets the target orientation for the angular drive.
     @param Accessor                         Constraint accessor to query
     @param OutPosTarget                     Target orientation

### GetAngularPlasticity
```angelscript
void GetAngularPlasticity(FConstraintInstanceAccessor& Accessor, bool& bAngularPlasticity, float32& AngularPlasticityThreshold)
```
Sets Constraint Angular Plasticity properties
     @param Accessor                                         Constraint accessor to query
     @param bAngularPlasticity                       Whether it is possible to reset the target angle from the angular displacement
     @param AngularPlasticityThreshold       Degrees needed to reset the rest state of the joint

### GetAngularSoftSwingLimitParams
```angelscript
void GetAngularSoftSwingLimitParams(FConstraintInstanceAccessor& Accessor, bool& bSoftSwingLimit, float32& SwingLimitStiffness, float32& SwingLimitDamping, float32& SwingLimitRestitution, float32& SwingLimitContactDistance)
```
Gets Constraint Angular Soft Swing Limit parameters
     @param Accessor                                         Constraint accessor to query
*     @param bSoftSwingLimit                          True is the swing limit is soft
     @param SwingLimitStiffness                      Stiffness of the soft swing limit. Only used when Soft limit is on ( positive value )
     @param SwingLimitDamping                        Damping of the soft swing limit. Only used when Soft limit is on ( positive value )
 @param SwingLimitRestitution                Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
     @param SwingLimitContactDistance        Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

### GetAngularSoftTwistLimitParams
```angelscript
void GetAngularSoftTwistLimitParams(FConstraintInstanceAccessor& Accessor, bool& bSoftTwistLimit, float32& TwistLimitStiffness, float32& TwistLimitDamping, float32& TwistLimitRestitution, float32& TwistLimitContactDistance)
```
Gets Constraint Angular Soft Twist Limit parameters
     @param Accessor                                         Constraint accessor to query
*     @param bSoftTwistLimit                          True is the Twist limit is soft
     @param TwistLimitStiffness                      Stiffness of the soft Twist limit. Only used when Soft limit is on ( positive value )
     @param TwistLimitDamping                        Damping of the soft Twist limit. Only used when Soft limit is on ( positive value )
 @param TwistLimitRestitution                Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
     @param TwistLimitContactDistance        Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

### GetAngularVelocityDriveSLERP
```angelscript
void GetAngularVelocityDriveSLERP(FConstraintInstanceAccessor& Accessor, bool& bOutEnableSLERP)
```
Gets whether the angular velocity slerp drive is enabled or not. Only relevant if the AngularDriveMode is set to SLERP
     @param Accessor                         Constraint accessor to query
     @param bOutEnableSLERP          Indicates whether the SLERP drive is enabled. Only relevant if the AngularDriveMode is set to SLERP

### GetAngularVelocityDriveTwistAndSwing
```angelscript
void GetAngularVelocityDriveTwistAndSwing(FConstraintInstanceAccessor& Accessor, bool& bOutEnableTwistDrive, bool& bOutEnableSwingDrive)
```
Gets whether angular velocity twist and swing drive is enabled or not. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param Accessor                         Constraint accessor to query
     @param bOutEnableTwistDrive     Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
 @param bOutEnableSwingDrive Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

### GetAngularVelocityTarget
```angelscript
void GetAngularVelocityTarget(FConstraintInstanceAccessor& Accessor, FVector& OutVelTarget)
```
Gets the target velocity for the angular drive.
     @param Accessor                         Constraint accessor to query
     @param OutVelTarget                     Target velocity

### GetAttachedBodyNames
```angelscript
void GetAttachedBodyNames(FConstraintInstanceAccessor& Accessor, FName& ParentBody, FName& ChildBody)
```
Gets Attached body names
     @param Accessor         Constraint accessor to query
     @param ParentBody       Parent body name of the constraint
     @param ChildBody        Child body name of the constraint

### GetContactTransferScale
```angelscript
void GetContactTransferScale(FConstraintInstanceAccessor& Accessor, float32& ContactTransferScale)
```
Gets Constraint Contact Transfer Scale properties
     @param Accessor                                         Constraint accessor to query
     @param ContactTransferScale                     Scale for transfer of child energy to parent.

### GetDisableCollsion
```angelscript
bool GetDisableCollsion(FConstraintInstanceAccessor& Accessor)
```
Gets whether bodies attched to the constraint can collide or not
     @param Accessor         Constraint accessor to query

### GetLinearBreakable
```angelscript
void GetLinearBreakable(FConstraintInstanceAccessor& Accessor, bool& bLinearBreakable, float32& LinearBreakThreshold)
```
Gets Constraint Linear Breakable properties
     @param Accessor                         Constraint accessor to query
     @param bLinearBreakable         Whether it is possible to break the joint with linear force
     @param LinearBreakThreshold     Force needed to break the joint

### GetLinearDriveParams
```angelscript
void GetLinearDriveParams(FConstraintInstanceAccessor& Accessor, float32& OutPositionStrength, float32& OutVelocityStrength, float32& OutForceLimit)
```
Gets the drive params for the linear drive.
     @param Accessor                         Constraint accessor to query
     @param OutPositionStrength      Positional strength for the drive (stiffness)
     @param OutVelocityStrength      Velocity strength of the drive (damping)
     @param OutForceLimit            Max force applied by the drive

### GetLinearLimits
```angelscript
void GetLinearLimits(FConstraintInstanceAccessor& Accessor, ELinearConstraintMotion& XMotion, ELinearConstraintMotion& YMotion, ELinearConstraintMotion& ZMotion, float32& Limit)
```
Gets Constraint Linear Motion Ranges
     @param Accessor Constraint accessor to query
     @param XMotion  Type of motion along the X axis
     @param YMotion  Type of motion along the Y axis
     @param ZMotion  Type of motion along the Z axis
     @param Limit    linear limit applied to all axis

### GetLinearPlasticity
```angelscript
void GetLinearPlasticity(FConstraintInstanceAccessor& Accessor, bool& bLinearPlasticity, float32& LinearPlasticityThreshold, EConstraintPlasticityType& PlasticityType)
```
Gets Constraint Linear Plasticity properties
     @param Accessor                                         Constraint accessor to query
     @param bAngularPlasticity                       Whether it is possible to reset the target position from the linear displacement
     @param AngularPlasticityThreshold       Delta from target needed to reset the target joint

### GetLinearPositionDrive
```angelscript
void GetLinearPositionDrive(FConstraintInstanceAccessor& Accessor, bool& bOutEnableDriveX, bool& bOutEnableDriveY, bool& bOutEnableDriveZ)
```
Gets whether linear position drive is enabled or not
     @param Accessor                         Constraint accessor to query
     @param bOutEnableDriveX         Indicates whether the drive for the X-Axis is enabled
     @param bOutEnableDriveY         Indicates whether the drive for the Y-Axis is enabled
     @param bOutEnableDriveZ         Indicates whether the drive for the Z-Axis is enabled

### GetLinearPositionTarget
```angelscript
void GetLinearPositionTarget(FConstraintInstanceAccessor& Accessor, FVector& OutPosTarget)
```
Gets the target position for the linear drive.
     @param Accessor                         Constraint accessor to query
     @param OutPosTarget                     Target position

### GetLinearSoftLimitParams
```angelscript
void GetLinearSoftLimitParams(FConstraintInstanceAccessor& Accessor, bool& bSoftLinearLimit, float32& LinearLimitStiffness, float32& LinearLimitDamping, float32& LinearLimitRestitution, float32& LinearLimitContactDistance)
```
Gets Constraint Linear Soft Limit parameters
     @param Accessor                                         Constraint accessor to query
*     @param bSoftLinearLimit                         True is the Linear limit is soft
     @param LinearLimitStiffness                     Stiffness of the soft Linear limit. Only used when Soft limit is on ( positive value )
     @param LinearLimitDamping                       Damping of the soft Linear limit. Only used when Soft limit is on ( positive value )
 @param LinearLimitRestitution               Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
     @param LinearLimitContactDistance       Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

### GetLinearVelocityDrive
```angelscript
void GetLinearVelocityDrive(FConstraintInstanceAccessor& Accessor, bool& bOutEnableDriveX, bool& bOutEnableDriveY, bool& bOutEnableDriveZ)
```
Gets whether linear velocity drive is enabled or not
     @param Accessor                         Constraint accessor to query
     @param bOutEnableDriveX         Indicates whether the drive for the X-Axis is enabled
     @param bOutEnableDriveY         Indicates whether the drive for the Y-Axis is enabled
     @param bOutEnableDriveZ         Indicates whether the drive for the Z-Axis is enabled

### GetLinearVelocityTarget
```angelscript
void GetLinearVelocityTarget(FConstraintInstanceAccessor& Accessor, FVector& OutVelTarget)
```
Gets the target velocity for the linear drive.
     @param Accessor                         Constraint accessor to query
     @param OutVelTarget                     Target velocity

### GetMassConditioningEnabled
```angelscript
bool GetMassConditioningEnabled(FConstraintInstanceAccessor& Accessor)
```
@brief Gets whether mass conditioning is enabled for the constraint.

### GetOrientationDriveSLERP
```angelscript
void GetOrientationDriveSLERP(FConstraintInstanceAccessor& Accessor, bool& bOutEnableSLERP)
```
Gets whether the angular orientation slerp drive is enabled or not. Only relevant if the AngularDriveMode is set to SLERP
     @param Accessor                         Constraint accessor to query
     @param bOutEnableSLERP          Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

### GetOrientationDriveTwistAndSwing
```angelscript
void GetOrientationDriveTwistAndSwing(FConstraintInstanceAccessor& Accessor, bool& bOutEnableTwistDrive, bool& bOutEnableSwingDrive)
```
Gets whether angular orientation drive are enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param Accessor                         Constraint accessor to query
     @param bOutEnableTwistDrive     Indicates whether the drive for the twist axis is enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param bOutEnableSwingDrive     Indicates whether the drive for the swing axis is enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

### GetParentDominates
```angelscript
bool GetParentDominates(FConstraintInstanceAccessor& Accessor)
```
Gets whether the parent body is not affected by it's child motion
     @param Accessor Constraint accessor to query

### GetProjectionParams
```angelscript
void GetProjectionParams(FConstraintInstanceAccessor& Accessor, bool& bEnableProjection, float32& ProjectionLinearAlpha, float32& ProjectionAngularAlpha)
```
Gets projection parameters of the constraint
     @param Accessor                                 Constraint accessor to query
     @param bEnableProjection                true to enable projection
     @param ProjectionLinearAlpha    how much linear projection to apply in [0,1] range
     @param ProjectionAngularAlpha   how much angular projection to apply in [0,1] range

### SetAngularBreakable
```angelscript
void SetAngularBreakable(FConstraintInstanceAccessor& Accessor, bool bAngularBreakable, float32 AngularBreakThreshold)
```
Sets Constraint Angular Breakable properties
     @param Accessor                                 Constraint accessor to change
     @param bAngularBreakable                Whether it is possible to break the joint with angular force
     @param AngularBreakThreshold    Torque needed to break the joint

### SetAngularDriveMode
```angelscript
void SetAngularDriveMode(FConstraintInstanceAccessor& Accessor, EAngularDriveMode DriveMode)
```
Switches the angular drive mode between SLERP and Twist And Swing
     @param Accessor         Constraint accessor to change
     @param DriveMode        The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock

### SetAngularDriveParams
```angelscript
void SetAngularDriveParams(FConstraintInstanceAccessor& Accessor, float32 PositionStrength, float32 VelocityStrength, float32 InForceLimit)
```
Sets the drive params for the angular drive.
     @param Accessor                         Constraint accessor to change
     @param PositionStrength         Positional strength for the drive (stiffness)
     @param VelocityStrength         Velocity strength of the drive (damping)
     @param InForceLimit                     Max force applied by the drive

### SetAngularLimits
```angelscript
void SetAngularLimits(FConstraintInstanceAccessor& Accessor, EAngularConstraintMotion Swing1MotionType, float32 Swing1LimitAngle, EAngularConstraintMotion Swing2MotionType, float32 Swing2LimitAngle, EAngularConstraintMotion TwistMotionType, float32 TwistLimitAngle)
```
Sets COnstraint Angular Motion Ranges
     @param Accessor                         Constraint accessor to change
     @param Swing1MotionType         Type of swing motion ( first axis )
     @param Swing1LimitAngle         Size of limit in degrees in [0, 180] range
 @param Swing2MotionType             Type of swing motion ( second axis )
     @param Swing2LimitAngle         Size of limit in degrees in [0, 180] range
 @param TwistMotionType              Type of twist motion
     @param TwistLimitAngle          Size of limit in degrees in [0, 180] range

### SetAngularOrientationTarget
```angelscript
void SetAngularOrientationTarget(FConstraintInstanceAccessor& Accessor, FRotator InPosTarget)
```
Sets the target orientation for the angular drive.
     @param Accessor                         Constraint accessor to change
     @param InPosTarget                      Target orientation

### SetAngularPlasticity
```angelscript
void SetAngularPlasticity(FConstraintInstanceAccessor& Accessor, bool bAngularPlasticity, float32 AngularPlasticityThreshold)
```
Sets Constraint Angular Plasticity properties
     @param Accessor                                         Constraint accessor to change
     @param bAngularPlasticity                       Whether it is possible to reset the target angle from the angular displacement
     @param AngularPlasticityThreshold       Degrees needed to reset the rest state of the joint

### SetAngularSoftSwingLimitParams
```angelscript
void SetAngularSoftSwingLimitParams(FConstraintInstanceAccessor& Accessor, bool bSoftSwingLimit, float32 SwingLimitStiffness, float32 SwingLimitDamping, float32 SwingLimitRestitution, float32 SwingLimitContactDistance)
```
Sets Constraint Angular Soft Swing Limit parameters
     @param Accessor                                         Constraint accessor to change
*     @param bSoftSwingLimit                          True is the swing limit is soft
     @param SwingLimitStiffness                      Stiffness of the soft swing limit. Only used when Soft limit is on ( positive value )
     @param SwingLimitDamping                        Damping of the soft swing limit. Only used when Soft limit is on ( positive value )
 @param SwingLimitRestitution                Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
     @param SwingLimitContactDistance        Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

### SetAngularSoftTwistLimitParams
```angelscript
void SetAngularSoftTwistLimitParams(FConstraintInstanceAccessor& Accessor, bool bSoftTwistLimit, float32 TwistLimitStiffness, float32 TwistLimitDamping, float32 TwistLimitRestitution, float32 TwistLimitContactDistance)
```
Sets Constraint Angular Soft Twist Limit parameters
     @param Accessor                                         Constraint accessor to change
*     @param bSoftTwistLimit                          True is the twist limit is soft
     @param TwistLimitStiffness                      Stiffness of the soft Twist limit. Only used when Soft limit is on ( positive value )
     @param TwistLimitDamping                        Damping of the soft Twist limit. Only used when Soft limit is on ( positive value )
 @param TwistLimitRestitution                Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
     @param TwistLimitContactDistance        Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

### SetAngularVelocityDriveSLERP
```angelscript
void SetAngularVelocityDriveSLERP(FConstraintInstanceAccessor& Accessor, bool bEnableSLERP)
```
Enables/Disables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP
     @param Accessor                         Constraint accessor to change
     @param bEnableSLERP                     Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

### SetAngularVelocityDriveTwistAndSwing
```angelscript
void SetAngularVelocityDriveTwistAndSwing(FConstraintInstanceAccessor& Accessor, bool bEnableTwistDrive, bool bEnableSwingDrive)
```
Enables/Disables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param Accessor                         Constraint accessor to change
     @param bEnableTwistDrive        Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param bEnableSwingDrive        Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

### SetAngularVelocityTarget
```angelscript
void SetAngularVelocityTarget(FConstraintInstanceAccessor& Accessor, FVector InVelTarget)
```
Sets the target velocity for the angular drive.
     @param Accessor                         Constraint accessor to change
     @param InVelTarget                      Target velocity

### SetContactTransferScale
```angelscript
void SetContactTransferScale(FConstraintInstanceAccessor& Accessor, float32 ContactTransferScale)
```
Set Contact Transfer Scale
     @param Accessor                                         Constraint accessor to change
     @param ContactTransferScale                     Set Contact Transfer Scale onto joints parent

### SetDisableCollision
```angelscript
void SetDisableCollision(FConstraintInstanceAccessor& Accessor, bool bDisableCollision)
```
Sets whether bodies attched to the constraint can collide or not
     @param Accessor                         Constraint accessor to change
     @param bDisableCollision        true to disable collision between constrained bodies

### SetLinearBreakable
```angelscript
void SetLinearBreakable(FConstraintInstanceAccessor& Accessor, bool bLinearBreakable, float32 LinearBreakThreshold)
```
Sets the Linear Breakable properties
     @param Accessor                         Constraint accessor to change
     @param bLinearBreakable         Whether it is possible to break the joint with linear force
     @param LinearBreakThreshold     Force needed to break the joint

### SetLinearDriveParams
```angelscript
void SetLinearDriveParams(FConstraintInstanceAccessor& Accessor, float32 PositionStrength, float32 VelocityStrength, float32 InForceLimit)
```
Sets the drive params for the linear drive.
     @param Accessor                         Constraint accessor to change
     @param PositionStrength         Positional strength for the drive (stiffness)
     @param VelocityStrength         Velocity strength of the drive (damping)
     @param InForceLimit                     Max force applied by the drive

### SetLinearLimits
```angelscript
void SetLinearLimits(FConstraintInstanceAccessor& Accessor, ELinearConstraintMotion XMotion, ELinearConstraintMotion YMotion, ELinearConstraintMotion ZMotion, float32 Limit)
```
Sets Constraint Linear Motion Ranges
     @param Accessor Constraint accessor to change
     @param XMotion  Type of motion along the X axis
     @param YMotion  Type of motion along the Y axis
     @param ZMotion  Type of motion along the Z axis
     @param Limit    linear limit to apply to all axis

### SetLinearPlasticity
```angelscript
void SetLinearPlasticity(FConstraintInstanceAccessor& Accessor, bool bLinearPlasticity, float32 LinearPlasticityThreshold, EConstraintPlasticityType PlasticityType)
```
Sets Constraint Linear Plasticity properties
     @param Accessor                                         Constraint accessor to change
     @param bLinearPlasticity                        Whether it is possible to reset the target position from the linear displacement
     @param LinearPlasticityThreshold        Delta from target needed to reset the target joint

### SetLinearPositionDrive
```angelscript
void SetLinearPositionDrive(FConstraintInstanceAccessor& Accessor, bool bEnableDriveX, bool bEnableDriveY, bool bEnableDriveZ)
```
Enables/Disables linear position drive
     @param Accessor                         Constraint accessor to change
     @param bEnableDriveX            Indicates whether the drive for the X-Axis should be enabled
     @param bEnableDriveY            Indicates whether the drive for the Y-Axis should be enabled
     @param bEnableDriveZ            Indicates whether the drive for the Z-Axis should be enabled

### SetLinearPositionTarget
```angelscript
void SetLinearPositionTarget(FConstraintInstanceAccessor& Accessor, FVector InPosTarget)
```
Sets the target position for the linear drive.
     @param Accessor                         Constraint accessor to change
     @param InPosTarget                      Target position

### SetLinearSoftLimitParams
```angelscript
void SetLinearSoftLimitParams(FConstraintInstanceAccessor& Accessor, bool bSoftLinearLimit, float32 LinearLimitStiffness, float32 LinearLimitDamping, float32 LinearLimitRestitution, float32 LinearLimitContactDistance)
```
Sets Constraint Linear Soft Limit parameters
     @param Accessor                                         Constraint accessor to change
*     @param bSoftLinearLimit                         True is the linear limit is soft
     @param LinearLimitStiffness                     Stiffness of the soft linear limit. Only used when Soft limit is on ( positive value )
     @param LinearLimitDamping                       Damping of the soft linear limit. Only used when Soft limit is on ( positive value )
 @param LinearLimitRestitution               Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
     @param LinearLimitContactDistance       Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

### SetLinearVelocityDrive
```angelscript
void SetLinearVelocityDrive(FConstraintInstanceAccessor& Accessor, bool bEnableDriveX, bool bEnableDriveY, bool bEnableDriveZ)
```
Enables/Disables linear velocity drive
     @param Accessor                         Constraint accessor to change
     @param bEnableDriveX            Indicates whether the drive for the X-Axis should be enabled
     @param bEnableDriveY            Indicates whether the drive for the Y-Axis should be enabled
     @param bEnableDriveZ            Indicates whether the drive for the Z-Axis should be enabled

### SetLinearVelocityTarget
```angelscript
void SetLinearVelocityTarget(FConstraintInstanceAccessor& Accessor, FVector InVelTarget)
```
Sets the target velocity for the linear drive.
     @param Accessor                         Constraint accessor to change
     @param InVelTarget                      Target velocity

### SetMassConditioningEnabled
```angelscript
void SetMassConditioningEnabled(FConstraintInstanceAccessor& Accessor, bool bEnableMassConditioning)
```
@brief Enable or disable mass conditioning for the constraint.

### SetOrientationDriveSLERP
```angelscript
void SetOrientationDriveSLERP(FConstraintInstanceAccessor& Accessor, bool bEnableSLERP)
```
Enables/Disables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP
     @param Accessor                         Constraint accessor to change
     @param bEnableSLERP                     Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

### SetOrientationDriveTwistAndSwing
```angelscript
void SetOrientationDriveTwistAndSwing(FConstraintInstanceAccessor& Accessor, bool bEnableTwistDrive, bool bEnableSwingDrive)
```
Enables/Disables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param Accessor                         Constraint accessor to change
     @param bEnableSwingDrive        Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
     @param bEnableTwistDrive        Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

### SetParentDominates
```angelscript
void SetParentDominates(FConstraintInstanceAccessor& Accessor, bool bParentDominates)
```
Sets whether the parent body is not affected by it's child motion
     @param Accessor                         Constraint accessor to change
     @param bParentDominates         true to avoid the parent being affected by its child motion

### SetProjectionParams
```angelscript
void SetProjectionParams(FConstraintInstanceAccessor& Accessor, bool bEnableProjection, float32 ProjectionLinearAlpha, float32 ProjectionAngularAlpha)
```
Sets projection parameters of the constraint
     @param Accessor                                 Constraint accessor to change
     @param bEnableProjection                true to enable projection
     @param ProjectionLinearAlpha    how much linear projection to apply in [0,1] range
     @param ProjectionAngularAlpha   how much angular projection to apply in [0,1] range

