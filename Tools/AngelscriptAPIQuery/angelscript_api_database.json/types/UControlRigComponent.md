# UControlRigComponent

**继承自**: `UPrimitiveComponent`

A component that hosts an animation ControlRig, manages control components and marshals data between the two

## 属性

### OnPreInitializeDelegate
- **类型**: `FControlRigComponentDelegate`

### OnPostInitializeDelegate
- **类型**: `FControlRigComponentDelegate`

### OnPreConstructionDelegate
- **类型**: `FControlRigComponentDelegate`

### OnPostConstructionDelegate
- **类型**: `FControlRigComponentDelegate`

### OnPreForwardsSolveDelegate
- **类型**: `FControlRigComponentDelegate`

### OnPostForwardsSolveDelegate
- **类型**: `FControlRigComponentDelegate`

### UserDefinedElements
- **类型**: `TArray<FControlRigComponentMappedElement>`

### bEnableLazyEvaluation
- **类型**: `bool`
- **描述**: When checked the rig will only run if any of the mapped inputs has changed

### LazyEvaluationPositionThreshold
- **类型**: `float32`
- **描述**: The delta threshold for a translation / position difference. 0.0 disables position differences.

### LazyEvaluationRotationThreshold
- **类型**: `float32`
- **描述**: The delta threshold for a rotation difference (in degrees). 0.0 disables rotation differences.

### LazyEvaluationScaleThreshold
- **类型**: `float32`
- **描述**: The delta threshold for a scale difference. 0.0 disables scale differences.

### bResetTransformBeforeTick
- **类型**: `bool`
- **描述**: When checked the transforms are reset before a tick / update of the rig

### bResetInitialsBeforeConstruction
- **类型**: `bool`
- **描述**: When checked the initial transforms on bones, nulls and controls are reset prior to a construction event

### bUpdateRigOnTick
- **类型**: `bool`
- **描述**: When checked this ensures to run the rig's update on the component's tick automatically

### bUpdateInEditor
- **类型**: `bool`
- **描述**: When checked the rig is run in the editor viewport without running / simulation the game

### bDrawBones
- **类型**: `bool`
- **描述**: When checked the rig's bones are drawn using debug drawing similar to the animation editor viewport

### bShowDebugDrawing
- **类型**: `bool`
- **描述**: When checked the rig's debug drawing instructions are drawn in the viewport

### ControlRigClass
- **类型**: `TSubclassOf<UControlRig>`

## 方法

### AddMappedCompleteSkeletalMesh
```angelscript
void AddMappedCompleteSkeletalMesh(USkeletalMeshComponent SkeletalMeshComponent, EControlRigComponentMapDirection InDirection)
```
Adds all matching bones to the rig, should not be used before OnPreInitialize Event

### AddMappedComponents
```angelscript
void AddMappedComponents(TArray<FControlRigComponentMappedComponent> Components)
```
Adds a series of mapped bones to the rig, should not be used before OnPreInitialize Event

### AddMappedElements
```angelscript
void AddMappedElements(TArray<FControlRigComponentMappedElement> NewMappedElements)
```
Adds the provided mapped elements to the component, should not be used before OnPreInitialize Event

### AddMappedSkeletalMesh
```angelscript
void AddMappedSkeletalMesh(USkeletalMeshComponent SkeletalMeshComponent, TArray<FControlRigComponentMappedBone> Bones, TArray<FControlRigComponentMappedCurve> Curves, EControlRigComponentMapDirection InDirection)
```
Adds a series of mapped bones to the rig, should not be used before OnPreInitialize Event

### CanExecute
```angelscript
bool CanExecute()
```
Returns true if the Component can execute its Control Rig

### ClearMappedElements
```angelscript
void ClearMappedElements()
```
Removes all mapped elements from the component

### DoesElementExist
```angelscript
bool DoesElementExist(FName Name, ERigElementType ElementType)
```
Returns true if an element given a type and name exists in the rig
@param Name The name for the element to look up
@param ElementType The type of element to look up

@return true if the element exists

### GetAbsoluteTime
```angelscript
float32 GetAbsoluteTime()
```
Get the ControlRig's local time in seconds since its last initialize

### GetBoneTransform
```angelscript
FTransform GetBoneTransform(FName BoneName, EControlRigComponentSpace Space)
```
Returns the transform of the bone in the requested space
@param BoneName The name of the bone to retrieve the transform for
@param Space The space to retrieve the transform in

@return the transform of the bone in the requested space

### GetControlBool
```angelscript
bool GetControlBool(FName ControlName)
```
Returns the value of a bool control
@param ControlName The name of the control to retrieve the value for

@return The bool value of the control

### GetControlFloat
```angelscript
float32 GetControlFloat(FName ControlName)
```
Returns the value of a float control
@param ControlName The name of the control to retrieve the value for

@return The float value of the control

### GetControlInt
```angelscript
int GetControlInt(FName ControlName)
```
Returns the value of an integer control
@param ControlName The name of the control to retrieve the value for

@return The int32 value of the control

### GetControlOffset
```angelscript
FTransform GetControlOffset(FName ControlName, EControlRigComponentSpace Space)
```
Returns the offset transform of a control
@param ControlName The name of the control to retrieve the offset transform for
@param Space The space to retrieve the offset transform in

@return The offset transform of a control

### GetControlPosition
```angelscript
FVector GetControlPosition(FName ControlName, EControlRigComponentSpace Space)
```
Returns the value of a position control
@param ControlName The name of the control to retrieve the value for
@param Space The space to retrieve the control's value in

@return The position value of the control

### GetControlRig
```angelscript
UControlRig GetControlRig()
```
Get the ControlRig hosted by this component

### GetControlRotator
```angelscript
FRotator GetControlRotator(FName ControlName, EControlRigComponentSpace Space)
```
Returns the value of a rotator control
@param ControlName The name of the control to retrieve the value for
@param Space The space to retrieve the control's value in

@return The rotator value of the control

### GetControlScale
```angelscript
FVector GetControlScale(FName ControlName, EControlRigComponentSpace Space)
```
Returns the value of a scale control
@param ControlName The name of the control to retrieve the value for
@param Space The space to retrieve the control's value in

@return The scale value of the control

### GetControlTransform
```angelscript
FTransform GetControlTransform(FName ControlName, EControlRigComponentSpace Space)
```
Returns the value of a transform control
@param ControlName The name of the control to retrieve the value for
@param Space The space to retrieve the control's value in

@return The transform value of the control

### GetControlVector2D
```angelscript
FVector2D GetControlVector2D(FName ControlName)
```
Returns the value of a Vector3D control
@param ControlName The name of the control to retrieve the value for

@return The Vector3D value of the control

### GetElementNames
```angelscript
TArray<FName> GetElementNames(ERigElementType ElementType)
```
Returns all of the names for a given element type (Bone, Control, etc)
@param ElementType The type of elements to return the names for

@return all of the names for a given element type (Bone, Control, etc)

### GetInitialBoneTransform
```angelscript
FTransform GetInitialBoneTransform(FName BoneName, EControlRigComponentSpace Space)
```
Returns the initial transform of the bone in the requested space
@param BoneName The name of the bone to retrieve the transform for
@param Space The space to retrieve the transform in

@return the initial transform of the bone in the requested space

### GetInitialSpaceTransform
```angelscript
FTransform GetInitialSpaceTransform(FName SpaceName, EControlRigComponentSpace Space)
```
Returns the initial transform of the space in the requested space
@param SpaceName The name of the space to retrieve the transform for
@param Space The space to retrieve the transform in

@return the initial transform of the space in the requested space

### GetSpaceTransform
```angelscript
FTransform GetSpaceTransform(FName SpaceName, EControlRigComponentSpace Space)
```
Returns the transform of the space in the requested space
@param SpaceName The name of the space to retrieve the transform for
@param Space The space to retrieve the transform in

@return the transform of the space in the requested space

### Initialize
```angelscript
void Initialize()
```
Initializes the rig's memory and calls the construction event

### OnPostConstruction
```angelscript
void OnPostConstruction(UControlRigComponent Component)
```

### OnPostForwardsSolve
```angelscript
void OnPostForwardsSolve(UControlRigComponent Component)
```

### OnPostInitialize
```angelscript
void OnPostInitialize(UControlRigComponent Component)
```

### OnPreConstruction
```angelscript
void OnPreConstruction(UControlRigComponent Component)
```

### OnPreForwardsSolve
```angelscript
void OnPreForwardsSolve(UControlRigComponent Component)
```

### OnPreInitialize
```angelscript
void OnPreInitialize(UControlRigComponent Component)
```

### SetBoneInitialTransformsFromSkeletalMesh
```angelscript
void SetBoneInitialTransformsFromSkeletalMesh(USkeletalMesh InSkeletalMesh)
```
Setup the initial transforms / ref pose of the bones based on a skeletal mesh

### SetBoneTransform
```angelscript
void SetBoneTransform(FName BoneName, FTransform Transform, EControlRigComponentSpace Space, float32 Weight, bool bPropagateToChildren)
```
Sets the transform of the bone in the requested space
@param BoneName The name of the bone to set the transform for
@param Space The space to set the transform in
@param Weight The weight of how much the change should be applied (0.0 to 1.0)
@param bPropagateToChildren If true the child bones will be moved together with the affected bone

### SetControlBool
```angelscript
void SetControlBool(FName ControlName, bool Value)
```
Sets the value of a bool control
@param ControlName The name of the control to set
@param Value The new value for the control

### SetControlFloat
```angelscript
void SetControlFloat(FName ControlName, float32 Value)
```
Sets the value of a float control
@param ControlName The name of the control to set
@param Value The new value for the control

### SetControlInt
```angelscript
void SetControlInt(FName ControlName, int Value)
```
Sets the value of an integer control
@param ControlName The name of the control to set
@param Value The new value for the control

### SetControlOffset
```angelscript
void SetControlOffset(FName ControlName, FTransform OffsetTransform, EControlRigComponentSpace Space)
```
Sets the offset transform of a control
@param ControlName The name of the control to set
@param OffsetTransform The new offset trasnform for the control
@param Space The space to set the offset transform in

### SetControlPosition
```angelscript
void SetControlPosition(FName ControlName, FVector Value, EControlRigComponentSpace Space)
```
Sets the value of a position control
@param ControlName The name of the control to set
@param Value The new value for the control
@param Space The space to set the value in

### SetControlRigClass
```angelscript
void SetControlRigClass(TSubclassOf<UControlRig> InControlRigClass)
```

### SetControlRotator
```angelscript
void SetControlRotator(FName ControlName, FRotator Value, EControlRigComponentSpace Space)
```
Sets the value of a rotator control
@param ControlName The name of the control to set
@param Value The new value for the control
@param Space The space to set the value in

### SetControlScale
```angelscript
void SetControlScale(FName ControlName, FVector Value, EControlRigComponentSpace Space)
```
Sets the value of a scale control
@param ControlName The name of the control to set
@param Value The new value for the control
@param Space The space to set the value in

### SetControlTransform
```angelscript
void SetControlTransform(FName ControlName, FTransform Value, EControlRigComponentSpace Space)
```
Sets the value of a transform control
@param ControlName The name of the control to set
@param Value The new value for the control
@param Space The space to set the value in

### SetControlVector2D
```angelscript
void SetControlVector2D(FName ControlName, FVector2D Value)
```
Sets the value of a vector2D control
@param ControlName The name of the control to set
@param Value The new value for the control

### SetInitialBoneTransform
```angelscript
void SetInitialBoneTransform(FName BoneName, FTransform InitialTransform, EControlRigComponentSpace Space, bool bPropagateToChildren)
```
Sets the initial transform of the bone in the requested space
@param BoneName The name of the bone to set the transform for
@param InitialTransform The initial transform to set for the bone
@param Space The space to set the transform in
@param bPropagateToChildren If true the child bones will be moved together with the affected bone

### SetInitialSpaceTransform
```angelscript
void SetInitialSpaceTransform(FName SpaceName, FTransform InitialTransform, EControlRigComponentSpace Space)
```
Sets the transform of the space in the requested space
@param SpaceName The name of the space to set the transform for
@param Space The space to set the transform in

### SetMappedElements
```angelscript
void SetMappedElements(TArray<FControlRigComponentMappedElement> NewMappedElements)
```
Replaces the mapped elements on the component with the provided array, should not be used before OnPreInitialize Event

### SetObjectBinding
```angelscript
void SetObjectBinding(UObject InObjectToBind)
```

### Update
```angelscript
void Update(float32 DeltaTime)
```
Updates and ticks the rig.

