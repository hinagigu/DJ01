# __Animation

## 方法

### AddAnimationNotifyEvent
```angelscript
const UAnimNotify AddAnimationNotifyEvent(UAnimSequenceBase AnimationSequenceBase, FName NotifyTrackName, float32 StartTime, TSubclassOf<UAnimNotify> NotifyClass)
```
Adds an Animation Notify Event to Notify track in the given Animation with the given Notify creation data

### AddAnimationNotifyEventObject
```angelscript
void AddAnimationNotifyEventObject(UAnimSequenceBase AnimationSequenceBase, float32 StartTime, const UAnimNotify Notify, FName NotifyTrackName)
```
Adds an the specific Animation Notify to the Animation Sequence (requires Notify's outer to be the Animation Sequence)

### AddAnimationNotifyStateEvent
```angelscript
const UAnimNotifyState AddAnimationNotifyStateEvent(UAnimSequenceBase AnimationSequenceBase, FName NotifyTrackName, float32 StartTime, float32 Duration, TSubclassOf<UAnimNotifyState> NotifyStateClass)
```
Adds an Animation Notify State Event to Notify track in the given Animation with the given Notify State creation data

### AddAnimationNotifyStateEventObject
```angelscript
void AddAnimationNotifyStateEventObject(UAnimSequenceBase AnimationSequenceBase, float32 StartTime, float32 Duration, const UAnimNotifyState NotifyState, FName NotifyTrackName)
```
Adds an the specific Animation Notify State to the Animation Sequence (requires Notify State's outer to be the Animation Sequence)

### AddAnimationNotifyTrack
```angelscript
void AddAnimationNotifyTrack(UAnimSequenceBase AnimationSequenceBase, FName NotifyTrackName, FLinearColor TrackColor)
```
Adds an Animation Notify Track to the Animation Sequence

### AddAnimationSyncMarker
```angelscript
void AddAnimationSyncMarker(UAnimSequence AnimationSequence, FName MarkerName, float32 Time, FName NotifyTrackName)
```
Adds an Animation Sync Marker to Notify track in the given Animation with the corresponding Marker Name and Time

### AddCurve
```angelscript
void AddCurve(UAnimSequenceBase AnimationSequenceBase, FName CurveName, ERawCurveTrackTypes CurveType, bool bMetaDataCurve)
```
Adds an Animation Curve by Type and Name to the given Animation Sequence

### AddFloatCurveKey
```angelscript
void AddFloatCurveKey(UAnimSequenceBase AnimationSequenceBase, FName CurveName, float32 Time, float32 Value)
```
Adds a Float Key to the specified Animation Curve inside of the given Animation Sequence

### AddFloatCurveKeys
```angelscript
void AddFloatCurveKeys(UAnimSequenceBase AnimationSequenceBase, FName CurveName, TArray<float32> Times, TArray<float32> Values)
```
Adds a multiple of Float Keys to the specified Animation Curve inside of the given Animation Sequence

### AddMetaData
```angelscript
void AddMetaData(UAnimationAsset AnimationAsset, TSubclassOf<UAnimMetaData> MetaDataClass, UAnimMetaData& MetaDataInstance)
```
Creates and Adds an instance of the specified MetaData Class to the given Animation Asset

### AddMetaDataObject
```angelscript
void AddMetaDataObject(UAnimationAsset AnimationAsset, UAnimMetaData MetaDataObject)
```
Adds an instance of the specified MetaData Class to the given Animation Asset (requires MetaDataObject's outer to be the Animation Asset)

### AddNodeAssetOverride
```angelscript
void AddNodeAssetOverride(UAnimBlueprint AnimBlueprint, const UAnimationAsset Target, UAnimationAsset Override, bool bPrintAppliedOverrides)
```
Adds an Animation Asset override for the provided AnimationBlueprint, replacing any instance of Target with Override

@param AnimBlueprint                                 The Animation Blueprint to add/set the Override for
@param Target                                                The Animation Asset to add an override for (overrides all instances of the asset)
@param Override                                              The Animation Asset to used to override the Target with (types have to match)
@param bPrintAppliedOverrides                Flag whether or not to print the applied overrides

### AddTransformationCurveKey
```angelscript
void AddTransformationCurveKey(UAnimSequenceBase AnimationSequenceBase, FName CurveName, float32 Time, FTransform Transform)
```
Adds a Transformation Key to the specified Animation Curve inside of the given Animation Sequence

### AddTransformationCurveKeys
```angelscript
void AddTransformationCurveKeys(UAnimSequenceBase AnimationSequenceBase, FName CurveName, TArray<float32> Times, TArray<FTransform> Transforms)
```
Adds a multiple of Transformation Keys to the specified Animation Curve inside of the given Animation Sequence

### AddVectorCurveKey
```angelscript
void AddVectorCurveKey(UAnimSequenceBase AnimationSequenceBase, FName CurveName, float32 Time, FVector Vector)
```
Adds a Vector Key to the specified Animation Curve inside of the given Animation Sequence

### AddVectorCurveKeys
```angelscript
void AddVectorCurveKeys(UAnimSequenceBase AnimationSequenceBase, FName CurveName, TArray<float32> Times, TArray<FVector> Vectors)
```
Adds a multiple of Vector Keys to the specified Animation Curve inside of the given Animation Sequence

### AddVirtualBone
```angelscript
void AddVirtualBone(const UAnimSequence AnimationSequence, FName SourceBoneName, FName TargetBoneName, FName& VirtualBoneName)
```
Adds a Virtual Bone between the Source and Target Bones to the given Animation Sequence

### ContainsMetaDataOfClass
```angelscript
bool ContainsMetaDataOfClass(const UAnimationAsset AnimationAsset, TSubclassOf<UAnimMetaData> MetaDataClass)
```
Checks whether or not the given Animation Asset contains Meta Data Instance of the specified Meta Data Class

### CopyAnimNotifiesFromSequence
```angelscript
void CopyAnimNotifiesFromSequence(UAnimSequenceBase SourceAnimationSequenceBase, UAnimSequenceBase DestinationAnimationSequenceBase, bool bDeleteExistingNotifies)
```
Copies animation notifies from Src Animation Sequence to Dest. Creates anim notify tracks as necessary. Returns true on success.

### DoesBoneNameExist
```angelscript
void DoesBoneNameExist(UAnimSequence AnimationSequence, FName BoneName, bool& bExists)
```
Checks whether or not the given Bone Name exist on the Skeleton referenced by the given Animation Sequence

### DoesCurveExist
```angelscript
bool DoesCurveExist(UAnimSequenceBase AnimationSequenceBase, FName CurveName, ERawCurveTrackTypes CurveType)
```
Checks whether or not the given Curve Name exist on the Skeleton referenced by the given Animation Sequence

### EvaluateRootBoneTimecodeAttributesAtTime
```angelscript
bool EvaluateRootBoneTimecodeAttributesAtTime(const UAnimSequenceBase AnimationSequenceBase, float32 EvalTime, FQualifiedFrameTime& OutQualifiedFrameTime)
```
Evaluates timecode attributes (e.g. "TCFrame", "TCSecond", etc.) of the root bone and returns the resulting qualified frame time.

@param AnimationSequenceBase: Anim sequence for which to evaluate the root bone attributes.
@param EvalTime: Time (in seconds) at which to evaluate the timecode bone attributes.
@param OutQualifiedFrameTime: Resulting qualified frame time from evaluation. If the anim sequence has an import file frame rate
    set, then that will be used as the frame rate of the qualified frame time. Otherwise, the sampling frame rate of the anim
    sequence is used. If no timecode attributes are present on the bone or if none can be evaluated, the passed object will not be modified.
@return: true if the root bone had timecode attributes that could be evaluated and a qualified frame time was set, or false otherwise.

### EvaluateRootBoneTimecodeSubframeAttributeAtTime
```angelscript
bool EvaluateRootBoneTimecodeSubframeAttributeAtTime(const UAnimSequenceBase AnimationSequenceBase, float32 EvalTime, float32& OutSubframe)
```
Evaluates the subframe timecode attribute (e.g. "TCSubframe") of the root bone and returns the resulting value.

Since the subframe component of FFrameTime is clamped to the range [0.0, 1.0), it cannot accurately represent the use
case where the timecode metadata represents subframe values as whole numbered subframes instead of as a percentage of a
frame the way the engine does. The subframe component of the FQualifiedFrameTime returned by
EvaluateRootBoneTimecodeAttributesAtTime() may not reflect the authored subframe metadata in that case.

This function allows access to the subframe values that were actually authored in the timecode metadata.

@param AnimationSequenceBase: Anim sequence for which to evaluate the root bone subframe attribute.
@param EvalTime: Time (in seconds) at which to evaluate the subframe timecode bone attribute.
@param OutSubframe: Resulting subframe value from evaluation. If no subframe timecode attribute is present
    on the bone or if it cannot be evaluated, the output parameter will not be modified.
@return: true if the root bone had a subframe timecode attribute that could be evaluated and a value was set, or false otherwise.

### FindBonePathToRoot
```angelscript
void FindBonePathToRoot(const UAnimSequenceBase AnimationSequenceBase, FName BoneName, TArray<FName>& BonePath)
```
Finds the Bone Path from the given Bone to the Root Bone

### GetAdditiveAnimationType
```angelscript
void GetAdditiveAnimationType(const UAnimSequence AnimationSequence, EAdditiveAnimationType& AdditiveAnimationType)
```
Retrieves the Additive Animation type for the given Animation Sequence

### GetAdditiveBasePoseType
```angelscript
void GetAdditiveBasePoseType(const UAnimSequence AnimationSequence, EAdditiveBasePoseType& AdditiveBasePoseType)
```
Retrieves the Additive Base Pose type for the given Animation Sequence

### GetAnimationCurveNames
```angelscript
void GetAnimationCurveNames(const UAnimSequenceBase AnimationSequenceBase, ERawCurveTrackTypes CurveType, TArray<FName>& CurveNames)
```
Retrieves the Names of the individual float curves for the given Animation Sequence

### GetAnimationGraphs
```angelscript
void GetAnimationGraphs(UAnimBlueprint AnimationBlueprint, TArray<UAnimationGraph>& AnimationGraphs)
```
Returns all Animation Graphs contained by the provided Animation Blueprint

### GetAnimationInterpolationType
```angelscript
void GetAnimationInterpolationType(const UAnimSequence AnimationSequence, EAnimInterpolationType& InterpolationType)
```
Retrieves the Animation Interpolation type for the given Animation Sequence

### GetAnimationNotifyEventNames
```angelscript
void GetAnimationNotifyEventNames(const UAnimSequenceBase AnimationSequenceBase, TArray<FName>& EventNames)
```
Retrieves all Unique Animation Notify Events found within the given Animation Sequence

### GetAnimationNotifyEvents
```angelscript
void GetAnimationNotifyEvents(const UAnimSequenceBase AnimationSequenceBase, TArray<FAnimNotifyEvent>& NotifyEvents)
```
Retrieves all Animation Notify Events found within the given Animation Sequence

### GetAnimationNotifyEventsForTrack
```angelscript
void GetAnimationNotifyEventsForTrack(const UAnimSequenceBase AnimationSequenceBase, FName NotifyTrackName, TArray<FAnimNotifyEvent>& Events)
```
Retrieves all Animation Notify Events for the given Notify Track Name from the given Animation Sequence

### GetAnimationNotifyTrackNames
```angelscript
void GetAnimationNotifyTrackNames(const UAnimSequenceBase AnimationSequenceBase, TArray<FName>& TrackNames)
```
Retrieves all Unique Animation Notify Track Names found within the given Animation Sequence

### GetAnimationSyncMarkers
```angelscript
void GetAnimationSyncMarkers(const UAnimSequence AnimationSequence, TArray<FAnimSyncMarker>& Markers)
```
Retrieves all the Animation Sync Markers for the given Animation Sequence

### GetAnimationSyncMarkersForTrack
```angelscript
void GetAnimationSyncMarkersForTrack(const UAnimSequence AnimationSequence, FName NotifyTrackName, TArray<FAnimSyncMarker>& Markers)
```
Retrieves all Animation Sync Markers for the given Notify Track Name from the given Animation Sequence

### GetAnimationTrackNames
```angelscript
void GetAnimationTrackNames(const UAnimSequenceBase AnimationSequenceBase, TArray<FName>& TrackNames)
```
Retrieves the Names of the individual ATracks for the given Animation Sequence

### GetAnimNotifyEventDuration
```angelscript
float32 GetAnimNotifyEventDuration(FAnimNotifyEvent NotifyEvent)
```
Returns the duration for a NotifyEvent, only non-zero for Anim Notify States

### GetAnimNotifyEventTriggerTime
```angelscript
float32 GetAnimNotifyEventTriggerTime(FAnimNotifyEvent NotifyEvent)
```
Returns the actual trigger time for a NotifyEvent

### GetBoneCompressionSettings
```angelscript
void GetBoneCompressionSettings(const UAnimSequence AnimationSequence, UAnimBoneCompressionSettings& CompressionSettings)
```
Retrieves the Bone Compression Settings for the given Animation Sequence

### GetBonePoseForFrame
```angelscript
void GetBonePoseForFrame(const UAnimSequenceBase AnimationSequenceBase, FName BoneName, int Frame, bool bExtractRootMotion, FTransform& Pose)
```

### GetBonePoseForTime
```angelscript
void GetBonePoseForTime(const UAnimSequenceBase AnimationSequenceBase, FName BoneName, float32 Time, bool bExtractRootMotion, FTransform& Pose)
```

### GetBonePosesForFrame
```angelscript
void GetBonePosesForFrame(const UAnimSequenceBase AnimationSequenceBase, TArray<FName> BoneNames, int Frame, bool bExtractRootMotion, TArray<FTransform>& Poses, const USkeletalMesh PreviewMesh)
```

### GetBonePosesForTime
```angelscript
void GetBonePosesForTime(const UAnimSequenceBase AnimationSequenceBase, TArray<FName> BoneNames, float32 Time, bool bExtractRootMotion, TArray<FTransform>& Poses, const USkeletalMesh PreviewMesh)
```

### GetCurveCompressionSettings
```angelscript
void GetCurveCompressionSettings(const UAnimSequence AnimationSequence, UAnimCurveCompressionSettings& CompressionSettings)
```
Retrieves the Curve Compression Settings for the given Animation Sequence

### GetFloatKeys
```angelscript
void GetFloatKeys(UAnimSequenceBase AnimationSequenceBase, FName CurveName, TArray<float32>& Times, TArray<float32>& Values)
```
Retrieves, a multiple of, Float Key(s) from the specified Animation Curve inside of the given Animation Sequence

### GetFloatValueAtTime
```angelscript
float32 GetFloatValueAtTime(UAnimSequenceBase AnimationSequenceBase, FName CurveName, float32 Time)
```
Retrieves an evaluated float value for a given time from the specified Animation Curve inside of the given Animation Sequence

### GetFrameAtTime
```angelscript
void GetFrameAtTime(const UAnimSequenceBase AnimationSequenceBase, float32 Time, int& Frame)
```
Retrieves the Frame Index at the specified Time Value for the given Animation Sequence

### GetMetaData
```angelscript
void GetMetaData(const UAnimationAsset AnimationAsset, TArray<UAnimMetaData>& MetaData)
```
Retrieves all Meta Data Instances from the given Animation Asset

### GetMetaDataOfClass
```angelscript
void GetMetaDataOfClass(const UAnimationAsset AnimationAsset, TSubclassOf<UAnimMetaData> MetaDataClass, TArray<UAnimMetaData>& MetaDataOfClass)
```
Retrieves all Meta Data Instances from the given Animation Asset

### GetMontageSlotNames
```angelscript
void GetMontageSlotNames(const UAnimMontage AnimationMontage, TArray<FName>& SlotNames)
```
Retrieves the Names of the Animation Slots used in the given Montage

### GetNodesOfClass
```angelscript
void GetNodesOfClass(UAnimBlueprint AnimationBlueprint, TSubclassOf<UAnimGraphNode_Base> NodeClass, TArray<UAnimGraphNode_Base>& GraphNodes, bool bIncludeChildClasses)
```
Returns all Animation Graph Nodes of the provided Node Class contained by the Animation Blueprint

### GetNumFrames
```angelscript
void GetNumFrames(const UAnimSequenceBase AnimationSequenceBase, int& NumFrames)
```
Retrieves the number of animation frames for the given Animation Sequence

### GetNumKeys
```angelscript
void GetNumKeys(const UAnimSequenceBase AnimationSequenceBase, int& NumKeys)
```
Retrieves the number of animation keys for the given Animation Sequence

### GetRateScale
```angelscript
void GetRateScale(const UAnimSequenceBase AnimationSequenceBase, float32& RateScale)
```
Retrieves the (Play) Rate Scale of the given Animation Sequence

### GetRawTrackData
```angelscript
void GetRawTrackData(const UAnimSequenceBase AnimationSequenceBase, FName TrackName, TArray<FVector>& PositionKeys, TArray<FQuat>& RotationKeys, TArray<FVector>& ScalingKeys)
```

### GetRawTrackPositionData
```angelscript
void GetRawTrackPositionData(const UAnimSequenceBase AnimationSequenceBase, FName TrackName, TArray<FVector>& PositionData)
```

### GetRawTrackRotationData
```angelscript
void GetRawTrackRotationData(const UAnimSequenceBase AnimationSequenceBase, FName TrackName, TArray<FQuat>& RotationData)
```

### GetRawTrackScaleData
```angelscript
void GetRawTrackScaleData(const UAnimSequenceBase AnimationSequenceBase, FName TrackName, TArray<FVector>& ScaleData)
```

### GetRootMotionLockType
```angelscript
void GetRootMotionLockType(const UAnimSequence AnimationSequence, ERootMotionRootLock& LockType)
```
Retrieves the Root Motion Lock Type for the given Animation Sequence

### GetSequenceLength
```angelscript
void GetSequenceLength(const UAnimSequenceBase AnimationSequenceBase, float32& Length)
```
Retrieves the Length of the given Animation Sequence

### GetTimeAtFrame
```angelscript
void GetTimeAtFrame(const UAnimSequenceBase AnimationSequenceBase, int Frame, float32& Time)
```
Retrieves the Time Value at the specified Frame Indexfor the given Animation Sequence

### GetTransformationKeys
```angelscript
void GetTransformationKeys(UAnimSequenceBase AnimationSequenceBase, FName CurveName, TArray<float32>& Times, TArray<FTransform>& Values)
```
Retrieves, a multiple of, Transformation Key(s) from the specified Animation Curve inside of the given Animation Sequence

### GetUniqueMarkerNames
```angelscript
void GetUniqueMarkerNames(const UAnimSequence AnimationSequence, TArray<FName>& MarkerNames)
```
Retrieves all the Unique Names for the Animation Sync Markers contained by the given Animation Sequence

### GetVariableFrameStrippingSettings
```angelscript
void GetVariableFrameStrippingSettings(const UAnimSequence AnimationSequence, UVariableFrameStrippingSettings& VariableFrameStrippingSettings)
```
Retrieves the Variable Frame Stripping Settings for the given Animation Sequence

### GetVectorKeys
```angelscript
void GetVectorKeys(UAnimSequenceBase AnimationSequenceBase, FName CurveName, TArray<float32>& Times, TArray<FVector>& Values)
```
Retrieves, a multiple of, Vector Key(s) from the specified Animation Curve inside of the given Animation Sequence

### IsRootMotionEnabled
```angelscript
bool IsRootMotionEnabled(const UAnimSequence AnimationSequence)
```
Checks whether or not Root Motion is Enabled for the given Animation Sequence

### IsRootMotionLockForced
```angelscript
bool IsRootMotionLockForced(const UAnimSequence AnimationSequence)
```
Checks whether or not Root Motion locking is Forced for the given Animation Sequence

### IsValidAnimationSyncMarkerName
```angelscript
bool IsValidAnimationSyncMarkerName(const UAnimSequence AnimationSequence, FName MarkerName)
```
Checks whether or not the given Marker Name is a valid Animation Sync Marker Name

### IsValidAnimNotifyTrackName
```angelscript
bool IsValidAnimNotifyTrackName(const UAnimSequenceBase AnimationSequenceBase, FName NotifyTrackName)
```
Checks whether or not the given Track Name is a valid Animation Notify Track in the Animation Sequence

### IsValidRawAnimationTrackName
```angelscript
bool IsValidRawAnimationTrackName(const UAnimSequenceBase AnimationSequenceBase, FName TrackName)
```
Checks whether or not the given Animation Track Name is contained within the Animation Sequence

### IsValidTime
```angelscript
void IsValidTime(const UAnimSequenceBase AnimationSequenceBase, float32 Time, bool& IsValid)
```
Checks whether or not the given Time Value lies within the given Animation Sequence's Length

### RemoveAllAnimationNotifyTracks
```angelscript
void RemoveAllAnimationNotifyTracks(UAnimSequenceBase AnimationSequenceBase)
```
Removes All Animation Notify Tracks from Animation Sequence

### RemoveAllAnimationSyncMarkers
```angelscript
void RemoveAllAnimationSyncMarkers(UAnimSequence AnimationSequence)
```
Removes All Animation Sync Markers found within the Animation Sequence, and returns the number of removed instances

### RemoveAllBoneAnimation
```angelscript
void RemoveAllBoneAnimation(UAnimSequence AnimationSequence)
```
Removes all Animation Bone Track Data from the given Animation Sequence

### RemoveAllCurveData
```angelscript
void RemoveAllCurveData(UAnimSequenceBase AnimationSequenceBase)
```
Removes all Animation Curve Data from the given Animation Sequence (Raw Animation Curves [Names] may not be removed from the Skeleton)

### RemoveAllMetaData
```angelscript
void RemoveAllMetaData(UAnimationAsset AnimationAsset)
```
Removes all Meta Data from the given Animation Asset

### RemoveAllVirtualBones
```angelscript
void RemoveAllVirtualBones(const UAnimSequence AnimationSequence)
```
Removes all Virtual Bones from the given Animation Sequence

### RemoveAnimationNotifyEventsByName
```angelscript
int RemoveAnimationNotifyEventsByName(UAnimSequenceBase AnimationSequenceBase, FName NotifyName)
```
Removes Animation Notify Events found by Name within the Animation Sequence, and returns the number of removed name instances

### RemoveAnimationNotifyEventsByTrack
```angelscript
int RemoveAnimationNotifyEventsByTrack(UAnimSequenceBase AnimationSequenceBase, FName NotifyTrackName)
```
Removes Animation Notify Events found by Track within the Animation Sequence, and returns the number of removed name instances

### RemoveAnimationNotifyTrack
```angelscript
void RemoveAnimationNotifyTrack(UAnimSequenceBase AnimationSequenceBase, FName NotifyTrackName)
```
Removes an Animation Notify Track from Animation Sequence by Name

### RemoveAnimationSyncMarkersByName
```angelscript
int RemoveAnimationSyncMarkersByName(UAnimSequence AnimationSequence, FName MarkerName)
```
Removes All Animation Sync Marker found within the Animation Sequence whose name matches MarkerName, and returns the number of removed instances

### RemoveAnimationSyncMarkersByTrack
```angelscript
int RemoveAnimationSyncMarkersByTrack(UAnimSequence AnimationSequence, FName NotifyTrackName)
```
Removes All Animation Sync Marker found within the Animation Sequence that belong to the specific Notify Track, and returns the number of removed instances

### RemoveBoneAnimation
```angelscript
void RemoveBoneAnimation(UAnimSequence AnimationSequence, FName BoneName, bool bIncludeChildren, bool bFinalize)
```
Removes an Animation Curve by Name from the given Animation Sequence (Raw Animation Curves [Names] may not be removed from the Skeleton)

    @param AnimationSequence : AnimSequence
    @param BoneName : Name of bone track user wants to remove
    @param bIncludeChildren : true if user wants to include all children of BoneName
@param bFinalize : If you set this to true, it will trigger compression. If you set bFinalize to be false, you'll have to manually trigger Finalize.

### RemoveCurve
```angelscript
void RemoveCurve(UAnimSequenceBase AnimationSequenceBase, FName CurveName, bool bRemoveNameFromSkeleton)
```
Removes an Animation Curve by Name from the given Animation Sequence (Raw Animation Curves [Names] may not be removed from the Skeleton)

### RemoveMetaData
```angelscript
void RemoveMetaData(UAnimationAsset AnimationAsset, UAnimMetaData MetaDataObject)
```
Removes the specified Meta Data Instance from the given Animation Asset

### RemoveMetaDataOfClass
```angelscript
void RemoveMetaDataOfClass(UAnimationAsset AnimationAsset, TSubclassOf<UAnimMetaData> MetaDataClass)
```
Removes all Meta Data Instance of the specified Class from the given Animation Asset

### RemoveVirtualBone
```angelscript
void RemoveVirtualBone(const UAnimSequence AnimationSequence, FName VirtualBoneName)
```
Removes a Virtual Bone with the specified Bone Name from the given Animation Sequence

### RemoveVirtualBones
```angelscript
void RemoveVirtualBones(const UAnimSequence AnimationSequence, TArray<FName> VirtualBoneNames)
```
Removes Virtual Bones with the specified Bone Names from the given Animation Sequence

### ReplaceAnimNotifies
```angelscript
void ReplaceAnimNotifies(UAnimSequenceBase AnimationSequenceBase, TSubclassOf<UAnimNotify> OldNotifyClass, TSubclassOf<UAnimNotify> NewNotifyClass, FOnNotifyReplaced OnNotifyReplaced)
```
Replaces animation notifies in the specified Animation Sequence

### ReplaceAnimNotifyStates
```angelscript
void ReplaceAnimNotifyStates(UAnimSequenceBase AnimationSequenceBase, TSubclassOf<UAnimNotifyState> OldNotifyClass, TSubclassOf<UAnimNotifyState> NewNotifyClass, FOnNotifyStateReplaced OnNotifyStateReplaced)
```
Replaces animation notifies in the specified Animation Sequence

### SetAdditiveAnimationType
```angelscript
void SetAdditiveAnimationType(UAnimSequence AnimationSequence, EAdditiveAnimationType AdditiveAnimationType)
```
Sets the Additive Animation type for the given Animation Sequence

### SetAdditiveBasePoseType
```angelscript
void SetAdditiveBasePoseType(UAnimSequence AnimationSequence, EAdditiveBasePoseType AdditiveBasePoseType)
```
Sets the Additive Base Pose type for the given Animation Sequence

### SetAnimationInterpolationType
```angelscript
void SetAnimationInterpolationType(UAnimSequence AnimationSequence, EAnimInterpolationType InterpolationType)
```
Sets the Animation Interpolation type for the given Animation Sequence

### SetBoneCompressionSettings
```angelscript
void SetBoneCompressionSettings(UAnimSequence AnimationSequence, UAnimBoneCompressionSettings CompressionSettings)
```
Sets the Bone Compression Settings for the given Animation Sequence

### SetCurveCompressionSettings
```angelscript
void SetCurveCompressionSettings(UAnimSequence AnimationSequence, UAnimCurveCompressionSettings CompressionSettings)
```
Sets the Curve Compression Settings for the given Animation Sequence

### SetIsRootMotionLockForced
```angelscript
void SetIsRootMotionLockForced(UAnimSequence AnimationSequence, bool bForced)
```
Sets whether or not Root Motion locking is Forced for the given Animation Sequence

### SetRateScale
```angelscript
void SetRateScale(UAnimSequenceBase AnimationSequenceBase, float32 RateScale)
```
Sets the (Play) Rate Scale for the given Animation Sequence

### SetRootMotionEnabled
```angelscript
void SetRootMotionEnabled(UAnimSequence AnimationSequence, bool bEnabled)
```
Sets whether or not Root Motion is Enabled for the given Animation Sequence

### SetRootMotionLockType
```angelscript
void SetRootMotionLockType(UAnimSequence AnimationSequence, ERootMotionRootLock RootMotionLockType)
```
Sets the Root Motion Lock Type for the given Animation Sequence

### SetVariableFrameStrippingSettings
```angelscript
void SetVariableFrameStrippingSettings(UAnimSequence AnimationSequence, UVariableFrameStrippingSettings VariableFrameStrippingSettings)
```
Sets the Variable Frame Stripping Settings for the given Animation Sequence

