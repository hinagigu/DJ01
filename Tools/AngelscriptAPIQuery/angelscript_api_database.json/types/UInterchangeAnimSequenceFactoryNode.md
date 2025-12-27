# UInterchangeAnimSequenceFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

## 方法

### GetAnimatedAttributeCurveName
```angelscript
void GetAnimatedAttributeCurveName(int Index, FString& OutAttributeCurveName)
```
Get the animated attribute curve name at the specified index.

### GetAnimatedAttributeCurveNames
```angelscript
void GetAnimatedAttributeCurveNames(TArray<FString>& OutAttributeCurveNames)
```
Get all animated attribute curve names.

### GetAnimatedAttributeCurveNamesCount
```angelscript
int GetAnimatedAttributeCurveNamesCount()
```
Return the number of animated attribute curve names this anim sequence drives. Curves are FRichCurve of type float.

### GetAnimatedAttributeStepCurveName
```angelscript
void GetAnimatedAttributeStepCurveName(int Index, FString& OutAttributeStepCurveName)
```
Get the animated attribute step curve name at the specified index.

### GetAnimatedAttributeStepCurveNames
```angelscript
void GetAnimatedAttributeStepCurveNames(TArray<FString>& OutAttributeStepCurveNames)
```
Get all animated attribute step curve names.

### GetAnimatedAttributeStepCurveNamesCount
```angelscript
int GetAnimatedAttributeStepCurveNamesCount()
```
Return the number of animated attribute step curve names this anim sequence drives.

### GetAnimatedMaterialCurveSuffixe
```angelscript
void GetAnimatedMaterialCurveSuffixe(int Index, FString& OutMaterialCurveSuffixe)
```
Get the animated material curve suffix with the specified index.

### GetAnimatedMaterialCurveSuffixes
```angelscript
void GetAnimatedMaterialCurveSuffixes(TArray<FString>& OutMaterialCurveSuffixes)
```
Get all animated material curve suffixes.

### GetAnimatedMaterialCurveSuffixesCount
```angelscript
int GetAnimatedMaterialCurveSuffixesCount()
```
Return the number of animated material curve suffixes this anim sequence drives. Curves are FRichCurve of type float.

### GetCustomAddCurveMetadataToSkeleton
```angelscript
bool GetCustomAddCurveMetadataToSkeleton(bool& AttributeValue)
```
Get the custom attribute AddCurveMetadataToSkeleton. Return false if the attribute is not set.

Note - If this setting is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.

### GetCustomDeleteExistingCustomAttributeCurves
```angelscript
bool GetCustomDeleteExistingCustomAttributeCurves(bool& AttributeValue)
```
Get the custom attribute DeleteExistingCustomAttributeCurves. Return false if the attribute is not set.

Note - If true, all previous custom attribute curves are deleted if you reimport.

### GetCustomDeleteExistingMorphTargetCurves
```angelscript
bool GetCustomDeleteExistingMorphTargetCurves(bool& AttributeValue)
```
Get the custom attribute DeleteExistingMorphTargetCurves. Return false if the attribute is not set.

Note: If true, all previous morph target curves are deleted if you reimport.

### GetCustomDeleteExistingNonCurveCustomAttributes
```angelscript
bool GetCustomDeleteExistingNonCurveCustomAttributes(bool& AttributeValue)
```
Get the custom attribute DeleteExistingNonCurveCustomAttributes. Return false if the attribute is not set.

Note - If true, all previous non-curve custom attributes are deleted if you reimport.

### GetCustomDoNotImportCurveWithZero
```angelscript
bool GetCustomDoNotImportCurveWithZero(bool& AttributeValue)
```
Get the custom attribute DoNotImportCurveWithZero. Return false if the attribute is not set.

Note - If this attribute is enabled, only curves that have a value other than zero will be imported. This is to avoid adding extra curves to evaluate.

### GetCustomImportAttributeCurves
```angelscript
bool GetCustomImportAttributeCurves(bool& AttributeValue)
```
Get the import attribute curves state. If true, all user custom attributes on nodes are imported.

Return false if the attribute is not set.

### GetCustomImportBoneTracks
```angelscript
bool GetCustomImportBoneTracks(bool& AttributeValue)
```
Get the import bone tracks state. If the attribute is true, bone tracks are imported. If the attribute
is false, bone tracks are not imported.

Return false if the attribute is not set. Return true if the attribute exists and can be queried.

### GetCustomImportBoneTracksRangeStart
```angelscript
bool GetCustomImportBoneTracksRangeStart(float& AttributeValue)
```
Get the import bone tracks start time in seconds. Return false if the attribute is not set.

### GetCustomImportBoneTracksRangeStop
```angelscript
bool GetCustomImportBoneTracksRangeStop(float& AttributeValue)
```
Get the import bone tracks end time in seconds. Return false if the attribute is not set.

### GetCustomImportBoneTracksSampleRate
```angelscript
bool GetCustomImportBoneTracksSampleRate(float& AttributeValue)
```
Get the import bone tracks sample rate. Return false if the attribute is not set.

### GetCustomMaterialDriveParameterOnCustomAttribute
```angelscript
bool GetCustomMaterialDriveParameterOnCustomAttribute(bool& AttributeValue)
```
Get the custom attribute MaterialDriveParameterOnCustomAttribute. Return false if the attribute is not set.

Note: If true, sets Material Curve Type for all custom attributes.

### GetCustomRemoveCurveRedundantKeys
```angelscript
bool GetCustomRemoveCurveRedundantKeys(bool& AttributeValue)
```
Get the custom attribute RemoveCurveRedundantKeys. Return false if the attribute is not set.

### GetCustomSkeletonFactoryNodeUid
```angelscript
bool GetCustomSkeletonFactoryNodeUid(FString& AttributeValue)
```
Get the unique ID of the skeleton factory node. Return false if the attribute is not set.

### GetCustomSkeletonSoftObjectPath
```angelscript
bool GetCustomSkeletonSoftObjectPath(FSoftObjectPath& AttributeValue)
```
Query the optional existing USkeleton this animation must use. If this attribute is set and the skeleton is valid,
the AnimSequence factory uses this skeleton instead of the one imported from GetCustomSkeletonFactoryNodeUid.
Pipelines set this attribute when the user wants to specify an existing skeleton.
Return false if the attribute was not set.

### GetMorphTargetNodeAnimationPayloadKeys
```angelscript
void GetMorphTargetNodeAnimationPayloadKeys(TMap<FString,FInterchangeAnimationPayLoadKey>& OutMorphTargetNodeAnimationPayloads)
```

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node creates.

### GetSceneNodeAnimationPayloadKeys
```angelscript
void GetSceneNodeAnimationPayloadKeys(TMap<FString,FInterchangeAnimationPayLoadKey>& OutSceneNodeAnimationPayloadKeys)
```

### InitializeAnimSequenceNode
```angelscript
void InitializeAnimSequenceNode(FString UniqueID, FString DisplayLabel)
```
Initialize node data.
@param UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.

### RemoveAnimatedAttributeCurveName
```angelscript
bool RemoveAnimatedAttributeCurveName(FString AttributeCurveName)
```
Remove the specified animated attribute curve name.

### RemoveAnimatedAttributeStepCurveName
```angelscript
bool RemoveAnimatedAttributeStepCurveName(FString AttributeStepCurveName)
```
Remove the specified animated attribute step curve name.

### RemoveAnimatedMaterialCurveSuffixe
```angelscript
bool RemoveAnimatedMaterialCurveSuffixe(FString MaterialCurveSuffixe)
```
Remove the specified animated material curve suffix.

### SetAnimatedAttributeCurveName
```angelscript
bool SetAnimatedAttributeCurveName(FString AttributeCurveName)
```
Add an animated attribute curve name.

### SetAnimatedAttributeStepCurveName
```angelscript
bool SetAnimatedAttributeStepCurveName(FString AttributeStepCurveName)
```
Add an animated attribute step curve name.

### SetAnimatedMaterialCurveSuffixe
```angelscript
bool SetAnimatedMaterialCurveSuffixe(FString MaterialCurveSuffixe)
```
Add an animated material curve suffix.

### SetAnimationPayloadKeysForMorphTargetNodeUids
```angelscript
void SetAnimationPayloadKeysForMorphTargetNodeUids(TMap<FString,FString> MorphTargetAnimationPayloadKeyUids, TMap<FString,uint8> MorphTargetAnimationPayloadKeyTypes)
```

### SetAnimationPayloadKeysForSceneNodeUids
```angelscript
void SetAnimationPayloadKeysForSceneNodeUids(TMap<FString,FString> SceneNodeAnimationPayloadKeyUids, TMap<FString,uint8> SceneNodeAnimationPayloadKeyTypes)
```

### SetCustomAddCurveMetadataToSkeleton
```angelscript
bool SetCustomAddCurveMetadataToSkeleton(bool AttributeValue)
```
Set the custom attribute AddCurveMetadataToSkeleton. Return false if the attribute could not be set.

Note - If this setting is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.

### SetCustomDeleteExistingCustomAttributeCurves
```angelscript
bool SetCustomDeleteExistingCustomAttributeCurves(bool AttributeValue)
```
Set the custom attribute DeleteExistingCustomAttributeCurves. Return false if the attribute could not be set.

Note - If true, all previous custom attribute curves are deleted if you reimport.

### SetCustomDeleteExistingMorphTargetCurves
```angelscript
bool SetCustomDeleteExistingMorphTargetCurves(bool AttributeValue)
```
Set the custom attribute DeleteExistingMorphTargetCurves. Return false if the attribute could not be set.

Note: If true, all previous morph target curves are deleted if you reimport.

### SetCustomDeleteExistingNonCurveCustomAttributes
```angelscript
bool SetCustomDeleteExistingNonCurveCustomAttributes(bool AttributeValue)
```
Set the custom attribute DeleteExistingNonCurveCustomAttributes. Return false if the attribute could not be set.

Note - If true, all previous non-curve custom attributes are deleted if you reimport.

### SetCustomDoNotImportCurveWithZero
```angelscript
bool SetCustomDoNotImportCurveWithZero(bool AttributeValue)
```
Set the custom attribute DoNotImportCurveWithZero. Return false if the attribute could not be set.

Note - If this attribute is enabled, only curves that have a value other than zero will be imported. This is to avoid adding extra curves to evaluate.

### SetCustomImportAttributeCurves
```angelscript
bool SetCustomImportAttributeCurves(bool AttributeValue)
```
Set the import attribute curves state. Return false if the attribute could not be set.

### SetCustomImportBoneTracks
```angelscript
bool SetCustomImportBoneTracks(bool AttributeValue)
```
Set the import bone tracks state. Pass true to import bone tracks, or false to not import bone tracks.

### SetCustomImportBoneTracksRangeStart
```angelscript
bool SetCustomImportBoneTracksRangeStart(float AttributeValue)
```
Set the import bone tracks start time in seconds. Return false if the attribute could not be set.

### SetCustomImportBoneTracksRangeStop
```angelscript
bool SetCustomImportBoneTracksRangeStop(float AttributeValue)
```
Set the import bone tracks end time in seconds. Return false if the attribute could not be set.

### SetCustomImportBoneTracksSampleRate
```angelscript
bool SetCustomImportBoneTracksSampleRate(float AttributeValue)
```
Set the import bone tracks sample rate. Return false if the attribute could not be set.

### SetCustomMaterialDriveParameterOnCustomAttribute
```angelscript
bool SetCustomMaterialDriveParameterOnCustomAttribute(bool AttributeValue)
```
Set the custom attribute MaterialDriveParameterOnCustomAttribute. Return false if the attribute could not be set.

Note: If true, sets Material Curve Type for all custom attributes.

### SetCustomRemoveCurveRedundantKeys
```angelscript
bool SetCustomRemoveCurveRedundantKeys(bool AttributeValue)
```
Set the custom attribute RemoveCurveRedundantKeys. Return false if the attribute could not be set.

### SetCustomSkeletonFactoryNodeUid
```angelscript
bool SetCustomSkeletonFactoryNodeUid(FString AttributeValue)
```
Set the unique ID of the skeleton factory node. Return false if the attribute cannot be set.

### SetCustomSkeletonSoftObjectPath
```angelscript
bool SetCustomSkeletonSoftObjectPath(FSoftObjectPath AttributeValue)
```
Set the optional existing USkeleton this animation must use. If this attribute is set and the skeleton is valid,
the AnimSequence factory uses this skeleton instead of the one imported from GetCustomSkeletonFactoryNodeUid.
Pipelines set this attribute when the user wants to specify an existing skeleton.

