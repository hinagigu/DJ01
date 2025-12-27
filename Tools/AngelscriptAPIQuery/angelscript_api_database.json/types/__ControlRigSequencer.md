# __ControlRigSequencer

## 方法

### AddConstraint
```angelscript
UTickableConstraint AddConstraint(UWorld World, ETransformConstraintType InType, UTransformableHandle InChild, UTransformableHandle InParent, bool bMaintainOffset)
```
Add a constraint possibly adding to sequencer also if one is open.
@param World The active world
@param InType Type of constraint to create
@param InChild The handle to the transormable to be constrainted
@param InParent The handle to the parent of the constraint
@param bMaintainOffset Whether to maintain offset between child and parent when setting the constraint
@return Returns the constraint if created all nullptr if not

### BakeConstraint
```angelscript
bool BakeConstraint(UWorld World, UTickableConstraint Constraint, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Bake the constraint to keys based on the passed in frames. This will use the open sequencer to bake. See ConstraintsScriptingLibrary to get the list of available constraints
@param World The active world
@param Constraint The Constraint to bake. After baking it will be keyed to be inactive of the range of frames that are baked
@param Frames The frames to bake, if the array is empty it will use the active time ranges of the constraint to determine where it should bake
@param TimeUnit Unit for all frame and time values, either in display rate or tick resolution
@return Returns True if successful, False otherwise

### BakeConstraints
```angelscript
bool BakeConstraints(UWorld World, TArray<UTickableConstraint>& InConstraints, FBakingAnimationKeySettings InSettings)
```
Bake the constraint to keys based on the passed in settings. This will use the open sequencer to bake. See ConstraintsScriptingLibrary to get the list of available constraints
@param World The active world
@param InConstraints The Constraints tobake.  After baking they will be keyed to be inactive of the range of frames that are baked
@param InSettings Settings to use for baking
@return Returns True if successful, False otherwise

### BakeControlRigSpace
```angelscript
bool BakeControlRigSpace(ULevelSequence InSequence, UControlRig InControlRig, TArray<FName> InControlNames, FRigSpacePickerBakeSettings InSettings, EMovieSceneTimeUnit TimeUnit)
```
Bake specified Control Rig Controls to a specified Space based upon the current settings
@param InSequence Sequence to bake
@param InControlRig ControlRig to bake
@param InControlNames The name of the Controls to bake
@param InSettings  The settings for the bake, e.g, how long to bake, to key reduce etc.
@param TimeUnit Unit for the start and end times in the InSettings parameter.

### BakeToControlRig
```angelscript
bool BakeToControlRig(UWorld World, ULevelSequence LevelSequence, UClass ControlRigClass, UAnimSeqExportOption ExportOptions, bool bReduceKeys, float32 Tolerance, FMovieSceneBindingProxy Binding, bool bResetControls)
```
Bake the current animation in the binding to a Control Rig track
@param World The active world
@param LevelSequence The LevelSequence we are baking
@param ControlRigClass The class of the Control Rig
@param ExportOptions Export options for creating an animation sequence
@param bKeyReduce If true do key reduction based upon Tolerance, if false don't
@param Tolerance If reducing keys, tolerance about which keys will be removed, smaller tolerance, more keys usually.
@param Binding The binding upon which to bake
@param bResetControls If true will reset all controls to initial value on every frame
@return returns True if successful, False otherwise

### BlendValuesOnSelected
```angelscript
bool BlendValuesOnSelected(ULevelSequence LevelSequence, EAnimToolBlendOperation BlendOperation, float32 BlendValue)
```
Peform specified blend operation based upon selected keys in the curve editor or selected control rig controls
@param LevelSequence The LevelSequence that's loaded in the editor
@param EAnimToolBlendOperation The operation to perform
@param BlendValue The blend value to use, range from -1(blend to previous) to 1(blend to next)

### CollapseControlRigAnimLayers
```angelscript
bool CollapseControlRigAnimLayers(ULevelSequence InSequence, UMovieSceneControlRigParameterTrack InTrack, bool bKeyReduce, float32 Tolerance)
```
* Collapse and bake all sections and layers on a control rig track to just one section.
*
* @param InSequence Sequence that has track to collapse
* @param InTrack Track for layers to collapse
* @param bKeyReduce If true do key reduction based upon Tolerance, if false don't
* @param Tolerance If reducing keys, tolerance about which keys will be removed, smaller tolerance, more keys usually.

### CollapseControlRigAnimLayersWithSettings
```angelscript
bool CollapseControlRigAnimLayersWithSettings(ULevelSequence InSequence, UMovieSceneControlRigParameterTrack InTrack, FBakingAnimationKeySettings InSettings)
```
* Collapse and bake all sections and layers on a control rig track to just one section using passed in settings.
*
* @param InSequence Sequence that has track to collapse
* @param InTrack Track for layers to collapse
* @param InSettings Settings that determine how to collapse

### Compensate
```angelscript
bool Compensate(UTickableConstraint InConstraint, FFrameNumber InTime, EMovieSceneTimeUnit TimeUnit)
```
Compensate constraint at the specfied time
@param InConstraint The constraint to compensate
@param InTime Time to compensate
@param TimeUnit Unit for the InTime, either in display rate or tick resolution
@return Returns true if it can compensate

### CompensateAll
```angelscript
bool CompensateAll(UTickableConstraint InConstraint)
```
Compensate constraint at all keys
@param InConstraint The constraint to compensate
@return Returns true if it can compensate

### DeleteConstraintKey
```angelscript
bool DeleteConstraintKey(UTickableConstraint Constraint, UMovieSceneSection ConstraintSection, FFrameNumber InTime, EMovieSceneTimeUnit TimeUnit)
```
Delete the Key for the Constraint at the specified time.
@param InConstraint The constraint whose key to move
@param ConstraintSection Section containing Cosntraint Key
@param InTime Time to delete the constraint.
@param TimeUnit Unit for the InTime, either in display rate or tick resolution
@return Will return false if function fails,  for example if there is no key at this time it will fail.

### DeleteControlRigSpace
```angelscript
bool DeleteControlRigSpace(ULevelSequence InSequence, UControlRig InControlRig, FName InControlName, FFrameNumber InTime, EMovieSceneTimeUnit TimeUnit)
```
Delete the Control Rig Space Key for the Control at the specified time. This will delete any attached Control Rig keys at this time and will perform any needed compensation to the new space.

@param InSequence Sequence to set the space
@param InControlRig ControlRig with the Control
@param InControlName The name of the Control
@param InTime Time to delete the space.
@param TimeUnit Unit for the InTime, either in display rate or tick resolution
@return Will return false if function fails,  for example if there is no key at this time it will fail.

### ExportFBXFromControlRigSection
```angelscript
bool ExportFBXFromControlRigSection(ULevelSequence Sequence, const UMovieSceneControlRigParameterSection Section, const UMovieSceneUserExportFBXControlRigSettings ExportFBXControlRigSettings)
```
Exports an FBX from the given control rig section.

### FindOrCreateControlRigComponentTrack
```angelscript
TArray<UMovieSceneTrack> FindOrCreateControlRigComponentTrack(UWorld World, ULevelSequence LevelSequence, FMovieSceneBindingProxy InBinding)
```
Find or create a Control Rig Component
@param World The world used to spawn into temporarily if binding is a spawnable
@param LevelSequence The LevelSequence to find or create
@param InBinding The binding (actor or component binding) to find or create the Control Rig tracks
@return returns Find array of component Control Rigs that were found or created

### FindOrCreateControlRigTrack
```angelscript
UMovieSceneTrack FindOrCreateControlRigTrack(UWorld World, ULevelSequence LevelSequence, const UClass ControlRigClass, FMovieSceneBindingProxy InBinding, bool bIsLayeredControlRig)
```
Find or create a Control Rig track of a specific class based upon the binding
@param World The world used to spawn into temporarily if binding is a spawnable
@param LevelSequence The LevelSequence to find or create
@param ControlRigClass The class of the Control Rig
@param InBinding The binding (actor or component binding) to find or create the Control Rig track
@return returns Return the found or created track

### GetActorWorldTransform
```angelscript
FTransform GetActorWorldTransform(ULevelSequence LevelSequence, AActor Actor, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get Actors World Transform at a specific time
@param LevelSequence Active Sequence to get transform for
@param Actor The actor
@param Frame Time to get the transform
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns World Transform

### GetActorWorldTransforms
```angelscript
TArray<FTransform> GetActorWorldTransforms(ULevelSequence LevelSequence, AActor Actor, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get Actors World Transforms at specific times
@param LevelSequence Active Sequence to get transform for
@param Actor The actor
@param Frames Times to get the transform
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns World Transforms

### GetConstraintKeys
```angelscript
bool GetConstraintKeys(UTickableConstraint InConstraint, UMovieSceneSection ConstraintSection, TArray<bool>& OutBools, TArray<FFrameNumber>& OutFrames, EMovieSceneTimeUnit TimeUnit)
```
Get the constraint keys for the specified constraint
@param InConstraint The constraint to get
@param ConstraintSection Section containing Cosntraint Key
@param OutBools Array of whether or not it's active at the specified times
@param OutFrames The Times for the keys
@param TimeUnit Unit for the time params, either in display rate or tick resolution
@return Returns true if we got the keys from this constraint

### GetConstraintsForHandle
```angelscript
TArray<UTickableConstraint> GetConstraintsForHandle(UWorld InWorld, const UTransformableHandle InChild)
```
Get all constraints for this object, which is described by a transformable handle
@param InChild The handle to look for constraints controlling it
@return Returns array of Constraints this handle is constrained to.

### GetControlRigPriorityOrder
```angelscript
int GetControlRigPriorityOrder(UMovieSceneTrack InSection)
```
Get Control Rig prirority order

### GetControlRigs
```angelscript
TArray<FControlRigSequencerBindingProxy> GetControlRigs(ULevelSequence LevelSequence)
```
Get all of the control rigs and their bindings in the level sequence
@param LevelSequence The movie scene sequence to look for Control Rigs
@return returns list of Control Rigs in the level sequence.

### GetControlRigWorldTransform
```angelscript
FTransform GetControlRigWorldTransform(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's World Transform at a specific time
@param LevelSequence Active Sequence to get transform for
@param ControlRig The ControlRig
@param ControlName Name of the Control
@param Frame Time to get the transform
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns World Transform

### GetControlRigWorldTransforms
```angelscript
TArray<FTransform> GetControlRigWorldTransforms(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's World Transforms at specific times
@param LevelSequence Active Sequence to get transform for
@param ControlRig The ControlRig
@param ControlName Name of the Control
@param Frames Times to get the transform
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns World Transforms

### GetControlsMask
```angelscript
bool GetControlsMask(UMovieSceneSection InSection, FName ControlName)
```
Get the controls mask for the given ControlName

### GetDefaultParentKey
```angelscript
FRigElementKey GetDefaultParentKey()
```
* Get the default parent key, can be used a parent space.

### GetFKControlRigApplyMode
```angelscript
EControlRigFKRigExecuteMode GetFKControlRigApplyMode(UControlRig InControlRig)
```
Get FKControlRig Apply Mode.
@param InControlRig Rig to test
@return The EControlRigFKRigExecuteMode mode it is in, either Replace,Additive or Direct

### GetLocalControlRigBool
```angelscript
bool GetLocalControlRigBool(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's bool value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a bool control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigBools
```angelscript
TArray<bool> GetLocalControlRigBools(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's bool values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a bool control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigEulerTransform
```angelscript
FEulerTransform GetLocalControlRigEulerTransform(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's EulerTransform value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a EulerTransfom control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigEulerTransforms
```angelscript
TArray<FEulerTransform> GetLocalControlRigEulerTransforms(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's EulerTransform values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a EulerTransform control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigFloat
```angelscript
float32 GetLocalControlRigFloat(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's float value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a float control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigFloats
```angelscript
TArray<float32> GetLocalControlRigFloats(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's float values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a float control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigInt
```angelscript
int GetLocalControlRigInt(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's integer value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a integer control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigInts
```angelscript
TArray<int> GetLocalControlRigInts(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's integer values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a intteger control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigPosition
```angelscript
FVector GetLocalControlRigPosition(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Position value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Position control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigPositions
```angelscript
TArray<FVector> GetLocalControlRigPositions(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Position values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Position control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigRotator
```angelscript
FRotator GetLocalControlRigRotator(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Rotator value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Rotator control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigRotators
```angelscript
TArray<FRotator> GetLocalControlRigRotators(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Rotator values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Rotator control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigScale
```angelscript
FVector GetLocalControlRigScale(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Scale value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Scale control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigScales
```angelscript
TArray<FVector> GetLocalControlRigScales(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Scale values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Scale control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigTransform
```angelscript
FTransform GetLocalControlRigTransform(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Transform value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Transform control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigTransformNoScale
```angelscript
FTransformNoScale GetLocalControlRigTransformNoScale(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's TransformNoScale value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a TransformNoScale control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigTransformNoScales
```angelscript
TArray<FTransformNoScale> GetLocalControlRigTransformNoScales(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's TransformNoScale values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a TransformNoScale control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigTransforms
```angelscript
TArray<FTransform> GetLocalControlRigTransforms(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Transform values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Transform control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetLocalControlRigVector2D
```angelscript
FVector2D GetLocalControlRigVector2D(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Vector2D value at a specific time
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Vector2D control
@param Frame Time to get the value
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Value at that time

### GetLocalControlRigVector2Ds
```angelscript
TArray<FVector2D> GetLocalControlRigVector2Ds(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit)
```
Get ControlRig Control's Vector2D values at specific times
@param LevelSequence Active Sequence to get value for
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Vector2D control
@param Frames Times to get the values
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@return Returns Values at those times

### GetSkeletalMeshComponentWorldTransform
```angelscript
FTransform GetSkeletalMeshComponentWorldTransform(ULevelSequence LevelSequence, USkeletalMeshComponent SkeletalMeshComponent, FFrameNumber Frame, EMovieSceneTimeUnit TimeUnit, FName ReferenceName)
```
Get SkeletalMeshComponent World Transform at a specific time
@param LevelSequence Active Sequence to get transform for
@param SkeletalMeshComponent The SkeletalMeshComponent
@param Frame Time to get the transform
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param ReferenceName Optional name of the referencer
@return Returns World Transform

### GetSkeletalMeshComponentWorldTransforms
```angelscript
TArray<FTransform> GetSkeletalMeshComponentWorldTransforms(ULevelSequence LevelSequence, USkeletalMeshComponent SkeletalMeshComponent, TArray<FFrameNumber> Frames, EMovieSceneTimeUnit TimeUnit, FName ReferenceName)
```
Get SkeletalMeshComponents World Transforms at specific times
@param LevelSequence Active Sequence to get transform for
@param SkeletalMeshComponent The SkeletalMeshComponent
@param Frames Times to get the transform
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param ReferenceName Optional name of the referencer
@return Returns World Transforms

### GetVisibleControlRigs
```angelscript
TArray<UControlRig> GetVisibleControlRigs()
```
Get all of the visible control rigs in the level
@return returns list of visible Control Rigs

### GetWorldSpaceReferenceKey
```angelscript
FRigElementKey GetWorldSpaceReferenceKey()
```
* Get the default world space key, can be used a world space.

### HideAllControls
```angelscript
void HideAllControls(UMovieSceneSection InSection)
```
Hides all of the controls for the given section

### ImportFBXToControlRigTrack
```angelscript
bool ImportFBXToControlRigTrack(UWorld World, ULevelSequence InSequence, UMovieSceneControlRigParameterTrack InTrack, UMovieSceneControlRigParameterSection InSection, TArray<FString> SelectedControlRigNames, UMovieSceneUserImportFBXControlRigSettings ImportFBXControlRigSettings, FString ImportFilename)
```
* Import FBX onto a control rig with the specified track and section
*
* @param InWorld World to import to
* @param InSequence Sequence to import
* @param InTrack Track to import onto
* @param InSection Section to import onto, may be null in which case we use the track's section to key
* @param SelectedControlRigNames  List of selected control rig names. Will use them if  ImportFBXControlRigSettings->bImportOntoSelectedControls is true
* @param ImportFBXControlRigSettings Settings to control import.
* @param InImportFileName Path to fbx file to create

### IsFKControlRig
```angelscript
bool IsFKControlRig(UControlRig InControlRig)
```
Whether or not the control rig is an FK Control Rig.
@param InControlRig Rig to test to see if FK Control Rig

### IsLayeredControlRig
```angelscript
bool IsLayeredControlRig(UControlRig InControlRig)
```
Whether or not the control rig is an Layered Control Rig.
@param InControlRig Rig to test to see if Layered Control Rig

### LoadAnimSequenceIntoControlRigSection
```angelscript
bool LoadAnimSequenceIntoControlRigSection(UMovieSceneSection MovieSceneSection, UAnimSequence AnimSequence, USkeletalMeshComponent SkelMeshComp, FFrameNumber InStartFrame, EMovieSceneTimeUnit TimeUnit, bool bKeyReduce, float32 Tolerance, EMovieSceneKeyInterpolation Interpolation, bool bResetControls)
```
Load anim sequence into this control rig section
@param MovieSceneSection The MovieSceneSectionto load into
@param AnimSequence The Sequence to load
@param MovieScene The MovieScene getting loaded into
@param SkelMeshComponent The Skeletal Mesh component getting loaded into.
@param InStartFrame Frame to insert the animation
@param TimeUnit Unit for all frame and time values, either in display rate or tick resolution
@param bKeyReduce If true do key reduction based upon Tolerance, if false don't
@param Tolerance If reducing keys, tolerance about which keys will be removed, smaller tolerance, more keys usually.
@param Interpolation The key interpolation type to set the keys, defaults to EMovieSceneKeyInterpolation::SmartAuto
@param bResetControls If true will reset all controls to initial value on every frame
@return returns True if successful, False otherwise

### MoveConstraintKey
```angelscript
bool MoveConstraintKey(UTickableConstraint Constraint, UMovieSceneSection ConstraintSection, FFrameNumber InTime, FFrameNumber InNewTime, EMovieSceneTimeUnit TimeUnit)
```
Move the constraint active key in the current open Sequencer
@param InConstraint The constraint whose key to move
@param ConstraintSection Section containing Cosntraint Key
@param InTime Original time of the constraint key
@param InNewTime New time for the constraint key
@param TimeUnit Unit for the time params, either in display rate or tick resolution
@return Will return false if function fails, for example if there is no key at this time it will fail, or if the new time is invalid it could fail also

### MoveControlRigSpace
```angelscript
bool MoveControlRigSpace(ULevelSequence InSequence, UControlRig InControlRig, FName InControlName, FFrameNumber InTime, FFrameNumber InNewTime, EMovieSceneTimeUnit TimeUnit)
```
Move the Control Rig Space Key for the Control at the specified time to the new time. This will also move any Control Rig keys at this space switch boundary.

@param InSequence Sequence to set the space
@param InControlRig ControlRig with the Control
@param InControlName The name of the Control
@param InTime Original time of the space key
@param InNewTime New time for the space key
@param TimeUnit Unit for the time params, either in display rate or tick resolution
@return Will return false if function fails, for example if there is no key at this time it will fail, or if the new time is invalid it could fail also

### RenameControlRigControlChannels
```angelscript
bool RenameControlRigControlChannels(ULevelSequence InSequence, UControlRig InControlRig, TArray<FName> InOldControlNames, TArray<FName> InNewControlNames)
```
Rename the Control Rig Channels in Sequencer to the specified new control names, which should be present on the Control Rig
@param InSequence Sequence to rename controls
@param InControlRig ControlRig to rename controls
@param InOldControlNames The name of the old Control Rig Control Channels to change. Will be replaced by the corresponding name in the InNewControlNames array
@param InNewControlNames  The name of the new Control Rig Channels
@return Return true if the function succeeds, false if it doesn't which can happen if the name arrays don't match in size or any of the new Control Names aren't valid

### SetConstraintActiveKey
```angelscript
bool SetConstraintActiveKey(UTickableConstraint InConstraint, bool bActive, FFrameNumber InFrame, EMovieSceneTimeUnit TimeUnit)
```
Set the constraint active key in the current open Sequencer
@param InConstraint The constraint to set the key
@param bActive Whether or not it's active
@param FrameTime Time to set the value
@param TimeUnit Unit for the time params, either in display rate or tick resolution
@return Returns true if we set the constraint to be the passed in value, false if not. We may not do so if the value is the same.

### SetControlRigApplyMode
```angelscript
bool SetControlRigApplyMode(UControlRig InControlRig, EControlRigFKRigExecuteMode InApplyMode)
```
Set the FK Control Rig to apply mode
@param InControlRig Rig to set
@param InApplyMode Set the EControlRigFKRigExecuteMode mode (Replace,Addtiive or Direct)
@return returns True if the mode was set, may not be set if the Control Rig doesn't support these modes currently only FKControlRig's do.

### SetControlRigLayeredMode
```angelscript
bool SetControlRigLayeredMode(UMovieSceneControlRigParameterTrack InTrack, bool bSetIsLayered)
```
* Convert the control rig track into absolute or layered rig
*
* @param InTrack Control rig track to convert
* @param bSetIsLayered Convert to layered rig if true, or absolute if false

### SetControlRigPriorityOrder
```angelscript
void SetControlRigPriorityOrder(UMovieSceneTrack InSection, int PriorityOrder)
```
Set Control Rig priority order

### SetControlRigSpace
```angelscript
bool SetControlRigSpace(ULevelSequence InSequence, UControlRig InControlRig, FName InControlName, FRigElementKey InSpaceKey, FFrameNumber InTime, EMovieSceneTimeUnit TimeUnit)
```
* Set the a key for the Control Rig Space for the Control at the specified time. If space is the same as the current no key witll be set.
*
* @param InSequence Sequence to set the space
* @param InControlRig ControlRig with the Control
* @param InControlName The name of the Control
* @param InSpaceKey  The new space for the Control
* @param InTime Time to change the space.
* @param TimeUnit Unit for the InTime, either in display rate or tick resolution

### SetControlRigWorldTransform
```angelscript
void SetControlRigWorldTransform(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FTransform WorldTransform, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's World Transform at a specific time
@param LevelSequence Active Sequence to set transforms for. Must be loaded in Level Editor.
@param ControlRig The ControlRig
@param ControlName Name of the Control
@param Frame Time to set the transform
@param WorldTransform World Transform to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey Whether or not to set a key.

### SetControlRigWorldTransforms
```angelscript
void SetControlRigWorldTransforms(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FTransform> WorldTransforms, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's World Transforms at a specific times.
@param LevelSequence Active Sequence to set transforms for. Must be loaded in Level Editor.
@param ControlRig The ControlRig
@param ControlName Name of the Control
@param Frames Times to set the transform
@param WorldTransform World Transform to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetControlsMask
```angelscript
void SetControlsMask(UMovieSceneSection InSection, TArray<FName> ControlNames, bool bVisible)
```
Set the controls mask for the given ControlNames

### SetLocalControlRigBool
```angelscript
void SetLocalControlRigBool(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, bool Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's bool value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a bool control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigBools
```angelscript
void SetLocalControlRigBools(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<bool> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's bool values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a bool control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigEulerTransform
```angelscript
void SetLocalControlRigEulerTransform(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FEulerTransform Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's EulerTransform value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a EulerTransform control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigEulerTransforms
```angelscript
void SetLocalControlRigEulerTransforms(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FEulerTransform> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's EulerTransform values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a EulerTransform control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigFloat
```angelscript
void SetLocalControlRigFloat(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, float32 Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's float value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a float control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigFloats
```angelscript
void SetLocalControlRigFloats(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<float32> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's float values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a float control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigInt
```angelscript
void SetLocalControlRigInt(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, int Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's int value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a int control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigInts
```angelscript
void SetLocalControlRigInts(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<int> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's int values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a int control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigPosition
```angelscript
void SetLocalControlRigPosition(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FVector Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's Position value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Position control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigPositions
```angelscript
void SetLocalControlRigPositions(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FVector> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's Position values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Position control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigRotator
```angelscript
void SetLocalControlRigRotator(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FRotator Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's Rotator value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Rotator control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigRotators
```angelscript
void SetLocalControlRigRotators(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FRotator> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's Rotator values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Rotator control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigScale
```angelscript
void SetLocalControlRigScale(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FVector Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's Scale value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Scale control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigScales
```angelscript
void SetLocalControlRigScales(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FVector> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's Scale values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Scale control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigTransform
```angelscript
void SetLocalControlRigTransform(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FTransform Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's Transform value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Transform control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigTransformNoScale
```angelscript
void SetLocalControlRigTransformNoScale(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FTransformNoScale Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's TransformNoScale value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a TransformNoScale control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigTransformNoScales
```angelscript
void SetLocalControlRigTransformNoScales(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FTransformNoScale> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's TransformNoScale values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a TransformNoScale control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigTransforms
```angelscript
void SetLocalControlRigTransforms(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FTransform> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's Transform values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Transform control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### SetLocalControlRigVector2D
```angelscript
void SetLocalControlRigVector2D(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, FFrameNumber Frame, FVector2D Value, EMovieSceneTimeUnit TimeUnit, bool bSetKey)
```
Set ControlRig Control's Vector2D value at specific time
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Vector2D control
@param Frame Time to set the value
@param Value The value to set
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param bSetKey If True set a key, if not just set the value

### SetLocalControlRigVector2Ds
```angelscript
void SetLocalControlRigVector2Ds(ULevelSequence LevelSequence, UControlRig ControlRig, FName ControlName, TArray<FFrameNumber> Frames, TArray<FVector2D> Values, EMovieSceneTimeUnit TimeUnit)
```
Set ControlRig Control's Vector2D values at specific times
@param LevelSequence Active Sequence to set value on
@param ControlRig The ControlRig
@param ControlName Name of the Control, should be a Vector2D control
@param Frames Times to set the values
@param Values The values to set at those times
@param TimeUnit Unit for frame values, either in display rate or tick resolution

### ShowAllControls
```angelscript
void ShowAllControls(UMovieSceneSection InSection)
```
Shows all of the controls for the given section

### SnapControlRig
```angelscript
bool SnapControlRig(ULevelSequence LevelSequence, FFrameNumber StartFrame, FFrameNumber EndFrame, FControlRigSnapperSelection ChildrenToSnap, FControlRigSnapperSelection ParentToSnap, const UControlRigSnapSettings SnapSettings, EMovieSceneTimeUnit TimeUnit)
```
Peform a Snap operation to snap the children to the parent.
@param LevelSequence Active Sequence to snap
@param StartFrame Beginning of the snap
@param EndFrame End of the snap
@param ChildrenToSnap The children objects that snap and get keys set onto. They need to live in an active Sequencer in the level editor
@param ParentToSnap The parent object to snap relative to. If animated, it needs to live in an active Sequencer in the level editor
@param SnapSettings Settings to use
@param TimeUnit Unit for frame values, either in display rate or tick resolution
@param Returns True if successful

### TweenControlRig
```angelscript
bool TweenControlRig(ULevelSequence LevelSequence, UControlRig ControlRig, float32 TweenValue)
```
Peform a Tween operation on the current active sequencer time(must be visible).
@param LevelSequence The LevelSequence that's loaded in the editor
@param ControlRig The Control Rig to tween.
@param TweenValue The tween value to use, range from -1(blend to previous) to 1(blend to next)

