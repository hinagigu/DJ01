# __SequencerTools

## 方法

### ClearLinkedAnimSequences
```angelscript
void ClearLinkedAnimSequences(ULevelSequence InLevelSequence)
```
* Clear all linked anim sequences between this level sequence and any linked anim sequences
*
* @InLevelSequence LevelSequence to clean links for

### CreateEvent
```angelscript
FMovieSceneEvent CreateEvent(UMovieSceneSequence InSequence, UMovieSceneEventSectionBase InSection, FSequencerQuickBindingResult InEndpoint, TArray<FString> InPayload)
```
Create an event from a previously created blueprint endpoint and a payload. The resulting event should be added only
to a channel of the section that was given as a parameter.
@param InSequence Main level sequence that holds the event track and to which the resulting event should be added.
@param InSection Section of the event track of the main sequence.
@param InEndpoint Previously created endpoint.
@param InPayload Values passed as payload to event, count must match the numbers of payload variable names in @InEndpoint.
@return The created movie event.
@see CreateQuickBinding

### CreateQuickBinding
```angelscript
FSequencerQuickBindingResult CreateQuickBinding(UMovieSceneSequence InSequence, UObject InObject, FString InFunctionName, bool bCallInEditor)
```
Create a quick binding to an actor's member method to be used in an event sequence.
@param InActor Actor that will be bound
@param InFunctionName Name of the method, as it is displayed in the Blueprint Editor. eg. "Set Actor Scale 3D"
@param bCallInEditor Should the event be callable in editor.
@return The created binding.

### ExportAnimSequence
```angelscript
bool ExportAnimSequence(UWorld World, ULevelSequence Sequence, UAnimSequence AnimSequence, UAnimSeqExportOption ExportOption, FMovieSceneBindingProxy Binding, bool bCreateLink)
```
* Export Passed in Binding as an Anim Seqquence.
*
* @InWorld World to export
* @InSequence Sequence to export
* @AnimSequence The AnimSequence to save into.
* @ExportOption The export options for the sequence.
* @InBinding Binding to export that has a skelmesh component on it
* @InAnimSequenceFilename File to create
* @bCreateLink If true will create a link between the animation sequence and the level sequence

### ExportFBXFromControlRig
```angelscript
bool ExportFBXFromControlRig(ULevelSequence Sequence, FString ActorWithControlRigTrack, const UMovieSceneUserExportFBXControlRigSettings ExportFBXControlRigSettings)
```
Exports an FBX from the section to key of the control rig track of the actor with the given name.

### ExportLevelSequenceFBX
```angelscript
bool ExportLevelSequenceFBX(FSequencerExportFBXParams InParams)
```
* Export Passed in Bindings and Tracks to FBX

### GetAnimSequenceLinkFromLevelSequence
```angelscript
ULevelSequenceAnimSequenceLink GetAnimSequenceLinkFromLevelSequence(ULevelSequence InLevelSequence)
```
* Get the links to the anim sequences if they exist on this level sequence
*
* @InLevelSequence LevelSequence to get links from
* @return Returns the link object if it exists, nullptr if it doesn't

### GetLevelSequenceLinkFromAnimSequence
```angelscript
UAnimSequenceLevelSequenceLink GetLevelSequenceLinkFromAnimSequence(UAnimSequence InAnimSequence)
```
* Get the link to the level sequence if it exists on this anim sequence
*
* @InAnimSequence AnimSequence to get links from
* @return Returns the link object if it exists, nullptr if it doesn't

### ImportFBXToControlRig
```angelscript
bool ImportFBXToControlRig(UWorld World, ULevelSequence InSequence, FString ActorWithControlRigTrack, TArray<FString> SelectedControlRigNames, UMovieSceneUserImportFBXControlRigSettings ImportFBXControlRigSettings, FString ImportFilename)
```
* Import FBX onto a control rig with the specified track name
*
* @InWorld World to import to
* @InSequence InSequence to import
* @ActorWithControlRigTrack ActorWithControlRigTrack The name of the actor with the control rig track we are importing onto
* @SelectedControlRigNames  List of selected control rig names. Will use them if  ImportFBXControlRigSettings->bImportOntoSelectedControls is true
* @ImportFBXControlRigSettings Settings to control import.
* @InImportFileName Path to fbx file to create

### ImportLevelSequenceFBX
```angelscript
bool ImportLevelSequenceFBX(UWorld InWorld, ULevelSequence InSequence, TArray<FMovieSceneBindingProxy> InBindings, UMovieSceneUserImportFBXSettings InImportFBXSettings, FString InImportFilename)
```
* Import FBX onto Passed in Bindings
*
* @InWorld World to import to
* @InSequence InSequence to import
* @InBindings InBindings to import
* @InImportFBXSettings Settings to control import.
* @InImportFileName Path to fbx file to import from
* @InPlayer Player to bind to

### IsEventEndpointValid
```angelscript
bool IsEventEndpointValid(FSequencerQuickBindingResult InEndpoint)
```
Check if an endpoint is valid and can be used to create movie scene event.
@param InEndpoint Endpoint to check.

### LinkAnimSequence
```angelscript
bool LinkAnimSequence(ULevelSequence Sequence, UAnimSequence AnimSequence, const UAnimSeqExportOption ExportOptions, FMovieSceneBindingProxy Binding)
```
* Links a LevelSequence's SkeletalMesh binding to an existing anim sequence.
*
* @InSequence Sequence to link from
* @AnimSequence The AnimSequence to link to.
* @ExportOption The export options that should be used when baking the LevelSequence.
* @InBinding Binding that has a skelmesh component on it

